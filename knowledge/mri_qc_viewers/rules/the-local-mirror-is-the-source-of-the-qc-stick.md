---
id: the-local-mirror-is-the-source-of-the-qc-stick
typ: regel
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-12
herkunft: 12.10.2026: QUALITY_CONTROLL/index.html war um 09:23 vom Stick verschwunden (andere Sitzung oder Kopiervorgang), aus ~/QUALITY_CONTROLL wiederhergestellt
verweist_auf: [qc-pages-english-sessions-in-one-window]
---

# Der Stick ist eine Kopie: Quelle jeder Stick-Seite ist der lokale Spiegel ~/QUALITY_CONTROLL

## Aussage
Jede Seite wird zuerst in den Spiegel `~/QUALITY_CONTROLL/<Bereich>/...` geschrieben (bzw. aus dem Projektordner dorthin
kopiert) und von dort auf den Stick. Index-Aenderungen immer im Spiegel machen und kopieren, nie nur auf dem Stick. Vor dem
Abziehen des Sticks: `sync`, dann je geaenderte Seite `cmp` Spiegel gegen Stick, dann `lsof +D` auf dem Stick (Browser-Tabs
halten Dateien offen). Verschwindet eine Datei vom Stick, ist der Spiegel die Wahrheit.

## Traegt
Jede Abgabe ueber den QC-Stick; parallele Sitzungen, die denselben Stick beschreiben.

## Traegt nicht
Daten, die nur auf dem Stick liegen (MODEL/, Sicherungen) -- die haben eigene Quellen.

## Bruchindikator
Eine Seite, die nur auf dem Stick existiert; ein Index, der im Spiegel aelter ist als auf dem Stick.

## Ablesung
12.10.2026 09:23-09:35 (Fehlen bemerkt, Spiegel gefunden, Kopie zurueck, alle Seiten per cmp geprueft 09:59).

## Verknuepft
- [qc-pages-english-sessions-in-one-window](qc-pages-english-sessions-in-one-window.md)
