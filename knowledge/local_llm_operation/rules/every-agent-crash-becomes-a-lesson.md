---
id: every-agent-crash-becomes-a-lesson
typ: regel
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-12
herkunft: Nutzer 12.10.2026: "ich will, dass Clara nicht abstuerzt; jedes Mal, wenn das passiert, wollen wir daraus lernen"
verweist_auf: [registry-pointed-at-half-a-model-agent-window-died, model-server-start-checks-card-and-picks-profile]
---

# Jeder Absturz des lokalen Agenten wird zu einem Befund mit Ursache, Abhilfe im Code und Bruchindikator

## Aussage
"Clara ist abgestuerzt" ist nie der Endzustand. Fuer jeden Absturz (totes tmux-Fenster, Dienst gestorben, Auftrag
steckengeblieben wegen Infrastruktur) gilt die feste Reihenfolge:
1. **Kette rekonstruieren** aus Logs mit Uhrzeit: llama-server.log, journalctl --user -u llama-server, clara --status,
   dauerlauf.log, modellstart.log. Nicht raten.
2. **Jeden Fehler in der Kette benennen** (meist sind es zwei bis drei: eine falsche Annahme, ein fehlender Check, ein
   Exit, wo Warten richtig waere).
3. **Abhilfe im Code**, nicht im Gedaechtnis: der Check wandert an die Stelle, die die Entscheidung trifft (modellstart,
   grossauftrag, agent.sh), mit Sicherung `*.vor-<datum>-<grund>` und einem Test der Entscheidung ohne Start.
4. **Befund ins Wiki** (local_llm_operation/findings) mit Bruchindikator, Verweis in SUMMARY, eine Tafelzeile.
5. **Agent bleibt am Leben**: Fehler beim Modellstart fuehren zu Warten und erneutem Versuch, nie zum Schliessen des Fensters.
   Nur der Nutzer schliesst Clara.

## Traegt
Clara (Hermes auf llama-server), ihre Dienste (llama-server, dauerlauf, modellwache) und die Werkzeuge, die sie starten.

## Traegt nicht
Fehler innerhalb eines Auftrags (falsches Ergebnis) -- dafuer gelten Abnahme und Tests.

## Bruchindikator
Ein zweiter Absturz mit derselben Ursache; ein Absturz ohne Befund im Wiki.

## Ablesung
Erster Fall nach dieser Regel: registry-pointed-at-half-a-model-agent-window-died (12.10.2026).

## Verknuepft
- [registry-pointed-at-half-a-model-agent-window-died](../findings/registry-pointed-at-half-a-model-agent-window-died.md)
- [model-server-start-checks-card-and-picks-profile](model-server-start-checks-card-and-picks-profile.md)
