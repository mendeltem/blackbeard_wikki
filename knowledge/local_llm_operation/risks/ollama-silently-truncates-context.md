---
id: ollama-silently-truncates-context
typ: risiko
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-03
herkunft: Claude-Code-Sitzung auf Victus, 2026-10-03
verweist_auf: [needle-recall-holds-to-125k, prefix-cache-single-slot]
---

# Ollama kuerzt einen zu langen Prompt stumm auf die Haelfte, und das Modell antwortet trotzdem

## Aussage
Ist der Prompt laenger als `num_ctx`, gibt Ollama keinen Fehler zurueck. Es
schneidet den **Anfang** ab und behaelt nur etwa `num_ctx / 2` Token vom Ende.
Gemessen mit `num_ctx 65536`: Prompts von 71k und 100k Token kamen jeweils mit
`prompt_eval_count = 32770` beim Modell an.

Das Modell merkt davon nichts. Im Needle-Test lag der echte Code im
abgeschnittenen Teil, ein Koeder ("der alte, ungueltige Code war ...") im
behaltenen. In 4 von 4 Laeufen nannte Qwen3.6 den Koeder, ohne Hinweis auf
Unsicherheit.

## Traegt
Jeder Agent auf Ollama (z. B. Hermes Agent) mit langen Sitzungen. Hermes bringt
allein rund 13k Token System-Prompt mit; bei `num_ctx 65536` bleiben etwa 50k fuer
die Arbeit, danach wird ohne Meldung die Haelfte des Verlaufs verworfen.
Gegenmittel: `num_ctx` so gross setzen, wie RAM es zulaesst (128k lief auf Victus,
siehe [needle-recall-holds-to-125k](../findings/needle-recall-holds-to-125k.md)),
und `prompt_eval_count` gegen die erwartete Laenge pruefen.

## Traegt nicht
llama.cpp-Server direkt: der lehnt einen zu langen Prompt mit HTTP 400 ab. Das ist
das gewuenschte Verhalten.

## Bruchindikator
`prompt_eval_count` in der Ollama-Antwort kleiner als die Laenge, die man geschickt
hat. Bei 32770 trotz laengerem Prompt ist die Kuerzung sicher.

## Ablesung
Eigene Messung, Ollama mit `qwen3.6:35b`, `/api/generate`, `num_ctx 65536`,
Temperatur 0, Thinking aus. 4 Laeufe ueber dem Limit, alle gekuerzt, alle falsch.

Zweiter Fall, 2026-10-06: Ein frisch geholtes `qwen3.5:9b` läuft in Ollama mit dem Standardkontext von 4 096 Token. Mit Denken brachen sieben von 20 Antworten bei rund 4 000 Token mitten im Denkteil ab und kamen leer zurück, ohne Fehlermeldung. Abhilfe wie bei Qwen3.6: eigene Variante mit `PARAMETER num_ctx 32768`. Siehe [everyday-tasks-qwen36-vs-qwen35-9b](../findings/everyday-tasks-qwen36-vs-qwen35-9b.md).

## Verknuepft
- [needle-recall-holds-to-125k](../findings/needle-recall-holds-to-125k.md)
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
- [everyday-tasks-qwen36-vs-qwen35-9b](../findings/everyday-tasks-qwen36-vs-qwen35-9b.md)
