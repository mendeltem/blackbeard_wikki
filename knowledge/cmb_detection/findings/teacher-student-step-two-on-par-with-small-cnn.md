---
id: teacher-student-step-two-on-par-with-small-cnn
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-16
herkunft: cmb_3d_unet_experiments (cmbx stage2 --method teacher_student vs cnn, nested 5-fold CV on the out-of-fold candidates of one T2* run of an in-house cohort), 2026-10-16
verweist_auf: [microbleednet-never-trains-its-teacher, second-stage-classifier-ported-reproduced, one-shared-candidate-classifier-for-all-cohorts]
---

# With a trained teacher, MicrobleedNet's teacher-student step 2 is on par with a small CNN

## Aussage
MicrobleedNet's candidate discrimination (teacher = feature extractor + voxel-wise segmentor + patch classifier,
student distilled with CE + 0.4 T^2 KL + 0.6 CE, T = 4), rebuilt for a 16 x 32 x 32 crop and with the teacher
actually trained, raised pooled lesion F1 over the first stage by +0.030; the small 3D CNN on the same candidates
by +0.028. The two are equal within the seed spread of the second stage (0.003-0.009). The failure of the
original's step 2 on our data (student at chance) is therefore a property of its code path (teacher never
trained), not of the teacher-student idea.

## Traegt
Same 1126 candidates, same folds, nested CV for both.

## Traegt nicht
One first-stage run, one seed per method, one cohort; absolute numbers of the in-house cohort stay private.

## Bruchindikator
A ten-seed comparison in which one of the two is consistently ahead by more than 0.01.

## Ablesung
Sundaresan V et al. Front Neuroinform 2023;17:1204186, doi:10.3389/fninf.2023.1204186; Hinton G, Vinyals O, Dean J,
arXiv:1503.02531 (2015). Package https://github.com/mendeltem/cmb_3d_unet_experiments (`cmbx stage2 --method
teacher_student`). Own run 2026-10-16.
