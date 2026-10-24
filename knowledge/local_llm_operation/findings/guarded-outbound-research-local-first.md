---
id: guarded-outbound-research-local-first
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-23
herkunft: Alita, Ausgangswache (system/guard) des lokalen Agenten, Reparatur und Umbau 2026-10-09
verweist_auf: [decision-model-as-profile-orchestrator, lean-hermes-toolsets]
---

# Recherche fuer einen Agenten ohne Netz: lokal zuerst, Cloud nur auf Zuruf, Waechter nur fuer eigene Daten

## Aussage
Ein lokaler Agent, der Patientendaten sieht, bekommt keinen Netzzugang; sein einziger Weg nach draussen ist ein
Waechterdienst auf Loopback, der jede Frage prueft (Muster, dann lokales Modell, dann Protokoll). Drei Lehren aus
dem Betrieb:

1. **Ein stiller Aussenweg ist ein toter Aussenweg.** Der Dienst rief `claude -p` mit dem Standardmodell auf;
   als dessen Kontingent erschoepft war, kam einen Monat lang nur "Fehler" zurueck, ohne dass es jemand merkte.
   Von 50 Fragen gingen 13 durch.
2. **Lokal zuerst reicht fuer Literaturfragen.** Offene Schnittstellen ohne Schluessel (arXiv, OpenAlex, Europe PMC,
   Semantic Scholar) liefern Titel und Abstracts; das lokale 27B-Modell erzeugt die Suchanfragen und antwortet nur
   aus den Abstracts mit [n]-Belegen. Eine PVS-Frage: 68 s, 47 Treffer, Antwort mit 14 Quellen, keine Cloud-Token.
   Schwaechen: einzelne fachfremde Treffer, Semantic Scholar drosselt (429), Europe PMC antwortet langsam.
   Wichtig: fuer die kurzen Aufrufe das Denken abschalten (`enable_thinking: false`), sonst verbraucht das
   Reasoning-Modell das Tokenbudget und liefert leere Suchanfragen.
3. **Der Waechter sperrt nur Eigenes.** Oeffentliche Datensaetze (VALDO, HCP-Aging, EPVS, ADNI, UK Biobank ...)
   samt Fallkennungen und Zahlen sind kein Datenschutzproblem; eigene Kohortennamen und ihre Kennungen sperren
   immer, auch neben einem oeffentlichen Namen. Vorher blockierten Muster wie "sub-042" oder "Kohorte" jede
   Frage zu oeffentlichen Daten.

## Traegt
- Literatur- und Methodenfragen ohne Cloud; Cloud-Modell (mit Websuche) nur mit ausdruecklichem Schalter.
- Jede ausgehende Frage protokolliert, mit Kennzeichen, ob Cloud benutzt wurde.

## Traegt nicht
- Fragen, die Volltexte oder nicht indizierte Quellen brauchen (Software-Dokumentation, Foren): dort ist die
  lokale Suche blind; dann Cloud auf Zuruf.
- Paralleles Arbeiten: der lokale Server hat einen Slot, Suchen laufen parallel, das Zusammenfassen nicht.

## Bruchindikator
Die lokale Antwort beruft sich ueberwiegend auf fachfremde Treffer, oder der Waechter laesst eine Frage mit
eigenem Kohortennamen durch.

## Ablesung
Eigene Tests 2026-10-09: 5 Pruefungen (2 oeffentlich frei, 3 gesperrt: eigene Kohorte, Pfad, Person), eine lokale
und eine Cloud-Frage end-to-end. Code: system/guard/{ask_outside,daemon,lokal_recherche}.py, frag-draussen.

## Nachtrag 2026-10-09: Auftragsplaner lokal
`system/werkzeuge/plane "Ziel"` laesst das lokale 27B (mit Denken) ein Ziel in 3-6 aufeinander aufbauende Auftraege
zerlegen (Ziel, Schritte, Ausgabedatei, Abnahme-Stichworte); das Werkzeug setzt den Hausrahmen dazu (keine GPU,
Recherche nur ueber den Waechter, Quellenpflicht) und verkettet ueber BRAUCHT. Erste Probe "PVS-Segmentierung
recherchieren": 66 s, fuenf brauchbare Auftraege (Netze, Verluste, zweite Stufe, Empfehlung), einer schwach
(CPU-Zeit eines untrainierten Netzes). Lehre: Vorschau vor dem Einreihen lesen, weil ein schwacher Auftrag in
der Kette die folgenden blockiert. Streichen ohne neues Planen: `plane --aus <planordner> --weglassen 4 --einreihen`;
danach pruefen, ob spaetere Auftraege noch auf die gestrichene Ausgabe verweisen (hier: Auftrag 5 wollte die
CPU-Messung lesen, von Hand in plan.json korrigiert). Die PVS-Kette mit vier Auftraegen ist am 2026-10-09 10:40
eingereiht, Clara arbeitet sie seriell ab.

## Nachtrag 2026-10-23: twelve days without literature after the network switch
On 2026-10-13 the workstation moved to a LAN route that reaches the internet only through the hospital HTTP proxy. The
proxy variables went into `~/.config/environment.d/` and the user manager, so every unit started *after* that day
inherits them. The guard daemon had been running since 2026-10-12 and kept its old environment: every open-API lookup
(PubMed E-utilities, Europe PMC, OpenAlex, Semantic Scholar, arXiv, all via `urllib`) failed with "Connection refused". Own guard log: last
successful lookup 2026-10-11 18:20, then 129 failed lookups; the 04:00 morning research swarm reported
"FAILED (no answers)", 0 of 8 questions, every day from 2026-10-21 on (before that the local model was busy).
Fix 2026-10-23 17:17: `systemctl --user restart guard-daemon`, nothing else. The new process carries `https_proxy`
and a `no_proxy` that keeps loopback and the hospital domain direct; a public test question came back in 40 s with
PubMed/PMC sources. A scan of all running user services showed the other pre-switch services (chat GUI, agent loop,
QC viewer, wiki server, embedding server) are loopback-only and need no proxy; the agent loop must not have one.
Lesson: after a network or proxy change, compare the start time of every long-running service with the time of the
change (`ps -o lstart= -p <MainPID>`, `/proc/<pid>/environ`); `environment.d` reaches only processes started later.
Sources: systemd `environment.d(5)`, https://www.freedesktop.org/software/systemd/man/latest/environment.d.html
(read at user-manager start, inherited by units it starts); Python `urllib.request.getproxies()`,
https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies (reads the process environment);
own guard log and service scan, 2026-10-23.
First run after the fix, 2026-10-24 04:00: 8 of 8 areas researched in 39 min, but the commit failed: the wiki's pre-commit hook renders HTML with `python3`, which in the timer's PATH is the system Python without `python-markdown`. The hook now falls back to the conda Python when `import markdown` fails; the day's page was committed by hand under the timer's minimal PATH (130b1e1). Second lesson: test a repaired pipeline to its last step, here the push.

## Verknuepft
- [decision-model-as-profile-orchestrator](../open_checks/decision-model-as-profile-orchestrator.md)
- [lean-hermes-toolsets](lean-hermes-toolsets.md)
