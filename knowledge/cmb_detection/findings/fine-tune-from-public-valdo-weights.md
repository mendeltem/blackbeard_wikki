---
id: fine-tune-from-public-valdo-weights
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-31
herkunft: cmb_3d_unet_experiments (cmbx get-model valdo_t2, train.init_from), check on one fold of an in-house T2* cohort, 2026-10-16
verweist_auf: [two-seeds-per-decision-below-0.08, count-lesions-on-the-fine-grid-deliver-a-label-map]
---

# Fine-tuning from the public VALDO weights beats training from scratch; unadapted they over-detect

## Aussage
The anisotropic U-Net trained on all 72 public VALDO cases (released weights, CC BY-NC-SA 4.0):
1. **Unadapted on another T2* cohort** it over-detects at the released stage-1 cell (threshold 0.6, 2 mm3): lesion F1
   rose monotonically with the threshold up to 0.9 (+0.09 F1 from 0.6 to 0.9, the best cell chosen on the target
   cases, so optimistic); it stays clearly below a model trained in the target domain. Full-data models give higher
   probabilities than cross-validation models (also noted in the release documentation).
2. **Fine-tuned** (all weights initialised from VALDO, `train.lr` 1e-4, 6 epochs, same recipe otherwise, ~7 min on one
   GPU): +0.11 F1 against 6 epochs from scratch and +0.03 against the 60-epoch from-scratch training on the same fold.
   With the default learning rate 3e-4 the gain was smaller (+0.04): a large learning rate destroys part of the start.
3. Channel changes are possible: input channels are matched by name; a new channel starts at zero weight, so the
   network first reproduces the pretrained output exactly (unit test) and learns the new channel during training.

4. **Learning curve (2026-10-31, interim: one fold of 5, stage 1, fixed cell 0.3 / 2 mm3, nested stratified draws,
   2-3 draws per n):** on an in-house 5 mm T2* cohort, full fine-tuning (30 epochs, lr 1e-4) was ahead of training from
   scratch (60 epochs) by about +0.05 F1 with 3 local scans, +0.04 with 5, +0.03 with 10 and about +0.01 from 15 scans
   on; both curves flattened at about 15 scans (within 0.02 of the all-scans value). With 3 local scans fine-tuning
   already recovered most of the zero-shot gap (zero-shot was about 0.2 F1 lower). Fine-tuning only the instance-norm
   affine parameters and the output head (Karani 2018) stayed below both, with 2-3x the false positives of full
   fine-tuning. Draw-to-draw spread at n <= 5 was about +-0.05 F1, at n >= 10 about +-0.02.

## Trägt
Weights load bit-identically in the training package and in the release package (max |difference| 0.0).
Fine-tuning gain 0.11 is above the seed noise of this recipe (0.03-0.08).

## Trägt nicht
One fold, one seed: the +0.03 against 60 epochs from scratch is inside the noise; needs 5 folds x 2 seeds before it
becomes a rule. Numbers of the in-house cohort are kept private (relative differences only here).

Point 4 is one fold of 15 test scans; folds 1-4 and an SWI cohort are running. Part of the zero-shot gap is the operating
point, not the weights (see [full-data-last-state-models-run-hotter](full-data-last-state-models-run-hotter.md)); the
calibration-only control ([calibrate-before-you-fine-tune](../rules/calibrate-before-you-fine-tune.md)) is pending.

## Bruchindikator
A 5-fold, 2-seed repetition where fine-tuning (lr 1e-4) does not beat short scratch training by more than the noise.

## Ablesung
VALDO: Sudre et al., Med Image Anal 2024;91:103029, doi:10.1016/j.media.2023.103029, PMID 37988921. Released weights:
https://github.com/mendeltem/microbleed_detection_3D_UNET/releases/tag/v0.1.0 (SHA-256 checked). Transfer learning in
medical imaging, background: Karani et al., MICCAI 2018, doi:10.1007/978-3-030-00928-1_54; Valverde et al., NeuroImage
Clin 2019;21:101638, doi:10.1016/j.nicl.2018.101638, PMID 30555005 (one-shot adaptation, MS lesions); Raghu et al., NeurIPS 2019, "Transfusion: Understanding Transfer Learning for Medical
Imaging" (arXiv:1902.07208). Own runs 2026-10-16 (cmbx, fold 0, seed 42) and 2026-10-30/31 (phase-2 learning curve, 46 runs, fold 0).

## Verknüpft
[two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md),
[count-lesions-on-the-fine-grid-deliver-a-label-map](../rules/count-lesions-on-the-fine-grid-deliver-a-label-map.md)
