---
id: pvs-apply-the-lesion-method
typ: pruefpunkt
status: offen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: PVS-Cluster (Alita, angelegt 2026-09-15), Bestandsaufnahme der Daten 2026-10-07; Uebertragung aus CMB/WMH
verweist_auf: [reference-first-then-metric-then-model, pipeline-failures-and-names-before-tuning, sensitivity-needs-a-discriminator, false-alarms-cluster-by-anatomy, geometry-follows-the-acquisition, operating-points-do-not-transfer, count-cases-behind-pooled-numbers]
---

# PVS: die Laesionsmethode anwenden, bevor ein Modell gebaut wird

## Aussage
Ausgangslage (gezaehlt, nicht geschaetzt): eine Kohorte von 103 Faellen mit je T1 (1 mm
isotrop) und FLAIR (0,86 x 0,86 x 5 mm, 27 Schichten); eine uebernommene MATLAB-Pipeline
(FreeSurfer, FSL, RORPO-Vesselness auf T1, WMH-Ausschluss ueber FLAIR) mit elf
Schwellensaetzen und einem vollen Lauf (Satz 11); 31 von 103 Faellen mit technischen
Fehlschlaegen (Orientierung T1, Dateityp); keine Handreferenz gesichtet. PVS sind
perivaskulaere Raeume (Virchow-Robin), nicht periventrikulaer.

Uebertragung, in dieser Reihenfolge, mit erwartetem Aufwand:
1. **Referenz klaeren** (Tage, keine GPU). Gibt es Handzeichnungen oder visuelle
   Ratings (Skala je Region: Basalganglien, Centrum semiovale, Mittelhirn, Hippocampus)?
   Wenn nein: 20 bis 30 zufaellige Faelle von Hand bewerten lassen, bevor eine Schwelle
   bewegt wird. Die OUTPUT-Ordner sind keine Wahrheit. [reference-first-then-metric-then-model]
2. **Fehlschlaege reparieren und Zwischenausgaben zaehlen** (Stunden). 31 Fehlschlaege
   klingen nach Technik; jede Ausgabe (T1-Normierung, RORPO-Karte, PVS-Maske,
   WMH-Ausschluss) einmal oeffnen, Voxel zaehlen, Masken-Anteil Nicht-Hirn messen.
   Pipeline in eigenen Worten beschreiben und am MATLAB-Code pruefen (welcher Filter,
   welche Sequenz, welche Maske wirklich). [pipeline-failures-and-names-before-tuning]
3. **Mass festlegen**: je Instanz (PVS-Zaehlung und Volumen je Region), gepaart je Fall
   mit Bootstrap; Verteilung je Fall mitberichten (PVS-Lasten sind schief).
   [count-cases-behind-pooled-numbers]
4. **Die elf Schwellensaetze als Kurve lesen, nicht als Kandidaten.** Jeder Satz ist ein
   Arbeitspunkt der Vesselness-Schwellen; wiederherstellen, womit Satz 11 gewaehlt wurde.
   Fortschritt kommt nicht aus Satz 12, sondern aus einem Trenner: PVS gegen Gefaess,
   gegen Lakune, gegen WMH. Erwartung: eine zweite Stufe (kleiner Kandidaten-
   Klassifikator auf RORPO-Kandidaten, Merkmale Form, Lage, T1/FLAIR-Verhaeltnis).
   [sensitivity-needs-a-discriminator], [operating-points-do-not-transfer]
5. **Fehlalarme nach Ort zaehlen** (Stunden, CPU) auf der Stichprobe aus 1: Anteil in
   Sulci, Kortex, Ventrikelnaehe, WMH-Rand. Vorsicht: PVS tragen selbst Liquorsignal,
   die Ortsregel darf nur ueber Lage gehen, nicht ueber Intensitaetsklasse.
   [false-alarms-cluster-by-anatomy]
6. **Rechenebene = T1.** 1 mm isotrop traegt das Signal; FLAIR mit 5 mm nur als grobe
   Nebenbedingung (WMH-Ausschluss), nie als Eingabe eines feinen Netzes ohne
   anisotrope erste Ebene. [geometry-follows-the-acquisition]
7. Erst danach ein lernendes Modell, und nur mit Rauschboden (drei Startwerte) und
   vorab festgelegter Regel. [noise-floor-before-effects]

## Traegt
Diesen PVS-Cluster; sinngemaess jede uebernommene Laesionspipeline mit Parameterdateien
und ohne Referenz.

## Traegt nicht
Die Punkte 4 bis 7 sind Erwartungen aus CMB/WMH, keine PVS-Messungen. Ob eine zweite
Stufe bei PVS traegt, ist offen; die Verwechsler (Gefaesse, Lakunen) sind andere.

## Bruchindikator
Punkt 1 ergibt eine belastbare Referenz mit hoher Uebereinstimmung zur Pipeline-Ausgabe
(ueber dem Rauschboden) -- dann ist die Pipeline die Referenz, und die Reihenfolge kippt
auf 2, 3, 5.

## Ablesung
Datenlage eigene Zaehlung 2026-09-15 und 2026-10-07 (Patientendaten, nur Summen).
Uebertragung: Erfahrungswerte aus den verknuepften Eintraegen. Visuelle PVS-Skala:
Potter et al., Cerebrovasc Dis 2015, doi:10.1159/000375153 (DOI nicht nachgeprueft).

## Verknuepft
- [reference-first-then-metric-then-model](../rules/reference-first-then-metric-then-model.md)
- [pipeline-failures-and-names-before-tuning](../rules/pipeline-failures-and-names-before-tuning.md)
- [sensitivity-needs-a-discriminator](../mechanisms/sensitivity-needs-a-discriminator.md)
- [false-alarms-cluster-by-anatomy](../mechanisms/false-alarms-cluster-by-anatomy.md)
- [geometry-follows-the-acquisition](../mechanisms/geometry-follows-the-acquisition.md)
- [operating-points-do-not-transfer](../rules/operating-points-do-not-transfer.md)
- [count-cases-behind-pooled-numbers](../rules/count-cases-behind-pooled-numbers.md)
