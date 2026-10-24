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
