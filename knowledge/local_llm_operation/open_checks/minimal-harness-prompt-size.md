---
id: minimal-harness-prompt-size
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-04
herkunft: Video Sam Witteveen "Which is The Best Qwen3.8-27B?", 2026-10-04; eigene Messung Hermes + OpenCode
verweist_auf: [prefix-cache-single-slot, hermes-delegates-to-opencode-locally, rule-lists-make-small-models-refuse]
---

# Kleiner Harness statt kleineres Modell?

## Aussage
Der Coding-Agent **Pi** kommt laut Video mit vier Werkzeugen (read, write, edit,
bash) und einem System-Prompt **unter 1000 Token** aus.

Gemessen auf Victus, Ollama-Log:

| Harness | Prompt der ersten Anfrage |
|---|---|
| OpenCode 1.18.34 | 10 879 Token |
| Hermes Agent v0.21.5 | rund 13 000 Token |

Bei einem Slot (siehe [prefix-cache-single-slot]) wird dieser Prompt nach jedem
Cache-Verlust neu eingelesen, bei rund 400 t/s also 27-33 s, bevor das Modell das
erste Token schreibt. Mit unter 1000 Token waeren es etwa 2-3 s.

Vermutung: Auf Victus ist der Harness ein groesserer Hebel als ein schnelleres
Modell. Dazu passt [rule-lists-make-small-models-refuse]: lange System-Prompts
schaden kleinen Modellen auch inhaltlich.

## Traegt
Nichts. Die Prompt-Groessen sind gemessen, die Wirkung auf Ergebnis und Wanduhr
nicht.

## Traegt nicht
QwenPi ist eigens fuer Pi trainiert. Laut Video ist nicht belegt, dass ein
Modell ohne dieses Training, etwa Qwen3.6-35B-A3B, in Pi gut arbeitet.

## Bruchindikator
entfaellt

## Ablesung
blind

## Zu messen
Pi mit Qwen3.6-35B-A3B ueber Ollama gegen OpenCode, dieselben Aufgaben wie in
[hermes-delegates-to-opencode-locally]. Erfasst werden Prompt-Token je Anfrage,
Wanduhr gesamt und ob die Tests gruen sind.

## Verknuepft
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
- [hermes-delegates-to-opencode-locally](../findings/hermes-delegates-to-opencode-locally.md)
- [rule-lists-make-small-models-refuse](../findings/rule-lists-make-small-models-refuse.md)
