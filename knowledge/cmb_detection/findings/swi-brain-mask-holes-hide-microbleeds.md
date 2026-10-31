---
id: swi-brain-mask-holes-hide-microbleeds
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-31
herkunft: QC of the model inputs (valdo-t2s/qc/build_model_input_qc.py) and mask fix wk0a, 2026-10-30
verweist_auf: [valdo-cohort-3-mask-is-a-head-mask, count-lesions-on-the-fine-grid-deliver-a-label-map]
---

# A brain mask cut at "image > 0" punches holes exactly where SWI phase masking drove microbleeds to zero

## Aussage
SWI magnitude images multiplied with a phase mask can contain voxels of exactly 0 inside the brain, at the darkest
spots: microbleeds and haemorrhage remnants. A preprocessing step that intersects the brain mask with "image > 0"
removes these voxels; after masking and contrast inversion they are black instead of bright, so the network cannot
see the lesion. In-house SWI: about 8 % of the reference microbleeds touched such a hole, and every scan had holes; raw
SWI was exactly 0 in about three quarters of the hole voxels. T2*-GRE of the same site: 0.5 %; public VALDO T2*: 0.
Fix: fill the brain mask (3D fill-holes plus slice-wise axial fill), rebuild the inputs from the raw scan inside the
filled mask (a raw 0 inside the brain becomes the brightest value after inversion). After the fix 0.8 % of the
reference lesions remained outside the mask, all at the true brain edge, none in a hole.

## Trägt
Overlay QC page (image, mask, holes, reference lesions) on all scans of three cohorts, before and after; unit test
(enclosed hole filled, open notch kept).

## Trägt nicht
Absolute SWI detection numbers measured before the fix are too low by an unknown amount; comparisons between methods on
the same inputs stay fair.

## Bruchindikator
A SWI pipeline without phase masking (raw magnitude only), or a skull strip that does not use an intensity cut.

## Ablesung
Own QC 2026-10-30 (aggregates only). SWI phase masking: Haacke et al., Magn Reson Med 2004;52:612-618,
doi:10.1002/mrm.20198, PMID 15334582.

## Verknüpft
[valdo-cohort-3-mask-is-a-head-mask](valdo-cohort-3-mask-is-a-head-mask.md)
