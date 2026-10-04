---
id: reasoning-effort-for-routine-agent-tasks
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-04
herkunft: Video Sam Witteveen "Which is The Best Qwen3.8-27B?", 2026-10-04; eigene Einrichtung Hermes + OpenCode
verweist_auf: [counting-needs-thinking, hermes-delegates-to-opencode-locally, dense-27b-vs-moe-on-8gb]
---

# Wie viel Thinking brauchen Routineaufgaben im Agenten?

## Aussage
Lokal ist das Modell decode-gebunden: jedes Denk-Token ist Wartezeit. Bei
30-35 t/s kosten 3000 Denk-Token rund eineinhalb Minuten.

Im Video halbiert eine niedrigere Reasoning-Stufe bei Qwen3.8-27B die Denk-Token,
kostet aber rund **9 Punkte Genauigkeit** (Herstellerangabe ThinkingCap).
Gleichzeitig ist auf Victus gemessen, dass Zaehlen und Laengen ohne Thinking
plausibel falsch werden (siehe [counting-needs-thinking]).

Offen ist der Bereich dazwischen: Code erklaeren, eine kleine Funktion, eine
Datei umbenennen. Ob Hermes und OpenCode dafuer volles Thinking brauchen, ist
nicht gemessen. Beide Werkzeuge lassen es einstellen: Hermes `--reasoning`,
OpenCode `--variant`.

## Traegt
Nichts.

## Traegt nicht
Eine pauschale Empfehlung "Thinking aus fuer schnelle Antworten". Der
IBAN-Befund zeigt, dass der Fehler dann nicht auffaellt.

## Bruchindikator
entfaellt

## Ablesung
blind

## Zu messen
Fuenf Routineaufgaben, je drei Laeufe, mit OpenCode auf Qwen3.6-35B-A3B bei
hoher und bei niedriger Stufe. Erfasst werden Denk-Token, Wanduhr und ob das
Ergebnis stimmt, geprueft durch Tests, nicht durch die Meldung des Agenten.
Eine der fuenf Aufgaben soll eine Zaehl- oder Laengenaufgabe sein, als Kontrolle
gegen [counting-needs-thinking].

## Verknuepft
- [counting-needs-thinking](../findings/counting-needs-thinking.md)
- [hermes-delegates-to-opencode-locally](../findings/hermes-delegates-to-opencode-locally.md)
- [dense-27b-vs-moe-on-8gb](dense-27b-vs-moe-on-8gb.md)
