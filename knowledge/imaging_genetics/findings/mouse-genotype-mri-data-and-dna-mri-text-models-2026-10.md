---
id: mouse-genotype-mri-data-and-dna-mri-text-models-2026-10
typ: befund
status: vorschlag
thema: knowledge/imaging_genetics
stand: 2026-10-24
herkunft: literature and web scan 2026-10-24 (one search pass plus re-check by the main session; PMIDs and DOIs re-fetched from PubMed, GitHub/arXiv/bioRxiv links opened, HTTP 200)
verweist_auf: []
---

# Mouse brain MRI exists with genotype *labels*, not per-animal genomes; no model yet reads DNA, MRI and text together

## Aussage
**Mouse data.** I found no public dataset with a per-animal genome sequence plus brain MRI. The genetics in mouse MRI
collections is a strain or a model label. A label still links to DNA, because the strains themselves are sequenced:
the Mouse Genomes Project sequenced 17 inbred strains, including C57BL/6J, DBA/2J and CAST/EiJ (Keane 2011), and the
Mouse Phenome Database serves strain-level variant calls. So "strain X + MRI of strain X + genome of strain X" can be
assembled. The number of distinct genotypes stays small (4 to about 26 per collection).

| Dataset | Genetics | MRI | Size | Access |
|---|---|---|---|---|
| Cambridge Huntington's mouse library (Sawiak 2012) | model label WT, R6/2 (CAG 109-464), YAC128 | ex vivo, high resolution, templates, grey/white and cortical-thickness maps | 399 brains, 9-80 weeks | public, "no constraints", Cambridge DSpace repository |
| MODEL-AD 5XFAD (Oblak 2021) and later late-onset AD models (Kotredes 2024) | transgene / humanized APOE4, Trem2 etc. | in vivo MRI (volumes), PET, plus transcriptomics, EEG, behaviour | several cohorts | public via AD Knowledge Portal (stated for 5XFAD) |
| Toronto MICe autism models (Ellegood 2014) | 26 model labels (knockouts, BTBR, CNVs) | ex vivo 7 T T2-weighted | 432 mice | no data-availability statement found |
| BXD recombinant inbred strains (Poot 2011) | BXD strain genotypes, QTL mapping | high-field MRI, corpus callosum volume | not stated in abstract | not stated |
| Duke four-strain MR microscopy (Wang 2020) | C57BL/6J, DBA/2J, CAST/EiJ, BTBR | ex vivo 9.4 T, structure + diffusion connectomes, 166 regions/hemisphere | 4 strains | not checked |
| IMPC (Dickinson 2016) | targeted knockouts on C57BL/6N | mostly embryo micro-CT/OPT/HREM; brain MRI only at P7 for some lethal lines | 1,751 knockouts (first release) | IMPC portal (not opened) |
| Allen DevCCF (Kronman 2024) | none per animal (atlas) | ex vivo 7 T, 7 ages E11.5-P56 | 66 MRI samples | download (kimlab.io) |
| Collaborative Cross / Diversity Outbred | full genotypes | no brain-MRI dataset found (3 PubMed queries) | - | - |

**Human counterparts** (genome + brain MRI): UK Biobank (application and fee; new applications reported paused, not
confirmed), ADNI (whole-genome sequencing under a separate agreement). Neither offers radiology text as a
ready-made training corpus (not checked in detail).

**Models.**
- **DNA language models:** Nucleotide Transformer (50 M-2.5 B parameters, Dalla-Torre 2024), HyenaDNA (up to 1 M
  tokens), Caduceus, DNABERT-2, Evo 2 (1-40 B parameters, up to 1 M context, weights on Hugging Face).
- **MRI and MRI+text models:** BrainIAC (brain-MRI foundation model, about 49,000 scans, Tak 2026), RadFM and M3D
  (3D medical images + text).
- **DNA + text:** ChatNT, and BioReason (Nucleotide Transformer or Evo 2 encoder feeding a Qwen3 language model;
  checkpoints announced, not released).
- **Genotype + MRI, contrastive shared embedding:** AlzCLIP (SNPs + MRI features, ADNI 758 + UK Biobank 261
  subjects) and COMICAL (genetic markers + imaging-derived phenotypes, UK Biobank; code and weights public).
- **No published model combines all three modalities.**

**Assessment (mine, not from the sources): how a "multilingual" DNA + MRI + English model would be built.**
- **Architecture:** the LLaVA pattern. Frozen modality encoders feed small projection layers into an LLM, and only
  the projectors plus LoRA adapters are trained. The encoders would be a DNA model (e.g. Evo 2 1B or Nucleotide
  Transformer 500M) and a 3D brain-MRI encoder (e.g. BrainIAC). BioReason already does the DNA half this way.
- **The bottleneck is paired data.** Training needs examples that have all three parts at once: DNA, MRI, and a text
  description.
  - In mouse, the text can be generated from metadata ("5XFAD, female, 6 months, smaller hippocampus"). DNA then
    means the transgene or the strain's variant set.
  - Mouse collections offer only tens of distinct genotypes, so a model cannot learn a general DNA -> brain mapping.
    It can learn a narrow task such as "genotype -> regional-volume signature -> description".
- **A cheaper first step:** a contrastive genotype-MRI embedding (as in COMICAL or AlzCLIP) plus a language model
  that explains it via tool calls, instead of one end-to-end model.
- **Hardware:** a 24 GB card can hold the frozen encoders, a 1-4 B LLM and LoRA training on small data.
- **Patient data:** genome + MRI + reports of patients must stay on the local machine; a cloud model never sees them.

## Nachtrag 2026-10-24: the clinical layer (cognitive scores, age, diagnosis)
A DNA + MRI + text model for dementia also needs the structured clinical layer, measured in the same people and
dated, ideally at several visits.

**What the layer contains.**
- **Demographics:** age at each visit, sex, years of education, ancestry.
- **Cognitive screening and staging:** MoCA with version and language, MMSE, CDR.
- **Neuropsychological battery:** for example the NACC UDS 3.0, which comes with norms by age, sex and education
  (Weintraub 2018).
- **Diagnosis:** clinical diagnosis and aetiology.
- **Fluid and PET biomarkers:** amyloid and tau PET, CSF, plasma p-tau, NfL, GFAP.
- **Genetics:** APOE genotype.
- **Health:** vascular and lifestyle risk factors, as in the Lancet Commission 2024 report; medication and stroke
  history.
- **MRI context:** derived MRI measures (hippocampal volume, WMH, microbleeds, infarcts) and acquisition metadata
  (scanner, field strength, sequence).

**Why each part matters.**
- **Scores are not interchangeable.** The MoCA catches MCI that the MMSE misses: in the original validation the
  MoCA had 90 % sensitivity for MCI against 18 % for the MMSE (Nasreddine 2005). MoCA scores run consistently lower
  than MMSE scores. Equipercentile conversion tables exist:
  - a German-speaking memory clinic, n = 803, plus a review of 19 conversion studies (Fasnacht 2022);
  - by dementia type (Roheger 2022);
  - in Parkinson's disease (van Steenoven 2014), validated across 1,161 patients with a mean difference of 0.05
    points, SD 1.84 (Lawton 2016).
- **Raw scores need norms.** Age, sex and education shift both test scores and brain volumes, so the model should
  see z-scores against norms, not only raw values.
- **Change over time is the strongest signal.** In ADNI's first year, 16.5 % of MCI participants progressed to
  dementia (Petersen 2010).

**How a language model takes it in (assessment).**
- Serialize the values as text with a fixed schema, units and dates. Write "missing" explicitly. Example:
  "age 72, female, education 12 y, MoCA 23/30 (v8.1, German), CDR-SB 1.5, APOE e3/e4".
- An LLM already knows what MoCA or CDR mean. What it lacks is the pairing with images and genomes in the same
  people.
- A separate tabular encoder is the alternative when exact arithmetic on many variables matters.

**Datasets with the clinical layer.**
- **Human:** ADNI (cognitive and functional measures, CSF, MRI/PET, longitudinal; Petersen 2010) and NACC (UDS
  battery; Weintraub 2018).
- **Mouse:** no cognitive scores; behavioural tests are the analogue. MODEL-AD includes behaviour (Oblak 2021).

| Source | What it shows | ID |
|---|---|---|
| Nasreddine 2005, J Am Geriatr Soc | MoCA validation: 90 % sensitivity for MCI vs 18 % for MMSE | PMID 15817019, [10.1111/j.1532-5415.2005.53221.x](https://doi.org/10.1111/j.1532-5415.2005.53221.x) |
| Fasnacht 2022, J Am Geriatr Soc | MoCA-MMSE conversion, 803 memory-clinic patients + review of 19 conversions | PMID 36346002, [10.1111/jgs.18124](https://doi.org/10.1111/jgs.18124) |
| Roheger 2022, J Am Med Dir Assoc | MMSE-MoCA conversion by dementia type (SveDem, 387) | PMID 35561758, [10.1016/j.jamda.2022.03.018](https://doi.org/10.1016/j.jamda.2022.03.018) |
| van Steenoven 2014, Mov Disord | MMSE/MoCA/DRS-2 conversion in Parkinson's disease | PMID 25381961, [10.1002/mds.26062](https://doi.org/10.1002/mds.26062) |
| Lawton 2016, Mov Disord | Validation of MoCA-MMSE conversion across 5 studies | PMID 26861697, [10.1002/mds.26498](https://doi.org/10.1002/mds.26498) |
| Weintraub 2018, Alzheimer Dis Assoc Disord | NACC UDS 3.0 battery, norms by age, sex and education | PMID 29240561, [10.1097/WAD.0000000000000223](https://doi.org/10.1097/WAD.0000000000000223) |
| Petersen 2010, Neurology | ADNI clinical characterization, 819 participants, MCI progression 16.5 %/year | PMID 20042704, [10.1212/WNL.0b013e3181cb3e25](https://doi.org/10.1212/WNL.0b013e3181cb3e25) |
| Livingston 2024, Lancet | Lancet Commission 2024 on dementia prevention (modifiable risk factors; abstract not available, text not re-read) | PMID 39096926, [10.1016/S0140-6736(24)01296-0](https://doi.org/10.1016/S0140-6736(24)01296-0) |

## Nachtrag 2026-10-24: the time axis ("4D": 3D MRI over years)
Understanding a disease like AD means knowing its course, not one snapshot. Four model families exist.

**Event order.**
- The event-based model learns the order of events across a cohort, without predefined clinical stages, from
  cross-sectional or longitudinal data (Fonteijn 2012, familial AD and Huntington's disease).
- SuStaIn adds subtypes, each with its own trajectory (Young 2018). It finds three AD subtypes, identifies genetic
  FTD genotypes from imaging alone, and predicts diagnostic conversion better than models without subtype or stage.

**Individual image forecasting.** Brain Latent Progression predicts a person's future 3D T1 MRI with a latent
diffusion model conditioned on subject metadata, with voxel-level uncertainty (Puglisi 2025). It was trained on
11,730 MRIs from 2,805 subjects and tested externally on 2,257 MRIs from 962 subjects; the code is public.

**Digital twin.** Operator learning of the spatiotemporal spread of amyloid, tau and neurodegeneration per patient,
used to simulate interventions in silico (Wang 2026; the authors claim >90 % prediction accuracy).

**Assessment (mine).**
- The building blocks for a "brain world model" exist separately:
  - an MRI encoder gives a latent brain state;
  - a dynamics module (BrLP-like) moves that state in time, conditioned on age, genotype (APOE or a DNA embedding)
    and clinical scores;
  - an LLM on top reads and explains the result.
- The data must be repeated visits of the same people with dates, scores and comparable scanners.
- "What if" simulations are only as good as the causal knowledge behind them. Associations such as
  neuroticism -> dementia (see dementia_risk_factors) must not be fed in as causes.

| Source | What it shows | ID |
|---|---|---|
| Fonteijn 2012, NeuroImage | Event-based disease progression model, familial AD and Huntington's disease | PMID 22281676, [10.1016/j.neuroimage.2012.01.062](https://doi.org/10.1016/j.neuroimage.2012.01.062) |
| Young 2018, Nat Commun | SuStaIn: subtypes and stages; three AD subtypes; better conversion prediction | PMID 30323170, [10.1038/s41467-018-05892-0](https://doi.org/10.1038/s41467-018-05892-0) |
| Puglisi 2025, Med Image Anal | Brain Latent Progression: individual future 3D MRI via latent diffusion, public code | PMID 40774097, [10.1016/j.media.2025.103734](https://doi.org/10.1016/j.media.2025.103734) |
| Wang 2026, NPJ Syst Biol Appl | Digital-twin operator learning of amyloid/tau/neurodegeneration dynamics | PMID 42082519, [10.1038/s41540-026-00719-x](https://doi.org/10.1038/s41540-026-00719-x) |

## Trägt
Choosing data and an architecture for a first genotype-MRI-text prototype; knowing that mouse MRI data carry
labels, and that strain genomes have to be joined in separately.

## Trägt nicht
Claims about model quality (none of the multimodal models was run here); open-weight status of Nucleotide
Transformer, HyenaDNA, Caduceus, DNABERT-2, RadFM, M3D and BrainIAC (not checked); exact access terms of UK Biobank
and ADNI today.

## Bruchindikator
A public mouse dataset with per-animal sequencing and brain MRI (e.g. Diversity Outbred mice with MRI), or a
published model that takes DNA, 3D MRI and text together.

## Ablesung
**How this was checked.**
- A search pass ran on 2026-10-24, and the main session then re-checked its sources.
- Every PMID below was re-fetched from PubMed; the DOIs match.
- The GitHub, arXiv and bioRxiv pages answered HTTP 200 on 2026-10-24.
- Dataset facts come from the PubMed abstracts. A few come from article pages the search pass opened (MICe 7 T and
  432 mice, Allen DevCCF 66 samples); the main session did not re-check those.

**Unverified.**
- Data portals: MICe, IMPC images, GeneNetwork BXD.
- Status of UK Biobank applications.
- The ChatNT model card and its licence.
- The Evo 2 Nature article itself; only the README link to it was seen.

### Sources
| Source | What it shows | ID |
|---|---|---|
| Keane 2011, Nature | Genome sequences of 17 inbred laboratory mouse strains | PMID 21921910, [10.1038/nature10413](https://doi.org/10.1038/nature10413) |
| Grubb 2014, Nucleic Acids Res | Mouse Phenome Database: strain-level genotypes and phenotypes, open download | PMID 24243846, [10.1093/nar/gkt1159](https://doi.org/10.1093/nar/gkt1159) |
| Sawiak 2012, PLoS One | 399 ex vivo HD mouse brains (R6/2 CAG series, YAC128, WT), public without constraints | PMID 23300918, [10.1371/journal.pone.0053361](https://doi.org/10.1371/journal.pone.0053361) |
| Oblak 2021, Front Aging Neurosci | MODEL-AD 5XFAD characterization incl. imaging; data public via AD Knowledge Portal | PMID 34366832, [10.3389/fnagi.2021.713726](https://doi.org/10.3389/fnagi.2021.713726) |
| Kotredes 2024, Alzheimer's & Dementia | MODEL-AD late-onset AD models: MRI volume loss with age, PET, multi-omics | PMID 38735056, [10.1002/alz.13828](https://doi.org/10.1002/alz.13828) |
| Ellegood 2014, Mol Psychiatry | 26 autism mouse models clustered by MRI neuroanatomy | PMID 25199916, [10.1038/mp.2014.98](https://doi.org/10.1038/mp.2014.98) |
| Poot 2011, PLoS One | BXD strains, MRI corpus callosum volume, QTL at Hnrpul1 | PMID 21572526, [10.1371/journal.pone.0018612](https://doi.org/10.1371/journal.pone.0018612) |
| Wang 2020, NeuroImage | 9.4 T MR microscopy and connectomes of four strains; heritable brain phenotypes | PMID 32818613, [10.1016/j.neuroimage.2020.117274](https://doi.org/10.1016/j.neuroimage.2020.117274) |
| Dickinson 2016, Nature | IMPC knockout phenotyping, embryo imaging | PMID 27626380, [10.1038/nature19356](https://doi.org/10.1038/nature19356) |
| Kronman 2024, Nat Commun | Allen developmental mouse brain coordinate framework (MRI templates) | PMID 39433760, [10.1038/s41467-024-53254-w](https://doi.org/10.1038/s41467-024-53254-w) |
| Dalla-Torre 2024, Nat Methods | Nucleotide Transformer DNA models, 50 M-2.5 B parameters | PMID 39609566, [10.1038/s41592-024-02523-z](https://doi.org/10.1038/s41592-024-02523-z) |
| Nguyen 2023, arXiv | HyenaDNA, long-range DNA model up to 1 M tokens | [arXiv 2306.15794](https://arxiv.org/abs/2306.15794) |
| Schiff 2024, arXiv | Caduceus, bidirectional reverse-complement-equivariant DNA model | [arXiv 2403.03234](https://arxiv.org/abs/2403.03234) |
| Zhou 2023, arXiv | DNABERT-2, multi-species DNA model | [arXiv 2306.15006](https://arxiv.org/abs/2306.15006) |
| Evo 2 repository | 1-40 B parameter DNA models, up to 1 M context, weights on Hugging Face | [github.com/ArcInstitute/evo2](https://github.com/ArcInstitute/evo2) |
| ChatNT, bioRxiv 2024 | DNA/RNA/protein tasks driven by English prompts | [10.1101/2024.04.30.591835](https://doi.org/10.1101/2024.04.30.591835) |
| Fallahpour 2025, arXiv; repository | BioReason: DNA encoder + Qwen3 LLM reasoning | [arXiv 2505.23579](https://arxiv.org/abs/2505.23579), [github.com/bowang-lab/BioReason](https://github.com/bowang-lab/BioReason) |
| Wu 2023, arXiv | RadFM, radiology foundation model for 2D/3D images + text | [arXiv 2308.02463](https://arxiv.org/abs/2308.02463) |
| Bai 2024, arXiv | M3D, 3D medical image + text dataset and model | [arXiv 2404.00578](https://arxiv.org/abs/2404.00578) |
| Tak 2026, Nat Neurosci (preprint medRxiv 2024) | BrainIAC, brain-MRI foundation model | PMID 41644653, [10.1038/s41593-026-02202-6](https://doi.org/10.1038/s41593-026-02202-6); PMID 39677480 |
| Wang 2025, Adv Sci | AlzCLIP: contrastive SNP + MRI embedding for AD | PMID 40788127, [10.1002/advs.202507629](https://doi.org/10.1002/advs.202507629) |
| Machado Reyes 2025, Bioinform Adv | COMICAL: genetic markers + imaging phenotypes foundation model, code and weights | PMID 40917653, [10.1093/bioadv/vbaf196](https://doi.org/10.1093/bioadv/vbaf196), [github.com/IBM/comical](https://github.com/IBM/comical) |
