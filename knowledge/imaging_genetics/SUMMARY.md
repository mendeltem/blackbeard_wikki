# imaging_genetics: Kurzstand

Stand 2026-10-24. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md).

2026-10-24, scan: **one native multimodal model instead of cooperating models.** The documented recipe is a cheap tokenizer per modality, one transformer with shared attention, and modality-specific feed-forward weights or experts against interference (Mixture-of-Transformers, MoMa). Whether modalities compete depends on model size relative to data and on the modality pair: speech-text needed 30 B to turn competition into synergy, but translation models under 1 B largely avoid interference, and early fusion is not worse than late fusion at small size (counter-checked 2026-10-24). Science models unify sequences (NatureLM, Evo 2, ESM3, Galactica); generalists are usually competitive but lose on precision tasks. No verified model takes text, DNA, 3D MRI and clinical numbers natively. See [one-native-multimodal-model-vs-model-ensembles-2026-10](findings/one-native-multimodal-model-vs-model-ensembles-2026-10.md).

2026-10-24, scan: public mouse brain MRI comes with genotype labels (strain, knockout, transgene), not per-animal
genomes; strain genomes (Mouse Genomes Project, Mouse Phenome Database) can be joined by label. Openly downloadable:
Cambridge Huntington's library (399 brains) and MODEL-AD data via the AD Knowledge Portal. Models exist for DNA
(Nucleotide Transformer, Evo 2, HyenaDNA), brain MRI (BrainIAC), MRI + text (RadFM, M3D), DNA + text (ChatNT,
BioReason) and SNP + MRI (AlzCLIP, COMICAL); none takes all three. See
[mouse-genotype-mri-data-and-dna-mri-text-models-2026-10](findings/mouse-genotype-mri-data-and-dna-mri-text-models-2026-10.md).
