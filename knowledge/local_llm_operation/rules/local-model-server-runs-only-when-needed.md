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
Ein `--sleep-idle-seconds`-Argument, das im Prozess steht
(`/proc/<pid>/cmdline`) und trotzdem nicht greift: **dann prueft man
vermutlich mit dem Server selbst.** `/props` und `/health` sind echte
Anfragen und setzen den Idle-Timer zurueck. Wer den Schwellwert mit
`curl /props` misst, misst sich selbst und sieht nie einen Schlafzustand.
Beruehrungsfrei messen geht nur ueber `nvidia-smi`, das den Server nicht
anspricht.

**Zweite Falle, am selben Tag erlebt:** wer den Schlaf prueft, indem er eine
Anfrage stellt ("weckt er wieder auf?"), **weckt ihn auf — und der VRAM ist
wieder belegt.** Am 21.10.2026 lief genau so ein Trainingsjob erneut in einen
CUDA-OOM, obwohl der Server Minuten vorher geschlafen hatte: der Aufwachtest
dazwischen hatte das Modell wieder geladen. Wer nach dem Test eine GPU-Arbeit
starten will, muss entweder die Leerlaufzeit abwarten oder den Start an eine
VRAM-Schranke binden (Schleife ueber `nvidia-smi --query-gpu=memory.free`,
erst starten wenn genug frei ist). Pruefen und Nutzen sind hier dieselbe
Handlung — die Reihenfolge entscheidet.

## Ablesung
Eigene Messung, 21.10.2026, Cle-Arbeit. Regler: `start.sh` von
`local_agentic_system`, Abschnitt "Ruhezustand". Testmodell und Endpunkt wie
oben; die 27B-Messung war zu diesem Zeitpunkt noch offen.

## Verknuepft
- [foreign-gpu-process-before-measuring](../rules/foreign-gpu-process-before-measuring.md)
- [remote-model-gets-only-data-free-skills-and-redacted-text](../rules/remote-model-gets-only-data-free-skills-and-redacted-text.md)
