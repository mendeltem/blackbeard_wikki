---
id: drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-08
herkunft: PVS-Arena Alita, Versuch C1 (DRIPS auf allen 200 HCP-Aging-Faellen, CPU) und Clara wp5 (Frangi), 2026-10-07/08
verweist_auf: [valdo-interrater-ceiling-and-drips-first-numbers, hcp-aging-labels-are-mostly-unet-silver, sensitivity-needs-a-discriminator, operating-points-do-not-transfer]
---

# DRIPS auf HCP-Aging: F1 0,55-0,58 ohne Training, Arbeitspunkt 0,15-0,2 stabil, ein Drittel der 1-2-Voxel-PVS -- Frangi bei 0,28

## Aussage
Auf allen 200 HCP-Aging-Faellen (T2 0,8 mm; Labels: 40 Hand, 160 U-Net-Silber, nur weisse Substanz) erreicht DRIPS
(synthetisch trainiert, Standardschwelle 0,1, CPU 70 s/Fall) Instanz-F1 0,549 [0,536; 0,562]; auf die SynthSeg-WM-Maske
beschnitten 0,584 (die Beschneidung entfernt nur Nicht-Annotiertes, also Label-Abdeckung, kein Modellgewinn). Recall 0,65,
Precision 0,51-0,56, Zaehlkorrelation je Fall Spearman 0,67-0,69. Schwellenkurve: Maximum 0,559 bei 0,15-0,2, out-of-fold
gewaehlte Falten-Schwellen 0,15/0,2/0,15/0,2/0,2 -> OOF-F1 0,558: der Arbeitspunkt ist auf 200 Faellen stabil, auf VALDO mit
12 Faellen springt er (0,1-0,3). Precision steigt mit der Schwelle bis 0,69, F1 nicht -- dieselbe flache Kurve wie auf VALDO.
Groessenklassen (Recall): 1-2 Voxel 0,33 bei Schwelle 0,1, 0,24 bei OOF-Schwelle; 3-5: 0,57; 6-20: 0,81; >20: 0,96.
Frangi mit festem Perzentil (99,0) auf denselben Daten: F1 0,279, Klasse 1-2 0,12; bei 99,8: 0,19 und 0,01.

## Traegt
Grundlinie und Arbeitspunkt fuer die PVS-Arena: DRIPS bei 0,1 plus Trenner (nicht hoehere Schwelle), weil die OOF-Schwelle
Precision mit den kleinsten PVS bezahlt (0,33 -> 0,24), die das Nutzerziel ausdruecklich will. Bestaetigt auf der dritten
Laesionslinie: Schwellen sind Arbeitspunkte, Fortschritt braucht einen Trenner.

## Traegt nicht
Experten-Wahrheit: 160 der 200 Masken stammen aus einem Frangi+U-Net; die Zahl misst Uebereinstimmung damit. Die ehrlichen
Punkte sind VALDO (0,33-0,35, Inter-Rater 0,29) und spaeter EPVS-2024. Basalganglien sind in HCP nicht markiert.

## Bruchindikator
Die 40 Handfaelle werden bekannt und DRIPS liegt dort deutlich unter 0,5; oder eine Ortsregel/zweite Stufe hebt den F1 nicht.

## Ablesung
pvs-arena/ergebnisse/hcp-aging/{drips-t010,drips-t010-wm,frangi-p990}/zusammenfassung.json, drips-t010_schwellenkurve.json
(skripte/schwellenkurve_oof.py), ARBEIT.md 02:00. Daten OpenNeuro ds005595 (CC BY-ND, lokal).

## Verknuepft
- [valdo-interrater-ceiling-and-drips-first-numbers](valdo-interrater-ceiling-and-drips-first-numbers.md)
- [hcp-aging-labels-are-mostly-unet-silver](hcp-aging-labels-are-mostly-unet-silver.md)
- [sensitivity-needs-a-discriminator](../../lesion_detection_method/mechanisms/sensitivity-needs-a-discriminator.md)
- [operating-points-do-not-transfer](../../lesion_detection_method/rules/operating-points-do-not-transfer.md)
