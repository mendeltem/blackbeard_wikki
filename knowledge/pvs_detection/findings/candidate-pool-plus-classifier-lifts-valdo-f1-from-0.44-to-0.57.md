---
id: candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-08
herkunft: PVS-Arena Alita, Versuch F1 (Pilot zweite Stufe), VALDO Task 1, 12 Maskenfaelle, leave-one-case-out, 2026-10-08 05:25
verweist_auf: [mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs, sensitivity-needs-a-discriminator, one-shared-candidate-classifier-for-all-cohorts, noise-floor-before-effects]
---

# Ein kleiner Trenner auf dem Kandidaten-Pool zweier Detektoren hebt den PVS-F1 auf VALDO von 0,44 auf 0,57 -- die CMB-Lektion wiederholt sich

## Aussage
Kandidaten = 26er-Komponenten der Vereinigung von DRIPS-T2 (Posterior >= 0,1, empfindlich, synthetisch trainiert) und
MedNet-PVS-T1w (Softmax >= 0,5, praezise, klinisch trainiert). Je Komponente 30 Merkmale ohne gelernte Filter: Groesse,
Ausdehnung, PCA-Linearitaet/Elongation, Zugehoerigkeit zu A/B/beiden, Posterior-Mittel/-Max beider Netze, z-Intensitaet
T1/T2/FLAIR innen und in der 1-Voxel-Huelle, SynthSeg-Gruppe am Schwerpunkt und Gruppenanteile der Huelle. Ziel: Komponente
beruehrt die Rater-1-Referenz. HistGradientBoosting, leave-one-case-out ueber 12 Faelle, Entscheidungsschwelle je Falte auf den
Trainingsfaellen (0,35-0,45, stabil). Ergebnis gegen Rater 1 (SABRE Ganzhirn, RSS Region): F1 0,572 [0,537; 0,606], Precision
0,70, Recall 0,51, Klasse 1-2 Voxel 0,30; je Fall 0,46-0,65. Zum Vergleich: MedNet-T1 allein 0,440 [0,366; 0,508] (Precision
0,45), Vereinigung 0,409 (Recall 0,72 = Decke), Schnitt 0,352, Inter-Rater 0,327. Erwartung vor dem Lauf war 0,46-0,52.

**Nachtrag 08.10. 07:20 (Ablationen und dritter Detektor, LOO, n = 12):** ohne Lage-Merkmale 0,571, ohne Netz-Posteriors
0,569, ohne Posteriors und Zugehoerigkeit 0,560, ohne Form 0,553, ohne T1-Intensitaeten 0,563, **ohne alle Intensitaeten 0,509**.
Der Gewinn kommt aus den Intensitaeten von Komponente und 1-Voxel-Huelle in T1/T2/FLAIR (die Netze sehen je eine Sequenz, der
Trenner drei), etwas aus der Form, nichts aus Lage oder Netz-Wahrscheinlichkeiten: ein Trenner, kein Ensemble. Startwerte 1/2
identisch (deterministischer GBM). Pool aus drei Detektoren (+ PINGU, F1 allein 0,449 = MedNet-T1): 0,582 [0,543; 0,619].

## Traegt
Die PVS-Arena und den Plan: Fortschritt kommt aus dem Trenner auf dem Pool, und zwar aus Mehr-Sequenz-Intensitaeten um den Kandidaten;, nicht aus Detektor-Rezepten oder Schwellen (vierte
Bestaetigung nach CMB-VALDO, CMB-SWI und den flachen PVS-Schwellenkurven). Vorgehen fuer BELOVE ohne eigene Labels: Pool aus
DRIPS-T1 und MedNet-T1, Trenner auf VALDO trainiert, dann Rating.

## Traegt nicht
n = 12, gelernt wird der Stil von Rater 1; Startwert-Rauschen des GBM noch nicht gemessen (laeuft); Merkmalswichtigkeit offen;
Uebertrag auf EPVS-2024, HCP und BELOVE offen. VALDO-Faelle mischen 1-mm- und 0,5-mm-Gitter.

## Bruchindikator
Auf EPVS-2024 oder BELOVE-Rating bringt der Trenner gegenueber MedNet-T1 keinen Gewinn, oder die Ablation zeigt, dass nur die
Posteriors tragen (dann ist es ein Ensemble, kein Trenner).

## Ablesung
pvs-arena/skripte/zweite_stufe_pilot.py, ergebnisse/valdo-task1/stufe2-pilot-drips-t2-mednet-t1/{zusammenfassung.json,ergebnis.csv},
logs/stufe2_pilot_valdo.log, ARBEIT.md 05:25-05:30.

## Verknuepft
- [mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs](mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs.md)
- [sensitivity-needs-a-discriminator](../../lesion_detection_method/mechanisms/sensitivity-needs-a-discriminator.md)
- [one-shared-candidate-classifier-for-all-cohorts](../../cmb_detection/findings/one-shared-candidate-classifier-for-all-cohorts.md)
- [noise-floor-before-effects](../../lesion_detection_method/rules/noise-floor-before-effects.md)
