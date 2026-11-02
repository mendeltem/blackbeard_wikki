---
id: grey-zone-at-four-cmb-threshold
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-11-01
herkunft: Projekt mb-arena (Alita), paper/patient_threshold.py (band robustness), stage-2 arms tset-tta8/-proto/-track, two seeds, 2026-11-01
verweist_auf: [fine-tune-from-public-valdo-weights, calibrate-before-you-fine-tune]
---

# At the four-CMB treatment threshold, a radiologist grey zone moves decisions -- a better classifier does not

## Aussage
For the anti-amyloid exclusion rule (more than four CMB; Cummings et al. 2023), the adapted two-stage detector at two
clinical sites flagged every patient truly above the threshold, but placed a sizeable share of eligible patients above it
too. Four ways to raise specificity were compared on the same out-of-fold candidates:
- a patient-level threshold chosen inside the cross-validation, a seed ensemble, and three newer stage-2 classifiers
  (test-time augmentation, prototype head, slice tracking): none moved patient-level specificity beyond its bootstrap
  interval -- although slice tracking raised SWI lesion F1 by about +0.08 (interval excluding 0);
- a grey zone: patients with a detector count of 3-8 go to a radiologist. Specificity of the remaining automatic decisions
  rose by roughly +0.2 to +0.3 (absolute) while no patient above the threshold was missed, with a minority of the patients referred. Fixed
  in advance; neighbouring bands (2-6, 4-10, 2-10) gave the same picture, and a band chosen inside the cross-validation
  (narrowest band reaching sensitivity and specificity >= 0.95 on the other folds; 4-8 in four folds, 4-6 in one) referred
  fewer patients and kept most of the gain.

Why: errors of a count-based rule cluster near the cut-off; far from it the detector is almost always on the right side,
so better lesion detection changes few decisions.

## Traegt
Clinical use of CMB detectors for count thresholds: use the detector to triage (decide the clear cases, refer the band
around the cut-off) instead of tuning lesion F1 further; report patient-level endpoints next to lesion F1.

## Traegt nicht
A treatment-screening population: the cohorts were not selected as anti-amyloid candidates, so burden and the share in the
band will differ. "Presence of any CMB" is a different question (one false positive flips it) and stays weak.

## Bruchindikator
On a screening population or an external site, the band refers the majority of the patients, or a classifier change
moves specificity beyond its interval.

## Ablesung
Own measurement 2026-11-01; own-cohort values given only as differences. Threshold rule: Cummings J, Apostolova L, Rabinovici
GD, et al. 2023, Lecanemab: Appropriate Use Recommendations, J Prev Alzheimers Dis 10(3):362-377, doi:10.14283/jpad.2023.30,
PMID 37357276. Tier 1b (one centre, interim folds).

## Verknuepft
- [fine-tune-from-public-valdo-weights](fine-tune-from-public-valdo-weights.md)
- [calibrate-before-you-fine-tune](../rules/calibrate-before-you-fine-tune.md)
