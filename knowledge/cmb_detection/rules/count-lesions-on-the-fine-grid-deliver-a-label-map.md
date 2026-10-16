---
id: count-lesions-on-the-fine-grid-deliver-a-label-map
typ: regel
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-16
herkunft: acceptance test of the inference of cmb_3d_unet_experiments, 2026-10-16
verweist_auf: [patches-not-whole-images-for-small-lesions]
---

# Count microbleeds on the model grid; deliver a label map on the input grid

## Aussage
A detector that works on a fine grid (0.5 x 0.5 x 1 mm) and writes its mask back onto the scan grid (e.g. 0.7 x 0.7 x
5 mm slices) can merge two neighbouring microbleeds into one connected component of the binary mask: measured 37
separate detections on the model grid, 36 components after resampling (nearest neighbour in world coordinates).
Microbleeds smaller than one input voxel can also vanish (kept here by setting their centre voxel).
Rule: the count comes from the model grid; besides the binary mask, write a label map in which detection k has value
k and matches entry k of the report (volume, probability, centre in mm and as input voxel).

## Trägt
Acceptance test on real scans: json count = distinct values of the label map = model-grid count for every case after
the change; before it, three of three checks on 5 mm data failed.

## Trägt nicht
Says nothing about whether the merged pair is clinically one or two microbleeds; the model grid decides.

## Bruchindikator
Counting components of a binary mask on thick slices and comparing them with a report.

## Ablesung
Own measurement 2026-10-16 (5 mm T2* slices). Background on small-lesion counting in CMB detection: Sudre et al.,
Med Image Anal 2024, doi:10.1016/j.media.2023.103029, PMID 37988921 (VALDO challenge).

## Verknüpft
[patches-not-whole-images-for-small-lesions](patches-not-whole-images-for-small-lesions.md)
