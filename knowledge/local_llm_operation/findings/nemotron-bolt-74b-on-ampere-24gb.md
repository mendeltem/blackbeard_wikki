---
id: nemotron-bolt-74b-on-ampere-24gb
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-23
herkunft: Alita (RTX A5000 24 GB, Ampere SM86, 62 GB RAM, driver 550 / CUDA 12.4), llama.cpp f64a498 built 2026-10-23 for sm_86, three runs 2026-10-23 09:06-09:16
verweist_auf: [local-stack-landscape-2026-10, hospital-model-hub-api-aliases-and-small-benchmark, flash-next-177b-moe-on-24gb-card]
---

# Nemotron 3.5 Bolt 74B-A9B (24GB GGUF) runs fully on an Ampere 24 GB card: 66-69 tok/s, 88.5 % on the 13-task bench at the old token budget

## Aussage
NVIDIA's own GGUF (`NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB.gguf`, 22 018 326 528 bytes, SHA-256 matches the Hub) loads
with a current llama.cpp (master f64a498, 2026-10-23, CUDA build for sm_86) completely on an RTX A5000. The GGUF card names
only Ada Lovelace and Blackwell, but the NVFP4 Mamba layers run on Ampere. Settings: `-ngl 99 --ctx-size 16384
--parallel 1 --flash-attn on --cache-type-k q8_0 --cache-type-v q8_0 --jinja`, no draft model, no vision projector.

| Measure | Value |
|---|---|
| Load time | 20-25 s |
| VRAM in use (16k context, one slot) | 22.2 GB of 24.6 GB; 1.9 GB left |
| Generation | 66-69 tok/s (Qwen3.8-27B Q4 on the same card: ~30 tok/s) |
| Prompt, 6 462 tokens | 1 222-1 320 tok/s |
| System message in the middle of the conversation | handled (answered "11") |
| Tool call (one function, OpenAI format) | correct call `get_weather({"city":"Berlin"})` |
| 13-task bench x 2, max 1 500 tokens (same as 2026-10-17) | **88.5 %** (Qwen3.8-27B Q4 on the same card, same day: 100 %) |
| Same bench, max 4 096 tokens | 96.2 % (Qwen3.8-27B Q4: 97.4 %) |
| Wall time for the 26 answers, 1 500 / 4 096 tokens | 206 s / 256 s (Qwen3.8-27B Q4: 254 s / 317 s) |
| Output tokens per answer, mean, 4 096 tokens | 608 (Qwen3.8-27B Q4: 380, at most 1 214) |

All three misses at 1 500 tokens were budget misses: the model was still reasoning and returned empty content (cohort
arithmetic twice, format task once). With 4 096 tokens one miss remained: "14" instead of 14.4 subjects. The long-prompt
summary needed 1 236 output tokens. Bolt reasons long by default; a budget made for the 27B starves it.

**Content caveat.** The format task passed on form, but both answers explained "SWI" as a police network or a
software system, not susceptibility-weighted imaging. The task is ambiguous (another model read it as SWI-Prolog
on 2026-10-17), but a neuroimaging assistant should pick the MRI reading. The bench's format scorer does not see this.

**Operational note (Alita).** `gpu-sperre lauf --platz` stops Clara's model server and says the model watchdog brings it
back. The watchdog does not restart it while any process matching `synthseg` runs, also a CPU-only SynthSeg. After the
test the server stayed down until it was started by hand. Remaining VRAM after stopping the server was 22 977 MiB (the
CPU embedding server keeps a 296 MiB CUDA context), so `--platz` above that fails with rc 4.

## Nachtrag 2026-10-23 17:30: the fair rerun of the 27B
Same bench, same day, same card: Qwen3.8-27B UD-Q4_K_M on Clara's live server (port 8000, one slot, 80k context, server
defaults for sampling), `llm_bench.py --repeats 2` with 4 096 and with 1 500 tokens. Result: **100 % at 1 500, 97.4 % at
4 096**. The only partial misses (4 096 run, both repeats) were the translation task answering "microhemorrhages"
instead of the scored word "microbleeds", i.e. sampling noise and a strict scorer, not the budget: the 27B never used
more than 1 214 output tokens, so 1 500 does not starve it. The 2026-10-17 value (94.9 %) came from a CPU-bound run at
5 tok/s with one timeout and is replaced by these numbers.
Verdict: on this bench the 27B is at least as accurate as Bolt (51.3/52 vs 48/52 answers over both budgets) and
needs fewer tokens per answer. Bolt's 2.2x token speed shrinks to about 20 % less wall time because it reasons longer,
and it misread "SWI". No reason to replace the 27B as Clara's default; The model files were deleted on 2026-10-24 (user decision); a new test means downloading the GGUF again and building llama.cpp f64a498 or later.
Side finding: the first rerun attempt died after one answer because the agent loop restarts the model server after
8 h uptime (`MODELL_FRISCH_H`) without checking whether the server is busy for another client; the restart needed
SIGKILL after 60 s. Proposal: skip the fresh start while `/slots` reports `is_processing`.
Results `results_q27_live_mt{1500,4096}.json` (session scratchpad), run 17:21-17:30.

## Trägt
24 GB cards from Ampere on with a llama.cpp from late October 2026; text and tool use at 16k context; tasks where speed
matters more than the last points of accuracy, if the token budget is raised to about 4k.

## Trägt nicht
A fine ranking: 13 tasks x 2 are a coarse filter, the gaps are 1-3 answers out of 26. Contexts above
16k (only 1.9 GB VRAM left with q8 KV), the vision projector (1.73 GB against 1.9 GB left, probably too tight), the DFlash
draft model, and agent work over many turns are all unmeasured. No patient data were involved.

## Bruchindikator
Bolt beats the 27B on a larger or agentic task set, or Bolt fails multi-turn agent tasks (Hermes/OpenCode) that the 27B
solves; then the speed gain does not pay. A llama.cpp update that changes NVFP4 kernels on Ampere: measure again.

## Ablesung
Own runs 2026-10-23 on Alita, script `bolt_test.sh` (server start, template probe, 6.5k prompt, tool call, then
`llm_bench.py --repeats 2`), results `results_bolt_ctx16384_mt1500.json` / `_mt4096.json` (session scratchpad). Tier 1a.
Benchmark of 2026-10-17: [hospital-model-hub-api-aliases-and-small-benchmark](hospital-model-hub-api-aliases-and-small-benchmark.md).
Model card (vendor, Tier 1b): https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
GGUF: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF
llama.cpp: https://github.com/ggml-org/llama.cpp (commit f64a498, 2026-10-23)
