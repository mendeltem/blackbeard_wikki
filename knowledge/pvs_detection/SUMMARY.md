# pvs_detection: Kurzstand 2026-10-07

- Neue Linie seit 2026-10-07 (Arena `~/data/work/pvs-arena`, Daten `~/data/work/pvs`). PVS = perivascular spaces.
- BELOVE: 103 Faelle, T1 ~1 mm (8 Geometrien, 8 Faelle 0,49 mm PSR), FLAIR 3-6 mm dick. Rechenebene T1.
- Uebernommene Edinburgh-MATLAB-Pipeline (RORPO): 73/103 Masken (Satz 11 = paramters_10, nbScales 10,
  GM-Schwelle 4). Die 30 Fehlschlaege sind ein Typfehler (Zahl -> Zeichen), keine Anatomie. MATLAB fehlt lokal.
- Masken: Hunderte Komponenten je Fall (280-920 nach Postprocessing). Metrik muss Zaehlung und Groessenklassen tragen.
- Keine Handreferenz. Oeffentlich: VALDO Task 1 (Zenodo), HCP-Aging PVS (OpenNeuro, 40 Hand), EPVS-2024 (Antrag).
- Modelle: MedNet-PVS (Apache, Gewichte CC BY), SHIVA v4 (NC), PINGU; Filter Frangi/RORPO. Metrik `pvs_metrik.py`.
- Nutzerwunsch: auch kleine PVS; Grenze ist die Voxelgroesse, Sensitivitaet nach Groessenklassen berichten.
- Literatur Runde 2 (07.10.): kleine PVS stehen nur in der HCP-T2-Referenz; Edinburgh verwirft < 3 mm; kein belegter
  Werkzeugvergleich mit gemeinsamer Metrik (Waymont 2024: 67 Ansaetze). MedNet-PVS-Gewichte: figshare defekt, Drive komplett.
- Metrik pvs_metrik.py misst jetzt Recall und Fehlalarmanteil je Groessenklasse (1-2, 3-5, 6-20, >20 Voxel).
- Nutzerziel 07.10. abends: Instanz-F1 maximieren; Plan A-F in pvs-arena/ARBEIT.md (Grundlinien, vortrainiert, Ortsregel, nnU-Net, zweite Stufe).
- Runde 3 (07.10. abends): EPVS-2024-Daten sind OPEN fuer zertifizierte Synapse-Nutzer (kein Antrag; Skript
  pvs-arena/skripte/epvs2024_synapse_laden.sh). HCP-Aging: 160/200 Masken sind U-Net-Silber, 40 Handfaelle nicht gekennzeichnet,
  nur WM -> Entwicklungsdaten, nicht Experten-Wahrheit. VALDO-Rater: Dice 0,53, F1 ~0,20 (Etikett-Decke niedrig). VALDO-Metrik:
  6er-Nachbarschaft, IoU > 10 %. Keine weiteren oeffentlichen Voxelmasken-Saetze; DoRA-PVS-Challenge 2026 verteilt keine Daten.
  Zweite Stufe: Startmerkmale aus MAPS-T1 (T1 < 0,9 Median, FLAIR < Mittel+SD, Linearitaet > 80 %), Gewinn selbst messen.
- Pipeline am Code (07.10.): Schwellen fast offen, Auswahl in der Nachverarbeitung (Kontrast 0,19 SD, 3-2000 Voxel, Rand 90 %),
  alles in Voxeln -> je Scanner ein anderes Verfahren; Kontrastfilter ist der Hauptverlust kleiner PVS. DRIPS (Bernal, Apache,
  Docker, Domain Randomisation) als vortrainiertes Verfahren G aufgenommen. STRIVE-2: Groesse trennt PVS/Lakune nicht, FLAIR-Rand und Form schon.
- ERSTE ZAHLEN (07.10. 23:00): VALDO Inter-Rater F1 0,29; DRIPS (synthetisch trainiert, Docker) auf T2 0,31 (SABRE 0,37), Recall 0,48,
  Precision 0,25, Schwellenkurve flach, Klasse 1-2 Recall 0,33 -> naechster Hebel Fehlalarme nach Ort (Clara wp7). Frangi auf HCP 0,16.
- 08.10. 02:00: DRIPS auf 200 HCP: F1 0,55 (0,58 WM-beschnitten), OOF-Schwelle 0,15-0,2 stabil, Klasse 1-2 Recall 0,33 bei 0,1;
  Frangi 0,28. VALDO (12): DRIPS-T2 0,35, T1 0,33, beide ueber Inter-Rater 0,29. Hebel: Ortsregel/zweite Stufe, nicht Schwelle.
- KORREKTUR 08.10. 04:20: VALDO-SABRE-Masken sind Ganzhirn, Regions = Zaehl-Slabs. Korrigiert: Inter-Rater 0,33; MedNet-T2 0,39,
  DRIPS-T2 0,35 (Klasse 1-2 Recall 0,45), DRIPS-T1 0,35. DRIPS gewinnt SABRE, MedNet-T2 gewinnt RSS; MedNet-T2 vs Rater 2 nur 0,07.
- 08.10. 05:00: MedNet-T1w (klinische T1) fuehrt VALDO mit F1 0,44 (Precision 0,45), findet aber die 1-2-Voxel-PVS am schlechtesten
  (0,12); DRIPS findet sie am besten (0,45). Naechster Schritt: Kandidaten-Pool DRIPS ∪ MedNet-T1 + Trenner.
- DURCHBRUCH 08.10. 05:25: zweite Stufe (Pool DRIPS ∪ MedNet-T1 + kleiner GBM-Trenner, LOO) auf VALDO F1 0,57 [0,54; 0,61] gegen 0,44;
  Precision 0,70, Klasse 1-2 0,30. Die CMB-Lektion (Trenner statt Schwelle) gilt auch fuer PVS. Offen: Rauschboden, Merkmale, EPVS/BELOVE.
- 08.10. 07:20: Ablation der zweiten Stufe: Mehr-Sequenz-Intensitaeten (Komponente vs Huelle) tragen den Gewinn (-0,06 ohne), Form -0,02,
  Lage und Posteriors 0; Pool aus drei Detektoren 0,58. PINGU auf VALDO 0,45 = MedNet-T1 (publizierte Dice ordneten falsch).
- 08.10. 13:00: Trenner auf HCP (200 Faelle, ein Detektor, nur T2): F1 0,58 -> 0,67 [0,66; 0,68], Precision 0,80 -- der Gewinn der
  zweiten Stufe haelt auf grosser Stichprobe und mit einer Sequenz. Clara wp7: Fehlalarme sitzen im WM, Ortsregel traegt nicht.

**Befund, neu 2026-10-08 (Alita):** Die PVS-Kette steht als Dokument: zwei Detektoren auf T1 (DRIPS >= 0,10 empfindlich, MedNet >= 0,50 praezise), Pool der 26er-Komponenten, 29 Merkmale (Form, Posterior, z-Intensitaeten innen/Huelle, SynthSeg-Gruppen), HistGradientBoosting-Trenner auf VALDO Rater 1 mit Schwelle 0,4. VALDO LOO 0,57 gegen 0,44; HCP-Aging 200 Faelle nur T2, nur DRIPS: 0,668 [0,657; 0,680] gegen 0,584. Eigene Kohorte ohne Referenz: Uebereinstimmung mit der Pipeline-Maske 0,35 (Praezision 0,83, Recall 0,23), 95 % der 1-2-Voxel-Kandidaten verworfen; QC-Schichtbetrachter lokal fuer die Expertensicht, Rating der 25 Faelle entscheidet.
