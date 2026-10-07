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
