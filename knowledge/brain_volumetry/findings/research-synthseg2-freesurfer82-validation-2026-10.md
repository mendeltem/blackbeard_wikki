---
id: research-synthseg2-freesurfer82-validation-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-19
herkunft: two independent research reports by the remote-model agent (Clara on the hospital model hub), checked by Claude Code 2026-10-19 (quellen-pruefen 65 refs, 0 wrong; QC-threshold claim checked against the full text of Billot 2023 PNAS)
verweist_auf: [research-segmentation-qc-at-scale-2026-10, research-cross-sectional-vs-longitudinal-consistency-2026-10, research-scanner-change-within-subject-longitudinal-2026-10]
---

# Literature: how good is SynthSeg 2 in FreeSurfer 8.2 (`mri_synthseg --parc --robust`) for longitudinal volumetry

## Aussage
- Accuracy: SynthSeg reaches mean Dice 0.88 against manual labels on 1 mm MPRAGE (supervised in-domain network 0.91,
  SAMSEG 0.85) and is designed for raw scans without skull stripping or bias correction [1]. The robust version with
  cortical parcellation, QC and ICV ("SynthSeg+") is what `--parc --robust` runs [2]. Thin structures (cortex) lose
  accuracy first; no per-parcel validation of labels 1001-1035/2001-2035 against manual tracing was found.
- QC threshold 0.65 is validated for the whole-scan decision: "reject if at least one region scores below 0.65" gave
  sensitivity 0.999, specificity 0.906, accuracy 0.981, AUC 0.998 against an expert's pass/fail on 594 clinical scans;
  the value was chosen on a validation set. Per structure the authors applied it (age trajectories) but did not
  validate it separately [2]. The two reports disagreed here; the full text settles it.
- Precision: within-scanner smallest detectable change in a six-package comparison ranged from about 1 % (whole brain)
  upwards, and every package showed systematic between-scanner differences (between-scanner SDC from 4.8 %, SynthSeg
  thalamus) [3]. A same-session test-retest in an own cohort gave SDC95 0.66 % (brain), 1.38 % (cortex), but 4.67 % for
  the thalamus, worse than the 2-3 % reported for SynthSeg and SAMSEG in [3] (full-text value, per review).
- The FreeSurfer longitudinal stream improves test-retest precision by 15-50 % over cross-sectional processing [4];
  per-session SynthSeg is cross-sectional, so change measures need `recon-all -long` or SAMSEG for confirmation.
- Versions: `recon-all` 8.0 replaced the front end with SynthSeg, SynthStrip and SynthMorph and gives different output
  than version 7; 8.1 and 8.2 give the same output as 8.0 (FreeSurfer release notes, documentation, not peer-reviewed)
  [D1]. Never mix 7.x and 8.x within one longitudinal series. The 8.2 notes also warn that different combinations of build
  and execution operating system can give different results, and offer `fs-allowed-os.txt` / `fs-allowed-versions.txt`
  to lock them [D1]: workstation and HPC runs of the same series must use the same build and OS, or be compared first.
- Scanner change: a major upgrade shifted whole-brain volume by 3.4 % in healthy controls; a fixed corrective term
  was estimated [5].
- Lesions: in ischaemic stroke, masking infarcts before automated segmentation made hippocampal volumes agree *less*
  with manual tracing [6]; evidence on lesion filling is mixed, so keep the unfilled segmentation as a sensitivity
  analysis.
- Trust at group level: ICV, brain, GM, WM, ventricles, total cortex, thalamus. Confirm with a second method:
  hippocampus, amygdala, pallidum, thalamus and all change measures.

## Trägt
Two independent reports (35 + 32 references; quellen-pruefen 65 PMIDs correct, 0 wrong, 2 preprint/documentation
items without PMID). Threshold numbers read in the full text of [2] (Table 1 and Methods).

## Trägt nicht
Most precision figures come from MS or healthy cohorts, not stroke; the thalamus value from [3] was not in its abstract.
No peer-reviewed validation of `recon-all` 8.2 itself was found (only documentation). Pallidum reliability for SynthSeg
specifically was not retrievable.

## Bruchindikator
A per-structure validation of the 0.65 threshold showing poor agreement with visual ratings, or a validation of
FreeSurfer 8.x showing version effects within 8.x.

## Ablesung
Sources:
1. Billot B, Greve DN, Puonti O, et al. 2023. SynthSeg: segmentation of brain MRI scans of any contrast and resolution without retraining. Med Image Anal 86:102789. DOI 10.1016/j.media.2023.102789. PMID 36857946.
2. Billot B, Magdamo C, Cheng Y, et al. 2023. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. PNAS 120:e2216399120. DOI 10.1073/pnas.2216399120. PMID 36802420.
3. van Nederpelt DR, Amiri H, Brouwer I, et al. 2023. Reliability of brain atrophy measurements in multiple sclerosis using MRI: an assessment of six freely available software packages for cross-sectional analyses. Neuroradiology 65:1459-1472. DOI 10.1007/s00234-023-03189-8. PMID 37526657.
4. Rusinek H, Bokacheva L, Chen H, et al. 2026. Test-retest reliability of FreeSurfer measures of neurodegeneration. NeuroImage 333:121920. DOI 10.1016/j.neuroimage.2026.121920. PMID 41966233.
5. Sinnecker T, Schadelin S, Benkert P, et al. 2022. Brain atrophy measurement over a MRI scanner change in multiple sclerosis. NeuroImage Clin 36:103148. DOI 10.1016/j.nicl.2022.103148. PMID 36007437.
6. Khlif MS, Egorova N, Werden E, et al. 2019. A comparison of automated segmentation and manual tracing in estimating hippocampal volume in ischemic stroke and healthy control participants. NeuroImage Clin 21:101581. DOI 10.1016/j.nicl.2018.10.019. PMID 30606656.
D1. FreeSurfer release notes 8.0.0-8.2.0, https://surfer.nmr.mgh.harvard.edu/fswiki/ReleaseNotes (documentation).
