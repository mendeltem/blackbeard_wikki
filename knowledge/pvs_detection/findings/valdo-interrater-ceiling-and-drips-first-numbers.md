---
id: valdo-interrater-ceiling-and-drips-first-numbers
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-08
herkunft: PVS-Arena Alita, Clara wp4 (Inter-Rater-Kette) und Versuch C2 (DRIPS auf VALDO Task 1), 2026-10-07 22:00-23:00
verweist_auf: [hcp-aging-labels-are-mostly-unet-silver, reference-first-then-metric-then-model, sensitivity-needs-a-discriminator, false-alarms-cluster-by-anatomy]
---

# VALDO Task 1: Rater stimmen zu F1 0,29 ueberein; ein synthetisch trainiertes Netz erreicht diese Decke ohne Training, mit Recall statt Precision

## Aussage
**Korrektur 2026-10-08 04:20:** Die VALDO-Regions-Datei ist bei SABRE nur die Zaehl-Slab-Maske, die PVSSeg-Masken sind
Ganzhirn; die Zahlen vom 07.10. beschnitten drei Viertel der SABRE-Referenz. Korrigiert (SABRE Ganzhirn, RSS mit Region, n = 12):
Inter-Rater F1 0,327 [0,253; 0,397] (Klasse 1-2: 0,34); MedNet-PVS-T2w (auf HCP trainiert) 0,388 [0,302; 0,468], DRIPS-T2 0,354
[0,260; 0,448], DRIPS-T1 0,351; DRIPS-T2 trifft 45 % der 1-2-Voxel-Referenz, MedNet-T2 19 %. DRIPS gewinnt SABRE (0,38 vs 0,30),
MedNet-T2 gewinnt RSS (0,47 vs 0,32). MedNet-T2 gegen Rater 2 nur 0,07 (verschiedene PVS-Populationen, offen). Der urspruengliche
Text unten bleibt als Beleg des Fehlers stehen.

Auf VALDO Task 1 (12 von 40 Trainingsfaellen haben Masken; 6 SABRE-Faelle mit zwei Ratern) betraegt die Uebereinstimmung
Rater 2 gegen Rater 1 mit der Arena-Metrik (26er-Komponenten, Beruehrung = Treffer, Region beschnitten) F1 0,294
[0,230; 0,363], Dice 0,24; in der Klasse 1-2 Voxel nur 0,17. Rater 2 markiert 2- bis 7-mal weniger PVS als Rater 1.
DRIPS (Bitar/Bernal 2025, nur auf synthetischen Roehren trainiert, Docker, CPU 70 s/Fall) erreicht ohne jedes Training
auf T2 gegen Rater 1 F1 0,309 (n = 8; nur SABRE 0,369, also UEBER der Inter-Rater-Grenze), auf T1 0,260; gegen Rater 2
0,20. Recall 0,48-0,51, Precision 0,20-0,25; die Schwellenkurve 0,05-0,6 ist flach (F1 0,28-0,31), Precision steigt
hoechstens auf 0,42 bei fallendem Recall. Klasse 1-2 Voxel: Recall 0,33 (T2) bei 88 % Fehlalarmanteil. Frangi mit fester
Perzentilschwelle liegt auf HCP-Labels bei F1 0,16.

## Traegt
Deutung jeder PVS-Zahl auf VALDO: Werte ueber ~0,3 gegen einen Rater sind Naehe zu dessen Stil, nicht "besser als Mensch";
beide Rater berichten. Hebelwahl: nicht die Schwelle (flach), sondern Fehlalarme nach Ort zaehlen und eine Ortsregel oder
zweite Stufe bauen (Wiki-Mechanismen bestaetigen sich auf der dritten Linie). Kleine PVS sind erreichbar (ein Drittel),
aber nur mit einem Trenner bezahlbar.

## Traegt nicht
n = 8 bzw. 6 Faelle: Intervalle breit, Richtungsangabe. Vier RSS-Faelle fehlten (Speicherabbruch) und laufen nach.
Keine Aussage ueber HCP (laeuft) oder EPVS-2024 (noch nicht geladen).

## Bruchindikator
Mit allen 12 Faellen oder auf EPVS-2024 faellt DRIPS-T2 deutlich unter 0,25, oder eine Ortsregel entfernt keine Fehlalarme
ohne Treffer zu kosten.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/{rater2-gegen-rater1,drips-t2-t010,drips-t1-t010}/zusammenfassung.json, Schwellenkurve
in ARBEIT.md 23:00; pvs_metrik.py mit Groessenklassen. Oeffentliche Daten (CC BY-NC 4.0).

## Verknuepft
- [hcp-aging-labels-are-mostly-unet-silver](hcp-aging-labels-are-mostly-unet-silver.md)
- [reference-first-then-metric-then-model](../../lesion_detection_method/rules/reference-first-then-metric-then-model.md)
- [sensitivity-needs-a-discriminator](../../lesion_detection_method/mechanisms/sensitivity-needs-a-discriminator.md)
- [false-alarms-cluster-by-anatomy](../../lesion_detection_method/mechanisms/false-alarms-cluster-by-anatomy.md)
