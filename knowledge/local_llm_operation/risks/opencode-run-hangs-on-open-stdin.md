---
id: opencode-run-hangs-on-open-stdin
typ: risiko
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-04
herkunft: Victus, Einrichtung Hermes + OpenCode, 2026-10-04
verweist_auf: [hermes-delegates-to-opencode-locally]
---

# `opencode run` haengt ohne Meldung, wenn stdin offen bleibt

## Aussage
Aus einem Skript oder Agenten-Tool gestartet, blieb `opencode run '...'` nach
`message=init` stehen. In 10 Minuten **kam keine einzige Anfrage bei Ollama an**.
Der Prozess lag in `ep_poll` bei 1 % CPU, ohne Netzwerkverbindung.

Derselbe Aufruf mit `</dev/null` lieferte die Antwort nach **82 s**.

Vermutung: `opencode run` liest bei nicht-interaktivem stdin den Inhalt als
Zusatz zur Nachricht und wartet auf EOF. Nicht im Quelltext nachgelesen.

## Traegt
Jeder Aufruf von `opencode run` aus Skripten, Cron oder einem anderen Agenten.
Dort immer `</dev/null` anhaengen.

## Traegt nicht
Der interaktive Start im Terminal. Dort ist stdin ein TTY.

## Bruchindikator
`opencode run` laeuft lange, und im Ollama-Log steht kein `POST
/v1/chat/completions`. Dann haengt es vor dem Modell, nicht im Modell.

## Ablesung
OpenCode 1.18.34. Prozesszustand ueber `ps -o wchan` und `/proc/<pid>/fd`,
Ollama-Log ueber `journalctl -u ollama`. Ein einzelner Fall. Der Hermes-Aufruf
im selben Test lief mit geschlossenem stdin durch, ob die Hermes-Skill das
selbst absichert, ist nicht geprueft.

## Verknuepft
- [hermes-delegates-to-opencode-locally](../findings/hermes-delegates-to-opencode-locally.md)
