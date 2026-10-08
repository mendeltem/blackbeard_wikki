---
id: check-what-a-region-file-means-before-the-first-number
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-08
herkunft: PVS-Arena Alita, VALDO Task 1, 2026-10-08 04:15 (Fehler des Cloud-Agenten, von Claras Inventar vorher angezeigt)
verweist_auf: [reference-first-then-metric-then-model, find-the-definition-before-interpreting-a-difference]
---

# Eine "Region"-Datei kann Zaehlgebiet, Annotationsgebiet oder Auswertegebiet bedeuten: vor der ersten Zahl messen, wie viel Referenz ausserhalb liegt

## Aussage
VALDO Task 1 liefert je Fall eine Regions-Maske und Masken. Auf der SABRE-Kohorte sind die Masken Ganzhirn, die Regions-Maske
aber nur die Slabs, in denen gezaehlt wurde (Count.csv: value, count, min_slice, max_slice). Die Arena-Metrik beschnitt
Referenz und Vorhersage auf die Region und warf damit 1070 von 1424 Rater-1-Komponenten weg; alle SABRE-Zahlen eines halben
Tages (Inter-Rater 0,29, DRIPS 0,37) galten nur fuer die Slabs. Das Inventar des lokalen Agenten hatte "in_regions = nein" fuer
SABRE gemeldet; der Cloud-Agent las es als Randungenauigkeit statt als Widerspruch. Aufgedeckt erst durch eine Zaehlung der
Komponenten je Regions-Label (Schwerpunkt), die 75 % auf Label 0 zeigte.
Vorschrift: vor der ersten Metrik je Kohorte den Anteil der Referenzkomponenten ausserhalb jeder benutzten Maske ausgeben
(eine Zeile); liegt er ueber wenigen Prozent, ist die Maske nicht die Annotationsgrenze. "in_regions = nein" ist ein Befund,
keine Fussnote.

## Traegt
Jede Challenge- oder Kohortenreferenz mit Zusatzmasken (Region, ROI, Slab, Hirnmaske); jede Metrik, die Vorhersagen auf eine
Maske beschneidet.

## Traegt nicht
Kohorten, deren Masken nachweislich innerhalb der Region liegen (VALDO RSS: in_regions = ja, Beschneidung bleibt richtig).

## Bruchindikator
Keiner; Vorbedingung.

## Ablesung
pvs-arena/ARBEIT.md 04:15-04:20, daten/valdo-task1/inventar.md (Spalte in-Regions), VALDO README (Count.csv-Felder).

## Verknuepft
- [reference-first-then-metric-then-model](reference-first-then-metric-then-model.md)
- [find-the-definition-before-interpreting-a-difference](../../agent_tooling/rules/find-the-definition-before-interpreting-a-difference.md)
