---
id: freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: literature research 13.10.2026 (PubMed-verified), for the DEMDAS-like stroke cohort (586 participants, 1616 sessions, 7 sites); full report demdas-gm/literatur/segmentation_best_practice_2026-10-13.md
verweist_auf: [longitudinal-volumetry-needs-error-statistics, synthseg-in-freesurfer-8-runs-on-cpu-only, cohort-copies-need-a-gzip-sweep]
---

# FreeSurfer as the main tool for a longitudinal stroke cohort: what the evidence says to do, in order

## Aussage
With FreeSurfer 8.2 as the main tool, the evidence-backed levers for volumes and cortical thickness in a stroke / small-vessel
cohort with visits at 0, 6, 36 and 60 months are, in order of expected gain:

1. **Longitudinal stream instead of per-session runs.** In 11 datasets (n = 3,611, FS 7.1) the cross-sectional stream was about
   0.25 ICC lower for change than the long stream; ICC of change for 3 visits was 0.24 at 2 years, 0.54 at 4, 0.72 at 6 [7]. The
   0 to 6-month contrast is therefore mostly noise; atrophy rates should come from 0/36/60 months. Baseline-only participants
   (121 of 586 here) are run as one-time-point bases and enter mixed models for intercept and covariate effects.
2. **Lesion handling before recon-all.** Unfilled WM lesions bias GM up and WM down (+2.3 % / -3.6 % for 15 ml, cut to 0.1 % by
   filling) [10]; masking alone does not remove the bias, refilling does [11]; 72 % of MS lesion volume was labelled GM and unfilled
   cortex came out thinner [12]. In chronic stroke / SVD (ONDRI, n = 155) a lesion- and atrophy-aware FreeSurfer procedure raised
   acceptable ratings from 18 % to 76 % (ribbon) and cut tissue-segmentation failures from 62 % to 8 % [13]. Fill WM lesions
   (WMH + WM infarct) with FSL lesion_filling; cortical or cavitary infarcts via inpainting (FastSurfer-LIT, validated on tumours
   and cavities, not yet on infarcts [14]) or masking; ALWAYS exclude lesion-overlapping vertices and voxels from ROI statistics.
3. **FLAIR for the pial surface (-FLAIRpial).** Plausible for WMH-rich brains, but no quantitative study was found: test it on
   30-40 sessions against Euler number, edit need and the local SDC95 before using it cohort-wide.
4. **QC gate per session.** Euler number is the best automated correlate of manual quality (AUC 0.98-0.99, n = 1,840) [15]; in the
   Maastricht Study Euler number and MRIQC were the best strategies and excluding global-morphology outliers made things worse [16];
   Qoala-T (AUC 0.98) needs recalibration [17]. Head motion lowers GM volume and thickness by about 0.7 % per mm/min even after
   visual QC [20], the same order as yearly atrophy, so keep a motion proxy as covariate.
5. **Local test-retest.** The 40 sessions with two T1 acquisitions in the same session give the cohort's own SDC95 per ROI;
   use it as the threshold for implausible within-subject jumps (section "errors" below) and to decide which small structures
   (amygdala, thalamus) are interpretable.
6. **Harmonisation on the tables.** ComBat removed scanner effects in cortical thickness across 11 scanners [21]; longComBat
   (ADNI, n = 663) is more powerful for change and controls type I error better than scanner-as-covariate [23]. Apply after QC,
   protecting age, sex, group and lesion load.
7. **SynthSeg only as comparator / fallback** for large tissue volumes: traveling-subject variation 3.1 % on average, up to
   15-20 %, amygdala and ventral DC 7-8 %, hippocampi systematically larger than FastSurfer's [8]; no independent evidence of
   better site robustness than FreeSurfer on 1 mm MPRAGE. SynthSeg inside FreeSurfer 8.2 is CPU-only here (see linked finding).

**Segmentation errors across time points (M0, M10, M60): detect and handle.** Detect per time point with Euler number (per-site
threshold), MRIQC, recalibrated Qoala-T; within participant flag residuals from a robust line above the local SDC95, non-monotonic
jumps in structures that only shrink, sudden asymmetry changes, and TIV drift (skull-strip or registration error). Handle in this
order: rerun with lesion-filled T1 (and -FLAIRpial where the FLAIR is good); manual edits only on flagged cases, one editor,
documented, on the cross-sectional run BEFORE building the base so the template inherits the fix (edits had large effects on
subcortical volumes in the Maastricht Study [16]); the long stream reduces time-point-specific errors but cannot repair an error in
the template [3,7]; exclude single time points, not participants; mixed models with a per-time-point QC covariate and a
sensitivity analysis, because failures concentrate in the sickest [13]. Expect a first-pass failure rate above 10 % in this
population (ONDRI unmodified: 11 % ribbon, 62 % tissue fails [13]).

## Traegt
Pipeline decisions for DEMDAS-like cohorts (Siemens 3T MPRAGE + FLAIR, infarcts, WMH, 7 sites); the ordering of Clara tasks
wd4 (QC gate), wd5 (long stream), wd6 (benchmark) and the pilot variants (baseline, lesion-filled, lesion-filled + FLAIRpial, LIT).

## Traegt nicht
Cohorts without FLAIR or without lesion masks; FastSurfer-longitudinal (no published reliability found); any claim about
-FLAIRpial effect sizes (none found); infarct-cavity filling (no study found).

## Bruchindikator
A published stroke-cohort comparison that ranks the tools differently; a quantitative -FLAIRpial study; FastSurfer-long reliability
data; a local pilot in which lesion filling does not lower the Euler number or SDC95.

## Ablesung
PubMed lookups 13.10.2026 (24 references, 20 PMID-verified, 4 marked unverified: Kondrateva 2025 and Uhr 2025 preprints, the
FastSurfer v2.4.2 software record, Backhausen 2016 title/DOI). Pilot numbers from demdas-gm (23 participants, 63 sessions).

## Quellen
1. Fischl B et al. 2002. Whole brain segmentation: automated labeling of neuroanatomical structures in the human brain. Neuron 33:341-355. DOI 10.1016/S0896-6273(02)00569-X. PMID 11832223.
2. Fischl B. 2012. FreeSurfer. NeuroImage 62:774-781. DOI 10.1016/j.neuroimage.2012.01.021. PMID 22248573.
3. Reuter M et al. 2012. Within-subject template estimation for unbiased longitudinal image analysis. NeuroImage 61:1402-1418. DOI 10.1016/j.neuroimage.2012.02.084. PMID 22430496.
4. Henschel L et al. 2020. FastSurfer: a fast and accurate deep learning based neuroimaging pipeline. NeuroImage 219:117012. DOI 10.1016/j.neuroimage.2020.117012. PMID 32526386.
5. Billot B et al. 2023. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets (SynthSeg). PNAS 120:e2216399120. DOI 10.1073/pnas.2216399120. PMID 36802420.
6. Cerri S et al. 2021. A contrast-adaptive method for simultaneous whole-brain and lesion segmentation in multiple sclerosis (SAMSEG). NeuroImage 225:117471. DOI 10.1016/j.neuroimage.2020.117471. PMID 33099007.
7. Vidal-Pineiro D et al. 2025. Reliability of structural brain change in cognitively healthy adult samples. Imaging Neuroscience 3:imag_a_00547. DOI 10.1162/imag_a_00547. PMCID PMC12319936.
8. Kondrateva E et al. 2025. Benchmarking the reproducibility of brain MRI segmentation across scanners and time. arXiv:2504.15931 (preprint, unverified).
9. DZNE software record: FastSurfer v2.4.2 release, https://pub.dzne.de/record/277720 (unverified).
10. Chard DT et al. 2010. Reducing the impact of white matter lesions on automated measures of brain gray and white matter volumes. J Magn Reson Imaging 32:223-228. DOI 10.1002/jmri.22214. PMID 20575080.
11. Battaglini M et al. 2012. Evaluating and reducing the impact of white matter lesions on brain volume measurements. Hum Brain Mapp 33:2062-2071. DOI 10.1002/hbm.21344. PMID 21882300.
12. Magon S et al. 2014. White matter lesion filling improves the accuracy of cortical thickness measurements in multiple sclerosis patients: a longitudinal study. BMC Neurosci 15:106. DOI 10.1186/1471-2202-15-106. PMID 25200127.
13. Ozzoude M et al. 2020. Cortical thickness estimation in individuals with cerebral small vessel disease, focal atrophy, and chronic stroke lesions. Front Neurosci 14:598868. DOI 10.3389/fnins.2020.598868. PMID 33381009.
14. Pollak C et al. 2025. FastSurfer-LIT: lesion inpainting tool for whole-brain MRI segmentation with tumors, cavities, and abnormalities. Imaging Neuroscience 3. DOI 10.1162/imag_a_00446. PMID 40109899.
15. Rosen AFG et al. 2018. Quantitative assessment of structural image quality. NeuroImage 169:407-418. DOI 10.1016/j.neuroimage.2017.12.059. PMID 29278774.
16. Monereo-Sanchez J et al. 2021. Quality control strategies for brain MRI segmentation and parcellation: practical approaches and recommendations - insights from the Maastricht Study. NeuroImage 237:118174. DOI 10.1016/j.neuroimage.2021.118174. PMID 34000406.
17. Klapwijk ET et al. 2019. Qoala-T: a supervised-learning tool for quality control of FreeSurfer segmented MRI data. NeuroImage 189:116-129. DOI 10.1016/j.neuroimage.2019.01.014. PMID 30633965.
18. Esteban O et al. 2017. MRIQC: advancing the automatic prediction of image quality in MRI from unseen sites. PLoS One 12:e0184661. DOI 10.1371/journal.pone.0184661. PMID 28945803.
19. Backhausen LL et al. 2016. Quality control of structural MRI images applied using FreeSurfer: a hands-on workflow to rate motion artifacts. Front Neurosci 10:558 (title/DOI unverified). PMID 27570508.
20. Reuter M et al. 2015. Head motion during MRI acquisition reduces gray matter volume and thickness estimates. NeuroImage 107:107-115. DOI 10.1016/j.neuroimage.2014.12.006. PMID 25498430.
21. Fortin JP et al. 2018. Harmonization of cortical thickness measurements across scanners and sites. NeuroImage 167:104-120. DOI 10.1016/j.neuroimage.2017.11.024. PMID 29155184.
22. Fortin JP et al. 2017. Harmonization of multi-site diffusion tensor imaging data. NeuroImage 161:149-170. DOI 10.1016/j.neuroimage.2017.08.047. PMID 28826946.
23. Beer JC et al. 2020. Longitudinal ComBat: a method for harmonizing longitudinal multi-scanner imaging data. NeuroImage 220:117129. DOI 10.1016/j.neuroimage.2020.117129. PMID 32640273.
24. Uhr V et al. 2025. Deep-learning versus classical pipelines and white-matter hypointensities. arXiv:2503.20571 (preprint, unverified).

## Verknuepft
- [longitudinal-volumetry-needs-error-statistics](../rules/longitudinal-volumetry-needs-error-statistics.md)
- [synthseg-in-freesurfer-8-runs-on-cpu-only](synthseg-in-freesurfer-8-runs-on-cpu-only.md)
- [cohort-copies-need-a-gzip-sweep](../rules/cohort-copies-need-a-gzip-sweep.md)
