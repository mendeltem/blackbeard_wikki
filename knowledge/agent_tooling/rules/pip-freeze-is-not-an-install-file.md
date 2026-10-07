---
id: pip-freeze-is-not-an-install-file
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Repo cmb-valdo-chain, Install-Test aus frischem Clone, 2026-10-07
verweist_auf: [traceability-map-for-a-results-repo]
---

# Ein pip freeze ist ein Protokoll, keine Installationsdatei -- die Installation gilt erst nach dem Test aus dem frischen Clone

## Aussage
Ein `pip freeze` der Arbeitsumgebung als `requirements-lock.txt` auszuliefern sieht nach
Reproduzierbarkeit aus und scheitert in der ersten Zeile: (1) Build-Kennungen wie
`torch==2.6.0+cu124` oder `torch_cluster==1.6.3%2Bpt26cu124` liegen nicht auf PyPI, das
`%2B` ist fuer pip sogar ein Syntaxfehler (sofortiger Abbruch, nichts installiert);
(2) die Datei enthaelt alles, was je in der Umgebung lag (160 Pakete, TensorFlow,
Graph-Bibliotheken), nicht das, was der Code importiert. Regel:

1. Die Installationsdatei enthaelt nur, was der Code importiert (`grep -rhoE '^(import|from) \w+'`
   ueber das Paket, gegen die Standardbibliothek gefiltert), mit den Versionen der
   Arbeitsumgebung gepinnt; schwere Rahmen (torch) mit ihrem eigenen Index separat davor.
2. Das volle `pip freeze` bleibt als `requirements-full-record.txt` mit Kopfzeile
   "Protokoll, nicht installierbar" -- es ist ein Beleg, kein Werkzeug.
3. Getestet ist eine Installation erst, wenn sie aus einem FRISCHEN Clone in einer NEUEN
   Umgebung mit genau den README-Befehlen bis zum Selbsttest laeuft; das Log gehoert ins Repo
   (`docs/INSTALL-TEST.md`). Der zweite Fund dieses Tests war ein `tqdm`-Import im
   Selbsttest, den die Hauptdatei nicht nannte.

## Traegt
Jedes Repo, dessen README "pip install -r" verspricht; besonders Forschungscode, der in
einer gewachsenen conda-Umgebung entstand.

## Traegt nicht
Container-Images oder conda-lock-Dateien mit explizitem Kanal und Build: dort ist das
volle Abbild die Installationsdatei.

## Bruchindikator
Ein frischer Clone, der mit der minimalen Datei installiert und dessen Selbsttest trotzdem
an einem fehlenden Paket scheitert -- dann fehlt ein Import in der Grep-Liste (dynamische
Importe, optionale Pfade).

## Ablesung
Eigener Test 2026-10-07: Lock-Datei rc=1 in Sekunde 1; minimale Datei + torch-CPU + tqdm:
SELFTEST PASSED in neuer Umgebung. Tier 1a.

## Verknuepft
- [traceability-map-for-a-results-repo](traceability-map-for-a-results-repo.md)
