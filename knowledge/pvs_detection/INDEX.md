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
