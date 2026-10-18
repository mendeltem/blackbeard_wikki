---
id: research-segmentation-qc-at-scale-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, checked by Claude Code 2026-10-18 (quellen-pruefen 0 wrong, 'Shows' spot checks against abstracts)
verweist_auf: [synthseg-cortex-qc-depends-on-site-not-protocol]
---

# Literature: quality control of automatic brain segmentation in ~1500 sessions

## Aussage
- No single automated score decides quality. The comparison of 12 QC strategies on 259 FreeSurfer-processed
  scans found manual QC reduced unexplained variance most, and that the best automated substitutes were the
  FreeSurfer Euler number and MRIQC scores, while excluding outliers on global morphological measures *increased*
  unexplained variance [1].
- The Euler number is the best-validated cheap structural QC metric: it correlated with manual ratings across
  samples and identified scans rated "unusable" with AUC 0.98-0.99 [3]. Surface-hole number, its close relative,
  reproducibly identified lower-quality scans with good specificity in 11,263 adolescent T1 scans [10].
- Supervised QC classifiers beat individual metrics, but only after training on ratings of the same kind of data:
  Qoala-T reached AUC 0.98 on a developmental cohort and transferred to two unseen datasets [4], whereas MRIQC and
  CAT12 agreed with visual QC only at kappa = 0.30 / 0.28 in an elderly clinical sample, and a classifier trained
  on those metrics and datasets reached 87.7% balanced accuracy (78.2% leave-one-site-out) [2].
- SynthSeg/SynthSeg+ do not remove the need for QC, but they do provide segmentation-side signals: SynthSeg+ adds
  automated detection of faulty segmentations mainly caused by very low scan quality [7][6], and SynthSeg QC scores
  exposed a systematic failure mode that was only visible when the cohort was rated and split by age (infant pass
  rate 36%, rising to 91% after rescale + crop to adult brain size and field of view) [8].
- Calibration on a rated subsample is the standard route [1][2][4], but the rated subsample must be large enough
  to bound the kappa confidence interval of interest, which can be planned explicitly [15]; a rating page with 53
  stratified sessions is a reasonable pilot but will give wide CIs and needs a documented prevalence correction.
- Visual QC protocols are mature and shareable: ENIGMA-style workflows rate raw images and, separately, identify
  and classify single-region parcellation errors by type, size and direction with standardised coding that
  computes an overall pass / minor / major / fail rating [11]; detailed hands-on rating scales exist for motion
  artefacts [16] and for paediatric data processed with FreeSurfer and ENIGMA tools [17].
- Rater effort can be cut without dropping the human decision: a team pipeline that visually inspects every
  pipeline output and aggregates ratings across pipelines and datasets achieved high inter-rater agreement on
  thousands of structural and diffusion scans at acceptable time cost [14]; standardised error taxonomies with
  severity scales show high between-rater reliability, and manual correction itself contributes at most ~3% error
  variance to subfield volumes [13].
- Editing is not automatically "better": manual edits reliably improve segmentation quality and reduce
  contrast-related bias in FreeSurfer morphometry [20], and in adolescent data they reproducibly altered cortical
  thickness and *strengthened* age-thickness associations [10], but they change subcortical volumes
  substantially and should be recorded as a binary covariate and reported [1][20].
- Longitudinal consistency is a QC measure in its own right: different hippocampal segmentation algorithms
  disagreed strongly on 1-year change (ICC 0.32 at 1.5 T, 0.15 at 3 T) and produced implausible volume growth in
  3-49% of subjects, with only ~51-58% of subjects passing stringent QC [18]; using FreeSurfer's longitudinal
  stream improved test-retest precision by 15-50%, and image quality indexed by the Euler number was a
  determinant of that precision [19].

### Practical recommendation (as written for our setup)
Setup: SynthSeg on ~1500 sessions, FreeSurfer recon-all on the same sessions, one blind rating page with 53
stratified sessions.

1. Run a two-track automated screen, not a single score.
   Track A (segmentation side): SynthSeg/SynthSeg+ automated fault detection output and the SynthSeg QC scores,
   reported as a pass rate per stratum [7][8]. Track B (image/surface side): FreeSurfer Euler number per
   hemisphere, MRIQC IQMs, plus a Qoala-T-style feature set from the FreeSurfer output [1][3][4][5]. Percentage
   of unexplained variance / measurement-error reduction is the metric that decided between strategies in the
   only head-to-head comparison available [1].
2. Use the Euler number as the primary scalar threshold, on both reconstructions, because it is the metric with
   the best documented and replicated agreement with human "unusable" ratings (AUC 0.98-0.99) [3] and it was
   among the two best automated strategies in the strategy comparison [1][19]. Do not use volume outliers of
   global morphological measures as an exclusion criterion [1].
3. Use the 53 rating page to calibrate, and extend it before freezing thresholds.
   - Rate all 53 blind; compute kappa / ICC between raters and between the automated decision and the consensus
     rating, per stratum, and report raw agreement too [2][13].
   - Treat 53 as a pilot: use the kappa CI width as the planning criterion and enlarge the rated set until the
     CI is narrow enough for the intended use (e.g. via the kappaSize approach [15]); stratify further if the
     failure rate differs by site, age/brain size or motion subgroup [2][4][8].
   - Because failure prevalence is usually low, report sensitivity and specificity rather than only kappa, and
     expect a clinically usable classifier with a modest kappa — that is the documented outcome in elderly
     clinical cohorts [2].
4. Make the rating protocol ENIGMA-compatible from the start.
   Region-level error identification (type, size, direction) plus a per-brain rating pass / minor / major / fail /
   discuss, recorded in a spreadsheet with standardised codes so the overall rating is computed automatically
   [11]; keep the motion-oriented raw-image scale for the raw-data decision [16], and keep the ROI-level variant
   (drop single regions with major errors instead of the whole session) [17].
5. Inspect every pipeline output visually, but cheaply. Design the page for low effort: one quick overlay view
   per session, a shared rating store, aggregation across pipelines (SynthSeg, recon-all) and datasets, and two
   raters on a subset to quantify agreement — this was feasible on a large cohort with high inter-rater agreement
   [14]. Report the QC protocol and the exclusion rate in the methods [12].
6. Decide the failure policy per failure type, and document it.
   - Fixable/systematic failures (geometry, field of view, brain size): re-run pre-processing with rescale/crop
     and re-screen before considering exclusion; this recovered a majority of failing scans in a developmental
     cohort [8].
   - Local/segmentation errors: prefer targeted manual edits over exclusion, record edit status per region, and
     run the main analysis with an edited-yes/no covariate and a sensitivity analysis without the edited cases
     [1][10][13][20].
   - Unusable raw data (severe motion, no segmentation of any tool): exclude and record, with the rating that
     justifies it [11][16].
   - Never silently exclude: exclusion changes effect estimates, and quality is correlated with age and with
     clinical variables, so exclusion can create or hide associations [3][4][10][18].
7. For sessions with repeated time points, add longitudinal consistency checks (implausible direction or size of
   volume change per structure, e.g. hippocampal volume increase beyond a noise threshold) as a separate red flag
   [18][19], and prefer FreeSurfer's longitudinal stream for the reported change measures (+15-50% precision)
   [19].
8. Report quality as a distribution, not as a binary: pass rates per stratum, Euler number distribution, number
   of edited sessions, and the QC-vs-outcome sensitivity analysis [1][10][12][21].

## Trägt
Every reference retrieved in the task; quellen-pruefen: 0 wrong PMIDs/titles, DOIs registered (2026-10-18); one "Shows"
sentence per reference from its abstract; spot checks consistent.

## Trägt nicht
Abstract-level evidence, a literature map rather than a systematic review. Open questions:

- How well do the SynthSeg QC scores and SynthSeg+'s fault detector rank against human ratings in *adult*
  cohorts? The retrieved evidence documents the failure mode mainly in developmental data (36% -> 91% pass rate
  after rescale/crop) [8] and its use in clinical data at scale without a human-rated benchmark [7].
- Which combination of features (Euler number, IQMs, SynthSeg scores, volume-based longitudinal deltas) gives
  the best calibrated classifier for our specific cohort and contrasts? The available answers are cohort-specific
  (kappa 0.30/0.28 in the elderly clinical sample [2], AUC 0.98 in developmental data [4]); this must be fitted on
  our own ratings.
- Exact sample size needed from our rating page to bound the kappa CI for a given prevalence and number of
  categories — computable [15] but requires a prior guess of the failure prevalence, which we should take from
  the 53-session pilot.
- Relative cost/benefit of editing versus re-running versus excluding, in terms of unexplained variance per
  working hour; the literature quantifies the effects on measurements [1][10][13][17][20] but not the effort
  balance at ~1500 sessions.
- Whether segmentations produced on different contrasts (or on multi-contrast input) can be mixed in one cohort
  analysis: input contrast systematically shifts cortical thickness and surface area and can change which
  associations are detected [20], which is relevant if not all sessions have the same T1 protocol.
- Uncertainty-based segmentation QC (deep ensembles, test-time augmentation) is promoted in the methodology
  literature but was not validated against visual ratings in the works retrieved here — treat as open, not as a
  recommendation.

## Bruchindikator
A cited abstract that does not contain the claim, or a newer study contradicting the recommendation.

## Ablesung
[1] Monereo-Sánchez J, de Jong JJA, Drenthen GS, et al. (2021) Quality control strategies for brain MRI
segmentation and parcellation: Practical approaches and recommendations - insights from the Maastricht study.
Neuroimage 237:118174. DOI 10.1016/j.neuroimage.2021.118174. PMID 34000406.
Shows: comparing 12 QC strategies (manual, automated MRIQC/Qoala-T/Euler/global morphometry/CNR, semi-automated)
on 259 FreeSurfer scans, manual QC reduced unexplained variance most, Euler numbers and MRIQC were the best
automated options, and exclusion based on global morphological measures increased unexplained variance. Cited as
the core head-to-head evidence for choosing Euler/MRIQC over volume outliers.

[2] Bhalerao G, Gillis G, Dembele M, et al. (2025) Automated quality control of T1-weighted brain MRI scans for
clinical research datasets: methods comparison and design of a quality prediction classifier. Imaging Neurosci
(Camb) 3:IMAG.a.4. DOI 10.1162/IMAG.a.4. PMID 40800787.
Shows: in 2438 T1w scans from 11 sites and 39 scanner models (mean age 71), agreement of MRIQC and CAT12
accept-reject ratings with visual QC was only kappa 0.30 and 0.28 and varied strongly by dataset, while a
classifier trained on their QC measures reached 87.7% balanced accuracy (78.2% leave-one-site-out). Cited for
threshold transferability, calibration on rated data and the prevalence/kappa caveat.

[3] Rosen AFG, Roalf DR, Ruparel K, et al. (2018) Quantitative assessment of structural image quality. Neuroimage
169:407-418. DOI 10.1016/j.neuroimage.2017.12.059. PMID 29278774.
Shows: against manual ratings of 1840 T1w volumes by three trained raters, the FreeSurfer Euler number correlated
with ratings across samples and identified "unusable" images with AUC 0.98-0.99, and quality biases cortical
thickness and age associations. Cited as the primary validation of the Euler number as an automated QC measure.

[4] Klapwijk ET, van de Kamp F, van der Meulen M, et al. (2019) Qoala-T: A supervised-learning tool for quality
control of FreeSurfer segmented MRI data. Neuroimage 189:314-329. DOI 10.1016/j.neuroimage.2019.01.014.
PMID 30633965.
Shows: a random-forest model trained on FreeSurfer output of 784 manually rated longitudinal scans predicted scan
quality with mean AUC 0.98 and generalised to two unseen datasets (N = 872), with younger participants having
lower quality. Cited for supervised QC classifiers and for the age-quality confounding.

[5] Esteban O, Birman D, Schaer M, et al. (2017) MRIQC: Advancing the automatic prediction of image quality in
MRI from unseen sites. PLoS One 12(9):e0184661. DOI 10.1371/journal.pone.0184661. PMID 28945803.
Shows: image quality metrics computed by MRIQC allow prediction of expert quality ratings on data from sites not
seen during training. Cited as the basis of the MRIQC IQM track in our QC screen.

[6] Billot B, Greve DN, Puonti O, et al. (2023) SynthSeg: Segmentation of brain MRI scans of any contrast and
resolution without retraining. Med Image Anal 86:102789. DOI 10.1016/j.media.2023.102789. PMID 36857946.
Shows: SynthSeg segments 5000 scans across six modalities and ten resolutions without retraining or fine-tuning,
i.e. contrast/resolution robustness is a design property, not a quality guarantee. Cited as the method reference
for the segmentation we are QC-ing.

[7] Billot B, Magdamo C, Cheng Y, et al. (2023) Robust machine learning segmentation for large-scale analysis of
heterogeneous clinical brain MRI datasets. Proc Natl Acad Sci U S A 120(9):e2216399120.
DOI 10.1073/pnas.2216399120. PMID 36802420.
Shows: SynthSeg+ adds cortical parcellation, ICV and automated detection of faulty segmentations caused mainly by
very low scan quality, demonstrated on an aging study of 14,000 scans. Cited as the available SynthSeg-side
automated QC signal.

[8] Dorfschmidt L, Mak MHC, Adler S, et al. (2026) AI segmentation requires accounting for brain size to maintain
performance on developmental MRI cohorts. bioRxiv 2026.07.22.739983. DOI 10.64898/2026.07.22.739983.
PMID 42539016.
Shows: in 26k scans across development, only 36% of infant scans passed automated QC, and rescaling to adult brain
size plus cropping to the adult field of view raised the pass rate to 91% (2803/3069). Cited for the systematic,
fixable failure mode and for per-stratum pass-rate reporting.

[9] Bedford SA, Ortiz-Rosa A, Schabdach JM, et al. (2023) The impact of quality control on cortical morphometry
comparisons in autism. Imaging Neurosci (Camb) 1:1-19. DOI 10.1162/imag_a_00022. PMID 38495338.
Shows: the FreeSurfer output QC tool FSQC was validated against the Euler number, two manual raw-image ratings and
two automated QC methods, and all QC measures showed strikingly similar spatial patterns with cortical thickness.
Cited for cross-validation of QC metrics against visual rating and for QC-by-region effects.

[10] Elyounssi S, Kunitoki K, Clauss JA, et al. (2025) Addressing artifactual bias in large, automated MRI
analyses of brain development. Nat Neurosci 28:1746-1756. DOI 10.1038/s41593-025-01990-7. PMID 40595447.
Shows: after visual QC of 11,263 ABCD scans, 55.1% of suboptimal scans showed bias in thickness/surface area that
produced false-positive and false-negative associations; surface hole number identified low quality with good
specificity and, as a covariate, partly mitigated the bias, and manual edits reproducibly altered thickness and
strengthened age-thickness associations. Cited for automatic metrics at scale, covariate use and the effect of
edits.

[11] Deutscher E, Dennis E, Burnett J, et al. (2025) ENIGMA's advanced guide for parcellation error identification
(EAGLE-I): An implementation in the context of brain lesions. MethodsX 15:103482. DOI 10.1016/j.mex.2025.103482.
PMID 40791643.
Shows: EAGLE-I standardises region-level error identification by type, size and direction and computes an overall
brain quality rating (pass, minor error, major error, fail, discuss), motivated by ambiguous rules and
inconsistent exclusion thresholds in earlier QC methods. Cited as the concrete visual QC protocol to adopt.

[12] Canada KL, Mazloum-Farzaghi N, Rådman G, et al. (2024) A (sub)field guide to quality control in hippocampal
subfield segmentation on high-resolution T2-weighted MRI. Hum Brain Mapp 45(14):e70004. DOI 10.1002/hbm.70004.
PMID 39450914.
Shows: a survey of 37 investigators found 81% rated QC as very or fairly important but only 46% reported their QC
processes, and the paper gives recommendations for correcting errors to maximise reliability and minimise bias.
Cited for the reporting standard our methods section should follow.

[13] Canada KL, Saifullah S, Gardner JC, et al. (2023) Development and validation of a quality control procedure
for automatic segmentation of hippocampal subfields. Hippocampus 33(9):1026-1040. DOI 10.1002/hipo.23552.
PMID 37246462.
Shows: a two-step QC procedure with an error taxonomy and severity scale had high between-rater reliability for
error identification and correction (cross-validated at a second site with different imaging parameters), and
manual correction introduced at most 3% error variance in volume measurement. Cited for rating reliability and
the measured cost of editing.

[14] Kim ME, Gao C, Newlin NR, et al. (2025) Scalable quality control on processing of large diffusion-weighted
and structural magnetic resonance imaging datasets. PLoS One 20(7):e0327388. DOI 10.1371/journal.pone.0327388.
PMID 40748971.
Shows: a team-oriented visual QC pipeline built for low time cost and effort (quick visualisation, shared rating
aggregation across pipelines and datasets) achieved mostly high agreement among raters and slight differences
from an automated QC method. Cited as the model for our rating page and for rater effort at cohort scale.

[15] Rotondi MA, Donner A (2012) A confidence interval approach to sample size estimation for interobserver
agreement studies with multiple raters and outcomes. J Clin Epidemiol 65(7):778-784.
DOI 10.1016/j.jclinepi.2011.10.019. PMID 22560852.
Shows: sample size for agreement studies can be planned to reach a pre-specified lower and upper confidence limit
for kappa with any number of raters and outcome categories, implemented in the R package kappaSize. Cited for
sizing and stratifying the rated subsample.

[16] Backhausen LL, Herting MM, Buse J, et al. (2016) Quality Control of Structural MRI Images Applied Using
FreeSurfer - A Hands-On Workflow to Rate Motion Artifacts. Front Neurosci 10:558. DOI 10.3389/fnins.2016.00558.
PMID 27999528.
Shows: the paper proposes a stepwise during- and after-acquisition QC workflow with an explicit rating scale and
exclusion criteria for motion artefacts in FreeSurfer-processed data, because existing rating systems differ and
workflows are rarely reported. Cited for the raw-image rating scale and exclusion definition.

[17] Pulli EP, Silver E, Kumpulainen V, et al. (2022) Feasibility of FreeSurfer Processing for T1-Weighted Brain
Images of 5-Year-Olds: Semiautomated Protocol of FinnBrain Neuroimaging Lab. Front Neurosci 16:874062.
DOI 10.3389/fnins.2022.874062. PMID 35585923.
Shows: a FreeSurfer v6.0 plus ENIGMA-tools protocol with a dichotomous inclusion rating and ROI-level assessment
to exclude individual regions with major errors; manual edits changed cortical thickness by less than 2% in all
regions. Cited for the ROI-level (partial) exclusion option and for the size of edit effects.

[18] Sankar T, Park MTM, Jawa T, et al. (2017) Your algorithm might think the hippocampus grows in Alzheimer's
disease: Caveats of longitudinal automated hippocampal volumetry. Hum Brain Mapp 38(6):2875-2896.
DOI 10.1002/hbm.23559. PMID 28295799.
Shows: five automated/semi-automated hippocampal algorithms on ADNI 1-year data showed only 50.8% (1.5 T) and
58.1% (3 T) of subjects passing stringent segmentation QC, implausible volume growth in 2.94-48.68% of subjects,
and poor agreement on change magnitude (ICC 0.319 at 1.5 T, 0.149 at 3 T). Cited for longitudinal consistency as
a QC signal and for algorithm-dependent failure rates.

[19] Rusinek H, Bokacheva L, Chen H, et al. (2026) Test-retest reliability of FreeSurfer measures of
neurodegeneration. Neuroimage 315:121920. DOI 10.1016/j.neuroimage.2026.121920. PMID 41966233.
Shows: in 100 older adults with two scans 5.5 weeks apart, longitudinal FreeSurfer processing improved precision
by 15-50% over cross-sectional processing, larger well-defined regions were more reliable, and image quality
indexed by the Euler number was a determinant of reliability. Cited for the longitudinal processing choice and
for the Euler-number/quality link.

[20] Wiskoski HE, Mushtaq R, Smith S, et al. (2026) Contrast input and manual interventions significantly affect
FreeSurfer morphometry and clinical correlations. Neuroimage 315:121831. DOI 10.1016/j.neuroimage.2026.121831.
PMID 41759954.
Shows: in two older cohorts, input contrast (T1-MPRAGE vs T1+FLAIR vs T1+SPACE) significantly shifted cortical
thickness, surface area and volumes and altered which age- and smoking-related associations were detected, while
T1-MPRAGE gave the highest baseline quality and manual editing reliably improved quality and reduced
contrast-related bias. Cited for the effect of manual edits and for the contrast contamination risk when mixing
protocols.

[21] Sanchez T, Mihailov A, Martí-Juan G, et al. (2026) Data quality biases normative models derived from fetal
brain MRI. Imaging Neurosci (Camb) 4:IMAG.a.1337. DOI 10.1162/IMAG.a.1337. PMID 42609916.
Shows: in 635 fetal MRI scans with a standardised continuous visual QC protocol, relaxing QC stringency
systematically biased normative centiles (strongest in the outer centiles), and the bias was structure dependent
and often not visible at the segmentation level. Cited for the argument that quality must be reported as a
distribution and can bias model-based analyses invisibly.

