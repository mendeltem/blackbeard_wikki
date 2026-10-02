---
id: freesurfer_histoatlas_segmentation
bereich: tools/mri/mri_segmentation
stand: 2026-10-02
herkunft: Projekt SEGMENTATION_PROJECT
sprache: python
---

# FreeSurfer-Segmentierung mit HistoAtlas (NextBrain) und SynthSeg

## Zweck
Methodik, um aus einem nativen T1w (und optional einer FLAIR mit WMH-Maske) drei Ebenen von Volumina zu bekommen:

1. rund 300 ROIs je Hemisphäre aus dem histologischen Atlas NextBrain (`mri_histo_atlas_segment_fireants`),
2. die aseg-Strukturen aus der Whole-Structure-Segmentierung, die dasselbe Werkzeug nebenbei schreibt,
3. GM, WM und CSF als Gruppierung dieser aseg-Labels, mit der WMH-Maske additiv darübergelegt.

Der Eintrag besteht aus zwei Teilen. Die Methodik (Befehle, Reihenfolge, Fallen) steht in diesem README. Der Code in `src/` deckt nur Stufe 4 ab, den Teil, der ohne FreeSurfer läuft und sich mit synthetischen Daten testen lässt. Das vollständige Pipeline-Skript bleibt im Projekt, weil es an eine Cluster-Umgebung und ein eigenes BIANCA-Modell gebunden ist.

## Wann verwenden, wann nicht
Verwenden, wenn regionale Volumina feiner als aseg gebraucht werden oder wenn eine WMH-Maske Atlas-ROIs zugeordnet werden soll.

Nicht verwenden, wenn nur GM, WM und CSF gefragt sind. Dann reicht `mri_synthseg --parc` plus der Code in `src/`; der Atlas kostet im Projekt über 52 GB RAM je Subject.

Nicht verwenden, wenn die Gewebevolumina bei starker WMH-Last zentral sind. Die Whole-Structure-Segmentierung läuft auf dem T1 und verbucht einen Teil der WMH als GM oder Ventrikel (siehe Grenzen). `mri_WMHsynthseg` auf der FLAIR ist dann die bessere Quelle.

## Methodik
Stand im Projekt: FreeSurfer 8.1.0, FSL 6.0.7.18, CPU. Fünf Stufen je Subject, nacheinander.

| Stufe | Schritt | Werkzeug | Ergebnis |
|---|---|---|---|
| 1 | WMH-Maske im FLAIR-Raum | wählbar: BIANCA, vorhandene Maske, `mri_WMHsynthseg` (Label 77), keine | binäre Maske |
| 2 | Atlas auf nativem T1w, ohne vorheriges Skull-Stripping | `mri_histo_atlas_segment_fireants` | `seg.left.nii.gz`, `seg.right.nii.gz` (0,4 mm), `lut.txt`, `vols.left.csv`, `vols.right.csv`, Whole-Structure-Segmentierung (1 mm) |
| 3 | WMH in den T1-Raum, dann ins Atlas-Grid, als eigenes Label einsetzen | `mri_coreg` (6 DOF), `mri_vol2vol --nearest` | `seg.<side>.withWMH.nii.gz`, WMH je ROI |
| 4 | aseg-Labels zu GM, WM, CSF gruppieren, WMH addieren | `src/aseg_tissue.py` | Volumina in mm³ je Label und je Gewebeklasse |
| 5 | T1, FLAIR und Labels in ein gemeinsames Grid für die Sichtkontrolle | `mri_vol2vol` | QC-Satz je Subject |

Festgelegte Entscheidungen und ihre Gründe:

- **Stufe 1 und 5 sind nicht fatal.** Scheitert die WMH-Maske, laufen Atlas und Volumetrie ohne WMH weiter, und der Status vermerkt das.
- **Registrierung FLAIR nach T1 rigide, 6 DOF.** Gleiche Session, gleicher Kopf. Masken werden immer mit `--nearest` resampelt.
- **WMH-Volumen wird im nativen FLAIR-Grid gezählt**, nicht nach dem Resampling. Die resampelten Masken dienen nur der Zuordnung zu ROIs.
- **WMH wird nur innerhalb der Hemisphäre eingesetzt** (`seg > 0`). Die Voxelzahl je ROI wird vor dem Überschreiben gezählt.
- **WMH-Label prüfen.** Standard ist 77. Ist 77 in der Atlas-LUT schon vergeben, ein freies Label nehmen (im Projekt 9001).
- **In Stufe 4 wird die WMH addiert, nicht überschrieben.** Codes: 1 GM, 2 WM, 3 CSF, 11 GM und WMH, 12 WM und WMH, 13 CSF und WMH. So bleibt die Zahl der Voxel mit Code 2 das WM ohne WMH, und man sieht, welcher Teil der Maske außerhalb des WM liegt.
- **Jedes aseg-Label bekommt zusätzlich eine eigene Zeile.** GM, WM und CSF lassen sich damit später anders zusammensetzen, ohne die Segmentierung neu zu rechnen.

## Aufruf

Stufen 2 und 3, wie sie im Projekt unter FreeSurfer 8.1.0 liefen (Argumente positional: Eingabe, Ausgabeordner, GPU 0 oder 1, Threads):

```bash
T1=/data/bids/sub-01/ses-01/anat/sub-01_ses-01_T1w.nii.gz
FLAIR=/data/bids/sub-01/ses-01/anat/sub-01_ses-01_FLAIR.nii.gz
WMH=/data/derivatives/sub-01/ses-01/wmh/sub-01_ses-01_WMH_mask.nii.gz
OUT=/data/derivatives/sub-01/ses-01/anat

mri_histo_atlas_segment_fireants "$T1" "$OUT" 0 9

mri_coreg --mov "$FLAIR" --ref "$T1" --reg "$OUT/flair2t1.lta" --dof 6 --threads 9
mri_vol2vol --mov "$WMH" --targ "$T1" --reg "$OUT/flair2t1.lta" --nearest --o "$OUT/WMH_in_T1.nii.gz"
mri_vol2vol --mov "$OUT/WMH_in_T1.nii.gz" --targ "$OUT/seg.left.nii.gz" --regheader --nearest --o "$OUT/WMH_on_seg_left.nii.gz"
mri_vol2vol --mov "$OUT/WMH_in_T1.nii.gz" --targ "$OUT/SynthSeg.mgz" --regheader --nearest --o "$OUT/WMH_on_synthseg.nii.gz"
```

Die FreeSurfer-Wiki (Stand 2026-04-15) dokumentiert für die Entwicklungsversion eine andere Syntax, ein Aufruf je Seite:

```bash
mri_histo_atlas_segment_fireants --i "$T1" --o "$OUT" --device cpu --side left --mode invivo
mri_histo_atlas_segment_fireants --i "$T1" --o "$OUT" --device cpu --side right --mode invivo
```

Welche der beiden Formen gilt, hängt am Build. Vor dem ersten Lauf `mri_histo_atlas_segment_fireants --help` lesen. Die Flag-Syntax ist hier nicht getestet.

Stufe 4, mit dem Code aus diesem Ordner:

```bash
TOOL=/path/to/blackbeard_wikki/tools/mri/mri_segmentation/freesurfer_histoatlas_segmentation
OUT=/data/derivatives/sub-01/ses-01/anat

python "$TOOL/src/run_aseg_tissue_volumes.py" --seg "$OUT/SynthSeg.mgz" --wmh "$OUT/WMH_on_synthseg.nii.gz" --out "$OUT/tissue_volumes.csv" --pallidum-vdc gm --labels-out "$OUT/tissue_labels.nii.gz"
```

Als Bibliothek:

```python
import sys
sys.path.insert(0, "/path/to/blackbeard_wikki/tools/mri/mri_segmentation/freesurfer_histoatlas_segmentation/src")
import aseg_tissue as at

img, aseg = at.load_labels("/data/derivatives/sub-01/ses-01/anat/SynthSeg.mgz")
label_class = at.class_of(at.CONVENTIONS["gm"])
lab = at.tissue_label_image(aseg, label_class)
rows = at.tissue_volumes(lab, at.voxel_mm3(img))
print(rows)
```

## Eingabe und Ausgabe
Eingabe für `run_aseg_tissue_volumes.py`:
- `--seg`: aseg-Labelbild (`.nii.gz` oder `.mgz`), mit oder ohne Desikan-Killiany-Parzellierung.
- `--wmh`: optionale binäre Maske im selben Grid wie `--seg`. Bei abweichendem Grid bricht das Skript mit Rückgabewert 2 ab und schreibt nichts.
- `--pallidum-vdc gm|wm`: wohin Pallidum und Ventral DC zählen. Standard `gm`.

Ausgabe: CSV im Long-Format mit den Spalten `measure, label, structure, side, volume_mm3`.
- `measure=tissue_volume`: `GM`, `WM`, `CSF`, `sum_GM_WM_CSF`, mit Maske zusätzlich `WM_minus_WMH`, `WMH_in_GM`, `WMH_in_WM`, `WMH_in_CSF`, `WMH_outside_classes`.
- `measure=tissue_fine`: eine Zeile je vorkommendem Label. Unbekannte Labels heißen `unmapped_label_<n>` und zählen in keine Gewebeklasse.

Rückgabewerte: 0 ohne Auffälligkeit, 1 mit Warnung (Ausgabe wird trotzdem geschrieben), 2 Eingabefehler.

Der Dateiname der Whole-Structure-Segmentierung hängt am Build: im Projekt `SynthSeg.mgz`, laut Wiki ein Ordner `SuperSynth/`. Per Glob suchen, nicht fest eintragen.

## Teststand
2026-10-02, Linux, Python 3.13.15, numpy 2.5.3, nibabel 5.4.2:
`python -m unittest discover -s tests -v` im Werkzeugordner → 18 Tests, bestanden. Nur synthetische Labelbilder.

Nicht in diesem Repo getestet: die Stufen 1, 2, 3 und 5. Sie liefen im Projekt als SLURM-Array über 60 Subjects mit FreeSurfer 8.1.0 erfolgreich durch; die Befehle oben sind aus diesem Skript übernommen.

## Grenzen

### GM, WM und CSF sind Konvention
Pallidum und Ventral DC stehen je nach Arbeit in GM oder in WM, bei gleichem SynthSeg-Labelsatz (Quellen in [PAPERS.md](PAPERS.md)). Die verwendete Konvention gehört in jede Tabelle und jeden Methodenteil. Choroid Plexus und WM-Hypointensitäten (Label 77) stehen bewusst in keiner Klasse.

`sum_GM_WM_CSF` ist die Summe der drei Klassen und keine validierte ICV-Schätzung. Ob Label 24 den gesamten extrazerebralen Liquor abdeckt, ist hier nicht geprüft.

### Der Kortex steckt nicht immer in Label 3 und 42
Im Projekt schrieb das Atlas-Werkzeug die Whole-Structure-Segmentierung mit Parzellierung: Kortex in 1001 bis 1035 und 2001 bis 2035, nicht in 3 und 42. Ohne diese Labels in der Zuordnung fiel der gesamte Kortex aus GM: gemessen 168 ml GM und GM/WM 0,31; nach der Korrektur GM/WM 1,32 bis 1,52. `src/aseg_tissue.py` kennt beide Varianten und warnt bei GM/WM außerhalb 0,8 bis 1,8.

### T1-basierte Segmentierung verwechselt WMH
Ein Teil der WMH ist in der Whole-Structure-Segmentierung als GM oder Ventrikel verbucht. `WMH_in_GM` und `WMH_in_CSF` sind deshalb QC-Zahlen, und `WM_minus_WMH` ist eine Näherung an normal erscheinendes WM, keine saubere Definition.

### Zwei Auflösungen
Der Atlas liegt auf 0,4 mm, die Whole-Structure-Segmentierung auf 1 mm. Die Summen der beiden Ebenen passen nicht aufeinander. Beim Herunterrechnen des Atlas auf 1 mm können dünne ROIs verschwinden; vorher und nachher die Labelmengen vergleichen.

### FSL und FreeSurfer in einem Prozess
HD-BET braucht in einer Conda-Umgebung `LD_LIBRARY_PATH=$CONDA_PREFIX/lib`. Genau damit bricht `fspython` beim Import von torch ab (`undefined symbol`, `c10`, `demangle`). Lösung im Projekt: `os.environ` nicht global ändern, sondern jedem Subprozess ein eigenes Umgebungs-Dict geben.

```python
import os
import subprocess

FS_ENV = os.environ.copy()
FS_ENV.pop("LD_LIBRARY_PATH", None)

FSL_ENV = os.environ.copy()
FSL_ENV["LD_LIBRARY_PATH"] = os.path.join(os.environ["CONDA_PREFIX"], "lib")

subprocess.run(["fspython", "-c", "import torch; print(torch.__version__)"], env=FS_ENV, check=True)
```

Dieser Einzeiler vor dem Array-Lauf kostet rund 20 Sekunden und erspart einen mehrstündigen Fehllauf.

### Ressourcen
Atlas auf CPU: maximaler Speicher über 52,8 GB, ein Lauf mit 48 GB brach mit OOM ab. Im Projekt gesetzt: 72 GB, 6 Stunden, 9 Threads je Subject. Laut Wiki ist keine GPU nötig; für `mri_WMHsynthseg` nennt die Wiki rund 32 GB RAM.

### Was dieser Eintrag nicht enthält
Das Pipeline-Skript selbst, das BIANCA-Modell, den QC-Viewer und alle Daten. Die BIANCA-Stufe (Stufe 1) steht in [wmh/bianca_flair_wmh](../wmh/bianca_flair_wmh/README.md).
