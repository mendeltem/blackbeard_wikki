---
id: microbleednet-never-trains-its-teacher
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-16
herkunft: source code of MicrobleedNet, github.com/v-sundaresan/microbleed-detection commit 958f1cb (= main on 2026-10-16), read on Alita; earlier fine-tuning runs of the original code (cmb-valdo-chain "Arm 6", 2026-09-29)
verweist_auf: [vessel-inpainting-removes-microbleeds-on-thick-slices, one-shared-candidate-classifier-for-all-cohorts]
---

# MicrobleedNet's published code never trains the teacher of its second stage

## Aussage
MicrobleedNet (Sundaresan et al. 2023) discriminates candidates with a teacher-student network: a multi-task teacher
(feature extractor, voxel-wise segmentor, patch classifier) and a student distilled from it (loss CE + 0.4 T^2 KL +
0.6 CE, T = 4 in the code). In the published code no command trains the teacher: `train`, `fine_tune` and
`cross_validate` all build `CDiscNet` + `CDiscClass24` and LOAD their weights from the model folder
(`cdisc_train_function.py`, `cdisc_finetune_function.py`, `crossvalidate_function.py`). When the files are missing the
inner handler only creates `ValueError(...)` without `raise`, so training continues and the student learns from a
randomly initialised teacher. "Training MicrobleedNet from scratch" with this code therefore means step 1 from scratch
and step 2 distilled from noise, unless the pretrained teacher files are put into the output folder.

## Trägt
Read at the source (commit 958f1cb, verified as current `main` with `git ls-remote`). Consistent with the earlier
observation that the fine-tuned original's student stayed at chance accuracy (0.5) on VALDO and two in-house cohorts
while step 1 learned normally.

## Trägt nicht
The original authors may train the teacher with code that was not published; the paper (Front Neuroinform 2023)
describes teacher training. A from-scratch run of the original was not measured.

## Bruchindikator
A later commit that trains `CDiscNet` (an optimizer over the teacher's parameters) or raises on a missing teacher.

## Ablesung
Sundaresan V, Arthofer C, Zamboni G, et al. Automated detection of cerebral microbleeds on MR images using knowledge
distillation framework. Front Neuroinform 2023;17:1204186, doi:10.3389/fninf.2023.1204186. Code:
https://github.com/v-sundaresan/microbleed-detection (commit 958f1cb). Knowledge distillation: Hinton G, Vinyals O,
Dean J. Distilling the knowledge in a neural network. arXiv:1503.02531 (2015). A port that trains the teacher:
https://github.com/mendeltem/cmb_3d_unet_experiments (`cmbx/stage2.py`, `method: teacher_student`).
