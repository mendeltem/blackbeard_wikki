---
id: one-native-multimodal-model-vs-model-ensembles-2026-10
typ: befund
status: vorschlag
thema: knowledge/imaging_genetics
stand: 2026-10-24
herkunft: literature scan 2026-10-24 (two search passes, every arXiv ID re-fetched from the arXiv API, DOIs from Crossref/PubMed, key numbers checked against abstracts)
verweist_auf: [mouse-genotype-mri-data-and-dna-mri-text-models-2026-10]
---

# One natively multimodal model instead of several cooperating models: the recipe exists for text+images, not yet for text+DNA+3D MRI+clinical numbers

## Aussage
**The recipe.**
- Every modality gets its own cheap tokenizer or patch layer: text BPE, image VQ codes or continuous patches, DNA
  nucleotides, protein residues, SMILES, numbers.
- One transformer with shared attention processes the mixed sequence.
- Each modality gets its own output head or loss.

**Five design families are documented:**
1. **Discrete early fusion,** everything as tokens in one decoder: Chameleon, Emu3, Gato, Unified-IO 2.
2. **Hybrid losses in one backbone:** Transfusion uses next-token loss for text and diffusion for images, scales
   better than quantizing images (models up to 7 B), and Show-o is similar.
3. **Decoupled visual front ends around one backbone:** Janus.
4. **Modality-specific parameters inside one model:**
   - Mixture-of-Transformers matches the dense baseline with 55.8 % of the FLOPs.
   - MoMa (modality-aware experts) saves 3.7x FLOPs.
5. **Shared perception encoders or embedding spaces:** Perceiver IO, ImageBind, Meta-Transformer, 4M/4M-21
   (any-to-any over tens of modalities).

**Interference is real, and it depends on scale.**
- Mixed-modal scaling laws model synergy and competition between modalities explicitly. A 30 B speech-text model
  beat the unimodal models (Aghajanyan 2023). The sub-pass read the paper body: competition dominates at small scale.
- A study of 457 natively multimodal models found no inherent advantage of late fusion (bolt-on encoders) over early
  fusion; mixture-of-experts lets the model learn modality-specific weights (Shukor 2025).
- Chameleon needed extra stabilization because shared weights let the modalities compete. The QK-norm and z-loss
  details come from the paper body, read by a sub-pass and not re-checked.
- Best-supported fix: keep attention shared and give each modality its own feed-forward weights or experts.

**Scientific "languages of nature" in one model.**
- **Sequence-only unification works:**
  - NatureLM: molecules, proteins, DNA/RNA and materials as tagged sequences in one model.
  - Galactica: SMILES and protein sequences inline in scientific text.
  - Intern-S1: a dynamic tokenizer for SMILES/FASTA, plus a time-series encoder.
  - Evo 2: DNA, with RNA and protein reached through the central dogma.
  - ESM3: protein sequence, structure and function tokens in one model.
- **Generalist biomedical models:** Med-PaLM M (text, images, genomics; 14 tasks), BiomedGPT, MedGemma, RadFM.
- **Generalists are usually competitive but lose on precision tasks.**
  - TxGemma was compared against specialists on 66 tasks: superior on 26, superior or comparable on 50.
  - Tx-LLM exceeds state of the art on 22 of 66 tasks.
  - Med-PaLM M loses to the dedicated DeepVariant on variant calling (number from the paper body, sub-pass).
- **3D MRI in a text model is expensive.** MedGemma 1.5 feeds up to 85 axial slices at 256 tokens each (about
  21,760 tokens; paper body, sub-pass). RadFM compresses 3D patches to 32 tokens per image with a Perceiver.
- **Numbers.** Galactica splits digits, Tx-LLM and TxGemma bin regression targets, and xVal proposes one continuous
  number token.
- **No verified model covers text + DNA/RNA + protein + molecules + 3D MRI + clinical numbers natively.**

**Assessment (mine): a practical path to one model.**
1. Start from an open LLM backbone.
2. Add modality tokenizers: nucleotides for DNA, 3D patch tokens compressed to a few dozen per scan for MRI, and
   numbers as text with units or an xVal-style continuous token.
3. Give DNA, MRI and tabular tokens their own feed-forward weights (Mixture-of-Transformers style) behind shared
   attention.
4. Train in two stages: align first with frozen encoders (cheap), then train jointly on mixed paired and unpaired
   data.

Native pretraining from scratch is data-centre scale. On a single 24 GB card the realistic options are continued
training or LoRA of an existing multimodal model at a few billion parameters. At that size the scaling laws predict
more competition than synergy, so a specialist ensemble can still win there.

## Trägt
Architecture choice for a multi-"language" model: shared attention plus modality-specific weights; which
tokenization exists per modality; what the generalist-vs-specialist evidence says.

## Trägt nicht
Performance claims for DNA + 3D MRI + text in one model (none published and verified); training budgets of the cited
models (not extracted); weight licences beyond what the abstracts state.

## Bruchindikator
A published natively multimodal model that includes 3D MRI and genomic sequence and beats specialist ensembles; or
scaling evidence that small mixed models (< 10 B) already gain from adding modalities.

## Ablesung
**Method.**
- Two search passes on 2026-10-24.
- All 43 arXiv IDs and DOIs were re-fetched by script (arXiv API, Crossref); the titles match.
- PMIDs were checked via PubMed.
- Numbers marked "paper body, sub-pass" were read from full texts by a sub-pass and not re-checked.

### Sources
| Source | What it shows | ID |
|---|---|---|
| Reed 2022 | Gato: one transformer for text, images, control actions | [arXiv 2205.06175](https://arxiv.org/abs/2205.06175) |
| Jaegle 2021 | Perceiver IO: general architecture for structured inputs and outputs | [arXiv 2107.14795](https://arxiv.org/abs/2107.14795) |
| Aghajanyan 2023 | Scaling laws for mixed-modal models: synergy vs competition; 30 B speech-text beats unimodal | [arXiv 2301.03728](https://arxiv.org/abs/2301.03728) |
| Girdhar 2023 | ImageBind: one embedding space for six modalities | [arXiv 2305.05665](https://arxiv.org/abs/2305.05665) |
| Zhang 2023 | Meta-Transformer: one framework for many modalities | [arXiv 2307.10802](https://arxiv.org/abs/2307.10802) |
| Mizrahi 2023 | 4M: massively multimodal masked modelling | [arXiv 2312.06647](https://arxiv.org/abs/2312.06647) |
| Bachmann 2024 | 4M-21: any-to-any model for tens of modalities | [arXiv 2406.09406](https://arxiv.org/abs/2406.09406) |
| Lu 2023 | Unified-IO 2: vision, language, audio, action autoregressively | [arXiv 2312.17172](https://arxiv.org/abs/2312.17172) |
| Gemini Team 2023 | Gemini: natively multimodal family (closed) | [arXiv 2312.11805](https://arxiv.org/abs/2312.11805) |
| Chameleon Team 2024 | Early-fusion token-based mixed-modal model, stable training recipe | [arXiv 2405.09818](https://arxiv.org/abs/2405.09818) |
| Wang 2024 | Emu3: next-token prediction for all modalities | [arXiv 2409.18869](https://arxiv.org/abs/2409.18869) |
| Xie 2024 | Show-o: one transformer for understanding and generation | [arXiv 2408.12528](https://arxiv.org/abs/2408.12528) |
| Wu 2024 | Janus: decoupled visual encoding in one model | [arXiv 2410.13848](https://arxiv.org/abs/2410.13848) |
| Zhou 2024 | Transfusion: next-token + diffusion in one transformer; scales better than discrete images | [arXiv 2408.11039](https://arxiv.org/abs/2408.11039) |
| Liang 2024 | Mixture-of-Transformers: modality-specific parameters, 55.8 % of dense FLOPs | [arXiv 2411.04996](https://arxiv.org/abs/2411.04996) |
| Lin 2024 | MoMa: modality-aware experts, 3.7x FLOPs savings | [arXiv 2407.21770](https://arxiv.org/abs/2407.21770) |
| Shukor 2025 | Scaling laws for native multimodal models, 457 models; early fusion not inferior | [arXiv 2504.07951](https://arxiv.org/abs/2504.07951) |
| Deng 2025 | BAGEL: emerging properties in unified multimodal pretraining | [arXiv 2505.14683](https://arxiv.org/abs/2505.14683) |
| Tong 2026 | Beyond language modeling: multimodal pretraining study (abstract only) | [arXiv 2603.03276](https://arxiv.org/abs/2603.03276) |
| Han 2026 | Towards physics of multimodal pretraining: modality synergy, early unification (abstract only) | [arXiv 2608.05000](https://arxiv.org/abs/2608.05000) |
| Hamamci 2025 | Better tokens for better 3D: vision-language modelling in 3D medical imaging | [arXiv 2510.20639](https://arxiv.org/abs/2510.20639) |
| Taylor 2022 | Galactica: science LLM with SMILES and protein sequences inline | [arXiv 2211.09085](https://arxiv.org/abs/2211.09085) |
| Pei 2023 / 2024 | BioT5 and BioT5+: text, molecules, proteins | [arXiv 2310.07276](https://arxiv.org/abs/2310.07276), [arXiv 2402.17810](https://arxiv.org/abs/2402.17810) |
| Xia 2025 | NatureLM: one sequence model for molecules, proteins, DNA/RNA, materials | [arXiv 2502.07527](https://arxiv.org/abs/2502.07527) |
| Bai 2025 (Intern-S1) / Zou 2026 (Intern-S1-Pro) | Scientific multimodal foundation model, SMILES/FASTA tokenizer, time series | [arXiv 2508.15763](https://arxiv.org/abs/2508.15763), [arXiv 2603.25040](https://arxiv.org/abs/2603.25040) |
| Nguyen 2024, Science | Evo: DNA model from molecular to genome scale | PMID 39541441, [10.1126/science.ado9336](https://doi.org/10.1126/science.ado9336) |
| Brixi 2026, Nature (Evo 2) | Genome modelling and design across all domains of life | PMID 41781614, [10.1038/s41586-026-10176-5](https://doi.org/10.1038/s41586-026-10176-5) |
| Hayes 2025, Science | ESM3: sequence, structure, function in one protein language model | PMID 39818825, [10.1126/science.ads0018](https://doi.org/10.1126/science.ads0018) |
| Tu 2023 | Med-PaLM M: generalist biomedical AI, 14 tasks incl. genomics | [arXiv 2307.14334](https://arxiv.org/abs/2307.14334) |
| Zhang 2024, Nat Med | BiomedGPT: generalist vision-language biomedical model | PMID 39112796, [10.1038/s41591-024-03185-2](https://doi.org/10.1038/s41591-024-03185-2), [arXiv 2305.17100](https://arxiv.org/abs/2305.17100) |
| Wu 2023 | RadFM: 2D and 3D radiology with text | [arXiv 2308.02463](https://arxiv.org/abs/2308.02463) |
| Bai 2024 | M3D: 3D medical image MLLM | [arXiv 2404.00578](https://arxiv.org/abs/2404.00578) |
| Sellergren 2025 / 2026 | MedGemma and MedGemma 1.5 technical reports | [arXiv 2507.05201](https://arxiv.org/abs/2507.05201), [arXiv 2604.05081](https://arxiv.org/abs/2604.05081) |
| Richard 2024, bioRxiv (ChatNT) | DNA/RNA/protein tasks by conversation (frozen DNA encoder + LLM) | [10.1101/2024.04.30.591835](https://doi.org/10.1101/2024.04.30.591835) |
| Chaves 2024 | Tx-LLM: one model for 66 therapeutic tasks, exceeds SOTA on 22 | [arXiv 2406.06316](https://arxiv.org/abs/2406.06316) |
| Wang 2025 | TxGemma: vs specialists superior on 26, superior or comparable on 50 of 66 tasks | [arXiv 2504.06196](https://arxiv.org/abs/2504.06196) |
| Golkar 2023 | xVal: continuous number token for scientific LMs | [arXiv 2310.02989](https://arxiv.org/abs/2310.02989) |
| Zhong 2024 | Benchmarking LLMs for molecule prediction tasks | [arXiv 2403.05075](https://arxiv.org/abs/2403.05075) |
| Luo 2023 | BioMedGPT: open multimodal generative pre-trained transformer for biomedicine | [arXiv 2308.09442](https://arxiv.org/abs/2308.09442) |
