---
id: demdas-meeting-primer-finke-2026-10-16
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-16
herkunft: study guide written for Mendel before the meeting with Carsten Finke (Charité neurology) on 28.10.2026 or later; Alita session 16.10.2026; PDF next to this file; all references checked in PubMed on 16.10.2026
verweist_auf: [demdas-volumetry-primer-2026-10-13, freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort, longitudinal-volumetry-needs-error-statistics]
---

# Study guide: DEMDAS, brain MRI and autoimmune encephalitis imaging, for a data scientist

Version 1, 16 October 2026. Written for Mendel Temuulen (data scientist) to prepare a meeting with Carsten Finke (Department of Neurology and Experimental Neurology, Charité). It is meant to be read, and also to be loaded into a notebook tool and turned into an audio overview, so it is written in full sentences and spells out every abbreviation the first time it appears. No patient data, no identifiers. Numbers from the literature carry a reference number in square brackets; the list is at the end.

**How to use it.** Part A explains the study and our processing pipeline, so that you can describe your own work in clinical words. Part B explains the imaging methods Carsten Finke uses. Part C connects the two and lists questions for the meeting. Part D is a glossary of all technical terms, and Part E explains the statistics that appear in his papers.

---

# Part A: the study and our pipeline

## 1. What DEMDAS is

The cohort we call DEMDAS is the German multicentre stroke cohort published as **DEDEMAS**, the **Determinants of Dementia After Stroke** study. The protocol paper by Wollenweber and colleagues describes a prospective observational study of 600 patients with an acute stroke and no dementia before the stroke [1]. The patients receive multimodal imaging (magnetic resonance imaging, and in part positron emission tomography of glucose metabolism and of amyloid, plus imaging of the retina), blood and cerebrospinal fluid biomarkers, and detailed cognitive testing. Follow-up lasts five years, and the main outcome is dementia after stroke. The study is registered as NCT01334749 [1].

Note on the name: in our folders and in earlier documents the study is written DEMDAS, and one earlier primer expanded it as "DZNE Mechanisms of Dementia After Stroke". The published name is DEDEMAS, Determinants of Dementia After Stroke [1]. In the meeting, say "the DEDEMAS stroke cohort".

Two later papers from the same cohort help you explain the clinical side. Among stroke survivors with mild cognitive impairment after stroke, positivity on amyloid positron emission tomography was rare (about 5 percent), which suggests that the cognitive problems after stroke are mostly not caused by Alzheimer pathology [2]. Telephone versions of cognitive screening tests were validated against detailed testing in the same cohort [3].

**Why the study matters.** About one in ten patients already has dementia before a first stroke, about one in ten develops new dementia soon after a first stroke, and more than one in three after a recurrent stroke [4]. Imaging is used to find out which brain changes predict this decline.

## 2. The imaging data we hold

The imaging set is organised in BIDS (Brain Imaging Data Structure), a standard folder and file naming scheme. Each participant has up to four sessions, named by months after the stroke: M0 (baseline, the acute phase), M6, M36 and M60. The scans are three tesla Siemens examinations from several sites. The series that matter:

- **T1-weighted MPRAGE** (magnetisation prepared rapid gradient echo), 1 millimetre isotropic. This is the anatomical image: grey matter is darker than white matter, cerebrospinal fluid is black. All volumetry and cortical thickness come from it.
- **FLAIR** (fluid attenuated inversion recovery). A T2-weighted image in which the water signal of the cerebrospinal fluid is suppressed, so lesions in the white matter appear bright. Used for white matter hyperintensities and old infarcts.
- **DWI** (diffusion weighted imaging) with the trace image and the **ADC** (apparent diffusion coefficient) map. Acute infarcts are bright on DWI and dark on ADC, because water movement is restricted in dying cells. In this cohort the diffusion sequence was acquired with several gradient directions (about 30 directions at one b-value in the series we checked), so in principle a diffusion tensor could be fitted, if the raw diffusion data are available and not only the scanner-derived maps. This needs checking.
- **T2* or SWI-like** gradient echo images at some sites, which show microbleeds and iron.

The earlier primer lists the counts of participants and sessions in our copy [see demdas-volumetry-primer-2026-10-13].

## 3. Our processing pipeline, step by step

Think of the pipeline as turning each T1 image into numbers per brain structure, while making sure that stroke lesions do not distort those numbers.

**Step 1: lesion masks.** Acute infarcts at baseline are segmented automatically from DWI, ADC and FLAIR with DeepISLES, an ensemble of the best methods of the ISLES 2022 challenge (Ischemic Stroke Lesion Segmentation; reference not yet checked, marked unverified). White matter hyperintensities get their own masks. Infarct masks are carried over to later sessions.

**Step 2: lesion filling.** A lesion inside the white matter has a grey-matter-like intensity on T1. Segmentation software then mistakes it for grey matter or cerebrospinal fluid, and volumes become wrong. Simply masking the lesion out does not fix this; replacing the lesion voxels with intensities of the surrounding normal-appearing white matter does [5]. We fill white matter hyperintensities this way (FSL lesion_filling). For infarcts we use a mirror fill: the lesion is replaced by the mirrored tissue of the healthy hemisphere. Filling is applied only where the lesion load is high enough to matter (infarct at least 1 millilitre, white matter hyperintensities outside the infarct at least 10 millilitres), because small loads had no measurable effect in our tests.

**Step 3: SynthSeg.** SynthSeg is a deep learning segmentation tool from the FreeSurfer team that was trained only on synthetic images with randomised contrast and resolution. It therefore works on scans of any contrast and resolution without retraining [6]. The robust version adds cortical parcellation, intracranial volume and automatic quality control, and reproduced known ageing atrophy patterns in 14,000 clinical scans [7]. It gives volumes of about 30 structures per session in minutes.

**Step 4: FreeSurfer recon-all.** FreeSurfer reconstructs the cortical surface from the T1 image and models most brain structures [8]. From the surfaces it computes cortical thickness, surface area and folding per region. One session takes about an hour. We run it on the Charité high performance computing cluster as a job array.

**Step 5: the longitudinal stream.** Instead of analysing each session on its own, FreeSurfer builds an unbiased within-subject template from all sessions of a person and initialises every session from it. This treats all time points identically and makes changes over time more precise [9]. This is what you want for atrophy rates after stroke.

**Step 6: quality control and statistics.** Every session is checked visually in our viewers (overlay switch, lesion panel), and the Euler number of the surfaces is used as an automatic quality measure. For every trend we also report measurement error: test-retest agreement, intraclass correlation coefficient and the smallest detectable change (see Part E).

**One sentence to say in the meeting:** "We take the T1 images of the DEDEMAS stroke cohort, segment and fill the stroke lesions, and then run SynthSeg and the FreeSurfer longitudinal stream on the cluster, with quality control and measurement error for every structure."

## 4. Small vessel disease: the vocabulary of the stroke side

Small vessel disease means damage to the small arteries, arterioles, capillaries and venules of the brain. Its imaging markers were standardised in the STRIVE recommendations (Standards for Reporting Vascular changes on nEuroimaging) [10] and updated in STRIVE-2 [11]:

- **Recent small subcortical infarct**: a small fresh infarct in the territory of one perforating artery.
- **Lacune**: a small fluid-filled cavity, the late stage of a small infarct or bleed.
- **White matter hyperintensities**: bright areas on FLAIR and T2 in the white matter, of presumed vascular origin. Their severity is often graded with the Fazekas scale, which goes back to Fazekas and colleagues in 1987 [12].
- **Cerebral microbleeds**: small round dark dots on T2* or SWI (susceptibility weighted imaging), caused by old blood (haemosiderin) [13, 14]. They can be rated with the Microbleed Anatomical Rating Scale [13].
- **Perivascular spaces**: fluid-filled spaces around vessels, bright on T2 like cerebrospinal fluid.
- **Brain atrophy**: loss of brain tissue, visible as larger ventricles and sulci, measured as volumes.

---

# Part B: what Carsten Finke works on

## 5. Autoimmune encephalitis in plain words

Autoimmune encephalitis is an inflammation of the brain in which the immune system makes antibodies against proteins of the nerve cells, often against receptors or channels at the synapse. The patients develop memory problems, psychiatric symptoms, seizures, movement disorders or sleep disorders. A clinical approach to diagnosis defines possible, probable and definite autoimmune encephalitis, so that treatment can start before the antibody result is known [15]. The most important antibody types in his papers:

- **NMDA receptor encephalitis** (N-methyl-D-aspartate receptor). Mostly young women; psychiatric symptoms, memory loss, seizures. Routine MRI is often normal.
- **LGI1 encephalitis** (leucine-rich glioma-inactivated 1). Mostly older men; limbic encephalitis with memory loss and characteristic brief seizures; the hippocampus is affected.
- **CASPR2 encephalitis** (contactin-associated protein-like 2). Variable: cognitive decline, seizures, nerve hyperexcitability, pain.
- **IgLON5 disease**. Sleep disorder, movement problems and swallowing problems, with a tau pathology in the brainstem.
- **GABA-A and GABA-B receptor encephalitis**, **MOG antibody disease** (myelin oligodendrocyte glycoprotein) and **NMOSD** (neuromyelitis optica spectrum disorder with aquaporin-4 antibodies) appear as related neuroimmunological diseases.

Treatment is immunotherapy (steroids, plasma exchange, immunoglobulins, rituximab). Many patients recover in their daily function, but memory and psychiatric problems often remain. Finding the brain changes behind these remaining symptoms is the main theme of his imaging work.

## 6. His imaging methods

**a) Volumetry and fractal dimensionality from T1.** Volumes come from FreeSurfer, as in our pipeline. **Fractal dimensionality** (abbreviated FD) is a single number that describes how complex the folded cortical surface is. A smooth surface has a fractal dimension close to 2, a strongly folded one is higher. It was shown to be more sensitive to ageing than cortical thickness or gyrification [16], and the choice of the spatial scale range matters for reliable values [17]. In LGI1 encephalitis (34 patients, up to three visits), fractal dimensionality was reduced in fronto-temporo-parietal cortex and subcortical regions, was more often the more important measure than volume, and was related to clinical and cognitive outcome [18]. In NMDA receptor encephalitis (70 patients and 70 matched controls), fractal dimensionality from T1 was combined with normative modelling and with outcomes; two thirds of the patients still had symptoms, mostly memory and psychiatric [19]. **Important for you: when Matthias wrote "FD", this most likely means fractal dimensionality, not a diffusion measure.**

**b) Diffusion tensor imaging.** Diffusion tensor imaging fits a small 3 by 3 matrix (the tensor) to the diffusion signal in every voxel. Its main directions give the direction of nerve fibres, and its values give how freely water moves [20]. From it come **fractional anisotropy** (FA, how strongly diffusion prefers one direction, high in intact fibre bundles) and **mean diffusivity** (MD, overall water mobility, rises when tissue is damaged). **NODDI** (neurite orientation dispersion and density imaging) uses two diffusion shells to separate neurite density from fibre dispersion, the two things that FA mixes [21]. In NMDA receptor encephalitis, Finke found widespread white matter changes on diffusion tensor imaging, strongest in the cingulum and related to disease severity, while routine MRI and grey matter were normal [22]. In LGI1 encephalitis he found hippocampal atrophy and abnormal hippocampal microstructure (mean diffusivity and FA) with persistent memory deficits [23], and later, with probabilistic tractography and network analysis, a reduced and reorganised white matter network linked to memory, attention and executive deficits despite immunotherapy [24].

**c) Resting-state functional MRI and connectivity.** Functional connectivity is the correlation over time of the BOLD signal (blood oxygen level dependent) between brain regions while the person rests in the scanner. In NMDA receptor encephalitis, hippocampal functional connectivity was reduced and predicted memory performance [22].

**d) Animal models.** Patient-derived monoclonal antibodies are injected into mice or rats, and the animals are scanned on the experimental 7 tesla MRI of the Charité. Mice with human NMDA receptor antibodies showed reduced hippocampal functional connectivity, similar to patients [25]. Human CASPR2 antibodies caused reduced resting-state connectivity in mice without short-term structural change [26]. He is also co-author of a mouse connectome pipeline in a model with vascular dementia features, which showed lacunar infarcts, microbleeds and progressive white matter change over six months [27].

**e) His own summary of the field.** In a 2026 review he writes that conventional MRI is indispensable for diagnosis, that atrophy over time reflects cumulative damage and outcome better than acute lesions, that volumetry and simple quantitative measures are closest to clinical use, and that advanced methods such as quantitative MRI, diffusion tensor imaging and resting-state functional MRI still need standardisation and validation [28].

---

# Part C: where your work and his work meet

## 7. Concrete overlaps

1. **Fractal dimensionality on our existing FreeSurfer output.** We already run recon-all and the longitudinal stream on the stroke cohort. Fractal dimensionality is computed from the cortical surfaces or ribbon that FreeSurfer produces [16, 17]. Adding it is a small extra step on data we already process, and it would let both groups compare a stroke cohort and an encephalitis cohort with the same measure.
2. **A shared, automated pipeline on the cluster.** His studies use FreeSurfer, fractal analysis, diffusion and normative models on cohorts of 25 to 70 patients. Our strength is running such steps reproducibly on more than a thousand sessions, with quality control and measurement error. A pipeline for volume plus fractal dimensionality, on the Charité cluster, would serve both.
3. **Longitudinal design.** His recent LGI1 work is longitudinal [18]. The FreeSurfer longitudinal stream [9] and our error statistics (smallest detectable change, intraclass correlation) are exactly the tools for that.
4. **Lesions.** Encephalitis patients can have lesions too. Our lesion filling experience [5] transfers.
5. **Diffusion.** Our pipeline has no diffusion tensor analysis yet. Whether DEDEMAS has usable raw diffusion data is an open question. This is an area where he has experience and we would learn.
6. **Normative modelling.** He uses normative models to compare each patient with a healthy reference [19]; the idea goes back to Marquand and colleagues [29]. For a stroke cohort the same idea could show which patients deviate most.

## 8. Questions to ask him

- Which software and settings do you use for fractal dimensionality (for example calcFD in MATLAB or a Python port, on the FreeSurfer surfaces or the ribbon)?
- Which sequences do your cohorts have: T1 only, or also multi-direction diffusion, FLAIR, SWI, resting-state functional MRI? Which field strength?
- How many patients and sessions, and are the data in BIDS?
- Where do you need help most: running FreeSurfer at scale, quality control, longitudinal processing, statistics, or something else?
- Is the goal a joint paper, a shared pipeline, or applying your measures to the stroke cohort?
- Who in your group does the image processing, so that we can talk technical details?
- Data protection: can the data be processed on the Charité cluster, and who must approve it?

## 9. Things to be careful about

- Do not promise that fractal dimensionality or diffusion "fit into the pipeline" before you have seen his data and methods.
- DEDEMAS is a stroke cohort, not an encephalitis cohort. The overlap is in methods, not in patients.
- Say clearly what you are: a data scientist who builds and runs the processing, not a neurologist. Ask him to explain clinical points; that is normal and welcome.

---

# Part D: glossary

- **ADC (apparent diffusion coefficient)**: map of water mobility from DWI; dark in acute infarcts.
- **Amyloid PET**: positron emission tomography that shows amyloid plaques, a sign of Alzheimer pathology.
- **Atrophy**: loss of brain tissue over time.
- **b-value**: strength of the diffusion weighting in a diffusion scan.
- **BIDS (Brain Imaging Data Structure)**: standard for naming and organising imaging files.
- **BOLD (blood oxygen level dependent) signal**: the signal measured in functional MRI.
- **CASE (Clinical Assessment Scale in Autoimmune Encephalitis)**: severity score for encephalitis patients.
- **Cerebrospinal fluid (CSF)**: the clear fluid around and inside the brain.
- **Cingulum**: a white matter bundle along the medial surface of the brain, part of the memory network.
- **Cortex, cortical ribbon**: the outer layer of grey matter; the ribbon is its 3D band between white matter and the pial surface.
- **Cortical thickness**: distance between the white matter surface and the pial surface, in millimetres.
- **DeepISLES**: ensemble of deep learning models from the ISLES 2022 challenge for acute infarct segmentation (reference unverified here).
- **DEDEMAS**: Determinants of Dementia After Stroke study; our "DEMDAS" cohort [1].
- **Dice coefficient**: overlap between two segmentations, from 0 (none) to 1 (identical).
- **DTI (diffusion tensor imaging)**: model of water diffusion per voxel; gives FA and MD [20].
- **DWI (diffusion weighted imaging)**: MRI sensitive to water movement; bright in acute infarcts.
- **Euler number**: topological measure of a reconstructed surface; many defects mean poor quality.
- **FA (fractional anisotropy)**: 0 to 1, how directional water diffusion is; lower when fibres are damaged.
- **Fazekas scale**: grading of white matter hyperintensity severity [12].
- **FD (fractal dimensionality)**: complexity of the cortical folding; in Finke's recent papers this is what FD means [18, 19].
- **FLAIR**: T2-weighted MRI with suppressed fluid signal; lesions appear bright.
- **FreeSurfer**: software suite for cortical surface reconstruction, thickness and volumes [8].
- **Functional connectivity**: correlation of BOLD signals between regions over time.
- **Grey matter, white matter**: grey matter holds the nerve cell bodies (cortex and deep nuclei); white matter holds the connecting fibres.
- **Haemosiderin**: iron-containing breakdown product of blood; makes microbleeds dark on SWI.
- **Hippocampus**: structure in the medial temporal lobe essential for memory; often affected in LGI1 encephalitis.
- **Immunotherapy**: treatments that suppress or modulate the immune system.
- **Infarct**: area of dead tissue after loss of blood supply (ischaemic stroke).
- **Intracranial volume (ICV)**: volume inside the skull; used to correct brain volumes for head size.
- **Lacune**: small fluid-filled cavity after a small infarct.
- **Lesion filling**: replacing lesion voxels with normal-appearing tissue intensities before segmentation [5].
- **LGI1, NMDAR, CASPR2, IgLON5, GABA-A/B, MOG, AQP4**: target proteins of the antibodies in different autoimmune diseases (see section 5).
- **Limbic encephalitis**: encephalitis focused on the limbic system (hippocampus, amygdala).
- **Longitudinal stream**: FreeSurfer processing that uses a within-subject template for several sessions [9].
- **MD (mean diffusivity)**: average water mobility; higher when tissue is damaged.
- **Microbleed**: small chronic bleed, dark dot on T2* or SWI [13].
- **MPRAGE**: the standard T1-weighted 3D sequence on Siemens scanners.
- **mRS (modified Rankin Scale)**: 0 (no symptoms) to 6 (dead), disability after stroke or encephalitis.
- **NODDI**: diffusion model for neurite density and orientation dispersion [21].
- **Normative modelling**: modelling the healthy range of a measure, then scoring each patient as a deviation from it [29].
- **Parcellation**: dividing the cortex into named regions (atlas).
- **Perivascular space**: fluid-filled space around a small vessel.
- **Probabilistic tractography**: reconstruction of likely fibre pathways from diffusion data.
- **Resting-state fMRI**: functional MRI without a task.
- **Small vessel disease**: disease of the small brain vessels; markers in STRIVE [10, 11].
- **STRIVE, STRIVE-2**: standards for imaging research in small vessel disease [10, 11].
- **SWI (susceptibility weighted imaging)**: MRI sensitive to iron, blood and veins [14].
- **SynthSeg**: contrast-agnostic deep learning segmentation [6, 7].
- **T1, T2, T2***: basic MRI contrasts; T1 for anatomy, T2 and FLAIR for lesions, T2* and SWI for blood and iron.
- **Tesla (T)**: field strength of the scanner; clinical 1.5 or 3 T, research 7 T.
- **Voxel**: the 3D pixel of an MRI image, for example 1 by 1 by 1 millimetre.
- **White matter hyperintensity (WMH)**: bright white matter area on FLAIR, mostly from small vessel disease.

---

# Part E: statistics you will meet in his papers

- **Propensity score matching**: each patient gets a healthy control with a similar probability of being a patient given age and sex; makes groups comparable [19, 24].
- **Linear mixed-effects model**: regression for repeated measures; each person gets their own intercept (and slope), so several visits per person can be analysed together [18].
- **Dominance analysis**: decides which of several correlated predictors (here volume or fractal dimensionality) explains more of an outcome [18].
- **Normative model and z-score**: a patient's value expressed as standard deviations from the healthy expectation for their age and sex [19, 29].
- **Effect size (Cohen's d)**: difference between groups in units of standard deviation; 0.2 small, 0.5 medium, 0.8 large.
- **Intraclass correlation coefficient (ICC)**: agreement of repeated measurements, 0 to 1; above 0.9 is excellent.
- **Smallest detectable change (SDC95)**: the change that exceeds measurement error with 95 percent confidence; 1.96 times the square root of 2 times the within-subject standard deviation.
- **Multiple comparison correction**: when testing many brain regions, p-values are corrected (for example false discovery rate) to avoid false positives.

---

## Quellen

All checked in PubMed on 16.10.2026.

1. Wollenweber FA et al. The Determinants of Dementia After Stroke (DEDEMAS) Study: protocol and pilot data. Int J Stroke 2014;9(3):387-92 (online 2013). DOI 10.1111/ijs.12092. PMID 23834337.
2. Wollenweber FA et al. Prevalence of amyloid positron emission tomographic positivity in poststroke mild cognitive impairment. Stroke 2016;47(10):2645-8. DOI 10.1161/STROKEAHA.116.013778. PMID 27539301.
3. Zietemann V et al. Validation of the Telephone Interview of Cognitive Status and Telephone Montreal Cognitive Assessment against detailed cognitive testing and clinical diagnosis of mild cognitive impairment after stroke. Stroke 2017;48(11):2952-7. DOI 10.1161/STROKEAHA.117.017519. PMID 29042492.
4. Pendlebury ST, Rothwell PM. Prevalence, incidence, and factors associated with pre-stroke and post-stroke dementia: a systematic review and meta-analysis. Lancet Neurol 2009;8(11):1006-18. DOI 10.1016/S1474-4422(09)70236-4. PMID 19782001.
5. Battaglini M, Jenkinson M, De Stefano N. Evaluating and reducing the impact of white matter lesions on brain volume measurements. Hum Brain Mapp 2012;33(9):2062-71. DOI 10.1002/hbm.21344. PMID 21882300.
6. Billot B et al. SynthSeg: segmentation of brain MRI scans of any contrast and resolution without retraining. Med Image Anal 2023;86:102789. DOI 10.1016/j.media.2023.102789. PMID 36857946.
7. Billot B et al. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. PNAS 2023;120(9):e2216399120. DOI 10.1073/pnas.2216399120. PMID 36802420.
8. Fischl B. FreeSurfer. NeuroImage 2012;62(2):774-81. DOI 10.1016/j.neuroimage.2012.01.021. PMID 22248573.
9. Reuter M et al. Within-subject template estimation for unbiased longitudinal image analysis. NeuroImage 2012;61(4):1402-18. DOI 10.1016/j.neuroimage.2012.02.084. PMID 22430496.
10. Wardlaw JM et al. Neuroimaging standards for research into small vessel disease and its contribution to ageing and neurodegeneration (STRIVE). Lancet Neurol 2013;12(8):822-38. DOI 10.1016/S1474-4422(13)70124-8. PMID 23867200.
11. Duering M et al. Neuroimaging standards for research into small vessel disease: advances since 2013 (STRIVE-2). Lancet Neurol 2023;22(7):602-18. DOI 10.1016/S1474-4422(23)00131-X. PMID 37236211.
12. Fazekas F et al. MR signal abnormalities at 1.5 T in Alzheimer's dementia and normal aging. AJR Am J Roentgenol 1987;149(2):351-6. DOI 10.2214/ajr.149.2.351. PMID 3496763. (Origin of the rating approach; the 0 to 3 grading is not described in the abstract.)
13. Gregoire SM et al. The Microbleed Anatomical Rating Scale (MARS): reliability of a tool to map brain microbleeds. Neurology 2009;73(21):1759-66. DOI 10.1212/WNL.0b013e3181c34a7d. PMID 19933977.
14. Haacke EM et al. Susceptibility weighted imaging (SWI). Magn Reson Med 2004;52(3):612-8. DOI 10.1002/mrm.20198. PMID 15334582.
15. Graus F et al. A clinical approach to diagnosis of autoimmune encephalitis. Lancet Neurol 2016;15(4):391-404. DOI 10.1016/S1474-4422(15)00401-9. PMID 26906964.
16. Madan CR, Kensinger EA. Cortical complexity as a measure of age-related brain atrophy. NeuroImage 2016;134:617-29. DOI 10.1016/j.neuroimage.2016.04.029. PMID 27103141.
17. Marzi C et al. Toward a more reliable characterization of fractal properties of the cerebral cortex of healthy subjects during the lifespan. Sci Rep 2020;10:16957. DOI 10.1038/s41598-020-73961-w. PMID 33046812.
18. Zhao W et al. (last author Finke C). Structural brain changes are linked to clinical and cognitive outcomes in anti-LGI1 encephalitis. Neurol Neuroimmunol Neuroinflamm 2026;13(6):e200649. DOI 10.1212/NXI.0000000000200649. PMID 42753224.
19. Krohn S et al. (last author Finke C). Structural brain changes and clinical outcomes of patients with NMDA receptor encephalitis in Germany: a cross-sectional study. Lancet Psychiatry 2026;13(9):734-46. DOI 10.1016/S2215-0366(26)00191-4. PMID 42586080.
20. Basser PJ, Mattiello J, LeBihan D. MR diffusion tensor spectroscopy and imaging. Biophys J 1994;66(1):259-67. DOI 10.1016/S0006-3495(94)80775-1. PMID 8130344.
21. Zhang H et al. NODDI: practical in vivo neurite orientation dispersion and density imaging of the human brain. NeuroImage 2012;61(4):1000-16. DOI 10.1016/j.neuroimage.2012.03.072. PMID 22484410.
22. Finke C et al. Functional and structural brain changes in anti-N-methyl-D-aspartate receptor encephalitis. Ann Neurol 2013;74(2):284-96. DOI 10.1002/ana.23932. PMID 23686722.
23. Finke C et al. Evaluation of cognitive deficits and structural hippocampal damage in encephalitis with leucine-rich, glioma-inactivated 1 antibodies. JAMA Neurol 2017;74(1):50-9. DOI 10.1001/jamaneurol.2016.4226. PMID 27893017.
24. Krohn S et al. (last author Finke C). Cognitive deficits in anti-LGI1 encephalitis are linked to immunotherapy-resistant white matter network changes. Neurol Neuroimmunol Neuroinflamm 2025;12(2):e200360. DOI 10.1212/NXI.0000000000200360. PMID 39879565.
25. Kuchling J et al. (last author Finke C). Impaired functional connectivity of the hippocampus in translational murine models of NMDA-receptor antibody associated neuropsychiatric pathology. Mol Psychiatry 2024;29(1):85-96. DOI 10.1038/s41380-023-02303-9. PMID 37875549.
26. van Hoof S et al. Human cerebrospinal fluid monoclonal CASPR2 autoantibodies induce changes in electrophysiology, functional MRI, and behavior in rodent models. Brain Behav Immun 2024;122:266-78. DOI 10.1016/j.bbi.2024.08.027. PMID 39142424.
27. Hall GR et al. Long-term connectome analysis reveals reshaping of visual, spatial networks in a model with vascular dementia features. Stroke 2022;53(5):1735-45. DOI 10.1161/STROKEAHA.121.036997. PMID 35105183.
28. Hartung TJ et al. (last author Finke C). The role of brain MRI in autoimmune encephalitis. Curr Opin Neurol 2026;39(3):332-40. DOI 10.1097/WCO.0000000000001484. PMID 41947644.
29. Marquand AF et al. Understanding heterogeneity in clinical cohorts using normative models: beyond case-control studies. Biol Psychiatry 2016;80(7):552-61. DOI 10.1016/j.biopsych.2015.12.023. PMID 26927419.

Unverified: DeepISLES reference (ISLES 2022 ensemble), named in step 1 and the glossary.

## Verknüpft
- [demdas-volumetry-primer-2026-10-13](demdas-volumetry-primer-2026-10-13.md)
- [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort](freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort.md)
- PDF: [demdas-meeting-primer-finke-2026-10-16.pdf](demdas-meeting-primer-finke-2026-10-16.pdf)
