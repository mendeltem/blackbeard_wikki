---
id: edinburgh-pipeline-rules-in-voxels-contrast-filter-kills-small-pvs
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-07
herkunft: MATLAB-Code der uebernommenen Edinburgh-PVS-Pipeline am Code gelesen (Sonnet-Agent + eigene Pruefung der Nachverarbeitung), PVS-Cluster Alita, 2026-10-07; pvs-arena/daten/PIPELINE-EDINBURGH.md
verweist_auf: [numeric-ids-became-char-codes-in-filenames, pipeline-failures-and-names-before-tuning, geometry-follows-the-acquisition, operating-points-do-not-transfer]
---

# Die Edinburgh-PVS-Pipeline entscheidet in der Nachverarbeitung, in Voxeln, und ihr Kontrastfilter frisst die kleinen PVS

## Aussage
Die uebernommene Pipeline (RORPO-Vesselness auf dem z-normierten, invertierten T1; Suchraum WM + tiefe Kerne +
Mittelhirn aus SynthSeg) setzt ihre Vesselness-Schwellen absolut auf einer 0..255-Skala; die in zehn Saetzen
durchprobierten Werte 3 bis 8 entsprechen 0,05 bis 0,25 SD -- die Schwellenstufe ist fast offen. Die eigentliche
Auswahl treffen fuenf Regeln danach (PVS_Postprocessing, Utils/getDefaultOptions.m:112-119): Kontrast Objekt gegen
1-Voxel-Schale >= 6 Grauwerte (0,19 SD), Groesse 3 bis 2000 Voxel, Randanteil am ROI < 90 %, dazu RORPO-Mindestpfad
3 Voxel und eine WM-Erosion um ceil(1/Voxelkante). Alle Regeln rechnen in VOXELN, nicht in mm: auf einer Kohorte mit
acht T1-Geometrien (0,39 bis 1 mm) ist das je Scanner ein anderes Verfahren. Fuer kleine PVS ist der Kontrastfilter
der Hauptverlust (Teilvolumen druekt den Kontrast unter die Schwelle), dann die 3-Voxel-Grenzen. Ein Formfilter fehlt.
Nebenbefunde: `_PVS_WMH_excluded` wird VOR dem WMH-Abzug gespeichert (Name irrefuehrend); das Alters-Template wird
immer auf 55 Jahre erzwungen; die Zaehl-/Volumenanalyse wird vom Hauptlauf nicht aufgerufen (keine Masstabelle).

## Traegt
Deutung der BELOVE-Pipeline-Masken als Vergleichsgroesse (konservativ, gitterabhaengig, kleine PVS fehlen systematisch);
jede MATLAB-freie Nachbildung (Frangi/RORPO + ROI + Regeln in mm, Kontrastfilter als Kurve). Allgemein: bei uebernommenen
Pipelines die Nachverarbeitung zuerst lesen -- dort steht der Arbeitspunkt, nicht in den "Schwellen"-Dateien.

## Traegt nicht
Zahlen zur Wirkung jeder Regel (nicht gemessen, nur aus dem Code gefolgert); RORPO-Pfadlaengen des Binaries unbekannt;
scborderFilter-Wirkungslosigkeit ist Folgerung, kein Lauf.

## Bruchindikator
Eine Ablation je Regel auf Handreferenz zeigt, dass der Kontrastfilter kleine PVS NICHT ueberproportional entfernt.

## Ablesung
PVS_lib: PVS_Postprocessing/{PVSPostprocessing,contrastFilter,volumeFilter,borderFilter}.m, Utils/getDefaultOptions.m,
PVS_Segmentation/{VSLFilter,getThresholdImage,PVSSegROI}.m, Structural_Brain_Segmentation/PVSROI.m, checkOptions.m;
Belege mit Zeilen in pvs-arena/daten/PIPELINE-EDINBURGH.md.

## Verknuepft
- [numeric-ids-became-char-codes-in-filenames](numeric-ids-became-char-codes-in-filenames.md)
- [pipeline-failures-and-names-before-tuning](../../lesion_detection_method/rules/pipeline-failures-and-names-before-tuning.md)
- [geometry-follows-the-acquisition](../../lesion_detection_method/mechanisms/geometry-follows-the-acquisition.md)
- [operating-points-do-not-transfer](../../lesion_detection_method/rules/operating-points-do-not-transfer.md)
