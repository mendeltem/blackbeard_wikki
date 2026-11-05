---
id: research-attrition-and-missing-data-longitudinal-stroke-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, public literature only; quellen-pruefen 2026-10-18 (21 references, 21 with PMID, 21 correct, 0 wrong); checked and committed by Claude Code
verweist_auf: [research-longitudinal-volumetry-statistics-after-stroke-2026-10, research-cross-sectional-vs-longitudinal-consistency-2026-10]
---

# Literature: drop-out and missing visits in long-term stroke and dementia imaging cohorts

## Aussage
- Attrition in long-term stroke/dementia cohorts is large and non-random: 40–77 % cumulative loss over 2–10 years is
  common, and the dominant causes are death, refusal, institutionalisation and loss of contact, not the imaging
  itself [1,2,4].
- Attrition is *informative*: the same variables that predict the outcome (older age, male sex, lower cognition,
  higher dementia rating, frailty/comorbidity, social isolation, more severe stroke) also predict drop-out
  [1,2,4,5]. A complete-case analysis therefore systematically drops the participants whose trajectories matter most.
- The bias can be quantified and is not small: after post-stroke patients unavailable for clinic visits were excluded,
  the measured 5-year dementia incidence fell from 29 % to 17 %, while the non-clinic-assessed patients had 45 %
  [3]. Inverse-probability-of-attrition weighting changed smoking–cognitive-decline estimates by 56–86 % [21].
- Death and non-participation must be distinguished and modelled as competing risks/events; collapsing them biases
  cognitive-decline and dementia-risk estimates [14,12,13].
- A linear mixed model fitted by (restricted) maximum likelihood is valid only under MAR and already uses all available
  observations; it is a defensible primary analysis but it is *not* a correction for informative drop-out [7,11].
- For outcome-related drop-out, the recommended toolkit is: multiple imputation (MI) with auxiliary variables, joint
  models of the longitudinal marker and the time-to-event, and pattern-mixture / delta-adjustment sensitivity analyses
  that deliberately depart from MAR [7,10,11,12,13].
- SDOH, transport, family support and the practical difficulty of bringing frail elderly patients to a scanner are
  modifiable drivers of LTFU, so retention is partly an operational problem, not only a statistical one [5].
- Image-quality exclusion is a second, independent, non-random filter: head motion biases cortical grey-matter volume
  and thickness downward by roughly 0.7 %/mm/min and remains significant even after a rigorous QC gate [15]; the
  Euler number is a reliable T1 quality measure but is regionally correlated with cortical thickness, so QC-based
  exclusion is itself a confounder of atrophy estimates [16].
- QC strategy matters: manual inspection is most reliable but subjective; Euler-number- and MRIQC-based outlier
  detection are the best automated alternatives, whereas excluding outliers on *global morphological measures*
  increases unexplained variance [17].
- Report the missing-data mechanism assumed, the proportion and pattern of missingness, the method, and at least one
  sensitivity analysis departing from MAR, per the TARMOS framework [8].

### Practical recommendation (as written for a multisite longitudinal stroke cohort)
Ordered, concrete, and mapped to the references.

**A. Design and measurement (before any modelling)**

1. Use every available follow-up channel, not just the scanner visit, to keep outcome ascertainment high. Pendlebury's
   protocol (home visit + telephone + primary-care record review) recovered 42 % of dementia diagnoses that clinic-only
   follow-up would have missed [3]. For our 0/6/36/60-month schedule, add a telephone/remote assessment and a
   record-based dementia/recurrent-stroke/death ascertainment at each wave.
2. Keep the same scanner per participant across waves if the schedule allows; always normalise volumes to intracranial
   volume; do not change the scanner vendor/model within a participant without recording it [18].
3. Treat head motion as a measured variable at every session (even though MPRAGE 1 mm is short) and include it as a
   covariate; a QC pass does not remove the motion bias [15,16].
4. Make the QC gate image-quality-based (Euler number / MRIQC-type metrics), and *log* every excluded time point with
   the reason. Do not gate on global morphological outliers — that increases unexplained variance [17]. Our
   SynthSeg QC >= 0.65 per-structure gate is fine, but record per-structure pass/fail, not only subject-level.
5. Expect lesion filling to help grey-matter measures on the raw-T1 side and to behave differently across software;
   report results on both raw T1 and lesion-filled T1 as a sensitivity analysis rather than choosing one [18].

**B. Primary analysis**

6. Primary: linear mixed model / restricted maximum likelihood on all available observations, with time, site, scanner,
   intracranial volume, age, sex, motion and lesion volume as fixed effects and random intercept + slope per
   participant. This is valid under MAR and uses incomplete trajectories [7].
7. Do *not* present the mixed model as a solution to informative drop-out. State explicitly the MAR assumption and
   list the auxiliary variables (baseline cognition, stroke severity/NIHSS, discharge disposition, comorbidity/frailty
   index, education, living situation, socioeconomic indicators) that predict both missingness and the outcome
   [1,2,4,5].
8. Harmonise with longComBat before trajectory modelling, and include scanner/site as a covariate in the model to
   protect against residual site effects [19].

**C. Missingness handling (the core of the question)**

9. Distinguish the missingness types in the data structure: (i) death, (ii) recurrent stroke / institutionalisation
   (competing events), (iii) refusal/no-contact, (iv) scan acquired but QC-failed, (v) sequence/metric missing. Do not
   collapse them [14,13].
10. Add a joint model of the longitudinal atrophy slope and the time-to-event of dementia/death (and ideally recurrent
    stroke as a competing risk) as the primary *sensitivity* model for the trajectory estimates; use it especially
    because SynthSeg volumes are measured with error, where a time-varying-covariate Cox model underestimates the
    marker–hazard association [11,12,13].
11. Run multiple imputation (with the auxiliary variables from item 7) as an alternative to the mixed model, and
    report how the two compare; use FIML as a third, cheap comparison [9].
12. Run a documented MNAR sensitivity analysis using MI with delta adjustment, with delta varying by an auxiliary
    variable (e.g. baseline cognition or frailty), and report the delta range at which conclusions change [10].
13. Quantify how much of the sample each filter removes: cumulative drop-out, per-visit scan availability, per-structure
    QC-fail rate, and sequence/modality availability — and compare baseline characteristics of retained vs lost
    participants in a table and an inverse-probability-of-participation weight [20,3].
14. Report the effect of assuming different outcomes for the missing: Du et al. found that 0–14.3 % of significant
    results became non-significant when alternative assumptions about LTFU patients were used [6]. Pre-specify a
    tipping-point analysis.

**D. Reporting**

15. Follow the TARMOS three-step framework [8]: (1) analysis plan stating the analysis model and the missing-data
    approach, and whether complete-records analysis is likely valid, whether MI is likely to help, and whether a
    sensitivity analysis on the mechanism is required; (2) examine the data and check those choices; (3) report the
    missing-data description, the method, all analyses, and interpret in light of missingness.
16. Minimum reporting set: proportion missing per variable per visit; mechanism assumed; reasons for missingness
    disaggregated (death/refusal/QC-fail/missing sequence); method; sensitivity analyses; and the software versions
    (SynthSeg 2 / FreeSurfer 8.2, longComBat) so the pipeline is reproducible [8,9].

**E. What is *not* recommended**

- Listwise deletion / complete-case analysis as the primary analysis [9,7].
- Gating on global morphological outliers [17].
- Reporting only clinic/scanner attendance without disaggregating non-attendance reasons [3,6].
- Presenting a mixed model as if it fixed non-random attrition [7].

## Trägt
21 references, each retrieved in the task with the literature tool and checked (PMID matches title, DOI registered at doi.org). Each reference carries one "Shows:" sentence from its abstract.

[1] Jacobsen E, Ran X, Liu A, et al. (2021). Predictors of attrition in a longitudinal population-based study of
aging. International Psychogeriatrics. doi:10.1017/S1041610220000447. PMID: 32301414.
Shows: 77 % of an aging cohort attrited over 10 years and drop-out was predicted by older age, male sex, lower
cognitive scores, higher clinical dementia ratings, lower function, inactivity and social isolation; the authors
conclude that ignoring attrition biases results when missingness relates to the outcome.

[2] Coley N, Gardette V, Touzé E, et al. (2008). Predictive factors of attrition in a cohort of Alzheimer disease
patients. The REAL.FR study. Neuroepidemiology. doi:10.1159/000144087. PMID: 18622142.
Shows: 40.5 % of 686 mild-to-moderate AD patients dropped out within 2 years, with refusal 20.9 %, death 20.1 %,
institutionalisation 19.8 % and loss to follow-up 19.8 %, at a constant ~12 % per 6-month wave, predicted by unrelated
caregiver, loss of autonomy and caregiver burden.

[3] Pendlebury ST, Chen PJ, Welch SJ, et al. (2015). Methodological Factors in Determining Risk of Dementia After
Transient Ischemic Attack and Stroke: (II) Effect of Attrition on Follow-Up. Stroke.
doi:10.1161/STROKEAHA.115.009065. PMID: 25953366.
Shows: in OXVASC 42 % of dementia diagnoses occurred in patients unavailable for clinic follow-up, and the 5-year
dementia incidence was 29 % overall but 17 % in clinic-assessed versus 45 % in non-clinic-assessed patients, so
excluding non-attenders halves the measured risk; multi-channel follow-up recovers most of it.

[4] Katsuno N, Li PZ, Bourbeau J, et al. (2023). Factors Associated with Attrition in a Longitudinal Cohort of Older
Adults in the Community. Chronic Obstructive Pulmonary Diseases. doi:10.15326/jcopdf.2022.0380. PMID: 37099700.
Shows: 77 % mean retention over a median 9 years in a multi-site cohort (dropout 39 %, loss of contact 27 %, death 9 %),
with lower education, higher pack-years, cardiovascular disease and higher anxiety/depression scores independently
predicting attrition.

[5] Larson S, John S, Gowrisankar S, et al. (2025). Social Determinants of Health Framework Identifies Patients at
Risk for Loss to Follow-Up After Stroke. Journal of the American Heart Association. doi:10.1161/JAHA.124.040986.
PMID: 40281658.
Shows: only 56 % of ~2600 ischaemic-stroke patients returned for follow-up; greater impairment, less education,
scheduling inflexibility and lack of home support were associated with lower follow-up, defining an at-risk population
and modifiable targets.

[6] Du P, Qin M, Liu Y, et al. (2026). Lost to follow-up in randomized clinical trials on long-term patient management
following stroke: A cross-sectional survey. International Journal of Stroke. doi:10.1177/17474930251394853.
PMID: 41137200.
Shows: across 58 post-stroke care trials, median LTFU was 9.0 % for patients with higher odds at older age and higher
female proportion, and assuming different event rates for LTFU patients rendered 0–14.3 % of significant results
non-significant.

[7] Ibrahim JG, Molenberghs G (2009). Missing data methods in longitudinal studies: a review. Test (Madrid).
doi:10.1007/s11749-009-0138-x. PMID: 21218187.
Shows: a detailed taxonomy of missing-data patterns, mechanisms (MCAR/MAR/MNAR), inferential paradigms and
sensitivity-analysis frameworks for longitudinal data, with concrete modelling devices and two case studies.

[8] Lee KJ, Tilling KM, Cornish RP, et al. (2021). Framework for the treatment and reporting of missing data in
observational studies: The Treatment And Reporting of Missing data in Observational Studies framework. Journal of
Clinical Epidemiology. doi:10.1016/j.jclinepi.2021.01.008. PMID: 33539930.
Shows: a three-step TARMOS framework — analysis plan, data examination, transparent reporting — to decide whether
complete-records analysis is valid, whether multiple imputation helps, and whether a missingness-mechanism sensitivity
analysis is required.

[9] Li L, Bayat M, Hayes TB, et al. (2025). Missing data approaches for longitudinal neuroimaging research: Examples
from the Adolescent Brain and Cognitive Development (ABCD) Study. Developmental Cognitive Neuroscience.
doi:10.1016/j.dcn.2025.101563. PMID: 40413902.
Shows: listwise deletion in large longitudinal neuroimaging datasets risks substantial bias, and multiple imputation,
propensity-score weighting and FIML are the recommended alternatives, illustrated with practical code on ABCD data.

[10] Leacy FP, Floyd S, Yates TA, et al. (2017). Analyses of Sensitivity to the Missing-at-Random Assumption Using
Multiple Imputation With Delta Adjustment: Application to a Tuberculosis/HIV Prevalence Survey With Incomplete
HIV-Status Data. American Journal of Epidemiology. doi:10.1093/aje/kww107. PMID: 28073767.
Shows: multiple imputation with delta adjustment imputes univariate missing data under general MNAR mechanisms and
enables sensitivity analyses with a constant delta or a delta varying by covariate, demonstrated on 34,446 survey
respondents.

[11] Asar Ö, Ritchie J, Kalra PA, et al. (2015). Joint modelling of repeated measurement and time-to-event data: an
introductory tutorial. International Journal of Epidemiology. doi:10.1093/ije/dyu262. PMID: 25604450.
Shows: in a nephrology case study a Cox model with a time-varying covariate substantially underestimated the
marker–hazard association because it ignores measurement error, whereas joint models combining a linear mixed-effects
model with a Cox model should be preferred.

[12] Proust-Lima C, Dartigues JF, Jacqmin-Gadda H (2016). Joint modeling of repeated multivariate cognitive measures
and competing risks of dementia and death: a latent process and latent class approach. Statistics in Medicine.
doi:10.1002/sim.6731. PMID: 26376900.
Shows: a joint latent-process/latent-class model handles multiple longitudinal markers of different natures together
with multiple causes of progression (dementia and death), with a score test for conditional independence and
individual dynamic cumulative incidences.

[13] van Oudenhoven FM, Swinkels SHN, Soininen H, et al. (2021). A competing risk joint model for dealing with
different types of missing data in an intervention trial in prodromal Alzheimer's disease. Alzheimer's Research &
Therapy. doi:10.1186/s13195-021-00801-y. PMID: 33752738.
Shows: a competing-risk joint model that models trajectory, timing and type of missingness simultaneously yielded
unbiased intervention-effect estimates in the LipiDiDiet trial despite high outcome-dependent missingness.

[14] Rajan KB, Leurgans SE (2010). Joint modeling of missing data due to non-participation and death in longitudinal
aging studies. Statistics in Medicine. doi:10.1002/sim.4010. PMID: 20645281.
Shows: treating non-participation and death as the same missingness type biases estimates in marginal models of
cognitive decline, and a multiple inverse-probability-weighting approach that separates the two missing-data types is
consistent and asymptotically normal under stated conditions.

[15] Reuter M, Tisdall MD, Qureshi A, et al. (2015). Head motion during MRI acquisition reduces gray matter volume and
thickness estimates. NeuroImage. doi:10.1016/j.neuroimage.2014.12.006. PMID: 25498430.
Shows: within-session motion tasks biased cortical grey-matter volume and thickness by about 0.7 % per mm/min of
motion, regionally varying and still significant after excluding scans that fail a rigorous quality check.

[16] Rosen AFG, Roalf DR, Ruparel K, et al. (2018). Quantitative assessment of structural image quality. NeuroImage.
doi:10.1016/j.neuroimage.2017.12.059. PMID: 29278774.
Shows: the FreeSurfer Euler number identified manually rated unusable T1 images with AUC 0.98–0.99 across samples but
was regionally related to cortical thickness, and failing to control for data quality systematically biased
age associations.

[17] Monereo-Sánchez J, de Jong JJA, Drenthen GS, et al. (2021). Quality control strategies for brain MRI segmentation
and parcellation: Practical approaches and recommendations - insights from the Maastricht study. NeuroImage.
doi:10.1016/j.neuroimage.2021.118174. PMID: 34000406.
Shows: comparing 12 QC strategies in 259 participants, manual QC reduced unexplained variance most, Euler-number and
MRIQC detection were the best automated alternatives, and excluding outliers on global morphological measures
increased unexplained variance and must be avoided.

[18] Guo C, Ferreira D, Fink K, et al. (2019). Repeatability and reproducibility of FreeSurfer, FSL-SIENAX and SPM brain
volumetric measurements and the effect of lesion filling in multiple sclerosis. European Radiology.
doi:10.1007/s00330-018-5710-x. PMID: 30242503.
Shows: across three Siemens scanners within-scanner variability was lower than between-scanner, ICV normalisation
improved FreeSurfer/SPM inter-scanner reproducibility, and lesion filling changed FSL-SIENAX/SPM/SPM-CAT but not
FreeSurfer output.

[19] Beer JC, Tustison NJ, Cook PA, et al. (2020). Longitudinal ComBat: A method for harmonizing longitudinal
multi-scanner imaging data. NeuroImage. doi:10.1016/j.neuroimage.2020.117129. PMID: 32640273.
Shows: in 663 ADNI participants additive and multiplicative scanner effects were present in cortical thickness and
longitudinal ComBat detected longitudinal change with more power and better type-I error control than cross-sectional
ComBat or unharmonised data with scanner as a covariate.

[20] Schoeler T, Speed D, Porcu E, et al. (2023). Participation bias in the UK Biobank distorts genetic associations
and downstream analyses. Nature Human Behaviour. doi:10.1038/s41562-023-01579-9. PMID: 37106081.
Shows: weighting UK Biobank to be representative changed SNP effect sizes and revealed novel associations for 12
traits, left heritability nearly unchanged (<= 5 %) but changed genetic correlations by up to 0.31 and Mendelian
randomisation estimates by up to 0.15.

[21] Weuve J, Tchetgen Tchetgen EJ, Glymour MM, et al. (2012). Accounting for bias due to selective attrition: the
example of smoking and cognitive decline. Epidemiology. doi:10.1097/EDE.0b013e318230e861. PMID: 21989136.
Shows: in the Chicago Health and Aging Project (n = 3713) higher previous cognitive score predicted both survival and
continued participation, and inverse-probability-of-attrition weighting increased the estimated smoking effect on
cognitive decline by 56–86 %, demonstrating an outcome-dependent missingness mechanism and a quantified bias.

## Trägt nicht
Open questions from the report:

- No retrieved reference validates a SynthSeg-specific QC threshold (ours: QC >= 0.65) against manual ratings in a
  stroke population; the QC literature assessed FreeSurfer Euler numbers and MRIQC [16,17]. The threshold's
  sensitivity/specificity relative to manual QC remains unverified here.
- No retrieved study quantifies the bias of *lesion-filled versus raw T1 atrophy slopes* in a longitudinal stroke
  cohort across scanners; Guo et al. compared software for MS lesion filling cross-sectionally [18], Magon et al.
  showed lesion filling changes cortical thickness longitudinally in MS, but not in a multi-site stroke cohort.
- The relative performance of competing-risk joint models versus MI with delta adjustment in a *stroke* cohort with
  a 5-year, sparse (0/6/36/60-month) schedule is not directly evidenced by retrieved work; the joint-model evidence
  comes from nephrology, AD trials and population ageing studies [11,13,12].
- How best to combine longComBat with a joint model (harmonise-then-model versus model site jointly) is not settled
  by the retrieved literature [19].

Claims rest on abstracts, not full texts, unless the report says otherwise.

## Bruchindikator
A full-text reading or a later consensus paper contradicts a cited effect size or recommendation; or our own cohort data show the opposite (for example no scanner effect at a scanner change).

## Ablesung
Report written 2026-10-18 by Clara (hospital model hub), question set by Claude Code after a pipeline audit; sources verified with quellen-pruefen the same day.

## Own run, 2026-11-05: do not read dropout-linked baseline scores as "who improves"
In a longitudinal rehabilitation cohort, baseline scores that predicted missing the last visit could not be read as predictors of improvement among those who stayed. One such score looked favourable in complete cases, with an interval above zero; the estimate fell by about three quarters under multiple imputation, and to about zero under a small pattern-mixture shift of those who left. Another score moved the opposite way, flat in complete cases and negative under the shift. So the sign depends on an assumption the data cannot test. Adding these scores did not improve leave-one-out prediction.
Working rule: sort every baseline column before the run (part of the outcome, measured later, linked to dropout, part of a total, validity problem) and state one reason per column. Keep dropout-linked scores out of the reported predictor list, but keep them in the imputation model, because auxiliary variables tied to missingness reduce bias there (Collins 2001, Psychol Methods, DOI 10.1037/1082-989X.6.4.330, unverified in this run). Staying out means the data cannot answer it, not that the column has no effect. Pattern-mixture reasoning: National Research Council 2010, The Prevention and Treatment of Missing Data in Clinical Trials, DOI 10.17226/12955 (unverified in this run).
