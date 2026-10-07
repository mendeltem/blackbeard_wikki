---
id: public-pvs-reference-data-and-models-2026-10
typ: befund
status: vorschlag
stand: 2026-10-07
thema: knowledge/pvs_detection
herkunft: Webrecherche zweier Sonnet-Agenten im PVS-Cluster Alita, 2026-10-07 (Details pvs-arena/literatur/)
verweist_auf: [reference-first-then-metric-then-model, operating-points-do-not-transfer]
---

# Oeffentliche PVS-Referenzdaten und vortrainierte Modelle, Stand Oktober 2026

## Aussage
Drei Quellen mit Handreferenz: (1) VALDO 2021 Task 1, 40 Trainingsfaelle, T1/T2/FLAIR, Referenz
lueckenhaft (Ganzhirn-Masken nur SABRE, RSS Teilschichten und Zaehlungen), Zenodo 4687995, CC BY-NC;
(2) EPVS Segmentation Challenge MICCAI 2024, 200 Faelle, Handmasken CSO+BG, drei Standorte, nur auf
Antrag (Synapse syn54100278), bester Test-Dice 0,33 CSO / 0,44 BG, Einbruch auf ungesehener Kohorte;
(3) HCP-Aging PVS, 200 T2 0,8 mm, OpenNeuro ds005595, CC BY-ND, nur 40 handkorrigiert, Rest Silver.
Vortrainiert und lokal lauffaehig: MedNet-PVS (MedNeXt, T1w klinisch und T2w HCP, Apache 2.0,
Gewichte CC BY 4.0, figshare braucht Browser-User-Agent), SHIVA-PVS v4 (T1 oder T1+FLAIR, TF >= 2.17,
CC BY-NC-SA, Gewichte nur per Browser), PINGU (nnU-Net v1, T1, ohne Lizenzangabe). Filter: Frangi
(skimage), RORPO (C++/pybind). Alle publizierten Zahlen stammen aus verschiedenen Kohorten und sind
nicht vergleichbar; ausserhalb des Trainingsstandorts bricht jede Methode ein.

## Traegt
Aufbau einer PVS-Arena: Referenz zuerst oeffentlich (HCP-40, VALDO), eigene Kohorte danach.

## Traegt nicht
Eignung fuer kleine PVS unter 1 mm; dafuer traegt kein 1-mm-T1. Nicht geprueft: PMC12782799
("Comprehensive Evaluation of Multiple ePVS Segmentation Tools"), segcsvd_PVS, Lizenz EPVS-2024.

## Bruchindikator
Ein weiterer offener Datensatz mit Voxel-Handlabels taucht auf (Repositorien nicht direkt durchsucht).

## Ablesung
Webseiten und arXiv (2208.07167, 2512.18197, 2508.20256, 2405.08337), DOIs nicht alle nachgeprueft;
Tabellen in `pvs-arena/literatur/datensaetze.md` und `methoden.md`.

## Verknuepft
- [reference-first-then-metric-then-model](../../lesion_detection_method/rules/reference-first-then-metric-then-model.md)
- [operating-points-do-not-transfer](../../lesion_detection_method/rules/operating-points-do-not-transfer.md)
