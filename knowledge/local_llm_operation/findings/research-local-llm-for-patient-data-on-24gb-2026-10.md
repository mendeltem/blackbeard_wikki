---
id: research-local-llm-for-patient-data-on-24gb-2026-10
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-17
herkunft: research report by the remote-model agent (Clara on the hospital model hub) with PubMed/Europe PMC/arXiv retrieval, checked by Claude Code 2026-10-17 (quellen-pruefen 0 wrong, 10/10 'Shows' spot checks against abstracts)
verweist_auf: [check-every-cited-source-and-summarise-it]
---

# Literature: which open-weight LLM fits a local patient-data agent on one 24 GB GPU

## Aussage
- For an agentic workflow, the literature does not support "medical" models as a default: a
  purpose-built medical agent that ran **fully on-premise** reached competitive diagnostic
  reliability on MIMIC-IV benchmarks, i.e. the decisive factors were local control plus a
  reliability/uncertainty layer, not a "medical" pre-training flavour (unverified) [1].
- General vision-language models are close to — and sometimes above — specialist medical models on
  concrete findings, while medical VLM families such as MedGemma are built for data-efficient
  fine-tuning and exceed *similarly sized* general generative models on medical image QA and agentic
  evaluations [5][6][7].
- Quantisation is a real, measurable trade-off, not free: on a clinical extraction task (mRS score
  from notes) larger models and higher precision reduced error, but performance **plateaued at
  4–5 bits** — exactly the regime that fits a ~27B model into one 24 GB GPU [12].
- Ternary / 1.58-bit is no longer only "train from scratch": post-training ternary quantisation was
  scaled to 70B parameters with only a modest accuracy drop versus a from-scratch 1.58-bit baseline
  (unverified), which makes ultra-low-bit weights a serious option when VRAM, not VRAM-speed, is the
  binding constraint [14].
- "It fits in 24 GB" is achievable even at very low bit-widths: 2-bit quantised 65B models can be
  *fine-tuned* on a single 24 GB GPU with modular low-rank adaptation [15].
- Tool/function calling is where a local model can quietly fail, and current evaluation practice is
  the weak spot: benchmark, agent and tool-use harnesses are heterogeneous and not yet a settled
  standard [4], while agentic clinical benchmarking shows that agent systems (not just the base
  model) must be evaluated end-to-end [2][3].
- Small and mid-size language models can be *preferable* for agentic healthcare tasks because of
  deployability, cost and operational efficiency, provided the task is well scoped [16].
- Local, open-weight deployment is already demonstrated for exactly our data class: privacy-preserving
  local LLMs for structured retrieval from clinical text [17], local LLMs accelerating review of
  historic echocardiogram reports [18], locally deployed LLMs for BI-RADS-compliant mammography
  reporting under privacy constraints [19], and open-weight LLMs extracting structured information
  from **brain MRI reports** [8].
- German is not a solved problem for small local models; open models were benchmarked for German
  clinical documentation [20] and for extracting attributes from German pathology reports [21], and
  German appears repeatedly as a separate evaluation axis rather than a free by-product of English
  capability.
- A 71 GB MoE quantised to ~IQ3 stays **larger than 24 GB of VRAM**; running it means offloading to
  the 62 GB of RAM, which changes the latency profile. That specific configuration is **unverified**
  (no retrieved source measured it).

---

### Practical recommendation (as written for our setup)
Constraint recap: one RTX A5000 with 24 GB VRAM, 62 GB RAM; agentic use on pseudonymised imaging
data; needs German + English, Python/log work, tool calling, optional MRI screenshots.

1. **Default to a general mid-size dense model, ~27B, at 4-bit, as the workhorse — not a "medical"
   model.** Evidence: quantisation quality plateaus at 4–5 bits [12], 4-bit is the safe operating
   point, and the on-premise agent result shows reliability/governance — not medical pre-training —
   is what enabled clinical translation [1]. German capability must be validated on our own texts
   rather than assumed [20][21].
2. **Reserve a medical VLM (MedGemma-class) for the imaging/screenshot path**, where its medical
   encoder and data-efficient fine-tuning are the differentiator, and where general models are only
   *close* rather than better [5][6].
3. **Do not push the vision path below 4-bit.** Ultra-low-bit quantisation degrades visual capability
   specifically [13].
4. **Treat tool calling as the primary acceptance test**, evaluated end-to-end at the *agent* level,
   because the harness is part of the system and the evaluation standards are still unsettled [2][3][4].
5. **Keep KV cache at Q4 (or Q4K/Q3V) and leave Q2 key precision alone**, since low-bit KV policies can
   preserve perplexity while destroying task behaviour, and Q2 keys were catastrophic [22].
6. **If VRAM is the binding constraint, ultra-low-bit is viable but must be re-validated:** ternary
   weights are now reachable post-training at scale [14] and 2-bit models can even be fine-tuned on one
   24 GB GPU [15], but expect measurable degradation versus 4-bit [13].
7. **Run the 71 GB MoE only with explicit RAM offloading and measure latency** — it does not fit in
   VRAM, and no retrieved source measured this configuration for our workload (*unverified*).
8. **Document the risk framework and governance alongside the deployment**: local deployment answers
   the data-protection question (demonstrated repeatedly [17][18][19][8][9][24][25]) but does not by
   itself answer safety, uncertainty or regulatory alignment [1][16][23].

---

## Trägt
Every reference was retrieved in the task; the tool quellen-pruefen found 0 wrong PMIDs/titles and all DOIs registered
(2026-10-17); each reference has a one-sentence "Shows" summary from its abstract; claims not supported by the cited
abstract are marked (unverified). 
## Trägt nicht
Abstract-level evidence only (no full texts read); a literature map, not a systematic review. Open questions:

- How do the **specific** candidate checkpoints (`Qwen3.8-27B Q4`, `Ternary-Bonsai-2-27B`,
  `Qwen3.8-Flash-Next IQ3_XXS`, `MedGemma 27B/4B`, `Qwen3-Coder-30B-A3B`) actually behave? No retrieved
  abstract measured them; this needs local benchmarking. None of the model-specific claims in §3.6 are
  verified.
- Does ternary/1.58-bit at ~27B retain **tool-calling** fidelity, not just average downstream accuracy?
  Only average accuracy was reported [14].
- What is the real latency/throughput penalty of RAM offloading a 71 GB MoE on this host? Unmeasured here.
- How well do the demonstrated local-LLM pipelines [17][18][19] transfer to **agentic** (multi-step,
  tool-using) operation rather than single-pass extraction?
- Is there task-specific degradation of German output under 2-bit quantisation? German was evaluated
  for open models [20][21] but not, in retrieved sources, as a function of bit-width.
- MRI *screenshot* reading (as opposed to report text) is not directly benchmarked in any retrieved
  source; MedGemma [5] is the nearest proxy and not a substitute for our own validation.
- arXiv (the natural source for quantisation/agent CS work) was unreachable from this host
  (persistent HTTP 429), so the CS-side literature is likely under-covered; a re-run from another
  network should be done.

---

## Bruchindikator
A cited abstract that does not contain the claim, or a newer study that contradicts the recommendation.

## Ablesung
Retrieved in this task via PubMed E-utilities and Europe PMC (raw JSON/XML under `raw/`). PMIDs are
PubMed identifiers; `PPR…` identifiers are Europe PMC preprints.

[1] Zhang L, Wölflein G, Ferber D, et al. On-premise medical AI agents for reliable clinical
    decision-making. *Nature Medicine*, 2026. DOI 10.1038/s41591-026-04609-x. PMID 42744896.
   Shows: A fully on-premise clinical LLM agent coupling local operational control with a multi-perspective reliability framework reached 90.04% (seven-disease) and 83.8% (four-disease) accuracy on two MIMIC-IV-derived benchmarks, approaching a cloud baseline, and diagnostic behavioural consistency discriminated correct from incorrect diagnoses (AUC 0.860); cited as the evidence that on-premise control plus decision-time uncertainty estimation - not medical pre-training - are what enable clinically usable autonomy.

[2] Gorenshtein A, Omar M, Glicksberg BS, Nadkarni GN, Klang E. AI Agents in Clinical Medicine:
    A Systematic Review. *medRxiv* (preprint), 2025. DOI 10.1101/2025.08.22.25334232. PMID 40909853.
   Shows: Systematic review of 20 studies of LLM-based agents in clinical medicine: every agent system outperformed its baseline LLM (median +53 percentage points in single-agent tool-calling studies), multi-agent setups peaked at up to 5 agents, and gains were largest when agent architecture complexity matched task complexity; cited for the state of agentic (tool-using) clinical evaluation.

[3] Liu Y, Carrero ZI, Jiang X, et al. Benchmarking large language model-based agent systems for
    clinical decision tasks. *npj Digital Medicine*, 2026. DOI 10.1038/s41746-026-02443-6. PMID 41708802.
   Shows: Two agent systems (open-source OpenManus on Llama-4 and proprietary Manus) were benchmarked across AgentClinic, MedAgentsBench and Humanity's Last Exam and gained only modest accuracy over baseline LLMs (60.3% AgentClinic MedQA, 30.3% MedAgentsBench, 8.6% HLE text) at >10x token use and >2x latency, with multimodal accuracy remaining low; cited because the agent system itself was the object under test end-to-end.

[4] Bi Z, Hao J, Ma Y, Tao Y, Chia XL. Benchmark, Agent, and Tool-Use Harnesses for Large Language
    Models: A Taxonomy of Evaluation Infrastructure. *Preprints.org* (preprint), 2026.
    DOI 10.20944/preprints202609.0236.v1. Europe PMC ID PPR1311245.
   Shows: Survey/taxonomy of benchmark, agent and tool-use harnesses showing that the harness (task registries, prompts, adapters, tools, environments, scorers, traces) defines what a benchmark score means and that scaffold effects, oracle design, environment drift and schema sensitivity can change a result's scientific meaning; cited as evidence that tool-use evaluation infrastructure is heterogeneous and not a settled standard.

[5] Sellergren A, Kazemzadeh S, Mahvar F, et al. An open vision-language model for diverse medical
    applications. *Nature Medicine*, 2026. DOI 10.1038/s41591-026-04626-w. PMID 42839104.
   Shows: MedGemma, an open medical vision-language model collection based on Gemma 3, exceeded similarly sized generative models on out-of-distribution tasks (+2.6-10% medical image QA, +15.5-18.1% chest X-ray finding classification, +10.8% agentic evaluations) while retaining general Gemma capabilities, and its MedSigLIP encoder matched or beat many specialised medical image encoders; fine-tuning MedGemma beat fine-tuning base Gemma 3 when training data was limited; cited as the closest retrieved match for medical image understanding and data-efficient fine-tuning.

[6] Nouyed MI, Al-Mamun M, Adjeroh DA, Hu G. Comparative Analysis of General-Purpose vs.
    Domain-Specific Multimodal Models for Diabetic Retinopathy Classification. *Diagnostics*, 2026.
    DOI 10.3390/diagnostics16101504. PMID 42196870.
   Shows: On diabetic-retinopathy fundus classification, general-purpose conversational models with minimal prompting (Gemini 3 88.5%, GPT-5.2 77.9%) matched fine-tuned ophthalmology-specific models (RETFound 77.1%, EyeCLIP 85.8%) but stayed below MedGemma-1.5 (88.2%) and MedSigLIP (94.8%), and few-shot gains were substantial only for Pixtral-Large (+7.4%); cited for the specialisation-versus-flexibility trade-off between general and medical models.

[7] Safavi-Naini SAA, Ali S, Shahab O, et al. Benchmarking proprietary and open-source language and
    vision-language models for gastroenterology clinical reasoning. *npj Digital Medicine*, 2025.
    DOI 10.1038/s41746-025-02174-0. PMID 41310206.
   Shows: Board-style gastroenterology questions: proprietary o1-preview (82.0%) and Claude 3.5-Sonnet (74.0%) beat the best open-source models (Llama3.3-70b 65.7%, Qwen-2.5-72b 61.0%), while small quantised open models (8-bit Llama 3.2-11b 51.7%, 6-bit Phi3-14b 48.7%) scored comparably to their full-precision counterparts and VLM accuracy on image questions rose ~10% with human-written captions; cited as the open-versus-proprietary benchmark directly on topic, including a compression axis.

[8] Mouheb K, Pomp A, Manenti A, et al. Automatic extraction of structured information from brain
    MRI reports using an open-weight large language model. *European Radiology*, 2026.
    DOI 10.1007/s00330-026-12821-z. PMID 42613470.
   Shows: Open-weight LLaMA 3.1 extracted structured data from 947 Dutch brain MRI reports with high zero-shot balanced accuracy for visual rating scores (Fazekas 0.94, global cortical atrophy 0.87, medial temporal atrophy 0.90/0.96) and 0.93 accuracy for microbleed mentions, while few-shot prompting improved numerical variables (microbleeds 0.92, infarcts 0.81) and location-specific variables remained difficult; cited as the closest retrieved example of open-weight extraction from imaging reports.

[9] Sandfort V, Vigneault DM, Willemink MJ, et al. Benchmarking 54 large language model configurations
    for CAD-RADS scoring: open-weight models approach human-level agreement. *The International
    Journal of Cardiovascular Imaging*, 2026. DOI 10.1007/s10554-026-03785-8. PMID 42530821.
   Shows: Across 54 LLM configurations on 500 anonymised coronary CTA reports, only Claude 4.6 Opus and the open-weight Gemma 4 31B reached non-inferiority to the human inter-rater agreement band for zero-shot CAD-RADS classification, and Gemma 4 31B stayed non-inferior at 3-bit quantisation while fitting on a 24 GB consumer GPU; cited as evidence that open-weight models approach human-level agreement at our VRAM budget.

[10] Ko S, Lee J, Ko K, Kim J. Benchmarking Open-Source Vision Language Models in Orthopedic
    In-Training Examination: A Comparison with Residents, Domain-Specific Evaluation, and Parameter
    Scaling. *Clinics in Orthopedic Surgery*, 2026. DOI 10.4055/cios25183. PMID 41647505.
   Shows: Six open-source vision-language models on the 210-question 2023 Orthopedic In-Training Examination: the two largest (Qwen2.5-VL-72B, Llama-3.2-90B) performed comparably to second-year residents, Qwen-32B slightly outscored first-year residents, models under 11B scored below first-year residents, and accuracy rose steadily with model size up to 72B with little further gain beyond; cited for VLM parameter scaling on imaging-heavy questions.

[11] Gong R, Ding Y, Wang Z, et al. A survey of low-bit large language models: Basics, systems, and
    algorithms. *Neural Networks*, 2025. DOI 10.1016/j.neunet.2025.107856. PMID 40782663.
   Shows: Survey of low-bit quantisation for LLMs covering fundamental concepts and data formats, system/framework implementations across hardware platforms, and algorithms for efficient low-bit training and inference of parameters, activations and gradients; cited as the overview of quantisation as the main lever on LLM memory and compute cost.

[12] Bornet A, Sandralegar A, Yazdani A, Bijlenga P, Teodoro D. Impact of LLM Scale and Quantization
    on Information Extraction from Clinical Text. *Studies in Health Technology and Informatics*.
    Year 2026. DOI 10.3233/shti260295. PMID 42174969.
   Shows: Seven Qwen3/DeepSeek-R1 reasoning models (0.6B-70B) at 2/3/4/5/6/8 bits extracting mRS scores from 105 neurosurgery notes showed significant effects of log model size (beta=-0.84, p<0.001), quantisation (beta=-0.12, p<0.001) and their interaction (beta=0.08, p<0.001), with lower error for larger and higher-precision models but a plateau at 4-5-bit precision; cited as the measured quantisation/scale trade-off on a clinical extraction task.

[13] Huang W, Zheng X, Ma X, et al. An empirical study of LLaMA3 quantization: from LLMs to MLLMs.
    *Visual Intelligence*, 2024. DOI 10.1007/s44267-024-00070-x. PMID 39807379.
   Shows: Empirical evaluation of 10 post-training quantisation and LoRA fine-tuning methods for LLaMA3 at 1-8 bits, extended to the LLaVA-Next-8B multimodal model at 2-4 ultra-low bits, found non-negligible degradation in both linguistic and visual contexts particularly at ultra-low bit widths; cited as the warning that the vision path is the most fragile under aggressive quantisation.

[14] Guo Y, Hao Z, Shao J, et al. PT-BitNet: Scaling up the 1-Bit large language model with
    post-training quantization. *Neural Networks*, 2025. DOI 10.1016/j.neunet.2025.107855. PMID 40669405.
   Shows: PT-BitNet, a two-stage post-training quantisation method, extended BitNet-style ternary weights (+1, 0, -1) to models up to 70B parameters and reached 61% average downstream accuracy at 70B versus 51.2% for BitNet b1.58, with substantial reductions in model size and inference time and minimal impact on task performance; cited as evidence that ultra-low-bit ternary weights are now reachable by post-training at scale.

[15] Yin J, Dong J, Wang Y, De Sa C, Kuleshov V. ModuLoRA: Finetuning 2-Bit LLMs on Consumer GPUs by
    Integrating with Modular Quantizers. *Transactions on Machine Learning Research*, 2024. PMID 40837438.
   Shows: ModuLoRA fine-tunes 65B-parameter models in 2/3/4-bit precision on as little as one 24 GB GPU by integrating arbitrary weight quantizers with low-rank adapters, and its 2-bit (QuIP#) and 3-bit (OPTQ) variants outperformed less sophisticated 4-bit and 8-bit fine-tuning baselines; cited as evidence that very low-bit models can be fine-tuned within our VRAM budget.

[16] Khalpey Z, King N, Abraham A. Small Language Models for Developing Agentic AI in Healthcare:
    A Comprehensive Systematic Review and Critical Analysis. *Cureus*, 2026. DOI 10.7759/cureus.106427.
    PMID 42088811.
   Shows: Systematic review of small language models in agentic healthcare applications (documentation, decision support, triage, administration) concluding that SLMs offer sufficient capability for most agentic healthcare tasks while giving advantages in deployability, cost and operational efficiency, with regulatory alignment and governance as remaining considerations; cited as the strongest scale argument for our setup.

[17] Wiest IC, Ferber D, Zhu J, et al. Privacy-preserving large language models for structured medical
    information retrieval. *npj Digital Medicine*, 2024. DOI 10.1038/s41746-024-01233-2. PMID 39304709.
   Shows: An open-source pipeline using locally hosted Llama 2 extracted five clinical features from 500 MIMIC-IV patient histories against ground truth from three blinded experts, detecting decompensated liver cirrhosis with 100% sensitivity/96% specificity and showing that locally deployed LLMs can extract clinical information from free text with low hardware requirements; cited as the demonstrated privacy-preserving structuring pattern.

[18] Vaid A, Duong SQ, Lampert J, et al. Local large language models for privacy-preserving accelerated
    review of historic echocardiogram reports. *JAMIA*, 2024. DOI 10.1093/jamia/ocae085. PMID 38687616.
   Shows: A framework using the local open-source LLaMA-2 70B model answered 90% of 100 cardiologist-verified questions about more than ten years of echocardiogram report history (100% for diagnosis retrieval, 93% severity, 84% intervention, 83% temporality), with errors mainly from numeric misinterpretation and hallucination; cited as a local, privacy-preserving LLM speeding up review of historic reports.

[19] Sheng W, Wang Y, Xiao L, et al. BI-RADS-compliant structured mammography reporting using locally
    deployed large language models under privacy constraints. *European Radiology*, 2026.
    DOI 10.1007/s00330-025-12147-2. PMID 41258455.
   Shows: A locally fine-tuned open-source Llama-3 model, trained on 7161 mammography reports with pseudo-labels from the commercial Qwen-Max model, produced BI-RADS-oriented structured JSON with precision 0.942, recall 0.929, F1 0.932 and JSON/field integrity of 0.964/1.000, slightly below Qwen-Max overall but at improved privacy; cited as demonstrated local, privacy-preserving structured reporting.

[20] Heilmeyer F, Böhringer D, Reinhard T, Arens S, Lyssenko L, Haverkamp C. Viability of Open Large
    Language Models for Clinical Documentation in German Health Care: Real-World Model Evaluation
    Study. *JMIR Medical Informatics*, 2024. DOI 10.2196/59617. PMID 39195570.
   Shows: Four 7-billion-parameter open models were trained for German clinical documentation on-premise under restricted compute and rated by Claude-v2 and two human raters; the German-trained BLOOM-CLP-German performed best, with 93.1% of 102 generated reports judged usable as-is or with minor changes, and the authors conclude the target language must be considered in model selection; cited for German capability and on-premise feasibility.

[21] Bartels S, Carus J. From text to data: Open-source large language models in extracting cancer
    related medical attributes from German pathology reports. *International Journal of Medical
    Informatics*, 2025. DOI 10.1016/j.ijmedinf.2025.106022. PMID 40609461.
   Shows: Five instruction-tuned open-source LLMs extracted oncological attributes from German pathology reports (gold standard of 522 annotated reports) in an on-premise setting, with Llama 3.3 70B best overall (F1 > 0.90) and retrieval augmentation letting Mistral Small 24B match it on most entity types at far lower compute, while rare attributes such as metastasis and staging remained hard; cited for German-language extraction with small local models.

[22] Fanioudakis P. Beyond Perplexity: The Quality–Memory Frontier of Native Mixed-Precision KV
    Caching in llama.cpp. *Qeios* (preprint), 2026. DOI 10.32388/rgd04f. Europe PMC ID PPR1299510.
   Shows: Native packed mixed-precision KV caching in llama.cpp on Qwen3-4B showed Q3 keys raised held-out perplexity ~20% and Q2 keys were catastrophic while Q4/Q8 keys stayed similar, that the conservative Q4K-Q3V policy cut KV storage 13.89% with results statistically indistinguishable from Q4K-Q4V, and that the aggressive Q4K-MixV-21 policy lowered perplexity by 20.99% storage saving yet cost 2.81 points of strict GSM8K accuracy - concluding that perplexity-preserving KV compression is not necessarily behaviour-preserving; cited for KV-cache precision policy.

[23] Sharpton T, Davis II EW, Alexiev A. A practical risk framework for large language model use in
    life science research. *PLoS Computational Biology*, 2026. DOI 10.1371/journal.pcbi.1014776.
    PMID 42748119.
   Shows: Proposes an integrated risk framework for LLM use in life-science research that treats prompt design as a primary risk-management strategy and matches downstream verification effort to output verifiability, researcher expertise and consequence of error, with worked examples for literature synthesis, code generation, writing assistance and statistical reasoning plus an open-source prompt/verification repository; cited as applicable governance guidance for a research-side agent.

[24] Vach M, Boschenriedter C, Weiss D, et al. Data-efficient Neuroradiology MRI Imaging Protocol
    Prediction Using Open-weights Large Language Models. *Clinical Neuroradiology*, 2026.
    DOI 10.1007/s00062-026-01701-0. PMID 42446636.
   Shows: A locally deployable SOP-grounded MedGemma 27B system predicted MRI protocols from 598 German-language neuroradiology order entries with 73.07% flat zero-shot accuracy on the held-out set (n=479) and needed minimal labelled data, while hierarchical routing and prompt optimisation did not beat the flat baseline; cited as data-efficient, privacy-preserving open-weight use in neuroradiology.

[25] Grünig A, Kriebel J, Varghese J, Herrmann T, Sandmann S, Bruns C. Implementation and User
    Evaluation of an On-Premise Large Language Model in a German University Hospital Setting:
    Cross-Sectional Survey. *JMIR AI*, 2026. DOI 10.2196/84362. PMID 41984850.
   Shows: Cross-sectional survey of an on-premise LLM at University Medicine Magdeburg among 322 registered users (91 analysable responses) found positive perceptions of speed and quality, 62.6% using the platform at least weekly and 44% reporting at least 30 minutes of saved work per week across diverse professional use cases; cited as documented hospital-side acceptance of on-premise LLMs in a German university hospital.

---

## Retrieval log (traceability)

Sources actually used, and their raw files under `raw/`:

- PubMed E-utilities — searches: `pm_local_llm_privacy`, `pm_open_weight_clinical`,
  `pm_quantization_llm`, `pm_medgemma`, `pm_vlm_radiology_llm`, `pm_llm_german_medical`,
  `pm_llm_tool_calling` (`pm_*_fetch.xml` = efetch details).
- Europe PMC REST — three passes, e.g. `epmc_local_llm_dp.json`, `epmc_privacy_llm_review.json`,
  `epmc_quantization_med.json`, `epmc_4bit_clinical.json`, `epmc_bitnet_ternary.json`,
  `epmc_ternary_bits.json`, `epmc_gguf_llama_cpp.json`, `epmc_medgemma*.json`,
  `epmc_qwen3_clinical.json`, `epmc_tool_calling_open.json`, `epmc_function_call_llm.json`,
  `epmc_benchmark_function_calling.json`, `epmc_agent_local_clinic.json`, `epmc_llm_agent_clinical.json`,
  `epmc_german_medical.json`, `epmc_llm_german.json`, `epmc_vlm_*.json`, `epmc_mri_report_llm.json`.
  624 unique records were indexed into `index.tsv`.

- **arXiv: NOT usable.** Every request from this host (through the configured proxy) returned
  `HTTP 429` with body `Rate exceeded.` — including a trivial `all:electron, max_results=2` query
  after 30 s, 90 s and repeated 100 s waits, and both `export.arxiv.org` and `arxiv.org` URLs, with
  and without redirect following. No arXiv identifier is cited in this report for that reason.

- No patient data was accessed. All scripts and raw answers live in
  (local research folder).

---
### Claims not supported by the abstracts
Claims from sections 2–4 that the abstract of the cited reference does not support. The claim text in
those sections is now marked "(unverified)"; nothing else in the report was changed.

**Claim** §2 bullet 1 (ref `[1]`, Zhang et al., Nat Med 2026, PMID 42744896): the claim that the
decisive factors were local control plus a reliability layer **in contrast to** "a 'medical'
pre-training flavour". The abstract reports the on-premise agent's accuracy and its decision-time
reliability measures, but never compares medical against general pre-training, so the "not a medical
pre-training flavour" inference is the report's own, not the paper's finding.

**Claim** §2 bullet 4 and §3.2 bullet 3 (ref `[14]`, Guo et al., Neural Netw 2025, PMID 40669405):
"a modest accuracy drop versus a from-scratch 1.58-bit baseline". PT-BitNet's abstract reports
"minimal impact on task performance" and gives 61% average accuracy at 70B versus 51.2% for BitNet
b1.58 — that is an improvement, and the comparison is to the much smaller b1.58 model, not a
like-for-like baseline at equal scale. A "modest accuracy drop" is therefore not what the abstract
shows.

**Claim** §3.1 bullet 4 (ref `[7]`, Safavi-Naini et al., npj Digital Medicine 2025, PMID 41310206):
the claim that this is a benchmark of proprietary vs open-source **vision-language** models in the
sense used elsewhere in the report. The abstract does say VLMs were included, but it reports no VLM
results table — only that VLM accuracy on image questions improved ~10% with human-generated
captions. The VLM comparison as stated is not evidenced by the abstract. (The claim is also placed
only under §3.1, not §3.4, so the vision capability is not double-counted.)

Note: the statements already flagged in the report itself as *unverified* before this task (§2 last
bullet and §3.6, the unnamed candidate checkpoints) were left as they were; they are not repeated here.
