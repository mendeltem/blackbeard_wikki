---
id: pvs-chain-as-built-2026-10
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-08
herkunft: Projekt pvs-arena (Alita), ARBEIT.md Abschnitte F1, F6.2, F3, QC-Betrachter 2026-10-08
verweist_auf: [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57, mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs, drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third, edinburgh-pipeline-rules-in-voxels-contrast-filter-kills-small-pvs, show-what-a-rule-removes-before-trusting-it]
---

# Die PVS-Kette, wie sie am 08.10.2026 gebaut ist: zwei Detektoren, ein Kandidatenpool, ein Trenner mit 29 Merkmalen

## Aussage
Die Kette ist die Uebertragung der Mikroblutungs-Methode auf perivaskulaere Raeume:
Kandidaten breit sammeln, dann eine zweite Stufe entscheiden lassen. Schritt fuer Schritt:

1. **Eingabe.** T1w 1 mm isotrop (RAS), dazu FLAIR auf T1 registriert (eigene Kohorte:
   FLAIR 0,86 x 0,86 x 5 mm; HCP-Aging nur T2; VALDO Task 1 T1 + T2 + FLAIR). Keine
   Schaedelentfernung, keine Intensitaetsnormierung ausser der je Detektor.
2. **Detektor A: DRIPS** (3D U-Net, oeffentliche Gewichte) auf T1, Posterior >= 0,10.
   Der empfindliche Detektor: auf HCP-Aging allein F1 0,58, kleine PVS (1-2 Voxel) Recall 0,34.
3. **Detektor B: MedNet-PVS** (klinischer Trainer) auf T1, Posterior >= 0,50. Der praezise
   Detektor: auf der eigenen Kohorte Praezision 0,77 gegen die Pipeline-Maske, findet aber
   nur ein Viertel der Komponenten und fast keine kleinen.
4. **Kandidatenpool.** 26-verbundene Komponenten der Vereinigung A ∪ B. Eigene Kohorte,
   73 Faelle: 36.618 Kandidaten (A-nur 21.467, beide 12.696, B-nur 2.455).
5. **29 Merkmale je Komponente.** Groesse, Ausdehnung, PCA-Linearitaet und Elongation;
   Mitgliedschaft in A / B / beiden; Posterior-Mittel und -Maximum beider Detektoren;
   z-normierte Intensitaet T1 und FLAIR innen und in der 1-Voxel-Huelle samt Differenz;
   SynthSeg-Gruppe am Schwerpunkt und Gruppenanteile in der Huelle (WM, Basalganglien,
   Kortex, Liquor, Stamm). Ohne T2, weil die eigene Kohorte keines hat.
6. **Trenner.** HistGradientBoosting, trainiert auf VALDO Task 1 (12 Faelle, 4.083
   Kandidaten, 1.156 positiv = beruehrt die Rater-1-Referenz), Schwelle 0,4. Auf VALDO
   leave-one-case-out F1 0,57 gegen 0,44 des besten Einzeldetektors; auf HCP-Aging in der
   schwaechsten Form (nur DRIPS, nur T2, 5-fach nach Fall, 200 Faelle) 0,668 [0,657; 0,680]
   gegen 0,584.
7. **Ausgabe.** Behaltene Komponenten als Maske und Liste (p, Voxel, Herkunft). Eigene
   Kohorte: 12.130 von 36.618 behalten (33 %); von den 12.841 Kandidaten mit 1-2 Voxeln
   nur 597 (5 %).
8. **Vergleich ohne Wahrheit.** Gegen die MATLAB-Pipeline-Maske (RORPO, Satz 11,
   Kontrast- und Groessenfilter) F1 0,348 [0,321; 0,375], Recall 0,23, Praezision 0,83.
   Das ist Uebereinstimmung, keine Genauigkeit: die Pipeline wirft kleine Komponenten
   selbst weg und fehlt bei 31 von 103 Faellen.
9. **Qualitaetskontrolle.** Schichtbetrachter wie bei den Mikroblutungen (zwei grosse
   axiale Bilder, links Pipeline-Maske blau, rechts schaltbar: behalten gruen, verworfen
   orange, DRIPS, MedNet; Zaehler je Schicht und Fall als Uebereinstimmung beschriftet).
   Nur lokal (127.0.0.1), fuer die Expertensicht. Dazu die verblindete Bewertungsseite
   fuer 25 Faelle (Kandidaten bestaetigen statt zeichnen) als erste Handreferenz.

## Traegt
- Die Reihenfolge "breit sammeln, dann trennen" traegt auf drei Datensaetzen (VALDO,
  HCP-Aging, eigene Kohorte in der Uebereinstimmung) und mit einer wie mit drei Sequenzen.
- Der Trenner ersetzt Ortsregeln: die Fehlalarme sitzen im WM und sind klein, eine
  Regel nach Ort hilft auf VALDO nicht (wp7), Intensitaets- und Formmerkmale schon.
- Form, Posterior und Lage reichen fuer die Untergrenze (HCP: nur T2). Jede weitere
  Sequenz hebt (VALDO-Ablationen: ohne T1 -0,009, ohne alles ausser Form deutlich mehr).

## Traegt nicht
- Genauigkeit auf der eigenen Kohorte: ohne Handreferenz sind alle Zahlen dort
  Uebereinstimmung mit einer Pipeline, die selbst nicht Wahrheit ist.
- Kleine PVS (1-2 Voxel): der Trenner im Rater-1-Stil wirft 95 % davon weg; ob das
  richtig ist, entscheidet nur das Rating.
- HCP-Labels sind zu 80 % U-Net-Silber: ein Teil des HCP-Gewinns kann Silber-Echo sein.
- Dicke FLAIR (5 mm) auf der eigenen Kohorte: die FLAIR-Merkmale sind dort groeber als
  im Training (VALDO).

## Bruchindikator
Das Rating der 25 Faelle zeigt, dass die vom Trenner verworfenen kleinen Kandidaten
mehrheitlich echte PVS sind (dann ist die Schwelle 0,4 oder der Rater-1-Stil falsch fuer
die eigene Kohorte), oder die Praezision der behaltenen faellt unter 0,7.

## Ablesung
Eigene Messungen in pvs-arena/ARBEIT.md (F1, F2, F3, F6.1, F6.2), pvs_metrik.py
(Komponenten-F1, Bootstrap ueber Faelle). Eigene Kohorte nur als Summen, nie Einzelfaelle;
Betrachter und Bewertungsseite verlassen das Haus nicht. Code als Repository
`pvs-arena-chain` (privat, ohne Daten).

## Nachtrag 2026-10-08: oeffentliche QC-Seite
VALDO Task 1 (12 Faelle, Rater 1) als oeffentliche QC-Seite mit dem Wiki-Tool qc_slice_viewer:
https://mendeltem.github.io/valdo-pvs-qc/ (Urteilsmodus und Vergleich der Teile; Zaehler der Seite =
Messskript 903 / 335 / 878; CC BY-NC 4.0). Die eigene Kohorte bleibt lokal.

## Verknuepft
- [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57](candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57.md)
- [mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs](mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs.md)
- [drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third](drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third.md)
- [edinburgh-pipeline-rules-in-voxels-contrast-filter-kills-small-pvs](edinburgh-pipeline-rules-in-voxels-contrast-filter-kills-small-pvs.md)
- [show-what-a-rule-removes-before-trusting-it](../../lesion_detection_method/rules/show-what-a-rule-removes-before-trusting-it.md)
