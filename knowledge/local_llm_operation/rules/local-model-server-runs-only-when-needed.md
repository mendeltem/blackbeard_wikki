---
id: local-model-server-runs-only-when-needed
typ: regel
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-21
herkunft: Cle-Arbeit, Gespraech mit Nutzer, 21.10.2026
verweist_auf: [foreign-gpu-process-before-measuring, remote-model-gets-only-data-free-skills-and-redacted-text]
---

# Der lokale Modellserver laeuft nur, wenn er gebraucht wird

## Aussage
Der Dienst `llama-server.service` ist `enabled` **und** das Konto hat
`Linger=yes`. Er startet also beim Booten ohne Login und laeuft dauerhaft.
Das ist fuer den Datenschutz richtig — Patientendaten duerfen die Maschine
nicht verlassen, also muss das lokale Profil ein lokales Gehirn haben —, hat
aber einen Preis: das 27B-Modell in Q4 belegt mit `--n-gpu-layers 99` und
`--ctx-size 81920` **20,4 von 24,6 GiB VRAM** im Leerlauf. Fuer jede
GPU-Arbeit daneben bleiben ~3 GiB.

Der Nutzer entschied am 21.10.2026: **die meisten Aufgaben gehen an das
Remote-Profil; das lokale Modell wird nur aktiviert, wenn Patientendaten
gelesen oder bearbeitet werden, und danach wieder abgeschaltet.**

Umgesetzt ohne die Datenschutz-Architektur anzutasten: `--sleep-idle-seconds`
in `start.sh`. Nach dieser Leerlaufzeit **entlaedt der Server das Modell, gibt
den VRAM frei und laedt es bei der naechsten Anfrage selbst nach.** Kein
Abschalten des Dienstes, kein Verlust der Aktivierbarkeit, nur kein
Dauerbelegen der Karte.

Gemessen am 0,5B-Testmodell (`--sleep-idle-seconds 15`, Port 8099):
`/props` zeigt zunaechst `is_sleeping=false`, nach der Leerlaufzeit `true`;
eine anschliessende Anfrage wird wieder bedient und laedt das Modell nach.

**Gemessen am echten Dienst** (27B Q4, `--ctx-size 81920`,
`--sleep-idle-seconds 300`, 21.10.2026):

| Zeitpunkt | VRAM belegt |
|---|---|
| in Betrieb | 21.770 MiB |
| 300 s Leerlauf | **1.618 MiB** |
| nach einer Anfrage | 21.774 MiB |

20,2 GiB werden also freigegeben. Das Aufwachen dauerte **11,4 s** bis zur
ersten Antwort. Vorher lagen hier 20,4 von 24,6 GiB dauerhaft an, daneben
blieben ~3 GiB fuer jede andere GPU-Arbeit.

## Traegt
Jeden Rechner mit einer lokal noetigen Inferenz und begrenztem VRAM.
Der Unterschied zwischen "erreichbar" und "geladen" ist genau das, was diese
Option liefert: die Architektur bleibt, die Belegung geht.

Die Zahlen sind ein Tausch, kein Sieg: 11 s Kaltstart gegen 20 GB, die sonst
dauerhaft weg sind. Wer die Karte fuer Trainings braucht, gewinnt klar.

## Traegt nicht
`--sleep-idle-seconds` gibt es **nicht in jedem Build** — vorher mit
`llama-server --help` pruefen, es gibt keine Umgebungsvariable dafuer, nur das
Argument.

Aufwachen kostet Ladezeit (bei 27B mehrere Sekunden bis Minuten). Fuer eine
Anfrage pro Stunde ist das ein guter Tausch, fuer einen Chat mit hoher
Frequenz nicht — dort ist der Kaltstart teurer als der gehaltene VRAM.

## Bruchindikator
**Zuerst eine Korrektur meiner eigenen ersten Fassung, 21.10.2026.** Ich hatte
hier geschrieben, `/props` und `/health` seien echte Anfragen und setzten den
Idle-Timer zurueck — wer damit messe, sehe nie einen Schlaf. **Das ist
falsch.** Im Quelltext (`tools/server/server-context.cpp`):

```
this->get_health = [this](const server_http_req &) {
    auto res = create_response(true);   // bypass_sleep
```
```
this->get_props = [this](const server_http_req &) {
    auto res = create_response(true);   // bypass_sleep
```

Beide Routen laufen mit `bypass_sleep = true` und werden ausdruecklich
**waehrend** des Schlafs bedient ("this endpoint can be accessed during
sleeping"). Auch die Queue bestaetigt es: `task_resets_idle_timer()` schliesst
nur `SERVER_TASK_TYPE_METRICS` aus, nicht Health oder Props. Messen mit
`/health` oder `/props` verhindert den Schlaf also **nicht**. Wer das
weiterverbreitet, schickt den naechsten auf eine falsche Spur — deshalb steht
die Berichtigung hier und nicht nur im Log.

**Der echte Bruchindikator ist eine echte Anfrage.** Jeder Aufruf, der
rechnet — `POST /v1/chat/completions`, auch "nur zum Test" — setzt den Timer
zurueck und laedt das Modell. Am 21.10.2026 lief ein Trainingsjob in einen
CUDA-OOM, weil Minuten vorher genau so ein Aufwachtest gelaufen war: der
Server hatte kurz zuvor geschlafen, war danach wieder wach, und die 20 GB
waren weg. **Pruefen und Nutzen sind hier dieselbe Handlung — die Reihenfolge
entscheidet.**

**Zweite Beobachtung, die man nicht fuer einen Fehler haelt:** der Schlaf
kommt spaeter als die eingestellte Zeit. Bei `--sleep-idle-seconds 300` und
letzter echter Anfrage um 18:53 trat er erst um ~19:02 ein, also nach ~9 min
statt nach 5. Die Queue **verschiebt** den Idle-Takt, statt ihn
zurueckzusetzen (`time_last_task = std::min(now, time_last_task + (now -
t_update_slots))`): die Zeit, die `update_slots` selbst braucht, zaehlt nicht
als Leerlauf. Wer nach dem Messen eine GPU-Arbeit startet, sollte deshalb
nicht auf die Uhr schauen, sondern den Start an eine VRAM-Schranke binden:
Schleife ueber `nvidia-smi --query-gpu=memory.free`, erst starten wenn genug
frei ist. Beruehrungsfrei messen geht nur ueber `nvidia-smi`, das den Server
gar nicht anspricht.

## Wer ihn legitim weckt
Nicht jeder Aufruf ist ein Fehlgriff. Der `guard-daemon.service` schickt jeden
ungeprueften Ausgang des gesperrten Agenten durch das lokale Modell
(`system/guard/ask_outside.py` -> `/v1/chat/completions` auf `:8000`). Solange
dieser Waechter laeuft, wacht der Server bei echter Ausgangspruefung auf — das
ist gewollt, kein Leck. Wer den VRAM dauerhaft braucht, muss diese Quelle
kennen, sonst sucht er sie in einem Timer, der nie der Taeter war.

**Zweiter Nutzen derselben Option:** weil das Modell austauschbar aus der
Registry kommt (`models.json`), kann Claude Codes Harness gegen dasselbe lokale
Modell laufen — `system/claude-lokal.sh`, im `.bashrc` als `cl` verlinkt. Es
setzt `ANTHROPIC_BASE_URL=http://127.0.0.1:8000`, `ANTHROPIC_MODEL` aus der
Registry und `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`; Werkzeuge,
Dateizugriff und `CLAUDE.md` bleiben dieselben. Getestet am 21.10.2026:
`claude-lokal.sh -p "Antworte nur mit dem Wort LOKAL"` antwortete `LOKAL`,
Exit 0, ueber `127.0.0.1:8000`. Der Server schlief danach von selbst wieder ein
(19:24 letzte Anfrage, 19:29 `free=22480`). Ein blankes `claude -p` dagegen
laeuft **nicht** lokal, sondern in die Cloud — die beiden nicht verwechseln.

## Ablesung
Eigene Messung, 21.10.2026, Cle-Arbeit. Regler: `start.sh` von
`local_agentic_system`, Abschnitt "Ruhezustand". Die 27B-Messung oben ist am
echten Dienst gelaufen (nicht mehr offen); das 0,5B-Testmodell diente nur dem
ersten Nachweis.

## Verknuepft
- [foreign-gpu-process-before-measuring](../rules/foreign-gpu-process-before-measuring.md)
- [remote-model-gets-only-data-free-skills-and-redacted-text](../rules/remote-model-gets-only-data-free-skills-and-redacted-text.md)
