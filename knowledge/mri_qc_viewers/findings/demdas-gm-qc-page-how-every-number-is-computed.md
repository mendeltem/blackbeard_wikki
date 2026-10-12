---
id: demdas-gm-qc-page-how-every-number-is-computed
typ: befund
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-12
herkunft: DEMDAS GM example (Alita, demdas-gm/gm_beispiel.py, gm_qc_axial.py, recon_alle.sh), user request 12.10.2026 "say for every number which software computed it and how"
verweist_auf: [qc-pages-explain-every-number-on-hover, qc-pages-english-sessions-in-one-window]
---

# DEMDAS GM QC page: how every number is computed (English, link target of the page's "? Methods" overlay)

## Aussage
This is the long form of the texts that the DEMDAS GM viewer (`QUALITY_CONTROLL/DEMDAS/gm_beispiel_qc/index.html`)
shows on hover and in its Methods overlay. Written in English on purpose: the page goes to third parties.
No patient data here, only methods. Software versions as installed on Alita on 2026-10-12.

**Input image.** 3D T1-weighted MPRAGE, about 1 mm isotropic, one per session. `run-2` (distortion-corrected)
is used when present, otherwise the ND image. No bias correction and no skull stripping before segmentation.

**Segmentation.** FreeSurfer 8.2.0 (`freesurfer-linux-ubuntu24_x86_64-8.2.0-20260314-d932c45`)
`mri_synthseg --parc --robust --vol --qc --cpu`, every session on its own (no longitudinal coupling).
Output: aseg structures plus Desikan-Killiany cortical parcellation on a 1 mm isotropic grid.
Volumes = label voxel count x voxel volume, in ml.

**RAW / INFARCT EXCLUDED.** RAW = every voxel carrying the label, as SynthSeg produced it.
INFARCT EXCLUDED = the same after removing every voxel inside the infarct mask.

**Infarct.** DeepISLES (`isles22_ensemble`) on DWI + ADC + FLAIR of the same session, computed in DWI space.
DWI rigidly registered to the T1 (FSL FLIRT, 6 dof, normalised mutual information); the mask is resampled
trilinearly to the SynthSeg grid and thresholded at 0.5. In follow-up sessions the DWI is usually negative, so
the chronic infarct is often absent there (a chronic-infarct model on T1/FLAIR is to follow).
Infarct side (from M0): infarct voxels inside left- vs right-hemisphere labels; left if left > 2 x right and
> 0.1 ml, right analogously, both otherwise, none below 0.1 ml in total.

**SynthSeg QC.** Minimum over the per-structure quality scores predicted by `mri_synthseg --qc` (0 to 1).
Below about 0.65: inspect.

**Aggregates (label sets).**
- Grey matter total = cortex (1000-1035, 2000-2035, plus 3 and 42) + subcortical GM (10-13, 17, 18, 26, 28,
  49-54, 58, 60) + cerebellar cortex (8, 47).
- White matter = 2, 41 (cerebral) + 7, 46 (cerebellar) + 16 (brain stem).
- CSF / ventricles = 4, 43, 5, 44, 14, 15, 24.
- Whole brain (GM+WM) = grey matter total + white matter; ventricles not included.
- ICV = "total intracranial" from the `--vol` table (SynthSeg's own estimate), identical in RAW and EXCLUDED.
- Brain / ICV (%) = 100 x whole brain / ICV.

**WMH (3D U-Net).** In-house 3D U-Net (architecture a12), ensemble of the five cross-validation fold models
trained on 311 manually labelled cases (CV Dice 0.71), probability threshold 0.5, native space, FLAIR (+T1).
Not part of SynthSeg. "-" = not computed for that session.

**Cortical thickness.** FreeSurfer 8.2.0 `recon-all -all -openmp 4`, cross-sectional (each session alone), on
the same T1. Thickness = distance between white and pial surface at every vertex, averaged per Desikan-Killiany
region (`ThickAvg` in `lh/rh.aparc.stats`); "Mean thickness" is FreeSurfer's cortex-wide mean. Displayed value
= (left + right) / 2, unweighted. "not computed yet" = recon-all has not finished for that session; the page
states how many sessions were finished at build time (31 of 63 on 2026-10-12; about 1 h per session, 17-28 GB
RAM peak, 30 runs were OOM-killed on 11.10. and are queued again; `dicke_nachbau.sh` rebuilds the page and
copies it to the stick whenever new sessions finish).

**Structures (right panel).** Volume of every single SynthSeg label, RAW and EXCLUDED; colour = FreeSurferColorLUT.

**Image alignment between sessions (display only).** Follow-up sessions are rigidly aligned (FLIRT, 6 dof,
normalised mutual information, brain-masked T1) to the participant's first segmented session; labels and infarct
nearest-neighbour. The panel shows the Dice overlap of the two brain masks (0.982-0.990 for all 40 follow-ups).
Volumes are not affected: they come from each session's native segmentation.

## Traegt
Reading the DEMDAS GM page and the Excel table `DEMDAS_GM_Beispiel.xlsx` (sheets Fokus, Volumen_ROH,
Volumen_OHNE_INFARKT, QC, WMH_3D_UNet). Any question "which software produced this number".

## Traegt nicht
Validity of the numbers (no reference segmentation on DEMDAS); the chronic infarct in follow-ups is missing
by construction; thickness hemispheric mean is unweighted.

## Bruchindikator
A generator change (gm_beispiel.py, gm_qc_axial.py, recon_alle.sh) that is not mirrored here and in the
page's `methoden()` dictionary; a FreeSurfer or DeepISLES update.

## Ablesung
Code read 2026-10-12: `demdas-gm/gm_beispiel.py` (segmentieren, infarkt, volumen, icv, qcwert, wmh_tabelle),
`gm_qc_axial.py` (auf_referenz, dicke, methoden), `recon_alle.sh`; `freesurfer/8.2.0/build-stamp.txt`;
`derivatives/demdas/infarkt/*/lauf.json` (werkzeug = DeepISLES isles22_ensemble).

## Verknuepft
- [qc-pages-explain-every-number-on-hover](../rules/qc-pages-explain-every-number-on-hover.md)
- [qc-pages-english-sessions-in-one-window](../rules/qc-pages-english-sessions-in-one-window.md)
