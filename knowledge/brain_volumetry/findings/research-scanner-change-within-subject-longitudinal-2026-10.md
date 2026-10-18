---
id: research-scanner-change-within-subject-longitudinal-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, public literature only; quellen-pruefen 2026-10-18 (24 references, 24 with PMID, 24 correct, 0 wrong); checked and committed by Claude Code
verweist_auf: [research-longitudinal-volumetry-statistics-after-stroke-2026-10, research-cross-sectional-vs-longitudinal-consistency-2026-10]
---

# Literature: scanner, software or coil change between visits of the same participant

## Aussage
- A scanner change is a real, structure- and method-dependent bias, not noise: whole-brain atrophy measures moved
  by about 3.4-4.1 % across a 1.5 T -> 3 T upgrade [1], and 2-4 % regional grey-matter differences appeared even
  between two 3 T scanners of the same vendor after a firmware/software upgrade [2].
- Direction and size depend on the structure and on the contrast: cortical thickness increased in frontal,
  temporal and cingulate regions while parietal thickness and amygdala, pallidum, hippocampus and striatum
  volumes decreased across a Tim Trio -> Prisma upgrade [3]; another upgrade produced 30 % higher and more
  variable neocortical CNR, larger frontal volumes/thickness, and WMH volumes that were 68 % smaller on FLAIR [4].
- Scanner *software* alone is enough: an SNR increase of ~24 % after a software upgrade shifted SPM5 grey-matter
  volumes by up to 4.3 % [5]. Head coils are equally dangerous: replacing an 8-channel with a 32-channel coil gave
  6-9 % relative grey/white-matter volume differences with identical sequences [6].
- Reliability can look excellent (ICC > 0.8) while systematic between-scanner differences remain statistically
  significant in a large majority of regions [2]; ICC alone therefore does not prove longitudinal comparability.
- Effect sizes from multi-scanner test-retest in MS: between-scanner smallest detectable change ranged from 4.8 %
  (SynthSeg, thalamus) to 29 % (CAT12, thalamus), whole-brain ~1 % within scanner [8]; scanner differences between
  1.5 T Siemens Avanto, 3 T Skyra and 3 T Prisma were systematic for all tested segmentation tools [21].
- SynthSeg is the most contrast/resolution-robust of the compared tools [18] and had the best between-scanner
  reproducibility for large structures in the MS comparison [8], but this robustness does not make it immune to
  site/coil effects (tissue classifiers still differ by manufacturer and SNR [9]).
- Two harmonisation families: statistical (ComBat / longitudinal ComBat) and image-level (deep learning contrast
  harmonisation). longComBat is more powerful and better calibrated than cross-sectional ComBat for longitudinal
  cortical thickness [13]; travelling-subject designs need only about 6 well-scanned travelling subjects to
  reduce measurement bias by up to 85 % [16]; longComBat/ComBat performs well for diffusion but does *not* always
  help structural data and can be harmful when no scanner effect exists [14].
- No harmonisation method reliably removes a real scanner *change* in longitudinal structural data in all cases:
  ComBat matched distributions but could not increase ICC or remove scanner-change effects, and CycleGAN / neural
  style transfer were only slightly better [15].
- Correction options in practice: model the scanner as a covariate/time-varying factor (a mixed model with scanner
  type was sufficient to remove the upgrade effect after a corrective term in MS [1]); or harmonise longitudinally
  (longComBat [13]); or add an image-level contrast harmonisation step [17].
- Minimum pre-slope checks: verify per-visit DICOM/ProtocolName, manufacturer, model, software version and receive
  coil (these fields drive all above effects [4,5,6]); run MRIQC-style raw-image QC (site effects limit
  classifier generalisation to unseen sites [22]); gate on Euler number / surface quality, which correlates with
  manual ratings and biases cortical thickness [20]; and, if possible, include travelling subjects or a phantom.

### Practical recommendation (as written for a multisite longitudinal stroke cohort)
1. Metadata audit first. For every session extract from DICOM: Manufacturer, ManufacturerModelName,
   SoftwareVersions, ReceiveCoilName/TransmitCoilName, ProtocolName, SequenceName, and any reconstruction/distortion
   flags. Cross-tabulate against visit (0/6/36/60 months) and site. Any field that changes within a participant is a
   candidate "scanner change" variable [4,5,6,9].
2. Model the change explicitly. In the planned linear mixed model, include a *time-varying* scanner variable
   (site x model x software x coil composite, as the travelling-subject work defines "scanner" [14]) as a fixed
   effect, or a random scanner effect, in addition to the planned covariates. Where a clean upgrade with controls
   exists, a corrective term estimated from stable (control/travelling) subjects is a defensible option [1].
3. Run longComBat as the planned harmonisation, but verify the assumption. Because harmonising structural data
   that has no scanner effect can remove biology [14], first quantify the scanner effect (ICC, and the
   travelling-subject Cohen's-d style bias metric [16]) before harmonising. longComBat is preferable to
   cross-sectional ComBat for longitudinal thickness [13].
4. Run both raw and lesion-filled SynthSeg. SynthSeg is designed to be contrast/resolution-robust [18] and had the
   best large-structure between-scanner reproducibility in the six-tool MS comparison [8]; report the raw-vs-filled
   difference as a sensitivity analysis (no clear global penalty for filling in MS [8]; lesion-aware longitudinal
   segmentation improves reliability in lesioned brains [19]).
5. QC gates as planned, but make them scanner-aware. Keep SynthSeg QC >= 0.65 per structure, keep the Euler-number
   gate (objective, correlates with manual quality and with thickness [20]), and add MRIQC raw-image metrics per
   visit because unseen-site generalisation of automated QC is imperfect [22]. Inspect QC pass-rate as a function
   of site/visit: a differential pass-rate is itself evidence of a scanner effect.
6. Reference-structure drift check. Report TIV and a small set of large, stable structures per participant across
   visits; procedure-dependent TIV reliability means TIV should not be assumed constant [11].
7. Interpret with realistic effect sizes. Between-scanner smallest detectable changes of several percent
   (e.g. 4.8-6.5 % for SynthSeg thalamus/whole brain in [8]) can exceed true 36-60-month atrophic change; where an
   upgrade is unavoidable mid-study, prioritise a travelling-subject sub-study and/or a soft image-level
   harmonisation as a sensitivity analysis [15,17].
8. Report everything that changed: gradient-distortion correction / reconstruction settings, sequence and coil are
   known to shift thickness and volumes even between scanners of the same vendor and field strength [2,4,5,6].

## Trägt
24 references, each retrieved in the task with the literature tool and checked (PMID matches title, DOI registered at doi.org). Each reference carries one "Shows:" sentence from its abstract.

1. Sinnecker T, Schädelin S, Benkert P, et al. (2022). Brain atrophy measurement over a MRI scanner change in
   multiple sclerosis. NeuroImage: Clinical. doi:10.1016/j.nicl.2022.103148. PMID: 36007437.
   Shows: in 20 MS patients and 26 controls, mean whole-brain volume change during a 1.5 T -> 3 T upgrade was
   -4.1 +/- 0.8 % (MS) vs -3.4 +/- 0.6 % (controls); a 3.4 % corrective term from controls removed the scanner
   association in a linear mixed-effects model. Cited for scanner-upgrade effect size on atrophy and for the
   corrective-term strategy.
2. Medawar E, Thieleking R, Manuilova I, et al. (2021). Estimating the effect of a scanner upgrade on measures of
   grey matter structure for longitudinal designs. PLoS ONE. doi:10.1371/journal.pone.0239021. PMID: 34610020.
   Shows: Verio vs Skyra (3 T, FreeSurfer longitudinal stream, 116 adults) had ICC > 0.8 yet significant differences
   in >= 67 % of regions (~2-4 %); distortion correction only slightly reduced bias. Cited for the "high ICC but
   systematic bias" point.
3. Plitman E, Bussy A, Valiquette V, et al. (2021). The impact of the Siemens Tim Trio to Prisma upgrade and the
   addition of volumetric navigators on cortical thickness, structure volume, and 1H-MRS indices. NeuroImage.
   doi:10.1016/j.neuroimage.2021.118172. PMID: 34082116.
   Shows: across the upgrade, frontal/temporal/cingulate thickness and thalamus volume increased while parietal
   thickness and amygdala, globus pallidus, hippocampus and striatum volumes decreased; 1H-MRS unaffected. Cited
   for direction-dependent effect sizes on thickness and subcortical volumes.
4. Potvin O, Khademi A, Chouinard I, et al. (2019). Measurement Variability Following MRI System Upgrade.
   Frontiers in Neurology. doi:10.3389/fneur.2019.00726. PMID: 31379704.
   Shows: Trio -> Prismafit upgrades yielded ~30 % higher and more variable neocortical CNR, larger frontal
   volume/thickness, and 68 % smaller WMH volumes on FLAIR. Cited for WMH and contrast effects of upgrades.
5. Shuter B, Yeh IB, Graham S, et al. (2008). Reproducibility of brain tissue volumes in longitudinal studies:
   effects of changes in signal-to-noise ratio and scanner software. NeuroImage. doi:10.1016/j.neuroimage.2008.02.003.
   PMID: 18394925.
   Shows: a software upgrade raised voxel intensity 5-fold and WM SNR by 24 %, shifting SPM5 GM volumes by up to
   4.3 %. Cited for scanner-software-only effects and the recommendation to monitor SNR.
6. Panman JL, To YY, van der Ende EL, et al. (2019). Bias Introduced by Multiple Head Coils in MRI Research: An 8
   Channel and 32 Channel Coil Comparison. Frontiers in Neuroscience. doi:10.3389/fnins.2019.00729. PMID: 31379483.
   Shows: with stable sequence parameters, 8- vs 32-channel coils produced 6-9 % relative GM/WM volume differences
   from altered contrast/segmentation. Cited for head-coil effect size.
7. Biberacher V, Schmidt P, Keshavan A, et al. (2016). Intra- and interscanner variability of magnetic resonance
   imaging based volumetry in multiple sclerosis. NeuroImage. doi:10.1016/j.neuroimage.2016.07.035. PMID: 27431758.
   Shows: two MS patients scanned six times on each of three 3 T scanners had significant between-scanner
   differences and marked within-scanner repeat variability; effect size must exceed this false-positive magnitude.
   Cited for repeatability vs reproducibility magnitudes.
8. van Nederpelt DR, Amiri H, Brouwer I, et al. (2023). Reliability of brain atrophy measurements in multiple
   sclerosis using MRI: an assessment of six freely available software packages for cross-sectional analyses.
   Neuroradiology. doi:10.1007/s00234-023-03189-8. PMID: 37526657.
   Shows: across three 3 T scanners, ICCs 0.4-1 between scanners; within-scanner SDC 1.02 % (SAMSEG whole brain) to
   14.55 % (FreeSurfer CSF), between-scanner SDC 4.83 % (SynthSeg thalamus) to 29.25 % (CAT12 thalamus), with no
   clear filled-vs-non-filled difference. Cited for SynthSeg/FreeSurfer between-scanner SDC.
9. Dadar M, Duchesne S. (2020). Reliability assessment of tissue classification algorithms for multi-center and
   multi-scanner data. NeuroImage. doi:10.1016/j.neuroimage.2020.116928. PMID: 32413463.
   Shows: one individual across 73 sessions / 27 sites; all six tools differed significantly across manufacturers
   and SNR tertiles. Cited for vendor/SNR-driven segmentation bias.
10. Haddad E, Pizzagalli F, Zhu AH, et al. (2023). Multisite test-retest reliability and compatibility of brain
    metrics derived from FreeSurfer versions 7.1, 6.0, and 5.3. Human Brain Mapping. doi:10.1002/hbm.26147.
    PMID: 36437735.
    Shows: v7.1 cortical thickness had low compatibility with older versions (ICC 0.37-0.61 on cingulate), similar
    for some surface areas and subcortical volumes, and version differences altered downstream age associations.
    Cited for pipeline/software-version effects (relevant to FreeSurfer 8.2 cross-sectional recon-all).
11. Koike S, Maikusa N, Cai L, et al. (2025). Estimation of the Intracranial Volume Is Crucial in Multi-Site
    Studies: Reliability for Longitudinal Investigations and Traveling Subjects. Human Brain Mapping.
    doi:10.1002/hbm.70405. PMID: 41190774.
    Shows: across 6524 scans, 21 sites and 13 machine types, eTIV vs sbTIV agreement varied by procedure (ICC
    0.62-0.94; 1.0 mm isotropic best; sbTIV more consistent longitudinally). Cited for TIV as a multi-site drift
    probe.
12. Reuter M, Schmansky NJ, Rosas HD, et al. (2012). Within-subject template estimation for unbiased longitudinal
    image analysis. NeuroImage. doi:10.1016/j.neuroimage.2012.02.084. PMID: 22430496.
    Shows: an unbiased within-subject template with identical treatment of all time points increases precision and
    discrimination power while avoiding over-regularisation. Cited for the principle behind longitudinal pipelines.
13. Beer JC, Tustison NJ, Cook PA, et al. (2020). Longitudinal ComBat: A method for harmonizing longitudinal
    multi-scanner imaging data. NeuroImage. doi:10.1016/j.neuroimage.2020.117129. PMID: 32640273.
    Shows: on 663 ADNI cortical thickness datasets, longitudinal ComBat was more powerful for detecting
    longitudinal change than cross-sectional ComBat and controlled type-I error better than unharmonised data with
    scanner as covariate. Cited for longComBat.
14. Richter S, Winzeck S, Correia MM, et al. (2022). Validation of cross-sectional and longitudinal ComBat
    harmonization methods for magnetic resonance imaging data on a travelling subject cohort. NeuroImage: Reports.
    doi:10.1016/j.ynirp.2022.100136. PMID: 36507071.
    Shows: in 73 travelling subjects / 161 scans, structural data had no scanner effect and harmonisation obscured
    biology, while diffusion data were successfully harmonised; longComBat was less effective for cross-sectional
    WM data. Cited for "do not harmonise without a scanner effect" and for harmonisation validation design.
15. Gebre RK, Senjem ML, Raghavan S, et al. (2023). Cross-scanner harmonization methods for structural MRI may
    need further work: A comparison study. NeuroImage. doi:10.1016/j.neuroimage.2023.119912. PMID: 36731814.
    Shows: GE -> Siemens comparison (113 crossover, 454 longitudinal) revealed scanner-change over/underestimation
    of cortical thickness; ComBat matched distributions but could not raise ICCs or remove scanner-change effects,
    and CycleGAN/NST only slightly better. Cited for the limits of harmonisation across a real scanner change.
16. Maikusa N, Zhu Y, Uematsu A, et al. (2021). Comparison of traveling-subject and ComBat harmonization methods
    for assessing structural brain characteristics. Human Brain Mapping. doi:10.1002/hbm.25615. PMID: 34402132.
    Shows: TS-GLM and TS-ComBat reduced measurement bias by up to 85 % and 81.3 % vs 59 % for ComBat, with at least
    six travelling subjects needed under matched protocols. Cited for travelling-subject design requirements.
17. Dewey BE, Zhao C, Reinhold JC, et al. (2019). DeepHarmony: A deep learning approach to contrast harmonization
    across scanner changes. Magnetic Resonance Imaging. doi:10.1016/j.mri.2019.05.041. PMID: 31301354.
    Shows: a U-Net trained on an 8-subject overlap cohort improved cross-protocol volume-consistency and largely
    removed protocol-change effects on MS atrophy calculations. Cited for image-level harmonisation.
18. Billot B, Greve DN, Puonti O, et al. (2023). SynthSeg: Segmentation of brain MRI scans of any contrast and
    resolution without retraining. Medical Image Analysis. doi:10.1016/j.media.2023.102789. PMID: 36857946.
    Shows: domain-randomised training makes SynthSeg robust to contrast and resolution changes, generalising across
    five modalities and ten resolutions without retraining. Cited for SynthSeg's robustness justification.
19. Cerri S, Greve DN, Hoopes A, et al. (2023). An open-source tool for longitudinal whole-brain and white matter
    lesion segmentation. NeuroImage: Clinical. doi:10.1016/j.nicl.2023.103354. PMID: 36907041.
    Shows: subject-specific latent variables enforcing temporal consistency raise test-retest reliability and
    sensitivity to longitudinal disease effects in AD/MS data. Cited for lesion-aware longitudinal segmentation.
20. Bedford SA, Ortiz-Rosa A, Schabdach JM, et al. (2023). The impact of quality control on cortical morphometry
    comparisons in autism. Imaging Neuroscience. doi:10.1162/imag_a_00022. PMID: 38495338.
    Shows: FreeSurfer surface quality interacts with clinical/demographic factors; thresholding by QC attenuates
    but does not eliminate quality impact, and inadequate QC control alters case-control results. Cited for QC as a
    mandatory step before morphometry.
21. Sederevičius D, Vidal-Piñeiro D, Sørensen Ø, et al. (2021). Reliability and sensitivity of two whole-brain
    segmentation approaches included in FreeSurfer - ASEG and SAMSEG. NeuroImage. doi:10.1016/j.neuroimage.2021.118113.
    PMID: 33940143.
    Shows: SAMSEG had significantly lower differences between repeated measures for intra- and inter-scanner data
    than ASEG without losing sensitivity. Cited for segmentation-method choice under scanner change.
22. Esteban O, Birman D, Schaer M, et al. (2017). MRIQC: Advancing the automatic prediction of image quality in MRI
    from unseen sites. PLoS ONE. doi:10.1371/journal.pone.0184661. PMID: 28945803.
    Shows: MRIQC's accept/exclude classifier reached 76 % +/- 13 % accuracy on new sites, i.e. it is susceptible to
    site effects and needs site-aware use. Cited for raw-image QC in a 7-site cohort.
23. Fortin JP, Cullen N, Sheline YI, et al. (2018). Harmonization of cortical thickness measurements across
    scanners and sites. NeuroImage. doi:10.1016/j.neuroimage.2017.11.024. PMID: 29155184.
    Shows: ComBat removed scanner-related variability in cortical thickness across two large multi-site studies
    (11 scanners) and increased power and reproducibility of subsequent analyses. Cited as the statistical
    foundation of the ComBat family used for structural MRI.
24. Radua J, Vieta E, Shinohara R, et al. (2020). Increased power by harmonizing structural MRI site differences
    with the ComBat batch adjustment method in ENIGMA. NeuroImage. doi:10.1016/j.neuroimage.2020.116956.
    PMID: 32470572.
    Shows: in 2897 schizophrenia cases and 3141 controls from 33 sites, ComBat mega-analysis substantially increased
    statistical significance versus random-effects meta-analysis and slightly versus mixed-effects mega-analysis.
    Cited for the power gain of ComBat over site-as-covariate approaches at scale.

## Trägt nicht
Open questions from the report:

- What is the exact effect size of a head-coil change specifically on SynthSeg 2 output? The coil literature we
  retrieved used VBM/FSL [6]; a direct SynthSeg coil comparison was not found.
- Can scanner/platform changes be detected automatically and reliably from DICOM headers in a longitudinal cohort
  (the sub-question's literal form)? No validated algorithm was retrieved; this remains unverified here and is a
  gap for a methods paper.
- Does longComBat remain calibrated when the scanner variable is *time-varying within subject* (an upgrade midway),
  as opposed to the between-subject site structure assumed in most ADNI-style evaluations [13,15]?
- Which is better for a stroke cohort with WMH: longComBat on FreeSurfer/SynthSeg volumes, a scanner covariate in
  the mixed model, or image-level deep harmonisation? The retrieved comparison suggests none dominates [15].
- Stroke-specific lesion-filling effects on cortical thickness across visits were not directly retrieved; the
  closest evidence is MS and general lesion-aware longitudinal segmentation [8,19].
- Whether a travelling-subject sub-study of ~6 participants [16] is sufficient when the coil, not just the
  platform, changes.

Claims rest on abstracts, not full texts, unless the report says otherwise.

## Bruchindikator
A full-text reading or a later consensus paper contradicts a cited effect size or recommendation; or our own cohort data show the opposite (for example no scanner effect at a scanner change).

## Ablesung
Report written 2026-10-18 by Clara (hospital model hub), question set by Claude Code after a pipeline audit; sources verified with quellen-pruefen the same day.
