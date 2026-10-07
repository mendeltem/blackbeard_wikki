# pvs_detection: Kurzstand 2026-10-07

- Neue Linie seit 2026-10-07 (Arena `~/data/work/pvs-arena`, Daten `~/data/work/pvs`). PVS = perivascular spaces.
- BELOVE: 103 Faelle, T1 ~1 mm (8 Geometrien, 8 Faelle 0,49 mm PSR), FLAIR 3-6 mm dick. Rechenebene T1.
- Uebernommene Edinburgh-MATLAB-Pipeline (RORPO): 73/103 Masken (Satz 11 = paramters_10, nbScales 10,
  GM-Schwelle 4). Die 30 Fehlschlaege sind ein Typfehler (Zahl -> Zeichen), keine Anatomie. MATLAB fehlt lokal.
- Masken: Hunderte Komponenten je Fall (280-920 nach Postprocessing). Metrik muss Zaehlung und Groessenklassen tragen.
- Keine Handreferenz. Oeffentlich: VALDO Task 1 (Zenodo), HCP-Aging PVS (OpenNeuro, 40 Hand), EPVS-2024 (Antrag).
- Modelle: MedNet-PVS (Apache, Gewichte CC BY), SHIVA v4 (NC), PINGU; Filter Frangi/RORPO. Metrik `pvs_metrik.py`.
- Nutzerwunsch: auch kleine PVS; Grenze ist die Voxelgroesse, Sensitivitaet nach Groessenklassen berichten.
