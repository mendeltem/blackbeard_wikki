---
id: literature-segmentation-qc-at-cohort-scale-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) with PubMed/Europe PMC retrieval, /home/uchralt/cle-arbeit/recherche/g_segmentation_qc_at_scale/REPORT.md, quellen-pruefen 0 wrong (21 refs)
verweist_auf: [synthseg-cortex-qc-depends-on-site-not-protocol, euler-number-needs-the-binary-not-the-log]
---

# Literature: how to control automatic segmentation quality in a cohort of ~1500 sessions

## Aussage
- There is exactly one head-to-head comparison of QC strategies at our scale: 12 strategies
  (2 manual, 5 automated: MRIQC, Qoala-T, global morphometry, Euler number, CNR; 5
  semi-automated) applied to 259 FreeSurfer-processed scans, judged by the reduction of
  unexplained variance. Manual QC won; Euler number and MRIQC were the best automated
  substitutes; exclusion on global morphological outliers **increased** unexplained
  variance [1, Monereo-Sanchez 2021, Neuroimage, doi:10.1016/j.neuroimage.2021.118174,
  PMID 34000406]. Do not trim on volume outliers.
- The Euler number is the best-validated cheap scalar: against 1840 manually rated T1w
  volumes it correlated with ratings across samples and separated "unusable" with
  AUC 0.98-0.99, and quality biased cortical thickness and age associations
  [2, Rosen 2018, Neuroimage, doi:10.1016/j.neuroimage.2017.12.059, PMID 29278774].
- Off-the-shelf automated QC does not transfer for free: in 2438 T1w scans (11 sites,
  39 scanner models, mean age 71) MRIQC and CAT12 accept/reject agreed with visual QC only
  at kappa 0.30 / 0.28 and varied strongly by dataset, while a classifier fitted on those
  same datasets reached 87.7% balanced accuracy (78.2% leave-one-site-out)
  [3, Bhalerao 2025, Imaging Neurosci, doi:10.1162/IMAG.a.4, PMID 40800787]. Supervised QC
  beats single metrics only after training on ratings of the same kind of data; Qoala-T
  reached AUC 0.98 in developmental data (784 rated scans) and transferred to two unseen
  datasets [4, Klapwijk 2019, Neuroimage, doi:10.1016/j.neuroimage.2019.01.014,
  PMID 30633965].
- SynthSeg/SynthSeg+ do not remove the need for QC but supply segmentation-side signals:
  SynthSeg+ adds automated detection of faulty segmentations mainly caused by very low scan
  quality, shown on 14 000 clinical scans [5, Billot 2023, PNAS,
  doi:10.1073/pnas.2216399120, PMID 36802420]. The QC scores themselves can fail
  systematically: in 26k developmental scans only 36% of infant scans passed, and rescaling
  to adult brain size plus cropping to the adult field of view raised the pass rate to 91%
  (2803/3069) [6, Dorfschmidt 2026, bioRxiv, doi:10.64898/2026.07.22.739983, PMID 42539016].
  Report pass rates per stratum, and treat a low pass rate as a fixable pre-processing bug
  before excluding subjects. This matches our own site-driven cortex pass rate.
- Visual QC protocols are mature and shareable: EAGLE-I classifies region-level
  parcellation errors by type, size and direction and computes a per-brain rating
  (pass / minor / major / fail / discuss) [7, Deutscher 2025, MethodsX,
  doi:10.1016/j.mex.2025.103482, PMID 40791643]; a hands-on motion rating scale for
  FreeSurfer data with explicit exclusion rules [8, Backhausen 2016, Front Neurosci,
  doi:10.3389/fnins.2016.00558, PMID 27999528]; a paediatric protocol that drops single
  regions with major errors instead of the whole session [9, Pulli 2022, Front Neurosci,
  doi:10.3389/fnins.2022.874062, PMID 35585923].
- Rater effort can be cut without dropping the human decision: a team-oriented visual QC
  pipeline built for low time cost (quick overlays, shared rating aggregation across
  pipelines and datasets) achieved mostly high inter-rater agreement on large structural and
  diffusion datasets [10, Kim 2025, PLoS One, doi:10.1371/journal.pone.0327388,
  PMID 40748971]. A documented subfield QC procedure with an error taxonomy had high
  between-rater reliability and manual correction contributed at most 3% error variance
  [11, Canada 2023, Hippocampus, doi:10.1002/hipo.23552, PMID 37246462]. In a survey of 37
  investigators, 81% called QC very important but only 46% reported their QC procedure
  [12, Canada 2024, Hum Brain Mapp, doi:10.1002/hbm.70004, PMID 39450914] -- report it.
- Editing is not free: manual edits reliably improve segmentation quality and reduce
  contrast-related bias [13, Wiskoski 2026, Neuroimage, doi:10.1016/j.neuroimage.2026.121831,
  PMID 41759954], but in 11 263 adolescent scans they reproducibly altered cortical
  thickness and strengthened age-thickness associations [14, Elyounssi 2025, Nat Neurosci,
  doi:10.1038/s41593-025-01990-7, PMID 40595447]. Record edit status (yes/no) and run a
  sensitivity analysis.
- Longitudinal consistency is a QC measure in its own right: five hippocampal algorithms on
  ADNI 1-year data let only 50.8% (1.5 T) / 58.1% (3 T) of subjects pass stringent QC,
  produced implausible volume growth in 2.94-48.68% of subjects, and agreed on change only
  at ICC 0.319 / 0.149 [15, Sankar 2017, Hum Brain Mapp, doi:10.1002/hbm.23559,
  PMID 28295799]. FreeSurfer's longitudinal stream improved test-retest precision by 15-50%
  and the Euler number was a determinant of reliability [16, Rusinek 2026, Neuroimage,
  doi:10.1016/j.neuroimage.2026.121920, PMID 41966233].
- Sizing the rated subsample is an explicit calculation, not a rule of thumb: sample size
  for agreement studies can be planned for a pre-specified lower and upper confidence limit
  of kappa, for any number of raters and categories, via the kappaSize R package
  [17, Rotondi 2012, J Clin Epidemiol, doi:10.1016/j.jclinepi.2011.10.019, PMID 22560852].
  A 53-session rated page is a pilot: wide kappa CI, so report raw agreement and
  sensitivity/specificity per stratum, not kappa alone.
- Quality biases downstream models and can do so invisibly: relaxing QC stringency shifted
  normative centiles of fetal brain MRI systematically, strongest in the outer centiles and
  often not visible at the segmentation level [18, Sanchez 2026, Imaging Neurosci,
  doi:10.1162/IMAG.a.1337, PMID 42609916].

## Traegt
Design of a QC gate for a large segmentation run and for the reporting standard of the
methods section: which automated measures to combine, why not to trim on volume outliers,
how to size and stratify a rated subsample, and what the failure policy per failure type is.

## Traegt nicht
Absolute thresholds (Euler cut-offs, kappa values, pass rates) are cohort specific; the
kappa 0.30/0.28 and AUC 0.98 numbers come from different populations and cannot be copied to
our data. Our own thresholds must be fitted on our own ratings [3,4].

## Bruchindikator
A cohort study that shows volume-outlier trimming *reducing* measurement error, or a
published SynthSeg QC score that is validated against human ratings in adult cohorts with a
kappa clearly above the classifier values in [3].

## Ablesung
Peer-reviewed except [6] (preprint, bioRxiv). All 21 references retrieved through PubMed /
Europe PMC in this task and checked with `quellen-pruefen` (0 wrong). Report:
/home/uchralt/cle-arbeit/recherche/g_segmentation_qc_at_scale/REPORT.md

## Verknuepft
- [synthseg-cortex-qc-depends-on-site-not-protocol](synthseg-cortex-qc-depends-on-site-not-protocol.md)
- [euler-number-needs-the-binary-not-the-log](../rules/euler-number-needs-the-binary-not-the-log.md)
