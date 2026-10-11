---
id: candidate-threshold-0.02-lifts-valdo-f1-0.59-to-0.65-small-pvs-recall-doubles
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: PVS-Arena Alita, F7.8 (skripte/kandidatendecke.py) und Versuch G4 (skripte/zweite_stufe_cnn.py --ta 0.02), VALDO Task 1 12 Handfaelle referenz_v2, LOO, 2026-10-11 14:40
verweist_auf: [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57, patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision, patch-cnn-second-stage-adds-nothing-on-valdo]
---

# Die Kandidatendecke war der Hebel: DRIPS-Schwelle 0,02 statt 0,10 hebt VALDO von 0,591 auf 0,650 und verdoppelt den Recall kleiner PVS

## Aussage
Zaehlung (F7.8): bei DRIPS-Posterior >= 0,10 traegt nur 45 % der Referenzkomponenten der Klasse 1-2 Voxel ueberhaupt einen Kandidaten
(VALDO; HCP 34 %), bei 0,02 sind es 75 % (HCP 63 %) bei 2,3x (2,0x) Kandidaten. Versuch G4 (Dreier-Pool DRIPS ∪ MedNet-T1 ∪ PINGU,
DRIPS-Schwelle 0,02, zweite Stufe GBM auf 35 Handmerkmalen bzw. Mischung GBM+Patch-CNN, LOO, Schwelle auf zurueckgehaltenen Faellen):
GBM 0,631 [0,586; 0,669], Mischung 0,650 [0,600; 0,697]; gepaart gegen Schwelle 0,10: GBM +0,040 [+0,013; +0,069] (9/12), Mischung +0,070
[+0,034; +0,107] (11/12). Gepoolt: Recall 0,526 -> 0,693 bei Praezision 0,72 -> 0,71 (Mischung 0,74); Klasse 1-2 Recall 0,31 -> 0,53,
TP 56 -> 101. Beide Geometrien gewinnen (SABRE 0,575 -> 0,643, RSS 0,584 -> 0,658). Mit den vielen schwachen Kandidaten traegt auch das
CNN in der Mischung (+0,019 [+0,007; +0,033]), waehrend es bei 0,10 nichts brachte.

## Traegt
Reihenfolge der Hebel bei Kandidat-plus-Trenner-Ketten: ERST die Decke messen (Anteil der Referenz, der ueberhaupt Kandidat ist, je
Groessenklasse), DANN den Trenner verbessern. Eine zweite Stufe, die Praezision liefert, erlaubt einen viel empfindlicheren
Kandidatengeber; die alte Schwelle 0,10 (aus der OOF-Kurve des Einzelverfahrens) war fuer die Kette falsch. Ziel "kleine PVS" ist damit
zum ersten Mal spuerbar bewegt. Neuer VALDO-Stand 0,650 (Inter-Rater 0,327).

## Traegt nicht
Wo der Tausch endet (0,01? MedNet/PINGU-Schwellen 0,3?) und ob HCP gleich reagiert, ist offen (G4b, G4-HCP). 12 Faelle, KI-Breite ~0,05.
BELOVE ohne T2: DRIPS-T1-Decke dort nicht gemessen.

## Bruchindikator
Auf HCP (200) bringt 0,02 statt 0,10 keinen gepaarten Gewinn, oder die Praezision bricht bei 0,01 ein, ohne dass der Recall weiter steigt.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/kandidatendecke-drips-t2 und hcp-aging/kandidatendecke-drips-t2 (zusammenfassung.json);
ergebnisse/valdo-task1/stufe2-cnn-pool3-ta002/{gbm,mix}; gepaarte Rechnung ARBEIT.md 11.10. 14:40.

## Nachtrag 2026-10-11 16:05: der Tausch endet bei 0,01/0,3 noch nicht (G4b)
DRIPS 0,01, MedNet-T1 0,3, PINGU 0,3 (12.356 Kandidaten, 3,4x): GBM 0,658 [0,610; 0,704], gepaart gegen 0,02/0,5 +0,027 [+0,003; +0,052] (9/12);
gepoolt Praezision 0,744 -> 0,779 UND Recall 0,693 -> 0,766, Klasse 1-2 Recall 0,66. Die 0,5-Mischung mit dem CNN liegt hier gleichauf (0,657, -0,001):
bei sehr vielen schwachen Kandidaten traegt das GBM die Posterior-Merkmale allein. Neuer VALDO-Stand 0,658; 0,005/0,2 wird geprueft (G4d).

## Verknuepft
- [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57](candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57.md)
- [patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision](patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision.md)
- [patch-cnn-second-stage-adds-nothing-on-valdo](patch-cnn-second-stage-adds-nothing-on-valdo.md)
