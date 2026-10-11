---
id: epvs-2024-submissions-are-public-docker-images-metric-equals-ours
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: Docker-Hub-/Registry-API (hub.docker.com/u/epvschallenge, kleine Layer gelesen), Report arXiv 2512.18197 (PDF), hzlab/EPVS_challenge evaluate.py; PVS-Arena Alita, 2026-10-11 04:15
verweist_auf: [epvs-2024-data-open-for-certified-synapse-users, dora-baseline-is-plain-unet-and-field-evaluates-on-t2w, candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57]
---

# Die sechs EPVS-2024-Einreichungen liegen als oeffentliche Docker-Images vor, und die offizielle Metrik ist unsere Regel

## Aussage
Die Organisatoren haben die eingereichten Verfahren am 18.03.2025 oeffentlich auf Docker Hub gestellt (Konto epvschallenge):
big_aehrc_epvs_segment (CSIRO, Sieger; MedNeXt, 3D unter 2,5 mm Schichtdicke, sonst 2D; 9,8 GiB), ccnu (11,1), hufsaim (3,5),
bearwalker (nnU-Net, 3,6), shivai_miccai2024_image (4,8), epvs_nicvicorob (mit FreeSurfer 7.4.1, 21,8). Einheitliche Schnittstelle
`/workspace/run_inference.sh <checkpoint> <inDir> <outDir>`, Eingabe `<id>/<id>_T1w|T2w|FLAIR.nii.gz`. Die MODELLE sind damit ohne
Synapse-Freigabe nutzbar; nur die DATEN bleiben gesperrt. Die offizielle Metrik (evaluate.py) ist skimage-label connectivity=3
(26er), Treffer = irgendein Vorhersagevoxel auf der Referenzkomponente, keine IoU-Schwelle, keine Mindestgroesse -- exakt die
Regel von pvs-arena/pvs_metrik.py. Testzahlen des Siegers (ungesehener Standort mit dicken Schichten im Test): Recall/Precision
CSO 0,32/0,53 (F1 ~0,40), BG 0,51/0,62 (~0,56); Recall ist bei allen Teams der Engpass (CSO 0,14-0,35).

## Traegt
Turnierplanung: sechs vortrainierte Teilnehmer ohne Antrag, ein Image zur Zeit (Platte), Mini-Lauf vor dem Volllauf. Vergleich der
Regel: unsere VALDO-/HCP-F1-Zahlen sind mit den Challenge-Zahlen in der Regel vergleichbar, in den Daten nicht. Erwartung: die
Container sind konservativ (Precision > Recall) -- als Kandidatengeber fuer den Pool begrenzt, als Trenner-Signal moeglich.

## Traegt nicht
Lizenz der Teamcodes (in den Images nur MedNeXt-Apache und NVIDIA-Basislizenz, "(c)2024 CSIRO"): lokale Forschungsauswertung ja,
Weitergabe nein. Laufzeit auf CPU (Docker hier ohne GPU-Zugang) ist ungemessen.

## Bruchindikator
Ein Image verlangt ein anderes Eingabeformat oder liefert auf VALDO leere Masken; oder Docker Hub nimmt die Images offline.

## Ablesung
hub.docker.com/v2/repositories/epvschallenge/ (6 Repos, 173-932 Pulls); Registry-Manifeste und Konfigurations-Blobs; kleine Layer
mit run_inference.sh gelesen (Scratch cfg_*.json, layers/); Report Tabellen 2, 5, 7; hzlab/EPVS_challenge evaluate.py Zeilen 58-95.
Arena-Notizen: pvs-arena/literatur/epvs2024_teams.md, epvs2024_report.md; Versuch H in ARBEIT.md.

## Verknuepft
- [epvs-2024-data-open-for-certified-synapse-users](epvs-2024-data-open-for-certified-synapse-users.md)
- [dora-baseline-is-plain-unet-and-field-evaluates-on-t2w](dora-baseline-is-plain-unet-and-field-evaluates-on-t2w.md)
- [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57](candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57.md)
