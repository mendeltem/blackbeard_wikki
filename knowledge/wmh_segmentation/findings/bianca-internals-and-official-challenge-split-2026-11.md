---
id: bianca-internals-and-official-challenge-split-2026-11
typ: befund
status: vorschlag
thema: knowledge/wmh_segmentation
stand: 2026-11-05
herkunft: own BIANCA runs on the public WMH Segmentation Challenge (60 training, 110 official test scans), 2026-11-05; source read in FSL 6.0.7.23 fsl/bin/bianca
verweist_auf: [human-rater-variance-and-good-dice-for-wmh-2026-10]
---

# BIANCA: what it really does internally, and its score on the official WMH Challenge test set

## Aussage
- **No scaling before the vote.** bianca fits sklearn NearestNeighbors (kd-tree, k = 40) on the feature table as it is
  (fsl/bin/bianca l.1275); probability = share of lesion labels among the 40 (classify_method knn, default).
- **Normalisation:** each image is normalised per scan with normalise_data = (x - mean) / SD over voxels **> 0** (l.328-334).
  The patch image (uniform_filter 3x3x1 of the normalised image / same filter of the brain mask, l.497-516) is normalised
  again over voxels > 0 - after the first z-scoring that is only the brighter part - so patch columns end up wider:
  SD in a 60-scan table FLAIR 1.18, FLAIR patch 3.15, T1 0.89, T1 patch 2.23, MNI x/y/z 1.0. Patch features therefore
  weigh about 2.6x more in the distance. At the brain edge the background enters the window and pulls the patch down.
- **noborder** = grey_dilation of the lesion mask with a 3x3x1 footprint (1 along the thickest axis): a 1-voxel ring.
- **--querysubjectnum inside --trainingnums** removes that row from training; with all rows as training, add a duplicate
  row as the query (we used row 61 = copy of row 1). bianca refuses to train without a query row.
- **bianca_cluster_stats minextent 2** keeps 2-voxel clusters (26-connected).
- **Official split, public data:** trained on all 60 training scans (HD-BET 2.0.1 brain masks, official label-1 masks, label 2
  ignored, FLAIR->MNI by registering the T1-in-FLAIR-space directly to MNI), cut-off 0.95 chosen on a 30/30 split inside the
  training data, WM mask from make_bianca_mask, clusters >= 3 voxels: mean Dice on the 110 official test scans **0.665**
  (cut-off only 0.586, + WM mask 0.665); per site Philips 3T 0.649, Siemens Trio 0.733, GE 3T 0.644, unseen GE 1.5T 0.584,
  unseen Philips PET/MR 0.659; volume r 0.903; lesions > 1 ml found 187/188, < 10 mm3 600/3470.

## Trägt
Recomputed independently for 4 cases and the per-site means (fact check 2026-11-05). Public data, numbers may be shown.

## Trägt nicht
One training set, one cut-off rule, one seed. Thick-slice and setting comparisons from the earlier run (BET, local masks)
are superseded and should not be cited.

## Bruchindikator
A text that says BIANCA "scales all features to the same spread", or a 30/30 split of the training set reported as the
challenge result.

## Ablesung
Sources: Griffanti L et al. 2016, NeuroImage 141:191-205, doi:10.1016/j.neuroimage.2016.07.018, PMID 27402600;
Kuijf HJ et al. 2019, IEEE TMI 38:2556-2568, doi:10.1109/TMI.2019.2905770, PMID 30908194; Isensee F et al. 2019,
Hum Brain Mapp 40:4952-4964, doi:10.1002/hbm.24750, PMID 31403237 (HD-BET). Data doi:10.34894/AECRSD (CC BY-NC 4.0).
Software FSL 6.0.7.23 (bianca), HD-BET 2.0.1. Practical: fsl_anat fails on input paths with spaces; the FSL 6.0.7.18
module on our HPC has a bianca without --seed.
