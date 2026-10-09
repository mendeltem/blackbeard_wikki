---
id: guarded-outbound-research-local-first
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-09
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

## Verknuepft
- [decision-model-as-profile-orchestrator](../open_checks/decision-model-as-profile-orchestrator.md)
- [lean-hermes-toolsets](lean-hermes-toolsets.md)
