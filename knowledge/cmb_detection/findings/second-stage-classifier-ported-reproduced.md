---
id: second-stage-classifier-ported-reproduced
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-16
herkunft: cmb_3d_unet_experiments (cmbx stage2, nested 5-fold CV on the out-of-fold maps of a 60-epoch T2* run of an in-house cohort), 2026-10-16
verweist_auf: [one-shared-candidate-classifier-for-all-cohorts, microbleednet-never-trains-its-teacher]
---

# The second-stage candidate classifier, ported into the training package, reproduces its gain

## Aussage
The small 3D CNN that re-checks every first-stage candidate (components above 0.15, 16 x 32 x 32 crop of image, FRST
and probability, 3 members) was ported from the research chain into the public training package. Trained with a nested
5-fold CV on the out-of-fold maps of a T2* run, it raised pooled lesion F1 by +0.028 over the first stage alone (score
threshold chosen out of fold), in line with the earlier research-chain result on the same kind of data.

## Trägt
Same candidate rule, crop, members and schedule as the research chain; nested CV (fold k scored by a classifier that
never saw fold k).

## Trägt nicht
One run, one seed of the first stage; the seed spread of the second stage was 0.003-0.009 in ten-seed measurements of
the research chain, the first stage spreads more. In-house numbers stay private (relative only).

## Bruchindikator
A second seed of the first stage where the classifier does not improve on the first stage.

## Ablesung
Two-stage design after Sundaresan et al., Front Neuroinform 2023;17:1204186, doi:10.3389/fninf.2023.1204186. Package:
https://github.com/mendeltem/cmb_3d_unet_experiments (`cmbx stage2`). Own run 2026-10-16.
