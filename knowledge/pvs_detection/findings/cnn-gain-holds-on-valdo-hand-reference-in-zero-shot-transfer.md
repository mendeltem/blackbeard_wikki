---
id: cnn-gain-holds-on-valdo-hand-reference-in-zero-shot-transfer
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: PVS-Arena Alita, Versuche G3a/G3b (skripte/zweite_stufe_cnn.py, Uebertragsmodus), VALDO Task 1 12 Handfaelle referenz_v2, 2026-10-11 12:51
verweist_auf: [patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision, patch-cnn-second-stage-adds-nothing-on-valdo, hcp-aging-labels-are-mostly-unet-silver]
---

# Der CNN-Gewinn der zweiten Stufe hält auf VALDO-Handreferenzen (+0,061 gepaart), der Zero-Shot-Uebertrag selbst ist unbrauchbar

## Aussage
Auf denselben VALDO-Kandidaten (DRIPS-T2 >= 0,1, nur T2) und gleicher Schwellenlogik: VALDO-intern (LOO, 11 Trainingsfaelle) GBM 0,412,
CNN 0,417, Mischung 0,425 (gepaart +0,014 [-0,019; +0,038], SABRE +0,038 / RSS -0,011). Zero-Shot von HCP (200 Faelle, nur WM-Silber)
auf VALDO: GBM 0,256, CNN 0,321, Mischung 0,317 -- alle unter DRIPS allein (0,354), weil der HCP-Trenner auf VALDO zu viel wegwirft
(GBM-Recall 0,19). Aber gepaart Mischung - GBM +0,061 [+0,019; +0,111], CNN - GBM +0,065 [+0,008; +0,131], besser in 9/12, auch auf RSS.
Der relative CNN-Gewinn aus HCP (+0,035) ist damit auf Handreferenzen belegt; der absolute Zero-Shot-Uebertrag nicht.

## Traegt
Die zweite Stufe fuer PVS soll ein CNN enthalten, aber auf der Zielkohorte feingetunt werden: Vortraining HCP + Feintuning VALDO (G5)
ist der naechste Hebel, nicht Zero-Shot. Auf VALDO tragen T1+FLAIR und der Dreier-Pool weit mehr (0,591) als jede T2-only-Stufe (0,425).

## Traegt nicht
Ob das CNN kleine PVS (Klasse 1-2) findet: in allen Varianten Recall 0,11-0,32, die Decke liegt beim Kandidatengeber (F7.8/G4).
BELOVE (kein T2) ist von diesem Befund nicht abgedeckt.

## Bruchindikator
Feintuning auf VALDO (G5) hebt die T2-only-Mischung nicht ueber 0,425 oder den Dreier-Pool-Trenner nicht ueber 0,591.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/stufe2-cnn-drips-t2only-loo (G3a) und stufe2-cnn-uebertrag-hcp (G3b), gepaarte Rechnung in ARBEIT.md
11.10. 12:17/12:51. Fehlerlehre: ID-Kollision sub-101..106 zwischen HCP und VALDO (Regel case-ids-are-dataset-local-prefix-when-pooling).

## Verknuepft
- [patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision](patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision.md)
- [patch-cnn-second-stage-adds-nothing-on-valdo](patch-cnn-second-stage-adds-nothing-on-valdo.md)
- [hcp-aging-labels-are-mostly-unet-silver](hcp-aging-labels-are-mostly-unet-silver.md)
