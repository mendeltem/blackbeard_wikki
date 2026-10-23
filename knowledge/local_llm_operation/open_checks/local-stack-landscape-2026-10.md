---
id: local-stack-landscape-2026-10
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-23
herkunft: Claude-Code-Sitzung Victus, Webrecherche in drei Strängen, 2026-10-06
verweist_auf: [moe-expert-offloading, prefix-cache-single-slot, dense-27b-vs-moe-on-8gb, laya-router-before-agent, lean-hermes-toolsets, minimal-harness-prompt-size, flash-next-177b-moe-on-24gb-card, nemotron-bolt-74b-on-ampere-24gb]
---

# Lokaler Arbeitsplatz, Stand Oktober 2026: was auf 8 und 24 GB zu messen lohnt

## Aussage
Webrecherche vom 2026-10-06 zu Modellen, Methoden und Entscheidungsmodellen für
eine Consumer-GPU. Fast alle Zahlen sind Herstellerangaben oder Blogs [V];
unabhängig [U] sind nur Artificial Analysis, localbench, Kaitchup und einzelne
Community-Messungen. Daraus folgen Messungen auf Victus, keine Setzungen.

**Modelle.**
- 8 GB: Qwen3.6-35B-A3B mit Experten auf der CPU bleibt die Wahl; nichts schlägt es nachweislich.
  Schnell und ganz auf der GPU: Qwen3.5-9B oder MiMo-V2.6-Distill-Qwen-9B [V].
  Ternary Bonsai 2 27B (Qwen3.8-27B ternär, 5,9 GB, 17.09.2026) ist unabhängig ungeprüft und braucht einen Fork.
- 24 GB: Qwen3.8-27B (14.08.2026, Apache 2.0) laut Artificial Analysis stärkstes kleines Open-Modell [U].
  Alternativen Laguna XS 2.1 (33B-A3B, braucht llama.cpp-PR #25165), Gemma 4 26B-A4B/31B.
  Deutsch: Soofi S (31,6B-A3,2B, Lizenz unklar).

**Methoden.**
- MTP-Speculative-Decoding in llama.cpp seit 16.05.2026 (`--spec-type draft-mtp --spec-draft-n-max 2`), +78 % auf Qwen3.6-27B [U, Blog].
- `--n-cpu-moe`-Sweep: auf 8 GB 32–41 tok/s für Qwen3.6-35B-A3B, bestes N 25, nicht monoton [U, Community].
  Victus misst bisher 19,4 (Windows) und 29,5 t/s (Ubuntu), siehe [moe-expert-offloading](../mechanisms/moe-expert-offloading.md).
- Prefix-Cache über `--cache-ram`/`--cache-reuse` nur bei byte-stabilem System-Prompt und Tool-Liste.
- KV-Cache q8_0 bei Qwen3.6 fast verlustfrei (KLD < 0,04), bei Gemma 4 nicht (0,108) [U, localbench 24.04.2026].
- OpenCode ohne ungenutzte Tools: 7 516 auf 5 335 Token im ersten Turn [U, Einzelmessung].

**Entscheidungsmodelle.**
- Routing: Arch-Router-1.5B und Embedding+kNN als Gegner für Laya. RouterArena und LLMRouterBench (2026) finden einfache kNN-Router oft gleichauf [U].
- Wächter für Shell-Befehle: Regelparser mit Allowlist, Modell nur für Grauzonen (Granite Guardian 4.1 8B, eigene Kriterien, Apache 2.0).
  Inhalts-Guards wie Qwen3Guard oder Llama Guard decken Shell-Gefahr nicht ab.
- Antwortprüfung: Skywork-Reward-V2 (0.6B–8B), LettuceDetect (ModernBERT, CPU).

## Zu prüfen
1. `--n-cpu-moe` 15–40 mit `llama-bench`, pp512/tg128, `-ub 512` gegen `-ub 4096`.
2. MTP an/aus, `--spec-draft-n-max` 1/2/3, Akzeptanz bei Code und Prosa.
3. KV f16/q8/q4 mit `llama-perplexity --kl-divergence` auf eigenen Agent-Logs.
4. Time-to-first-token ab Turn 2 mit/ohne `--cache-ram`, volles gegen reduziertes Tool-Set.
5. Laya gegen Arch-Router gegen Embedding+kNN auf den 60 Routing-Fällen in local_models `tools/laya/faelle/route.jsonl`.
6. 50 gefährliche und 50 harmlose Shell-Befehle: Regelparser gegen Granite Guardian 4.1.

## Trägt nicht
Dass eines der genannten Modelle auf Victus besser ist. Keine der Zahlen ist hier gemessen;
mehrere Ranking-Seiten widersprachen den Modellkarten und wurden verworfen.

## Bruchindikator
Je Punkt unter "Zu prüfen" eine eigene Messung auf Victus; Ergebnis als Befund, dieser Prüfpunkt wird dann geschlossen oder verkleinert.

## Ablesung
Quellen [V]/[U] wie markiert, unter anderem:
- https://github.com/ggml-org/llama.cpp/pull/23269
- https://huggingface.co/blog/Doctor-Shotgun/llamacpp-moe-offload-guide
- https://localbench.substack.com/p/kv-cache-quantization-benchmark
- https://kaitchup.substack.com/p/serving-exllamav3-with-tabbyapi-accuracy
- https://artificialanalysis.ai/models/open-source/small
- https://jacar.es/en/opencode-with-local-models/
- https://arxiv.org/abs/2506.16655 (Arch-Router)
- https://arxiv.org/abs/2601.07206 (LLMRouterBench)
- https://huggingface.co/ibm-granite/granite-guardian-4.1-8b

Vollständiger Stand mit allen Quellen: local_models `recherche/stand/2026-10-06.md`, täglich fortgeschrieben.

## Addendum 2026-10-23: newest models against Alita (RTX A5000 24 GB, Ampere SM86, 62 GB RAM)
Desk research on 2026-10-23, nothing measured on Alita yet. [V] = vendor or blog, checked on the model card.

| Model (date) | Size | Fits Alita? | Note |
|---|---|---|---|
| NVIDIA Nemotron 3.5 Bolt 74B-A9B-24GB (HF 2026-10-15, OpenMDW-1.1) | 74B total, 9B active; experts IQ2_XXS (2.0625 bit), Mamba layers NVFP4, embedding/head Q8_0, quantization-aware distillation | yes, measured 2026-10-23 ([finding](../findings/nemotron-bolt-74b-on-ampere-24gb.md)) | Only new October model built for 24 GB. Hybrid Mamba-2/Transformer LatentMoE, text+image+video, up to 256K context, German listed. Vendor table against Qwen3.6-35B-A3B BF16: Terminal-Bench 2.1 50.98 vs 44.38, BrowseComp 66.75 vs 48.74, GPQA Diamond 86.43 vs 83.40, but AA-Omniscience accuracy 16.90 vs 19.47 and non-hallucination 61.27 vs 65.85 [V]. No comparison with Qwen3.8-27B. |
| DeepSeek-V4.1-Flash-1017 (2026-10) | 763B (552B backbone + 196B Engram), FP8 with FP4 experts | no | Smallest GGUF UD-IQ1_S 233 GB, Unsloth recommends 128-145 GB RAM+VRAM, needs llama.cpp PR #30817. Alita has 86 GB RAM+VRAM. |
| Qwen3.8-Flash-Next (2026-08) | 125B + 51B n-gram table, 6B active | yes, slow | Vendor: DeepSWE 58.7 vs 42.2 and SWE-bench Pro 62.5 vs 61.7 against Qwen3.8-27B [V]. Measured here 2026-10-07: 15-23 tok/s, RAM at the limit ([flash-next-177b-moe-on-24gb-card](../findings/flash-next-177b-moe-on-24gb-card.md)); files removed 2026-10-17. |
| Qwen3.8-27B (2026-08, Apache 2.0) | 27.8B dense, Q4_K_M 16.4 GB | yes (in service) | October guides still name it the 24 GB pick [V]; no newer dense model of this class with independent numbers found. |

**Catch for Bolt on Alita.** The NVIDIA GGUF card lists only Ada Lovelace and Blackwell; Ampere is not named.
Its smallest llama-server recipe is "28GB" (32 GB card or 64 GB unified memory). The command uses `--spec-type draft-dflash`
with a 998 MB draft model. Unsloth's IQ2_XXS is 22 GB plus the vision projector, with 24-32 GB RAM minimum.
Measured 2026-10-23: it runs fully on the A5000 (SM86), 66-69 tok/s, 22.2 GB at 16k context, 88.5 % / 96.2 % on the 13-task bench at 1 500 / 4 096 tokens against 100 % / 97.4 % for the 27B (same card, same day), so not a replacement; see [nemotron-bolt-74b-on-ampere-24gb](../findings/nemotron-bolt-74b-on-ampere-24gb.md).

Out of reach (multi-GPU, only seen in news roundups, not checked): Meta Muse Spark Open 816B-A42B (2026-10-15),
DeepSeek-V4-Pro, Reflection AI Beam 501B-A23B (announced 2026-10-05, weights pending).

**Next measurement:** Bolt IQ2_XXS with a current llama.cpp build in its own folder, experts partly on the CPU
(`--n-cpu-moe`) if 24 GB is not enough. Run the six check questions and the Clara task test against Qwen3.8-27B Q4
(2026-10-17: 27B 95 %). Report tok/s at a 5k prompt.

Sources (opened 2026-10-23):
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB (model card: release 10/15/2026, quantization, benchmark table, languages)
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF (GGUF files, supported architectures, 28GB/32GB recipes)
- https://unsloth.ai/docs/models/nemotron-3.5-bolt (IQ2_XXS 22 GB, RAM guidance, "build latest llama.cpp")
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 (763B, FP8/FP4, MIT, vLLM/SGLang) and its config.json (384 experts, 6 per token)
- https://unsloth.ai/docs/models/deepseek-v4.1-flash (GGUF 233-508 GB, 128-145 GB minimum, llama.cpp PR #30817)
- https://huggingface.co/Qwen/Qwen3.8-Flash-Next (125B + 51B n-gram, 6B active, benchmarks against 27B)
- https://dev.to/gpunz/how-much-vram-do-open-llms-really-need-real-gguf-sizes-for-35-models-october-2026-28n2 (GGUF sizes of 35 models, 2026-10-20)

## Verknüpft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
- [dense-27b-vs-moe-on-8gb](dense-27b-vs-moe-on-8gb.md)
- [laya-router-before-agent](../findings/laya-router-before-agent.md)
- [lean-hermes-toolsets](../findings/lean-hermes-toolsets.md)
- [minimal-harness-prompt-size](minimal-harness-prompt-size.md)
- [flash-next-177b-moe-on-24gb-card](../findings/flash-next-177b-moe-on-24gb-card.md)
