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

**Nachtrag 12.10.2026 (nachmittags), ganze Seite kopieren, nie nur den Index:** Eine QC-Seite ist Index + Mosaik-Sprites + info.json
als EIN Stand. Nach dem Neubau der DEMDAS-GM-Seite (11.10. 18:48) wurde nur index.html in den Spiegel kopiert, die Sprites blieben
vom 17:31-Bau (Kachelhoehe 163 statt 160 px). Die Seite schnitt die Kacheln am falschen Versatz: oben in jedem Bild ein bunter
Streifen aus dem unteren Ende der Nachbarschicht, vom Nutzer als "Label ausserhalb des Hirns" gemeldet. Abhilfe: Kopie immer als
`rsync -rt --delete` des ganzen Seitenordners (Bau -> Spiegel -> Stick) und danach `qc_mirror_check.py` (demdas-gm): prueft je
Kopie rsync-Trockenlauf gegen den Bau und je Sprite die Bildgroesse gegen das Kachelraster aus info.json (cols*w, rows*h).
Allgemeiner Pruefpunkt: zeigt ein Betrachter am Bildrand Inhalt einer anderen Schicht, zuerst Sprite-Groesse gegen Raster pruefen,
bevor man die Segmentierung verdaechtigt (Inselsuche in der Segmentierung war hier negativ: 0 Inseln >= 50 Voxel in 62 von 63 Sitzungen).

## Traegt
Jede Abgabe ueber den QC-Stick; parallele Sitzungen, die denselben Stick beschreiben.

## Traegt nicht
Daten, die nur auf dem Stick liegen (MODEL/, Sicherungen) -- die haben eigene Quellen.

## Bruchindikator
Eine Seite, die nur auf dem Stick existiert; ein Index, der im Spiegel aelter ist als auf dem Stick; ein Index, der juenger ist als seine Sprites (Kachelraster passt nicht zur Bildgroesse).

## Ablesung
12.10.2026 09:23-09:35 (Fehlen bemerkt, Spiegel gefunden, Kopie zurueck, alle Seiten per cmp geprueft 09:59).

## Verknuepft
- [qc-pages-english-sessions-in-one-window](qc-pages-english-sessions-in-one-window.md)
