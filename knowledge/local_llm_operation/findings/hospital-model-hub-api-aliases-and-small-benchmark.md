---
id: hospital-model-hub-api-aliases-and-small-benchmark
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-17
herkunft: API tests and a 13-task benchmark against the hospital's on-premise model hub (Clé), Alita session 2026-10-16/17
verweist_auf: [clara-cle-agents-solve-bounded-code-tasks-slower, remote-model-gets-only-data-free-skills-and-redacted-text]
---

# The hospital model hub API: OpenAI-compatible, five aliases, tool calls work, reasoning needs a large max_tokens

## Aussage
1. The hub exposes an OpenAI-compatible API (`/models`, `/chat/completions`, `/audio/transcriptions`) with a personal
   `sk-` key from the web UI (Settings, Account). It is reached directly inside the intranet; the outbound proxy does not
   know the host. Aliases: `fast` (Qwen 3.8 Flash Next), `frontier` (DeepSeek V4.1 Flash), `eu` (Mistral Small 4),
   `light` (Muse Glimmer 30B), `vision`, `clea` (the hub's own assistant).
2. 13 scored tasks x 2 (neuroimaging MCQs, extraction from a synthetic report, arithmetic, code run against tests, format,
   translation, a fake-paper hallucination probe): clea 100 %, frontier 96 %, fast 92 %, light 92 %, eu 84 %;
   fast 180 tok/s, frontier/clea 85 tok/s. The misses of fast and frontier were EMPTY answers: hidden reasoning used up
   max_tokens 1500; with 6000 they solved them. eu answered "number only" tasks with the full derivation.
3. Tool calling works (`finish_reason: tool_calls`) for fast, frontier and clea, so agent harnesses (Hermes, OpenCode)
   can run on it. Without a system prompt the hub adds ~750 prompt tokens per request; with the agent's own system prompt
   that addition disappeared (306 instead of ~800 prompt tokens).
4. Usage is counted per user per month (reset date shown); a limit is not shown in the UI, the manual or the API headers.
5. Local comparison, same benchmark: Ternary-Bonsai-2-27B (PQ2_0, 6.8 GB, PrismML llama.cpp fork) 92 %, 45 tok/s, tool calls
   work, fits next to other GPU jobs on a 24 GB card. (Qwen3.8-27B Q4 run pending.)

## Trägt
Benchmark script and results 2026-10-16/17 (llm_bench.py, results_cle_20261016.json, results_bonsai.json); tool-call probes.

## Trägt nicht
13 tasks are a coarse filter, not a ranking of close models; the format task was ambiguous ("SWI" read as SWI-Prolog).
Patient data is not allowed on the hub without the data protection officer's approval.

## Bruchindikator
A visible token limit, a changed alias mapping, or tool calls failing on an alias.

## Ablesung
- Ascléa GmbH: Clé Gebrauchsanweisung, Manual_DE_2026-07-09, section 6.4.7 API (internal document)
- own runs 2026-10-16/17
