# Installation

## Geprüfte Umgebung
Linux, Python 3.13.15, keine GPU, 2026-10-02. Nur der Rechenkern `wmh_post.py` und seine Tests.

## Abhängigkeiten
Für `wmh_post.py` und die Tests:
```
numpy==2.5.3
scipy==1.18.1
nibabel==5.4.2
```

Für den vollen Ablauf im Skill, hier nicht geprüft:
- FSL 6.0.7.18 (`bianca`, `fast`, `flirt`, `fslmaths`, `bet`)
- FreeSurfer ab 7.2 (`mri_synthseg`, `mri_synthsr`, `mri_synthstrip`)
- HD-BET (`hd-bet`)
- pandas und openpyxl für die Ergebnistabellen
- MNI152 T1 1 mm, hirnextrahiert (liegt in FSL unter `data/standard`)
- ein mit `--saveclassifierdata` gespeicherter BIANCA-Klassifikator

## Schritte
1. Ordner kopieren.
2. `pip install numpy scipy nibabel`
3. Prüfen:
```
cd tools/mri/mri_segmentation/wmh/bianca_flair_wmh
python -m unittest discover -s tests
```
