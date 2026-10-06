---
id: everyday-tasks-qwen36-vs-qwen35-9b
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-06
herkunft: Victus, local_models tools/alltag, Läufe 2026-10-06 08:34 bis 10:56
verweist_auf: [counting-needs-thinking, ollama-silently-truncates-context, laya-router-before-agent, separate-prefill-from-decode]
---

# 20 Alltagsaufgaben: Qwen3.6-35B-A3B 20/20 mit Denken, Qwen3.5-9B schnell aber unzuverlässig

## Aussage
20 Aufgaben, die man an ein lokales Modell abgeben würde, jede maschinell geprüft:
Rechnen, Wochentag, Mail nach JSON, Tickets einordnen, Übersetzen, Zusammenfassen,
Regex, `slugify`, Bugfix, SQL, Bash-Befehl, Log zählen, CSV-Umsatz, Commit-Zeile,
erfundene Firma, Primzahlen, Buchstaben zählen, Mail an Vermieter, GB nach GiB,
Code-Ausgabe. Python und SQL werden ausgeführt. Jede Prüfung ist gegen eine bekannt
gute und eine bekannt schlechte Antwort getestet. Direkt über die Ollama-API, ohne
Agenten, Temperatur 0, jede Variante allein auf der GPU.

| Variante | richtig | Gesamt | Median je Aufgabe | Ausgabe-Token |
|---|---|---|---|---|
| Qwen3.6-35B-A3B (`qwen3.6-64k`) ohne Denken | 17/20 | 223 s | 10,7 s | 875 |
| Qwen3.6-35B-A3B mit Denken | **20/20** | 479 s | 21,2 s | 23 967 |
| Qwen3.5-9B (`num_ctx 32768`) ohne Denken | 13/20 | **31 s** | **0,6 s** | 757 |
| Qwen3.5-9B mit Denken | 18/20 | 1 481 s | 66,4 s | 58 584 |

- **Qwen3.6 ohne Denken** scheitert an `slugify`, an der CSV-Summe (nennt die Region
  mit dem größten Einzelpreis) und am Zählen der e in "Erdbeerkuchen" (2 statt 4).
  Mit Denken löst es alle drei. Passt zu [counting-needs-thinking](counting-needs-thinking.md).
- **Qwen3.5-9B ohne Denken** liegt ganz auf der GPU und antwortet im Median nach
  0,6 s, verrechnet sich aber: Serverkosten 95,76 statt 302,40 €, 22,76 statt
  22,35 GiB, eine Primzahl vergessen, eine Log-Zeile eines anderen Dienstes
  mitgezählt, Code-Ausgabe falsch vorhergesagt. Text, Übersetzung, Einordnen und
  JSON-Extraktion löst es alle.
- **Qwen3.5-9B mit Denken** denkt rund 2,4-mal so viel wie Qwen3.6 und ist dadurch
  dreimal langsamer als dieses, obwohl es ganz auf der GPU liegt. Einmal lief es in die Grenze von
  8 192 Ausgabe-Token, einmal kam eine leere Antwort ohne Token-Angabe.

Wiederholt wurden Qwen3.6 mit Denken (drei Läufe) und Qwen3.5-9B ohne Denken
(drei Läufe, zwei davon mit 4 096 Kontext, was ohne Denken nicht stört): jeweils
gleiche Punktzahl, bei Temperatur 0 reproduzierbar. Qwen3.6 ohne Denken und
Qwen3.5-9B mit Denken bei 32k liefen je einmal. Zeiten nur aus Läufen ohne fremde Last.

## Trägt
Die Modellwahl auf Victus für kurze Einzelaufgaben: Qwen3.6 mit Denken als Standard,
Denken nötig bei Zählen, Code und Rechnen über Tabellen. Qwen3.5-9B ohne Denken
höchstens für Text- und Extraktionsaufgaben, bei denen ein Fehler billig ist.

## Trägt nicht
- Agenten-Aufgaben mit Werkzeugen (Hermes, OpenCode). Hier wurde nur die API gefragt.
- Andere Rechner: Qwen3.6 liegt auf Victus zu 78 % auf der CPU, auf 24 GB ganz auf der GPU.
- Allgemeine Rangfolge der Modelle. 20 Aufgaben, je ein Lauf je Variante ohne Last.

## Bruchindikator
Ein zweiter Satz Aufgaben derselben Art, bei dem Qwen3.5-9B ohne Denken bei Rechen-
und Zählaufgaben mithält oder Qwen3.6 mit Denken deutlich unter 20/20 fällt.

## Ablesung
Eigene Messung. local_models `tools/alltag/` (aufgaben.json, alltag.py), Läufe
`laeufe/20261006-0834_qwen3.6-64k-ohne-denken`, `20261006-1031_qwen3.6-64k`,
`20261006-1031_qwen3.5-9b-32k-ohne-denken`, `20261006-1056_qwen3.5-9b-32k`.

Zwei eigene Fehler unterwegs, behoben:
- Die Prüfung der Firma-Frage lehnte eine richtige Antwort ab ("keine öffentlichen
  oder verifizierten Daten"). Nach Korrektur und Neubewertung: Qwen3.6 mit Denken
  20 statt 19.
- Der erste 9B-Lauf mit Denken nutzte Ollamas Standardkontext von 4 096 Token,
  sieben Antworten waren leer, siehe [ollama-silently-truncates-context](../risks/ollama-silently-truncates-context.md).

Laya routete 19 der 20 Aufgaben lokal (nur das Zählen an Claude), 13/20 richtig
zwischen Hermes und OpenCode, siehe [laya-router-before-agent](laya-router-before-agent.md).

## Verknüpft
- [counting-needs-thinking](counting-needs-thinking.md)
- [ollama-silently-truncates-context](../risks/ollama-silently-truncates-context.md)
- [laya-router-before-agent](laya-router-before-agent.md)
- [separate-prefill-from-decode](../rules/separate-prefill-from-decode.md)
