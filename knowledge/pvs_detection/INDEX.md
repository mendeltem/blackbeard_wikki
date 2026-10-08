# pvs_detection

Perivaskulaere Raeume (PVS, Virchow-Robin; nicht periventrikulaer) im Hirn-MRT automatisch erkennen.
Eigene Kohorte BELOVE (103 Faelle, Patientendaten, nur Summen), Arena unter `~/data/work/pvs-arena`.
Methode: [lesion_detection_method](../lesion_detection_method/INDEX.md), Pruefpunkt
[pvs-apply-the-lesion-method](../lesion_detection_method/open_checks/pvs-apply-the-lesion-method.md).

Stand 2026-10-07. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt | Status |
|---|---|---|---|
| befund | [numeric-ids-became-char-codes-in-filenames](findings/numeric-ids-became-char-codes-in-filenames.md) | 30/103 Fehlschlaege der uebernommenen MATLAB-Pipeline sind char(Fallnummer) im Dateinamen; 73 Faelle haben Masken | getragen |
| befund | [public-pvs-reference-data-and-models-2026-10](findings/public-pvs-reference-data-and-models-2026-10.md) | VALDO T1, EPVS-2024 (Antrag), HCP-Aging (40 Hand); MedNet-PVS, SHIVA v4, PINGU, Frangi/RORPO | vorschlag |
| befund | [small-pvs-only-in-hcp-t2-reference](findings/small-pvs-only-in-hcp-t2-reference.md) | Edinburgh/Challenge-Referenzen beschneiden unter 3 mm; nur HCP-Aging-T2 (0,8 mm) traegt 1-Voxel-PVS; kein Werkzeugvergleich mit gemeinsamer Metrik | vorschlag |
| befund | [epvs-2024-data-open-for-certified-synapse-users](findings/epvs-2024-data-open-for-certified-synapse-users.md) | Synapse-API: keine Access Requirements, OPEN; Download nur mit zertifiziertem Konto + Token; "nur auf Anfrage" war falsch | getragen |
| befund | [hcp-aging-labels-are-mostly-unet-silver](findings/hcp-aging-labels-are-mostly-unet-silver.md) | 160/200 HCP-Masken sind U-Net-Vorhersagen, 40 Handfaelle unmarkiert, nur WM; VALDO-Inter-Rater F1 ~0,20 | vorschlag |
| befund | [edinburgh-pipeline-rules-in-voxels-contrast-filter-kills-small-pvs](findings/edinburgh-pipeline-rules-in-voxels-contrast-filter-kills-small-pvs.md) | Schwellen fast offen (0,05-0,25 SD); Auswahl durch Kontrast >= 0,19 SD, 3-2000 Voxel, Rand 90 %, alles in Voxeln auf 8 Geometrien; kein Formfilter | getragen |
| befund | [valdo-interrater-ceiling-and-drips-first-numbers](findings/valdo-interrater-ceiling-and-drips-first-numbers.md) | Inter-Rater F1 0,29 (Klasse 1-2: 0,17); DRIPS ohne Training T2 0,31 / SABRE 0,37, Recall 0,48, Precision 0,25, Kurve flach -> Ort statt Schwelle | vorschlag |
| befund | [drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third](findings/drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third.md) | 200 HCP-Faelle: DRIPS F1 0,55/0,58 (WM), OOF-Schwelle 0,15-0,2 stabil, Klasse 1-2 Recall 0,33; Frangi 0,28 | vorschlag |
| befund | [mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs](findings/mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs.md) | VALDO 12: MedNet-T1 0,44 (Prec 0,45, Klasse 1-2 nur 0,12), MedNet-T2 0,39, DRIPS 0,35 (Klasse 1-2 0,45), Rater 0,33; Kurven flach -> Pool + Trenner | vorschlag |
