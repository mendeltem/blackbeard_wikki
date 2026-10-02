---
id: bianca_flair_wmh
bereich: tools/mri/mri_segmentation/wmh
stand: 2026-10-02
herkunft: Projekt BIANCA Inference
sprache: prompt (Skill) und python
---

# bianca_flair_wmh

## Zweck
Hält fest, wie Mendel White Matter Hyperintensities auf FLAIR segmentiert: Preprocessing, BIANCA-Inferenz mit vortrainiertem Klassifikator, Postprocessing mit Schwelle, WM-Masking und Aufteilung in periventrikulär und tief, dazu das QC.

Zwei Teile:
- [src/SKILL.md](src/SKILL.md): der Ablauf als Skill für einen Agenten, mit den exakten Befehlen, den gesetzten Werten und den Fallen, die im Projekt aufgetreten sind.
- [src/wmh_post.py](src/wmh_post.py): der Rechenkern des Postprocessings als kleine Bibliothek. LPM plus WM- und Ventrikelmaske hinein, Masken und Volumina heraus. Braucht kein FSL.

## Wann verwenden, wann nicht
Verwenden, wenn ein Agent WMH-Volumina aus FLAIR rechnen, eine bestehende WMH-Pipeline prüfen oder den Methodenteil dazu schreiben soll. `wmh_post.py` allein, wenn eine LPM schon vorliegt und nur Schwelle, Masking und PV/tief fehlen.

Nicht verwenden als fertige Pipeline. Die Stufen 1 und 2 (HD-BET, FAST, SynthSeg, SynthSR, FLIRT, BIANCA) stehen hier nur als Befehle im Skill, nicht als lauffähiger Code. Die vollständigen Skripte mit SLURM-Orchestrierung, QC-Report und Editor liegen im Projekt BIANCA Inference und sind noch nicht in dieser Wiki (siehe Grenzen).

Nicht verwenden ohne FLAIR und ohne vortrainierten Klassifikator.

## Aufruf
Skill: `src/SKILL.md` als Skill laden oder dem Agenten als Kontext geben.

Rechenkern:
```python
import sys
sys.path.insert(0, "tools/mri/mri_segmentation/wmh/bianca_flair_wmh/src")
import nibabel as nib
import wmh_post as wp

P = "/pfad/zum/subject"
r = wp.postprocess(nib.load(P + "/sub-001_LPM.nii.gz"),
                   nib.load(P + "/sub-001_WMmask.nii.gz"),
                   nib.load(P + "/sub-001_vent.nii.gz"),
                   thr=0.90, pv_dist_mm=10.0)
print(r["wm_ml"], r["pv_ml"], r["deep_ml"])
wp.save_mask_like(r["wm"], r["ref"], P + "/sub-001_thr" + r["tag"] + "_WM.nii.gz")
```

## Eingabe und Ausgabe
Eingabe: LPM im FLAIR-Raum, WM-Maske und Ventrikelmaske in beliebigem Gitter desselben Weltraums (typisch 1 mm isotrop aus SynthSeg), optional eine Infarktmaske.

Ausgabe von `postprocess()`: dict mit den Arrays `raw`, `wm`, `pv`, `deep` im LPM-Gitter, dem Referenzbild `ref` und den Volumina `raw_ml`, `wm_ml`, `pv_ml`, `deep_ml`, `wm_mask_ml`, `lesion_mask_ml`. `pv_ml + deep_ml == wm_ml`. Bei leerer Ventrikelmaske sind `pv`, `deep` und ihre Volumina `None`.

## Teststand
2026-10-02, Linux, Python 3.13.15, numpy 2.5.3, scipy 1.18.1, nibabel 5.4.2, im Werkzeugordner:
`python -m unittest discover -s tests` → 11 Tests, bestanden.

Geprüft auf einem Phantom mit zwei Gittern (FLAIR 2 x 2 x 5 mm, Segmentierung 1 mm): Masken kommen auf dem FLAIR-Gitter an, PV und tief sind disjunkt und ergeben zusammen die WM-maskierte Karte, die Distanz ist in mm, die PV-Grenze folgt dem Parameter, Läsions-Removal greift, leere Ventrikelmaske und leere LPM.

Nicht geprüft: alles, was FSL, FreeSurfer oder HD-BET braucht. Die Befehle im Skill sind aus dem Projektcode abgeschrieben und in dieser Umgebung nicht gelaufen. Der Skill selbst wurde nicht an einem Agenten erprobt.

Ein Test prüft weniger, als sein Name sagt: `test_saved_mask_ignores_slope_of_reference` besteht mit nibabel 5.4.2 auch ohne den Slope-Reset in `save_mask_like`. Das im Projektcode beschriebene Problem ließ sich hier nicht nachstellen.

## Grenzen
- Der Klassifikator ist nicht enthalten und nicht öffentlich. Ohne ihn ist Stufe 2 nicht ausführbar.
- Die Pipeline-Skripte fehlen. Die im Projekt abgelegten Fassungen stammen aus verschiedenen Ständen und passen nicht zusammen (der QC-Report erwartet ein Modul und Pfade, die die abgelegte Bibliothek nicht kennt). Sie sollten aus dem laufenden Stand auf dem Cluster kommen, mit bereinigter Konfiguration.
- `wmh_post.py` ist nach dem Projektcode nachgebaut, nicht daraus kopiert. Abweichungen zur Pipeline: keine Kappung der Distanzkarte, kein Hirnvolumen, keine Tabellen.
- Die Aussagen im Abschnitt Fallen des Skills sind Erfahrung aus einem Projekt, keine gemessenen Befunde.
