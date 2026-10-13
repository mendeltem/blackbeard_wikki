---
id: chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: visual review of all 17 multi-session pilot participants of a stroke cohort (55 sessions, review sheets per participant), 13.10.2026
verweist_auf: [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort, synthseg-in-freesurfer-8-runs-on-cpu-only]
---

# Chronic infarcts are invisible to DWI-based masks and get label 0 from SynthSeg; follow-up volumes need a carried-forward mask

## Aussage
In a longitudinal stroke cohort the acute infarct mask (DeepISLES on DWI/ADC/FLAIR) exists at baseline but is empty at 6, 36 and
60 months in 12 of 17 reviewed participants, because the chronic scar no longer restricts diffusion. SynthSeg (--robust) then
assigns the encephalomalacic cavity label 0 (it drops out of every tissue total AND of the intracranial volume) and labels the
gliotic rim as white matter or cortex. The "infarct excluded" variant is therefore complete only at baseline. A new infarct between
visits (one participant, 7 ml at an unscheduled 10-month visit) is caught by the DWI mask at that visit only. Rigid alignment of
follow-ups to baseline (FLIRT 6 dof, brain-masked T1) reached Dice 0.982-0.990 in all 55 sessions; FLAIR, DWI and ADC registered with
`flirt -nosearch` onto the T1 grid matched in every session; within-participant ICV drift stayed below 1.7 %.

## Traegt
Any longitudinal volumetry with acute-phase lesion masks; the decision to build chronic masks (union of earlier masks moved forward
+ a T1-based chronic-infarct model such as MAPPING/ATLAS) before interpreting follow-up GM/WM/CSF; a "new infarct" flag per session.

## Traegt nicht
Cohorts with lesion masks drawn on every visit; small lacunar infarcts that SynthSeg absorbs into CSF labels.

## Bruchindikator
A SynthSeg version that labels cavities as CSF; a DWI-based model that detects chronic lesions.

## Ablesung
13.10.2026, per-participant review sheets (T1+labels, FLAIR+mask, DWI+mask, counted groups, same slice across sessions); mask volumes
per session from the QC page data; label 0 verified by counting labels outside the counting groups (0 ml in all 55 sessions).

## Quellen
- Ozzoude M et al. 2020. Cortical thickness estimation in individuals with cerebral small vessel disease, focal atrophy, and chronic stroke lesions. Front Neurosci 14:598868. DOI 10.3389/fnins.2020.598868. PMID 33381009.
- Billot B et al. 2023. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. PNAS 120:e2216399120. DOI 10.1073/pnas.2216399120. PMID 36802420.
- Liew SL et al. 2022. A large, curated, open-source stroke neuroimaging dataset to improve lesion segmentation algorithms (ATLAS v2.0). Sci Data 9:320. DOI 10.1038/s41597-022-01401-7 (unverified this session).

## Verknuepft
- [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort](freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort.md)
- [synthseg-in-freesurfer-8-runs-on-cpu-only](synthseg-in-freesurfer-8-runs-on-cpu-only.md)
