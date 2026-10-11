---
id: touch-based-instance-metrics-need-a-volume-side-condition
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-11
herkunft: pvs_detection, Versuche G4/G4b/G4d (VALDO Task 1, 12 Handfaelle), 2026-10-11 17:40; Metrikregel identisch mit der offiziellen EPVS-2024-Auswertung
verweist_auf: [noise-floor-before-effects, show-what-a-rule-removes-before-trusting-it, count-cases-behind-pooled-numbers]
---

# Eine Instanz-Metrik mit Beruehrungsregel belohnt Verschmelzung -- Ranglisten brauchen Dice, Volumenverhaeltnis und Mehrfachtreffer als Nebenbedingung

## Regel
Zaehlt eine Metrik eine Referenzkomponente als Treffer, sobald irgendein Vorhersagevoxel sie beruehrt, und eine Vorhersagekomponente als
richtig, sobald sie irgendeine Referenz beruehrt, dann steigt der Instanz-F1, wenn Vorhersagen zu grossen Blobs verschmelzen: ein Blob,
der 86 Referenzen beruehrt, zaehlt als 86 Treffer und EINE richtige Vorhersage. Jede Massnahme, die Kandidaten wachsen laesst (niedrigere
Schwelle, Dilatation, Vereinigung mehrerer Detektoren), kann so "gewinnen", ohne besser zu detektieren.
Deshalb traegt jede Instanz-Rangliste drei Nebenzahlen: Dice, Vol_pred/Vol_ref und den Anteil der Vorhersagen mit >= 2 Referenzen.
Ein Lauf mit Vol_pred/Vol_ref > 2 oder Mehrfachtreffer-Anteil > 20 % zaehlt nicht als Gewinn, bis die Vorhersagen getrennt sind
(Wasserscheide auf dem Posterior, Ausgabe bis Halbmaximum) oder eine Zuordnung mit IoU-Schwelle bestaetigt.

## Belege
PVS auf VALDO (GBM-Trenner, 12 Faelle): Kandidatenschwelle 0,10 -> 0,02 -> 0,01 -> 0,005: Instanz-F1 0,591 -> 0,631 -> 0,658 -> 0,626,
gleichzeitig Dice 0,365 -> 0,307 -> 0,241 -> 0,156, Vol_pred/Vol_ref 1,4 -> 3,7 -> 7,4 -> 17, maximale Referenzen je Vorhersage 8 -> 38 -> 86 -> 243.
Die gepaarten Konfidenzintervalle der F1-Gewinne schlossen die Null aus -- die Statistik war sauber, die Metrik nicht.
Die offizielle EPVS-2024-Metrik (hzlab/EPVS_challenge, connectivity=3, Beruehrung) hat dieselbe Luecke.

## Verknuepft
- [noise-floor-before-effects](noise-floor-before-effects.md)
- [show-what-a-rule-removes-before-trusting-it](show-what-a-rule-removes-before-trusting-it.md)
- [count-cases-behind-pooled-numbers](count-cases-behind-pooled-numbers.md)
