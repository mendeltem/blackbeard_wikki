---
id: small-pvs-only-in-hcp-t2-reference
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-07
herkunft: Literaturrunde 2 im PVS-Cluster Alita (Sonnet-Agent, ~17 Aufrufe), 2026-10-07; Details pvs-arena/literatur/vergleich_und_kleine_pvs.md
verweist_auf: [public-pvs-reference-data-and-models-2026-10, reference-first-then-metric-then-model, geometry-follows-the-acquisition]
---

# Kleine PVS stehen nur in der HCP-Aging-T2-Referenz; Edinburgh- und Challenge-Referenzen sind nach unten beschnitten

## Aussage
Wer PVS unterhalb von 3 mm Laenge finden will, braucht eine Referenz, die sie enthaelt. Die Edinburgh-Pipeline
(Ballerini 2018) verwirft Komponenten unter 3 mm Laenge, und die EPVS-Challenge-2024-Referenz folgt deren Vorgaben;
typische Referenz-PVS bei 1 mm T1 haben 4 bis 9 Voxel (Rashid 2023, Tab. S2). Die HCP-Aging-T2-Masken (0,8 mm
isotrop, OpenNeuro ds005595) enthalten PVS bis zu einer Voxeldicke, Inter-Rater-Dice 0,97 laut Preprint, aber nur
im Marklager und nur 40 der 200 Faelle sind handkorrigiert (welche, ist im Datensatz nicht markiert). Im
rauschfreien Phantom (Bernal 2022, Duarte Coello 2024) findet Frangi bei 1 mm Zylinder ab 1 mm Durchmesser und 2 mm
Laenge, RORPO noch 0,4 mm; T1 allein verpasst kleine PVS (Valdes Hernandez 2024, 228 Faelle; Rashid: T2 0,81/0,83
gegen T1 0,63/0,77 Sensitivitaet/Praezision). Keine gefundene Studie misst, ob 1-2-Voxel-Kandidaten bei 1 mm T1
echte PVS oder Rauschen sind. Vergleiche mehrerer Werkzeuge auf denselben Daten gibt es kaum: Waymont 2024
(NeuroImage 297:120685) zaehlt 112 Arbeiten, 67 Ansaetze, keine vergleichbaren Metriken; LeFevre 2026
(Alzheimer's & Dementia, n = 30) nennt nur fuer das hauseigene nnU-Net Zahlen (Dice BG 0,73, WM 0,63).

## Traegt
Wahl der Referenz fuer eine PVS-Arena mit dem Ziel "auch kleine PVS": kleine Klassen auf HCP-T2 messen,
T1-Modelle dagegen pruefen; Mindestgroesse als Kurve fahren; 1-2-Voxel-Treffer bei 1 mm T1 als Klasse "unsicher".

## Traegt nicht
Ob die kleinen HCP-Markierungen klinisch relevante PVS sind; STRIVE-, Potter- und 7-T-Angaben stammen aus
Suchzusammenfassungen, nicht aus gelesenen Volltexten.

## Bruchindikator
Ein Datensatz mit 1-mm-T1-Handlabels, der 1-2-Voxel-PVS enthaelt und Inter-Rater-Werte dafuer berichtet.

## Ablesung
arXiv 2512.18197 (EPVS-Challenge, Tabellen gelesen), Ballerini 2018 (arXiv 1704.07699), Bernal 2022
(doi 10.1016/j.mri.2022.07.016), Rashid 2023, Waymont 2024 (PDF), medRxiv 2025.03.19.25324269 (HCP-Aging);
DOIs teils nicht nachgeprueft, siehe Datei.

## Verknuepft
- [public-pvs-reference-data-and-models-2026-10](public-pvs-reference-data-and-models-2026-10.md)
- [reference-first-then-metric-then-model](../../lesion_detection_method/rules/reference-first-then-metric-then-model.md)
- [geometry-follows-the-acquisition](../../lesion_detection_method/mechanisms/geometry-follows-the-acquisition.md)
