---
id: local-stack-landscape-2026-10
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-06
herkunft: Claude-Code-Sitzung Victus, Webrecherche in drei Strängen, 2026-10-06
verweist_auf: [moe-expert-offloading, prefix-cache-single-slot, dense-27b-vs-moe-on-8gb, laya-router-before-agent, lean-hermes-toolsets, minimal-harness-prompt-size]
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

## Verknüpft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
- [dense-27b-vs-moe-on-8gb](dense-27b-vs-moe-on-8gb.md)
- [laya-router-before-agent](../findings/laya-router-before-agent.md)
- [lean-hermes-toolsets](../findings/lean-hermes-toolsets.md)
- [minimal-harness-prompt-size](minimal-harness-prompt-size.md)
