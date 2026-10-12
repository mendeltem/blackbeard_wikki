---
id: registry-pointed-at-half-a-model-agent-window-died
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-12
herkunft: Alita 12.10.2026 10:19-10:35, Nutzer: "ich will, dass Clara nicht abstuerzt; jedes Mal, wenn das passiert, wollen wir daraus lernen"
verweist_auf: [model-server-start-checks-card-and-picks-profile, every-agent-crash-becomes-a-lesson]
---

# Die Registry zeigte auf ein halbes Modell: der Dienst starb beim Laden, der Agent beendete sich, Claras Fenster war tot

## Aussage
Ablauf: Nutzer tippt `clara --warten`, die Karte ist von einem Training belegt, `modellstart` waehlt das einzige Profil, das
neben ein Training darf (flash, 7,5 GiB). Dessen Datei ist ein GGUF in zwei Teilen -- der zweite Teil liegt nicht auf der Platte
(models.json: flash und flash-s je 1/2 Teile, nur flash-xxs vollstaendig). llama-server: "failed to open GGUF file ...-00002-of-00002"
-> exit 1 -> systemd meldet "gestorben" -> modellstart rc 2 -> agent.sh `exit 2` -> das tmux-Fenster zeigt "Pane is dead".
Aus Nutzersicht: "Clara ist abgestuerzt". Drei Fehler in einer Kette:
1. **Registry ungeprueft**: ein Profil galt als "passt", obwohl seine Datei unvollstaendig war (Tafel-Regel 2: eine halbe Datei
   ist keine Datei). Jetzt prueft `modellstart` vor der Wahl jede Datei samt aller Teile (`-NNNNN-of-NNNNN`) und meldet
   "Modelldatei fehlt/unvollstaendig" statt "passt".
2. **Agent beendet sich bei Fehlstart**: mit `--warten` versucht agent.sh jetzt bis 30 min alle 60 s erneut, statt das Fenster zu
   schliessen (Sicherung agent.sh.vor-20261012-warten-bei-fehlstart).
3. **Veraltete Sperre**: die GPU-Sperrdatei trug die PID eines schon beendeten Schlangen-Laeufers; `modellstart` haelt eine tote
   PID fuer lebendig? Nein -- es prueft `ps`, aber die Datei blieb liegen, weil der Laeufer per SIGTERM starb und seinen
   Aufraeumzweig nicht erreichte. Offen: Sperre mit Zeitstempel und Pruefung "PID lebt" an EINER Stelle (grossauftrag).

## Traegt
Jeden Start des Modellservers neben einem Training; jede Registry-Pflege (add-model.sh, Downloads in Teilen).

## Traegt nicht
Abstuerze des Modells im Betrieb (OOM, Kontextueberlauf) -- andere Ursachen, eigene Befunde.

## Bruchindikator
Ein "Pane is dead" in Claras tmux-Sitzung ohne neuen Wiki-Befund; ein Profil in models.json, dessen Datei fehlt und das
`modellstart --pruefen` trotzdem als "passt" fuehrt.

## Ablesung
system/logs/llama-server.log Zeilen 413888-413905, journalctl --user -u llama-server 10:20:00-10:20:12, `clara --status`
("Pane is dead (status 2, 10:20:06)"), Test der Auswahl nach dem Patch: q4 passt, flash/flash-s "unvollstaendig", flash-xxs passt.

## Verknuepft
- [model-server-start-checks-card-and-picks-profile](../rules/model-server-start-checks-card-and-picks-profile.md)
- [every-agent-crash-becomes-a-lesson](../rules/every-agent-crash-becomes-a-lesson.md)
