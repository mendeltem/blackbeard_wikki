---
id: synthseg-parc-moves-cortex-labels
typ: regel
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: own pipeline audit 2026-10-18 (Alita); two own scripts of 2026-10-17 counted the cortex with labels 3/42 only
verweist_auf: [synthseg-cortex-qc-depends-on-site-not-protocol, research-scanner-change-within-subject-longitudinal-2026-10]
---

# SynthSeg with --parc has no labels 3/42: the cortex is 1001-1035 / 2001-2035

## Aussage
`mri_synthseg --parc` (FreeSurfer 8.2.0, SynthSeg 2) replaces Left/Right-Cerebral-Cortex (FreeSurfer LUT 3/42) by the
Desikan-Killiany parcels 1001-1035 and 2001-2035. Code that selects the cortex as `[3, 42]` silently gets zero voxels:
on 2026-10-17 a cohort volume table had cortex = 0 ml in every session (so no cortex growth flag could ever fire), and a
rating page drew no cortex outline on any of its images, which also made a vision model's "no cortex error" verdicts
meaningless. Rule: cortex = `[3, 42] + range(1000, 1036) + range(2000, 2036)`, and every new label list is checked
against `np.unique` of one real segmentation before a cohort run (zero-voxel classes are an error, not a result).

## Trägt
Own audit 2026-10-18: after the fix the outline appears on every image (orange pixels per image from ~3 to ~44 000) and
the cortex volume column is non-zero. Label definitions: FreeSurferColorLUT; Billot et al. 2023, PNAS,
"Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets",
doi:10.1073/pnas.2216399120, PMID 36802420 (SynthSeg 2 with cortical parcellation).

## Trägt nicht
Without `--parc` the labels 3/42 exist; code must handle both.

## Bruchindikator
A structure total of exactly 0 in every row of a table, or an overlay colour that never appears in the rendered images.

## Ablesung
2026-10-18, pipeline audit of a ~1500-session cohort; pixel count of the overlay colour per image, `np.unique` of a segmentation.
