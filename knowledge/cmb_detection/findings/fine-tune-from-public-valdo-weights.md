---
id: fine-tune-from-public-valdo-weights
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-16
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

## Trägt
Weights load bit-identically in the training package and in the release package (max |difference| 0.0).
Fine-tuning gain 0.11 is above the seed noise of this recipe (0.03-0.08).

## Trägt nicht
One fold, one seed: the +0.03 against 60 epochs from scratch is inside the noise; needs 5 folds x 2 seeds before it
becomes a rule. Numbers of the in-house cohort are kept private (relative differences only here).

## Bruchindikator
A 5-fold, 2-seed repetition where fine-tuning (lr 1e-4) does not beat short scratch training by more than the noise.

## Ablesung
VALDO: Sudre et al., Med Image Anal 2024;91:103029, doi:10.1016/j.media.2023.103029, PMID 37988921. Released weights:
https://github.com/mendeltem/microbleed_detection_3D_UNET/releases/tag/v0.1.0 (SHA-256 checked). Transfer learning in
medical imaging, background: Raghu et al., NeurIPS 2019, "Transfusion: Understanding Transfer Learning for Medical
Imaging" (arXiv:1902.07208). Own runs 2026-10-16 (cmbx, fold 0, seed 42).

## Verknüpft
[two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md),
[count-lesions-on-the-fine-grid-deliver-a-label-map](../rules/count-lesions-on-the-fine-grid-deliver-a-label-map.md)
