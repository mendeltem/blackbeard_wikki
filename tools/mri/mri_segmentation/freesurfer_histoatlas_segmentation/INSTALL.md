# Installation

## Geprüfte Umgebung
Code in `src/` und Tests: Linux, Python 3.13.15, keine GPU, 2026-10-02.

Stufen 1 bis 3 und 5 der Methodik: im Projekt mit FreeSurfer 8.1.0 und FSL 6.0.7.18 auf einem SLURM-Cluster gelaufen, CPU. In diesem Repo nicht nachgestellt.

## Abhängigkeiten
Für `src/` und `tests/`:

```
numpy==2.5.3
nibabel==5.4.2
```

Ältere Versionen sind nicht geprüft. Es werden nur `nib.load`, `nib.save`, `Nifti1Image`, `MGHImage` und `np.unique`, `np.bincount` benutzt.

Für die FreeSurfer-Stufen: eine FreeSurfer-Installation, die `mri_histo_atlas_segment_fireants`, `mri_coreg` und `mri_vol2vol` enthält, plus die Atlasdateien. Laut FreeSurfer-Wiki (Stand 2026-04-15) fragt das Werkzeug beim ersten Lauf nach dem Download des Atlas und verlangt die aktuelle Entwicklungsversion. Im Projekt lief es mit 8.1.0 und einem zusätzlichen Atlas-Verzeichnis, auf das `FREESURFER_HOME` für diese Aufrufe zeigte.

## Schritte

```bash
TOOL=/path/to/blackbeard_wikki/tools/mri/mri_segmentation/freesurfer_histoatlas_segmentation

python -m pip install numpy==2.5.3 nibabel==5.4.2
cd "$TOOL"
python -m unittest discover -s tests -v
python "$TOOL/src/run_aseg_tissue_volumes.py" --help
```

Vor dem ersten FreeSurfer-Lauf:

```bash
which mri_histo_atlas_segment_fireants mri_coreg mri_vol2vol
mri_histo_atlas_segment_fireants --help
fspython -c "import torch; print(torch.__version__)"
```

Scheitert die letzte Zeile mit `undefined symbol`, ist `LD_LIBRARY_PATH` verschmutzt. Siehe README, Abschnitt "FSL und FreeSurfer in einem Prozess".
