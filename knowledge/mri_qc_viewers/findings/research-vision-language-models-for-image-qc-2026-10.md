---
id: research-vision-language-models-for-image-qc-2026-10
typ: befund
status: vorschlag
thema: knowledge/mri_qc_viewers
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, checked by Claude Code 2026-10-18 (quellen-pruefen 0 wrong, 'Shows' spot checks against abstracts)
verweist_auf: [synthseg-cortex-qc-depends-on-site-not-protocol]
---

# Literature: can vision-language models pre-sort medical image / segmentation QC?

## Aussage
- No retrieved study shows a VLM performing *autonomous* QC triage on medical **segmentation overlays**. The closest
  published work is a benchmark of object-detection QC in which the medical domains were the hardest and where the
  authors explicitly recommend *supervised*, not autonomous, deployment [1].
- On **image-level QC tasks** (chest radiograph technical QC, CT report consistency) multimodal LLMs are feasible but
  clearly task- and modality-dependent; the authors frame their own study as a feasibility benchmark supporting
  multi-centre validation "rather than immediate clinical deployment" [2].
- On **perceptual MRI attributes** the picture is the same: a compact medical VLM (MedGemma-4B) reached 97% accuracy on
  modality and 80% on body part, but only **41% on orientation** and 32% on contrast phase [4]. Single-slice MRI
  lesion detection by eight open VLMs showed high variability plus a strong positive-response (over-calling) tendency [3].
- **Agreement with experts is moderate, not high.** ChatGPT-4o vs two radiologists on breast ultrasound BI-RADS gave
  κ = 0.59 / 0.62, while the two radiologists agreed with κ = 0.83; the model failed exactly in the intermediate
  categories and misread normal anatomy as lesions [5].
- **Image-only questions are much harder than text-only ones.** GPT-4o/GPT-4V scored 73.5%/69.3% overall but only
  55.6%/50.3% on image-based radiology exam questions, with poor self-calibration (AUC 0.64–0.66) [6].
- In some studies passing *descriptions* to the model beats giving it the **raw image**: GPT-4-based (text) 43% vs
  GPT-4V (image) 8% in musculoskeletal radiology [7]; the authors conclude that appropriate descriptions of findings
  matter more than the pixels.
- **Hallucination is the dominant failure mode** and is documented at rates of 5.4–17.4% for several medical VLMs in
  report generation, versus 0.1% for radiologists — the best model reached parity, others did not [12]. Reviews list
  hallucination as the main barrier to trust and propose multi-agent / RAG / uncertainty quantification as mitigations [13].
- **Overlays and image-displayed cues help, but they also create new error classes:** adding key images raised
  workflow-error recall (63.2%→75.4%, 72.0%→83.6%) yet produced false positives on 18/60 error-free reports, mainly
  from **body-marker misinterpretation** — directly relevant to coloured overlay interpretation [11].
- **Laterality/orientation is a documented weak spot with concrete numbers:** GPT-4V's 7/7 incorrect neuroradiology
  diagnoses were exactly the image-dominant ones, and orientation was the worst perceptual sub-task for MedGemma [4,8].
  A generative-AI tool solved *laterality* error triage with 97.4–98.3% accuracy, but on a text-and-report task, not on
  raw segmentations [10].
- **Classical, non-VLM QC is a strong baseline and should be the comparison arm:** uncertainty-based QC on 47,431
  echocardiography studies [18], automatic error-region detection on knee/calf MRI with sensitivity 0.92–0.95 [15], and
  large-cohort organ-segmentation QC reporting ~90% error-free cases [16]. Traffic-light systems explicitly built for
  human-in-the-loop exist for segmentation quality [17].
- **Validate against the intended reference standard, with the reference standard being the human verdicts**: LLM-as-a-judge
  work shows that judge reliability depends on rubric granularity and scale, and that criteria that work for human raters
  do not automatically transfer to an LLM judge [20,21]; CLAIM 2024 gives the reporting frame for such an evaluation [22].
- **A local, open-weight deployment is exactly the right choice for patient data**: locally hosted open-weight LLMs at
  7–33B parameters run on workstation-class hardware, keep images inside the institution, and are recommended together
  with vision-language / medical models such as MedGemma [23]; the same argument is made for privacy-preserving on-premises
  multimodal models [24], and MedGemma is published as an open medical VLM with a medical vision encoder [25].

**Bottom line:** a 27B local VLM is *not* yet evidence-backed as an autonomous QC gate on segmentation overlays. It is
evidence-backed as a *triage/human-in-the-loop* component — provided it is evaluated against the human verdicts, its
errors are reported per class (including laterality/orientation and hallucination), and a classical uncertainty/error-region
baseline is run alongside it.

### Practical recommendation (as written for our setup)
Local 27B VLM, montage of 9 axial slices with coloured segmentation outlines, 4-way verdict
(`pass / cortex wrong / subcortical wrong / unsure`), n = 53 cases with human verdicts.

1. **Frame the model as pre-sorter, not decider.** The evidence supports triage with human-in-the-loop only [1,19,23].
   Design the workflow so that `unsure` and every model-flagged case goes to a human; measure how much human time the
   pre-sorting actually saves (the gatekeeper study measured this: ~30% gross reduction, 15.6% false removal [19]).
2. **Report per class and per error type.** With 53 cases, a single global accuracy is uninformative. Report a 4×4
   confusion matrix, per-class sensitivity/specificity, and the pattern of `pass`↔`unsure` confusion, since borderline
   classes are where VLM agreement collapses [5].
3. **Use κ against the human verdicts, and report the human–human κ** as the reference ceiling [5]. Also report
   sensitivity for "any error" (a pre-sorter's most important number) separately from exact-class accuracy.
4. **Run a raw-vs-overlay ablation.** Because no study isolates coloured outlines, treat overlay format as an
   experimental factor: (a) montage with coloured outlines, (b) raw montage without outlines, (c) montage + a short
   structured text description. Justification: overlays/markers both helped and produced new errors [11], and text
   descriptions outperformed raw images in one head-to-head [7].
5. **Probe the known failure modes explicitly.** Include orientation/laterality checks (MedGemma: 41% [4]; laterality
   errors in GPT-4V [8]) and colour/overlay-marker probes (body-marker misinterpretation caused false positives [11]).
6. **Add the hallucination/consistency test cheaply.** Ask the same montage twice with a paraphrase and a light
   perturbation and accept only agreeing verdicts; report the acceptance rate and the accuracy among accepted cases [14].
7. **Keep a non-VLM baseline in the same experiment** — an uncertainty/error-region QC score [15,18] — so that the 27B
   model's added value is quantified rather than assumed.
8. **Report with CLAIM 2024** and pre-register the metrics, the reference standard and the exclusion rules [22].
9. **Deploy locally.** 27B at Q4/low-bit quantization is in the range that runs on workstation-class hardware; document
   the quantization, the prompt, the model hash and the date, and be aware that quantization can cost accuracy [23].
10. **Do not use a closed cloud model on patient images**, and do not let the model write anything into the clinical
    record — the retrieved evidence (hallucination rates, sycophancy, misread anatomy) is squarely against unsupervised
    clinical use [12,13,28,5].

## Trägt
Every reference retrieved in the task; quellen-pruefen: 0 wrong PMIDs/titles, DOIs registered (2026-10-18); one "Shows"
sentence per reference from its abstract; spot checks consistent.

## Trägt nicht
Abstract-level evidence, a literature map rather than a systematic review. Open questions:

- Is there *any* published evaluation of a VLM judging **segmentation masks visually as overlay images** (as opposed to
  QC of detection outputs or of image acquisition)? Not found in PubMed/Europe PMC for this report — this is the main gap.
- Does a **9-slice montage** help or hurt? Reading a single slice is documented [3]; multi-slice montage perception by
  VLMs is not.
- How much does **outline colour** change the verdict? No retrieved evidence; it must be measured here.
- What is a defensible **acceptance threshold** for a pre-sorter — sensitivity for "any error" ≥ ? at what false-removal
  cost? The gatekeeper study gives one data point (65.6% sensitivity, 15.6% false removal) but no consensus threshold [19].
- Can **quantization** of a 27B model (needed for workstation deployment) be shown not to degrade orientation/laterality
  judgement? [23] flags quantization-induced accuracy loss as a governance risk; no medical-task numbers found.
- Is a **purpose-built VLM-IQA model** (trained on quality reasoning) better than a general 27B chat VLM here? Non-medical
  evidence says yes for distortion tasks [29,30]; untested on segmentation overlays.
- How should `unsure` be handled statistically — as a third class, or as abstention with its own acceptance-rate metric [14]?

## Bruchindikator
A cited abstract that does not contain the claim, or a newer study contradicting the recommendation.

## Ablesung
[1] Abdelkader M. (2026) Vision-Language Models for automated quality control: a benchmarking framework and comprehensive study. Scientific Reports. DOI: 10.1038/s41598-026-55179-4. PMID: 42191872.
Shows: nine VLMs judging the semantic correctness of object-detection outputs across five domains reached 8.5-82.8% accuracy (mean 45.7%), with medical domains the hardest (HAM10000 mean 7.3%), leading the authors to recommend supervised rather than autonomous deployment — cited here as the closest benchmark to VLM-based QC and as the reason to treat our 27B model as a pre-sorter.

[2] Qin Z, Gui Q, Bian M, et al. (2026) Benchmarking large language models for quality control of chest radiographs and CT reports: a retrospective multimodal study. European Journal of Radiology. DOI: 10.1016/j.ejrad.2026.112840. PMID: 41932016.
Shows: on 161 radiographs with 12 radiologist-defined QC labels and 219 CT reports, Gemini 2.0 Flash was strongest for CXR technical QC while GPT-4o and Qwen2.5-VL-72B were balanced but weaker, and the authors present it as a feasibility benchmark supporting multi-centre validation rather than immediate clinical deployment — cited for the claim that image-level QC classification is feasible but task- and modality-dependent.

[3] Kim J, Kim B, Ko JS, Dong J, Youn SY, Jang J, Ahn K. (2026) Benchmarking Open-Source Vision-Language Models for Brain Metastasis Assessment on Single-Slice Contrast-Enhanced MRI. Preprint. DOI: 10.64898/2026.08.24.26361169.
Shows: eight open general and medical VLMs on 200 single axial CE-T1 slices differed widely in slice-level lesion detection, MiniCPM-V-4.5 had the best balanced accuracy (80.5%, 95% CI 75.0-85.5), and most models showed a strong positive-response tendency — cited because it is the nearest published evaluation of open VLMs on single axial MRI slices and documents the over-calling bias.

[4] Sartoretti T, Jayet A, Saliba T, Richiardi J, Pozzessere C, Rotzinger DC, et al. (2026) MedGemma Evaluation for Fundamental Radiological Imaging Classification Tasks. F1000Research (preprint). DOI: 10.12688/f1000research.187443.1.
Shows: MedGemma-4B on 600 multicentre radiological images scored 97% on modality and 80% on body part but only 41% on orientation and 32% on contrast phase — cited because orientation is exactly a perceptual sub-task our montage QC depends on, and a medical VLM is not automatically good at it.

[5] Erkoc N, Karlı EH, Tunay E, Cimilli AT. (2025) Concordance between artificial intelligence and radiologists in BIRADS classification of breast ultrasound: A study using ChatGPT-4o. Clinical Imaging. DOI: 10.1016/j.clinimag.2025.110636. PMID: 41110275.
Shows: ChatGPT-4o on 405 breast ultrasound images agreed only moderately/substantially with the two radiologists (κ = 0.593 and 0.621) while the radiologists agreed almost perfectly (κ = 0.832), with the weakest agreement in the intermediate BI-RADS 3 category (κ = 0.487) and with ribs/fibroglandular tissue misread as lesions — cited as the concrete kappa-based benchmark for VLM-human agreement and its ceiling.

[6] Martini RS, Sang A, Saunders P, Bala W, Li H, Moon JT, Balthazar P. (2026) Artificial Intelligence in Radiology: Performance of ChatGPT-4v and GPT-4o on Diagnostic Radiology in-Training (DXIT) Examination Questions. Journal of the American College of Radiology. DOI: 10.1016/j.jacr.2025.10.026. PMID: 41173086.
Shows: on 1,136 DXIT questions GPT-4o and GPT-4V scored 73.5% and 69.3% overall but only 55.6% and 50.3% on image-based questions, with weak confidence calibration (ROC-AUC 0.64/0.66) — cited for the gap between text-only and image-based performance of general-purpose multimodal models.

[7] Horiuchi D, Tatekawa H, Oura T, Shimono T, Walston SL, Takita H, Matsushita S, et al. (2025) ChatGPT's diagnostic performance based on textual vs. visual information compared to radiologists' diagnostic performance in musculoskeletal radiology. European Radiology. DOI: 10.1007/s00330-024-10902-5. PMID: 38995378.
Shows: on 106 musculoskeletal cases GPT-4-based ChatGPT given text reached 43% accuracy versus 8% for GPT-4V given the images, significantly lower than both radiologists (41% resident, 53% board-certified) — cited because it argues for testing a structured-description arm against a raw-image arm.

[8] Sussan TT, Brawley RR, Eckroth J, Mossell JE, Weitao T. (2026) Diagnostic Accuracy of GPT-4 With Vision in Neuroradiology Board-Style Exam Questions: Cross-Sectional Case-Based Study. JMIR Neurotechnologies. DOI: 10.2196/69708. PMID: 42078574.
Shows: GPT-4V diagnosed 22/29 neuroradiology cases correctly (76%), and all seven incorrect diagnoses were the image-dominant ones (self-reported image attribution >=70%), while correct diagnoses relied significantly more on text (P<.001) — cited as evidence that excessive visual reliance marks the error cases, a useful triage signal.

[9] Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, et al. (2025) Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. DOI: 10.2196/65146. PMID: 39919278.
Shows: GPT-4V answered 73.1-88.9% of image-based USMLE/DRQCE questions correctly, but among its incorrect answers 76.3% showed image misunderstandings and 45.5% inference errors, with expert hints reducing errors by ~40% — cited for the hidden-error structure behind high headline accuracy.

[10] Kathait AS, Garza-Frias E, Sikka T, et al. (2024) Assessing Laterality Errors in Radiology: Comparing Generative Artificial Intelligence and Natural Language Processing. Journal of the American College of Radiology. DOI: 10.1016/j.jacr.2024.06.014. PMID: 38960083.
Shows: of 898 NLP-flagged laterality errors only 36% were real reporting errors, and a generative-AI tool identified the absence of a mismatch with 97.4% accuracy from text and 98.3% with combined vision and text — cited as evidence that laterality triage is solvable, but on a text/report task rather than on raw images or masks.

[11] Zou M, Xiao M, Zhu Q, et al. (2026) Multimodal Large Language Models for Breast Ultrasound Report Auditing: Workflow-Error Detection, False-Positive Burden, and Limits of Key-Image Interpretation. Journal of Imaging Informatics in Medicine. DOI: 10.1007/s10278-026-02163-z. PMID: 42547701.
Shows: adding report-embedded key images raised error-level recall from 63.2% to 75.4% (GPT-5.5) and 72.0% to 83.6% (Gemini 3.1 Pro), with gains concentrated on image-displayed cues, but also produced false positives on 18/60 error-free reports mainly through body-marker misinterpretation, and key-image input underperformed physician-interpreted findings (AUC 0.879 vs 0.971) — cited for both the upside and the new error class that overlay/marker input introduces.

[12] Lim WH, Lee JY, Lee JH, et al. (2026) Comparative evaluation of generative AI models for chest radiograph report generation in the emergency department. European Radiology. DOI: 10.1007/s00330-026-12648-8. PMID: 42268300.
Shows: among five medical VLMs blind-read against radiologist reports on 478 patients, one model reached a lower RADPEER 3b rate and comparable hallucination rate to radiologists while the others had 16.8-43.0% disagreement and 5.4-17.4% hallucination rates — cited as the best quantified spread of hallucination across VLMs versus a radiologist reference.

[13] Salehi S, Singh Y, Horst KK, et al. (2025) Agentic AI and Large Language Models in Radiology: Opportunities and Hallucination Challenges. Bioengineering (Basel). DOI: 10.3390/bioengineering12121303. PMID: 41463600.
Shows: the review documents hallucination as the principal barrier to trust in radiology LLMs and evaluates multi-agent role-based systems, retrieval-augmented generation and uncertainty quantification as mitigations that remain computationally demanding and clinically unvalidated — cited for the failure-mode taxonomy and mitigation menu.

[14] Ma Y, Duan Z, Wang P, Dunn AG, Naseem U, Kim J. (2026) Ask Twice, Look Twice: Training-Free Consistency Filtering for Reliable Medical VQA. Preprint. DOI: 10.21203/rs.3.rs-7867052/v1.
Shows: medical VQA models gave inconsistent answers under semantically equivalent paraphrases and light visual perturbations, and a training-free, model-agnostic filter that accepts an answer only when outputs agree raised reliability while reporting acceptance rate — cited as the cheapest applicable robustness test for our 27B verdicts.

[15] Zaman FA, Zhang L, Zhang H, et al. (2023) Segmentation quality assessment by automated detection of erroneous surface regions in medical images. Computers in Biology and Medicine. DOI: 10.1016/j.compbiomed.2023.107324. PMID: 37591161.
Shows: a CNN trained to locate erroneous boundary-surface regions without ground truth reached average sensitivity 0.95 and 0.92 with PPV 0.78 and 0.91 on 3D knee and calf-muscle MRI — cited as the non-VLM error-region baseline that any VLM pre-sorter must be compared against.

[16] Kart T, Fischer M, Winzeck S, et al. (2022) Automated imaging-based abdominal organ segmentation and quality control in 20,000 participants of the UK Biobank and German National Cohort Studies. Scientific Reports. DOI: 10.1038/s41598-022-23632-9. PMID: 36333523.
Shows: in 20,000 participants about 90% of datasets had no relevant segmentation errors, the error rate varied strongly by organ, and image-derived features deviated relevantly when errors were present — cited to set the expected base rate: in a mostly-clean cohort an over-calling pre-sorter wastes human time.

[17] Kist AM, Razi S, Groh R, et al. (2025) Predicting semantic segmentation quality in laryngeal endoscopy images. PLoS One. DOI: 10.1371/journal.pone.0314573. PMID: 40608748.
Shows: an automatic system predicted segmentation quality (IoU) on par with human raters and used a traffic-light scheme to flag problematic frames for human-in-the-loop improvement — cited as the template for a pre-sorting QC layer with an explicit human hand-off.

[18] Zhang X, Cerna AEU, Stough JV, et al. (2022) Generalizability and quality control of deep learning-based 2D echocardiography segmentation models in a large clinical dataset. International Journal of Cardiovascular Imaging. DOI: 10.1007/s10554-022-02554-7. PMID: 35201510.
Shows: across 47,431 echocardiography studies five segmentation models showed median absolute errors comparable to inter-observer error, and a quality-control method based on segmentation uncertainty further improved the results — cited as the uncertainty-based QC baseline for segmentation.

[19] Nesturi A, Gaviria DD, Zeng J, et al. (2026) Reducing Clinician Annotation Fatigue in Open-Set Federated Learning: A Client-Adaptive Vision-Language Gatekeeper. Journal of the American College of Radiology. DOI: 10.1016/j.jacr.2026.09.023. PMID: 42822685.
Shows: a VLM gatekeeper withholding radiophague-artefact mammograms reached ROC-AUC 0.85 for artefact discrimination, withheld 101/154 artefact images at a 15.6% false-removal rate on in-distribution images, cut gross annotation time ~30% and raised queue purity to 92.5%, while the authors demand prospective multireader validation — cited as the closest working blueprint for VLM-based pre-sorting and its measured benefit and cost.

[20] Gu J, Jiang X, Shi Z, et al. (2026) A survey on LLM-as-a-judge. Innovation (Cambridge). DOI: 10.1016/j.xinn.2025.101253. PMID: 42254963.
Shows: the survey formalises LLM-as-a-judge, showing that reliability must be engineered (consistency, bias mitigation, task adaptation) and proposing a reliability-oriented benchmark — cited for treating our VLM verdict as a measurement instrument that has to be validated, not trusted.

[21] Borisov A, Burtsev T, Kosov P, et al. (2026) Key aspects of fine-tuning and applying LLM-as-a-judge for clinical data summaries in the radiological workflow. Frontiers in Artificial Intelligence. DOI: 10.3389/frai.2026.1768005. PMID: 41940108.
Shows: in fine-tuning an LLM judge for radiology summaries, rating-scale size showed no definitive association with agreement, and criteria that work for human raters were not always suitable for an LLM judge, with detailed rubric descriptions giving the highest consistency for most criteria — cited for concrete rubric-design guidance.

[22] Akinci D'Antonoli T, Adams LC, Amyar A, et al. (2026) Checklist for Artificial Intelligence in Medical Imaging (CLAIM): Explanation, Elaboration, and Examples. Radiology: Artificial Intelligence. DOI: 10.1148/ryai.260835. PMID: 42813998.
Shows: the article explains all 44 items of the CLAIM 2024 Update, a Delphi-consensus reporting framework covering data sourcing, model development, evaluation and reporting with a public online tool — cited as the reporting standard for our validation study.

[23] Nahm WJ, Yin ES, Milam EC, et al. (2026) Local Deployment of Open-Weight Language Models in Dermatology: Viewpoint on Privacy, Equity, and Practical Implementation. JMIR Dermatology. DOI: 10.2196/94764. PMID: 42627943.
Shows: model compression and MoE architectures have lowered hardware thresholds so 7-33B open-weight models run on workstation-class hardware with modest GPUs, local hosting keeps clinical images under institutional control and avoids vendor deprecation, and the authors combine local LLMs with vision-language and medical models such as MedGemma while warning about quantization-induced accuracy loss and requiring governance frameworks — cited as the direct justification and risk list for our local 27B deployment.

[24] Kwon S, Kim Y, Jhon M, et al. (2026) On-premises open-source large language models for privacy-preserving multimodal depression screening. International Journal of Medical Informatics. DOI: 10.1016/j.ijmedinf.2026.106577. PMID: 42379124.
Shows: an on-premises open-source multimodal LLM was implemented and evaluated for a privacy-sensitive clinical screening task — cited as a published precedent that on-premises multimodal inference on patient data is practical.

[25] Sellergren A, Kazemzadeh S, Mahvar F, Kiraly A, Traverse M, Kohlberger T, Gao, et al. (2026) An open vision-language model for diverse medical applications. Nature Medicine. DOI: 10.1038/s41591-026-04626-w. PMID: 42839104.
Shows: the MedGemma collection of medical vision-language foundation models together with the MedSigLIP medical vision encoder improves out-of-distribution medical image question answering by 2.6-10% and chest X-ray finding classification by 15.5-18.1% over base models, and data-efficient fine-tuning of MedGemma beats fine-tuning the base model — cited as the open medical VLM baseline to compare a local 27B general model against.

[26] Zhu Q, Hou B, Mathai TS, et al. (2025) How well do multimodal LLMs interpret CT scans? An auto-evaluation framework for analyses. Journal of Biomedical Informatics. DOI: 10.1016/j.jbi.2025.104864. PMID: 40578543.
Shows: GPTRadScore correlated well with clinician assessment (Pearson 0.75-0.91) and was superior to BLEU/METEOR/ROUGE, but GPT-4V, Gemini Pro Vision, LLaVA-Med and RadFM had low location/type accuracy that only improved markedly after fine-tuning (location 3.41% to 12.8%) — cited for both the evaluation-metric idea and the observation that medical VLMs describe images poorly without fine-tuning.

[27] Alzughaibi S. (2026) Bridging semantics and clinical fidelity: a section-based assessment of a vision-language model (RadVLM) for chest x-ray report generation. Frontiers in Digital Health. DOI: 10.3389/fdgth.2026.1882716. PMID: 42723869.
Shows: RadVLM's chest radiograph Impressions were more readable than reference reports while entity-relation fidelity was poor (RadGraph F1 0.251), and the association between semantic similarity and structural fidelity was too weak to be clinically useful — cited as the warning that fluent output is not evidence of correct visual content.

[28] Min CK. (2026) Information matters, but cues are dangerous: a comparative evaluation of three multimodal AI chatbots in oral and maxillofacial radiology. Dentomaxillofacial Radiology. DOI: 10.1093/dmfr/twag061. PMID: 42623108.
Shows: three multimodal chatbots on 90 cases reached only 0-60% accuracy from the panoramic image alone and no model was acceptable for clinical use; correct verbal cues helped but a misleading cue caused decline, and one model accepted a false benign suggestion in 96% of cases it had initially called normal — cited for sycophancy as a concrete risk when a human hint or prior verdict accompanies the image.

[29] You Z, Gu J, Cai X, et al. (2025) Enhancing Descriptive Image Quality Assessment With a Large-Scale Multi-Modal Dataset. IEEE Transactions on Image Processing. DOI: 10.1109/TIP.2025.3639998. PMID: 41364577.
Shows: a purpose-built VLM-based image-quality model trained on a 495K dataset significantly outperformed prior VLM-IQA models and proprietary GPT-4V on distortion identification, instant rating and reasoning — cited as evidence that general-purpose VLMs are not state of the art for quality assessment.

[30] Ge Q, Min X, Wu S, Li Y, Zhai G. (2026) The New Frontier of Quality Evaluation for Visual Sensors: A Survey of Large Multimodal Model-Based Methods. Sensors (Basel). DOI: 10.3390/s26082530. PMID: 42076638.
Shows: the survey reviews how vision-language and multimodal large language models move visual quality assessment from scalar prediction to language-conditioned, explainable assessment, and identifies robustness and efficiency as open challenges — cited for the state of the art and the open problems in LMM-based quality evaluation.

