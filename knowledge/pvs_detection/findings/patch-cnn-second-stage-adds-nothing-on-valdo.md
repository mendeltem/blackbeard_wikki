---
id: patch-cnn-second-stage-adds-nothing-on-valdo
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: PVS-Arena Alita, Versuch G (skripte/zweite_stufe_cnn.py), VALDO Task 1, 12 Faelle mit Handmasken, referenz_v2, LOO, 2026-10-11 04:29
verweist_auf: [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57]
---

# Ein Patch-CNN als zweite Stufe bringt bei PVS auf VALDO nichts -- der CMB-Hebel uebertraegt sich nicht

## Aussage
Auf den Kandidaten des Dreier-Pools (DRIPS-T2 ∪ MedNet-T1 ∪ PINGU) wurde ein kleines 3D-CNN (16-mm-Wuerfel, 7 Kanaele T1z/T2z/
FLAIRz/Maske/3 Posteriors, 3 Startwerte, 25 Epochen) gegen den HistGradientBoosting-Trenner auf 35 Handmerkmalen gemessen,
gleiches Protokoll (LOO je Fall, Schwelle auf zurueckgehaltenen Faellen): CNN allein 0,517 [0,433; 0,578], GBM 0,591 [0,558; 0,623],
Mischung 0,580 [0,538; 0,615]. Gepaart: Mischung - GBM -0,011 [-0,033; +0,007], besser in 4/12; CNN - GBM -0,074 [-0,145; -0,020].
Groessenklasse 1-2 unveraendert (Recall 0,31 / 0,31 / 0,27). Der CNN-Verlust sitzt in den RSS-Faellen (0,49 mm, 106-171 Kandidaten
je Fall): sub-209 0,156 gegen 0,525. Nebenbefund: Schwelle auf zurueckgehaltenen statt Trainingsfaellen aendert den GBM um +0,009.

## Traegt
Hebelwahl bei PVS: die zweite Stufe lebt von den Intensitaetsmerkmalen (FLAIR/T2-Huelle), die das GBM schon hat; ein gelerntes
Filter auf ~1000 positiven Komponenten aus 9 Faellen bringt keine Information dazu. Der Kontrast zur CMB-Linie (+0,045 durch das
gemeinsame CNN) ist eine Fallzahl- und Erscheinungsfrage, kein Widerspruch. Zwei Geometrien in 12 Faellen sind fuer ein CNN zu wenig.

## Traegt nicht
HCP-Aging (200 Faelle, eine Geometrie, zehnmal mehr Positive) ist nicht gemessen -- dort koennte das CNN anders ausfallen (G2 geplant).
Andere CNN-Groessen, laengeres Training, Vortraining ohne Etiketten wurden nicht probiert.

## Bruchindikator
Auf HCP (5-fach, nur T2, DRIPS-Kandidaten) hebt die Mischung den Trenner um mehr als 0,02 gegen 0,668.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/stufe2-cnn-pool3/{cnn,gbm,mix}/zusammenfassung.json; gepaarte Rechnung in ARBEIT.md 11.10. 04:30.

## Verknuepft
- [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57](candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57.md)
