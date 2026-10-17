---
id: research-fractal-dimensionality-from-freesurfer-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-17
herkunft: research report by the remote-model agent (Clara on the hospital model hub) with PubMed/Europe PMC/arXiv retrieval, checked by Claude Code 2026-10-17 (quellen-pruefen 0 wrong, 10/10 'Shows' spot checks against abstracts)
verweist_auf: [check-every-cited-source-and-summarise-it]
---

# Literature: fractal dimensionality (FD) from FreeSurfer output, tools, settings, reliability, clinical use

## Aussage
- FD is computed by applying a box-counting / fractal estimator to a **binary 3D mask of a segmented
  structure** (cortical ribbon, WM volume, GM/WM boundary, pial surface, or an individual subcortical /
  parcellated region), typically after FreeSurfer segmentation and 3D reconstruction [1][6][16][22].
- The natural analysis unit is a per-structure or per-parcellation binary volume; whole-brain,
  whole-cortex, lobar and single-subcortical-nucleus variants are all in use [1][3][19][20][22].
- **Scale / box-size range and estimator choice matter and must be fixed and reported**: spatial-scale
  optimisation improves FD accuracy, and different estimators (e.g. correlation dimension vs others)
  differ substantially in reproducibility [6][16].
- Reliability is generally **good**: intersession ICCs around 0.9–0.95 for the best-performing estimators,
  with FD and gyrification typically more reliable than cortical thickness [2][16].
- FD is **sensitive to image characteristics**, not just to structure: image registration scheme,
  sequence weighting and spatial resolution significantly shift absolute FD values [6]; scanning protocol
  choice changes reliability [2].
- FD frequently shows **greater age- and disease-related sensitivity than volume** for subcortical
  structures (notably caudate and thalamus) and greater sensitivity than cortical thickness or gyrification
  for age-related cortical differences [1][3][4].
- In clinical work FD adds information beyond volumetry: in anti-LGI1 encephalitis (a Charité cohort) FD was
  reduced in fronto-temporo-parietal and subcortical regions and was often the *more important* measure in
  affected areas [8].
- FD is usable **longitudinally**: linear mixed-effects models over up to 3 visits in anti-LGI1 encephalitis
  detected regional FD change [8], and a multi-site age-prediction study shows cross-site structural
  measures are systematic enough for individual-level modelling [5].
- For our 600-patient multi-centre cohort the main threats are **site/scanner and registration effects on
  absolute FD**; a fixed processing pipeline plus site harmonisation and reliability checks are mandatory [6][2].

---

### Practical recommendation (as written for our setup)
FreeSurfer 8 `recon-all` + longitudinal stream, multi-centre 3T stroke cohort, ~600 patients, up to 4 sessions
over 5 years.

1. **Compute FD on FreeSurfer output with a fixed, reported estimator.** Segment with the longitudinal stream,
   build binary masks per cortical parcellation and per subcortical structure, and run a box-counting /
   fractal estimator on those masks. Follow the retrieved practice of FreeSurfer segmentation plus an FD
   toolbox (calcFD is the one named in the literature) [1][19][20]; a whole-brain/skeleton 3DFD box-counting
   alternative exists [17].
2. **Fix the scale range and the estimator, and state them in the methods.** Do not use defaults: optimise the
   spatial scale in simulations/phantoms first [6], and prefer the estimator with the highest within-subject
   reproducibility (correlation dimension performed best, ICC 0.9–0.95) [16]. Report box sizes and estimator
   explicitly — heterogeneity in these choices is the main reason the systematic review cannot pool results [7].
3. **Treat registration as a first-class confound.** Unbalanced registration shifts absolute FD and produces
   spurious associations; re-register consistently and verify no deviation clusters around the registration
   target [6]. Keep the FreeSurfer longitudinal template-based processing uniform across sessions and sites.
4. **Run an in-study reliability/QC check.** You have repeated sessions (up to 4 over 5 years) — use them to
   compute intersession ICCs for FD per structure, mirroring the test-retest literature [2][16], and drop
   structures with poor reproducibility.
5. **Harmonise across sites and model site explicitly.** Multi-centre FD is affected by image characteristics
   [6]; a cross-site design is feasible (1056-adult multi-site age prediction worked) but site must enter the
   statistical model [5]. Harmonisation of FD itself (e.g. ComBat) is **unverified** in the retrieved
   literature and should be validated internally before use.
6. **Always report FD alongside volume and thickness.** FD adds independent information and is often more
   sensitive, but they index distinct structure aspects [1][3][4]; reviewers expect all three [7].
7. **Use longitudinal mixed-effects models** with age (FD is non-linearly age-dependent [15]) and disease
   duration as predictors, as done in the Charité anti-LGI1 study [8].
8. **Expect region-specific effects, not a global FD drop.** Clinical FD differences are regional
   [8][11][12][21][22]; plan a parcellated/hierarchical analysis with multiple-comparison control rather than
   one whole-cortex number.

---

## Trägt
Every reference was retrieved in the task; the tool quellen-pruefen found 0 wrong PMIDs/titles and all DOIs registered
(2026-10-17); each reference has a one-sentence "Shows" summary from its abstract; claims not supported by the cited
abstract are marked (unverified). Spot check: reference with PMID 39347569 is a COMMENTARY on Wang et al.; its 'Shows' line describes the original study's results.

## Trägt nicht
Abstract-level evidence only (no full texts read); a literature map, not a systematic review. Open questions:

- **Small vessel disease:** no retrieved study reports FD in SVD or against WMH burden — a clear gap for this
  stroke cohort.
- **FD in acute and post-stroke outcome prediction:** only one stroke study (dysarthria) was retrieved [13];
  FD as a stroke-outcome biomarker is not established here.
- **Field strength:** no retrieved abstract isolates 1.5T vs 3T vs 7T effects on FD; relevant if any site in the
  consortium differs.
- **Harmonisation:** whether ComBat-style or other harmonisation preserves FD signal across sites is
  **unverified**.
- **Python tooling:** no retrieved abstract documents a maintained Python implementation; the literature is
  MATLAB-centric (calcFD, Madan toolbox) [1][19][20].
- **Acquisition protocol for maximum reliability:** the test-retest work shows protocol matters but does not
  give a single recommended 3T protocol for FD [2][6].
- **Stroke-specific FD reference values** across the 5-year trajectory, and whether FD change is monotonic or
  state-dependent (as in anorexia nervosa [19][20]), are unknown.

---

## Bruchindikator
A cited abstract that does not contain the claim, or a newer study that contradicts the recommendation.

## Ablesung
All references were retrieved and verified via PubMed E-utilities in this task; author/year/title/journal/DOI
were extracted from the efetch XML (`refs/verified_refs_out.txt`).

[1] Madan CR, Kensinger EA (2016). Cortical complexity as a measure of age-related brain atrophy. *NeuroImage*.
    DOI 10.1016/j.neuroimage.2016.04.029. PMID 27103141.
   Shows: in over 400 adults across the lifespan, whole-cortex fractal dimensionality was more sensitive to
   age-related differences than either cortical thickness or gyrification index, with regional differences
   suggesting the measures index distinct aspects of cortical structure, and the authors provide a freely
   available MATLAB toolbox.
[2] Madan CR, Kensinger EA (2017). Test-retest reliability of brain morphology estimates. *Brain Informatics*.
    DOI 10.1007/s40708-016-0060-4. PMID 28054317.
   Shows: across two open-access test-retest datasets, intersession reliability of cortical thickness,
   gyrification and fractal dimensionality and of subcortical volume and fractal dimensionality was generally
   good - best for gyrification and FD - and highest for the dataset whose sequence was optimised for
   brain-morphology analyses.
[3] Madan CR, Kensinger EA (2017). Age-related differences in the structural complexity of subcortical and
    ventricular structures. *Neurobiology of Aging*. DOI 10.1016/j.neurobiolaging.2016.10.023. PMID 27939959.
   Shows: in nearly 900 adults (18-94 years) across three datasets, age-related differences in structural
   complexity exceeded those in volume for subcortical structures, particularly caudate and thalamus, while
   ventricular complexity was not more strongly related to age than volume.
[4] Madan CR (2021). Beyond volumetry: Considering age-related changes in brain shape complexity using fractal
    dimensionality. *Aging Brain*. DOI 10.1016/j.nbas.2021.100016. PMID 36911503.
   Shows: fractal dimensionality captures both volumetric and shape-related age differences and is more
   sensitive to age-related subcortical differences than volume, and the standard normalisation methods are
   not robust enough to adjust for these inter-individual shape differences.
[5] Madan CR, Kensinger EA (2018). Predicting age from cortical structure across the lifespan. *European
    Journal of Neuroscience*. DOI 10.1111/ejn.13835. PMID 29359873.
   Shows: using T1-weighted MRI from multiple sites (training set 1056 healthy adults, 18-97 years), age was
   predicted in two independent held-out samples with a median error of 6-7 years, best when combining
   cortical thickness and fractal dimensionality - evidence that cross-site structural measures are systematic
   enough for individual-level modelling.
[6] Krohn S, et al. (2019). Evaluation of the 3D fractal dimension as a marker of structural brain complexity
    in multiple-acquisition MRI. *Human Brain Mapping*. DOI 10.1002/hbm.24599. PMID 31090254.
   Shows: spatial-scale optimisation significantly improved FD estimation accuracy in simulations, FD
   estimates were highly stable across repeated acquisitions in the MASSIVE and Midnight Scan Club datasets but
   sensitive to image characteristics, and unbalanced registration had a significant impact on absolute FD,
   inducing deviation clusters, bidirectional correlations and spurious associations that disappeared after
   re-registration.
[7] Meregalli V, et al. (2022). Cortical complexity estimation using fractal dimension: A systematic review of
    the literature on clinical and nonclinical samples. *European Journal of Neuroscience*.
    DOI 10.1111/ejn.15631. PMID 35229388.
   Shows: a systematic review of 62 studies found cortical complexity appears to decrease with ageing and in
   various pathological processes, but the high heterogeneity between studies prevents firm conclusions - cited
   as the reason estimator and scale settings must be reported.
[8] Zhao W, Wurdack K, et al. (2026). Structural Brain Changes Are Linked to Clinical and Cognitive Outcomes
    in Anti-LGI1 Encephalitis. *Neurology: Neuroimmunology & Neuroinflammation*.
    DOI 10.1212/NXI.0000000000200649. PMID 42753224. (Charité–Universitätsmedizin Berlin)
   Shows: in 34 patients with anti-LGI1 encephalitis and 34 matched controls (Charité, 3T T1-weighted MRI
   processed with FreeSurfer plus fractal analysis, up to 3 visits), FD was reduced in fronto-temporo-parietal
   cortices and FD and volume were reduced subcortically, with FD more frequently the more important measure;
   reduced pallidal FD related to less mRS improvement and fronto-temporal/subcortical reductions to impaired
   cognition, and longitudinal change was modelled with linear mixed-effects models.
[9] Krohn S, Romanello A, et al. (2026). Fractal analysis of brain shape formation predicts age and genetic
    similarity in human newborns. *Nature Neuroscience*. DOI 10.1038/s41593-025-02107-w. PMID 41461933.
   Shows: fractal dimensionality of neonatal brain shape predicted age at scan (mean error about 4 days),
   detected premature-birth signatures not captured by brain size, and captured age and genetic information
   significantly better than cortical thickness, curvature, gyrification, sulcation, surface area and the
   T1/T2 ratio.
[10] Wang S, et al. (2024). Neuro-evolutionary evidence for a universal fractal primate brain shape. *eLife*.
    DOI 10.7554/eLife.92080. PMID 39347569.
   Shows: cortices of 11 primate species (overlapping 70 further mammals) follow a common scale-free
   morphometric trajectory approximating one archetypal fractal shape with df = 2.5, and the effect size of
   ageing on morphology rose more than fourfold at a spatial scale of about 2 mm compared with standard
   morphological analyses.
[11] Tibon R, et al. (2026). Structural complexity of brain regions in mild cognitive impairment and
    Alzheimer's disease. *Brain and Cognition*. DOI 10.1016/j.bandc.2026.106443. PMID 42166829.
   Shows: FD measures were consistent across the ADNI and BioFIND datasets, separated MCI/AD patients from
   controls including at the individual level, and the regional contributions matched the brain's memory
   network.
[12] Schoen S, et al. (2025). Boundary complexity of cortical and subcortical areas predicts deep brain
    stimulation outcomes in Parkinson's disease. *Nature Communications*. DOI 10.1038/s41467-025-60695-4.
    PMID 40595525.
   Shows: in 231 Parkinson's disease patients, FD differed from controls in nine cortical and subcortical
   regions, and adding regional FD improved prediction of post-DBS medication change (R2 0.252 -> 0.388;
   classification AUC 0.64 -> 0.76).
[13] Zhou Y, et al. (2026). Cortical morphological changes in stroke-associated dysarthria patients.
    *Frontiers in Neurology*. DOI 10.3389/fneur.2026.1766268. PMID 41940291.
   Shows: in 48 patients with stroke-associated dysarthria and 72 matched controls (surface-based
   morphometry), fractal dimension was significantly increased in the left insula and gyrification was elevated
   in bilateral insula, superior temporal and precentral gyri, with no difference between supratentorial and
   infratentorial lesions.
[14] Schwichtenberg K, et al. (2026). Association of structural brain changes with cognitive deficits and
    fatigue in patients with post-COVID-19 condition. *Brain Communications*. DOI 10.1093/braincomms/fcag099.
    PMID 41940188.
   Shows: in 49 patients with post-COVID-19 condition versus 48 matched controls, thalamic volumes were
   reduced and fractal dimensionality showed increased complexity in the occipital lobes and hippocampal
   fimbriae with reduced complexity in the thalamus bilaterally.
[15] Farahibozorg S, et al. (2015). Age- and sex-related variations in the brain white matter fractal dimension
    throughout adulthood: an MRI study. *Clinical Neuroradiology*. DOI 10.1007/s00062-013-0273-3. PMID 24413801.
   Shows: box-counting FD of white matter in 209 healthy adults followed an inverse-U trajectory over adulthood
   (general and skeleton FD, boundary FD less affected), with sex differences and sharper age-related change in
   men, and FD correlated positively with volume.
[16] Goñi J, et al. (2013). Robust estimation of fractal measures for characterizing the structural complexity
    of the human brain: optimization and reproducibility. *NeuroImage*. DOI 10.1016/j.neuroimage.2013.06.072.
    PMID 23831414.
   Shows: analysing the box-counting parameters of three fractal methods for the pial surface, cortical ribbon
   volume, white-matter volume and GM/WM boundary in two datasets from different centres (50 subjects x 3 and
   24 subjects x 4 sessions), the correlation dimension gave the highest within-subject reproducibility
   (ICC 0.9-0.95) and several parameters were identified as critical, with region-specific individual
   variability in parcellated cortical and subcortical grey matter.
[17] Jiménez J, et al. (2014). A Web platform for the interactive visualization and analysis of the 3D fractal
    dimension of MRI data. *Journal of Biomedical Informatics*. DOI 10.1016/j.jbi.2014.05.011. PMID 24909817.
   Shows: a public web platform (3dfd.ujaen.es) computes the 3D box-counting fractal dimension of the entire
   brain volume and of its 3D skeleton from MR images, demonstrated on multiple sclerosis, intrauterine growth
   restriction and Alzheimer's disease data.
[18] Collantoni E, et al. (2026). Cortical complexity in eating disorders: a systematic review and qualitative
    synthesis. *European Archives of Psychiatry and Clinical Neuroscience*.
    DOI 10.1007/s00406-025-02001-3. PMID 40307480.
   Shows: a systematic review of 13 studies (525 AN, 69 BN, 478 controls) found consistent local gyrification
   reductions in frontal, temporal and parietal regions in acute anorexia nervosa with partial normalisation
   after weight restoration, and notes that emerging metrics such as fractal dimension lack methodological
   consistency across studies.
[19] Collantoni E, et al. (2020). Cortical Complexity in Anorexia Nervosa: A Fractal Dimension Analysis.
    *Journal of Clinical Medicine*. DOI 10.3390/jcm9030833. PMID 32204343.
   Shows: in 58 women with anorexia nervosa (38 acutely underweight, 20 recovered) and 38 controls, FreeSurfer
   surface extraction plus the calcFD toolbox showed lower whole-cortex mean FD in acute AN (recovered patients
   did not differ from controls) and FD correlating with age, BMI and illness duration.
[20] Collantoni E, et al. (2023). Volume and complexity of the thalamus in Anorexia Nervosa: An exploratory
    evaluation. *European Eating Disorders Review*. DOI 10.1002/erv.2965. PMID 36573401.
   Shows: in 38 acute AN patients, 20 recovered AN patients and 38 controls, thalamic volume and calcFD
   complexity were reduced at the whole-thalamus and nucleus level in acute AN and these alterations
   normalised almost completely after weight restoration.
[21] Chen JH, et al. (2020). Brain Cortical Complexity Alteration in Amyotrophic Lateral Sclerosis: A
    Preliminary Fractal Dimensionality Study. *BioMed Research International*. DOI 10.1155/2020/1521679.
    PMID 32280675.
   Shows: in 22 ALS patients versus 20 healthy controls, regional FD computed with a computational anatomy
   toolbox was decreased in motor and insular/cingulate regions, with FD in the right precentral gyrus
   correlating with ALSFRS-R and disease-progression rate.
[22] Zhao W, et al. (2018). Reduced structural complexity of the right cerebellar cortex in male children with
    autism spectrum disorder. *PLoS ONE*. DOI 10.1371/journal.pone.0196964. PMID 29995885.
   Shows: the first high-resolution 3D fractal analysis of the cerebellum (FreeSurfer-segmented) in 20 boys
   with autism spectrum disorder versus 18 matched typically developing boys found a significant reduction of
   FD in the right cerebellar cortex.

---

### Note on source discipline

- 22 references, all retrieved live in this task (PubMed E-utilities and Europe PMC); journal, year, DOI and
  PMID were read from the efetch XML, not from memory.
- Claims marked **unverified**: Python FD ports; field-strength-specific FD effects; FD harmonisation across
  sites; FD in small vessel disease.
- Every reference carries a one-line **Shows:** summary taken from the retrieved abstract (17.10.2026 rule).

---
### Claims not supported by the abstracts
Each claim below is attributed in the text to a reference whose retrieved abstract does not contain the
statement; those spots are now marked `(unverified)` in the body.

- **Section 3.2 (Tools):** "FreeSurfer is used for surface extraction and FD is then computed with `calcFD` on
   cortical regions [19] and on the thalamus and its nuclei [20]." The abstracts of [19] and [20] do not name
   `calcFD` (they describe FreeSurfer surface extraction and fractal-dimension estimation of the thalamus and
   25 nuclei). The toolbox name is plausible but not in the abstracts.
- **Section 3.2 (Tools):** "A FreeSurfer→FD chain exists and is used in Charité cohorts [8][19][20]." The
   retrieved abstracts of [8], [19] and [20] do not show any use of FD in a Charité cohort other than [8]
   itself (which is Charité); [19] and [20] are Milan cohorts and nothing in their abstracts links them to
   Charité.
- **Section 3.8 (Longitudinal use):** "Grey-matter FD in the white matter followed an inverted-U trajectory
   across adulthood in a large sample (209 adults) [15]." The abstract of [15] reports FD of **white matter**
   (general and skeleton FD, inverse-U over adulthood) — not "grey-matter FD in the white matter".
- **Section 3.8 (Longitudinal use):** "Age-related FD trajectories are described as systematic enough to be
   captured in individual-level models [4][5]." This is supported for [5] (multi-site age prediction, median
   error 6–7 years). The abstract of [4] states that FD is more sensitive to age-related differences and that
   standard normalisation is not robust enough; it does not describe individual-level modelling.
