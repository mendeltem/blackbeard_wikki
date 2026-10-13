---
id: infarct-filling-before-synthseg-does-not-remove-the-infarct-2026-10-13
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: DEMDAS pilot, 4 participants / 17 sessions, infarct_fill.py (FSL lesion_filling and enantiomorphic fill), SynthSeg 8.2.0 --parc --robust, 2026-10-13 evening
verweist_auf: [demdas-pipeline-protocol-v1, demdas-gm-qc-page-for-pia-12-participants-2026-10-13]
---

# Filling the infarct in the T1 before SynthSeg does not take it out of the grey-matter count

## Aussage
User decision 13.10.2026 evening: "filling before segmentation, implement everywhere". Measured first on the pilot before any
rollout: 17 sessions of the 4 reviewer participants, two filling methods, SynthSeg (FreeSurfer 8.2.0, `--parc --robust`, CPU)
on the filled T1, volumes compared with the RAW run:
- `wm`: FSL `lesion_filling`, WM mask = SynthSeg labels 2/41 minus the infarct, only components touching cerebral WM are filled
  (the tool refuses others). Cerebellar infarcts are never filled (labels 7/46 are not "WM" for lesion_filling).
- `mirror`: enantiomorphic fill (Nachev 2008): T1 flipped left-right, FLIRT 6 dof onto itself, infarct voxels replaced by the
  mirrored contralateral intensities scaled to the local level, 1-voxel feathered rim.

Result: the filled region is still labelled as grey matter by SynthSeg, because SynthSeg follows anatomy (shape prior), not
intensity. 110 ml territorial infarct (KOP7N936 M0): inside the mask RAW 68.6 ml GM / 36.2 ml WM; after `wm` fill 63.7 / 43.8;
after `mirror` 57.5 / 43.3. GM total changes by -0.6 % (`wm`) and -1.1 % (`mirror`), versus -8.0 % when the infarct is excluded
after segmentation. 51 ml cerebellar infarct (L2F7N926 M0): `wm` changes nothing (no component touches cerebral WM), `mirror`
-1.5 % GM with 39.5 of 46.7 ml still GM inside the mask. 7 ml and 6 ml infarcts: -0.1 to -0.3 %. Sessions without a mask:
identical to RAW (the run was a no-op there, 12 of 17 sessions; the `--min-ml` skip had a bug, fixed afterwards).

Consequence: "fill before" and "exclude after" are not alternatives for infarcts under SynthSeg. Filling changes the image but
the count stays; only the mask-based exclusion changes the count. The MS lesion-filling literature (Battaglini 2012, Chard
2010) concerns intensity-driven segmenters (FAST, SPM) and WM lesions; it does not transfer to cortical/cerebellar infarcts
under SynthSeg. If filling is wanted for FreeSurfer recon-all surfaces (a different question: surface placement, not counting),
that remains a v2 candidate on the HPC pilot. Cost: `wm` ~90 s, `mirror` ~220 s per session on the loaded CPU, 4 threads.

## Trägt
- `derivatives/demdas/fill_v2/{wm,mirror}/<id>_synthseg_parc.nii.gz`, `_T1w_filled.nii.gz`, `summary.csv`, `lauf.log` (34 runs, 0 failed).
- Check image of the 110 ml case (raw / wm / mirror T1 and the labels inside the mask) viewed 13.10. ~20:10.

## Trägt nicht
- Only 5 sessions carry a mask above 0.5 ml; no test-retest of the filled variant; no recon-all on the filled T1 yet.

## Bruchindikator
- A segmenter whose GM-in-mask drops below ~20 % after filling would make filling a real alternative; SynthSeg does not.

## Ablesung
- Battaglini M et al. Hum Brain Mapp 2012;33:2062-2071, doi:10.1002/hbm.21344; Chard DT et al. JMRI 2010;32:223-228,
  doi:10.1002/jmri.22214; Nachev P et al. Neuroimage 2008;39:1215-1226, doi:10.1016/j.neuroimage.2007.10.002;
  Billot B et al. PNAS 2023, doi:10.1073/pnas.2216399120. Own data: Tier own.

## Verknüpft
- [demdas-pipeline-protocol-v1](demdas-pipeline-protocol-v1.md)
