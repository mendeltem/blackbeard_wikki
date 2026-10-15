---
id: wmh-synthseg-far-below-own-3d-unet
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-15
herkunft: wmh-modell201/pool311 on Alita, 2026-10-15 (question: is a public tool better than our a12 for filling WMH before segmentation?)
verweist_auf: [official-label-2-rule-deletes-the-prediction, brain-mask-is-part-of-the-model, measure-tails-paired-not-by-percentile]
---

# WMH-SynthSeg is far below our own 3D U-Net (a12) on 311 manually labelled cases

## Statement
Paired on the same 311 cases (WMH Challenge train 60 + test 110, BELOVE 56, WMH_SHAE 65, maastricht 20), same references,
same brain mask, official label-2 rule, threshold 0.5:

| metric | a12 (5-fold out-of-fold) | WMH-SynthSeg (FreeSurfer 8.2.0, v10) |
|---|---|---|
| Dice | **0.711** | 0.415 (difference +0.296, 95 % bootstrap CI +0.280 to +0.312; a12 better in 307/311) |
| voxel sensitivity / precision | 0.736 / 0.721 | 0.466 / 0.463 |
| lesion recall / lesion F1 | 0.633 / 0.657 | 0.228 / 0.295 |
| absolute volume difference, median | 18 % | 48 % (mean 39 % vs 135 %) |
| Spearman predicted vs reference volume | 0.963 | 0.784 |

By WMH load: below 5 ml Dice 0.573 vs 0.228 (WMH-SynthSeg over-calls, median +2.7 ml); above 15 ml 0.824 vs 0.576
(WMH-SynthSeg under-calls, median -8.1 ml). a12 wins in every cohort, including the external-style cohorts.

## Applies to
Choosing a WMH mask for lesion filling or WMH volume on FLAIR with T1 available, cohorts like these (3 T, clinical FLAIR).

## Does not apply to
WMH-SynthSeg's own use case: T1-only or low-field/portable scans without FLAIR. Here it received the same preprocessed
(skull-stripped, normalised, partly 3-mm-slice) FLAIR as a12, not the raw image; its probabilities were resampled
linearly from 1 mm to the evaluation grid. That may cost it some Dice, but not 0.30.

## Break indicator
WMH-SynthSeg on raw FLAIR reaching within 0.05 Dice of a12 on the same cases.

## Source
Scripts pool311/wmhsynthseg/auswerten.py (paired bootstrap, 5000 draws, seed 2026) and methode/wmh_auswerten.py; QC page
QUALITY_CONTROLL/WMH/WMH_SEGMENTATION (20 cases, built with the shared qc_slice_viewer; page Dice equals script Dice within 0.004).
WMH-SynthSeg: Laso et al., ISBI 2024, doi:10.1109/isbi56570.2024.10635502. Note: FreeSurfer's bundled torch has no CUDA;
the unchanged inference.py runs on GPU from a CUDA environment (11 s instead of 109 s per case), needs up to 20 GB VRAM alone.

## Linked
- [official-label-2-rule-deletes-the-prediction](official-label-2-rule-deletes-the-prediction.md)
- [brain-mask-is-part-of-the-model](brain-mask-is-part-of-the-model.md)
