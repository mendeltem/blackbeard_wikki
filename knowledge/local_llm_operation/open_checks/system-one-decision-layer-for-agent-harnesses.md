---
id: system-one-decision-layer-for-agent-harnesses
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-19
herkunft: Alita, web research 2026-10-19 (sources opened and checked one by one, see Ablesung); own routing measurement 2026-10-08
verweist_auf: [decision-model-as-profile-orchestrator, laya-router-before-agent, lean-hermes-toolsets]
---

# A "System One" decision layer in the agent harness: four decisions, local model only, measure on own cases first

## Aussage
"System One" models (TypeSafe's Jev and its open clones) answer typed questions (Choice, Score, yes/no) with a
probability in 30-500 ms instead of generating text. Inside an agent harness they fit four decision points:
(1) which model handles the turn, (2) which prepared context (profile, skill set, saved prefix slot) it starts from,
(3) whether a tool call runs without asking, (4) whether a result passes (task done, source supports the claim).
Not to be confused with JEPA (LeCun's joint-embedding world models: V-JEPA 2.1, VL-JEPA, LeWorldModel): no JEPA model
was found that makes harness decisions.

State 2026-10-19 (foreign numbers unless marked):

| model | open | evidence | use here |
|---|---|---|---|
| Jev (TypeSafe) | no, hosted API only | JevBench reference 71.5; vendor's own workflow evals 67.8 % vs 74.1 % of a frontier model | only for text without data |
| H2O-Lightning-4B (h2oai, Qwen3.5-4B) | Apache-2.0, GGUF | model card: JevBench v1.1 composite 72.5 (> Jev 71.5), ECE 0.017, 29 ms p50 | strongest local candidate |
| decider-4b v2.1 (Mapika) | Apache-2.0, GGUF | own run 2026-10-08: 50/60 vs kNN 49/60, 21/21 at p >= 0.8 | already on Alita |
| Kev-4B | Apache-2.0 | JevBench rank 37, but ties decider-4b on an independent 11-task panel (coverage at 5 % error 0.555 vs 0.556) | comparison candidate |

The leaderboard does not transfer: on the independent panel a raw Qwen3-4B with ~72 % accuracy reaches only 0.091
coverage at 5 % error, because its confidence does not separate right from wrong answers.

## Traegt
- Harness: Hermes. Version 0.20.5 already has `approvals.mode: smart` with an auxiliary approval model; most
  ready-made System One plugins target Hermes (approvals, routing, skill choice). OpenCode and Claude Code work through
  plugins / PreToolUse and Stop hooks.
- Fixed rules before the model: anything that touches patient data goes to the local model, never decided by the
  classifier; a deterministic deny list (cohort guard) runs before any learned approval gate; unclear cases escalate
  to the human. A reviewed gate is safer than blanket allowlist entries for whole command classes.
- A hosted System One model sees the state it judges: data-free text only. Local clones speak the same wire format
  (`POST /v1/systemone`), so plugins switch by base URL.
- Order: local service (decider-4b, H2O-Lightning-4B) -> own test set (routing cases, real approval requests from the
  harness logs, acceptance checks) scored as coverage at 5 % error against embedding kNN -> one week shadow mode
  (decide and log, do not act) -> live with threshold p >= 0.8, below that unchanged.

## Traegt nicht
- Taking a leaderboard rank as the choice: rank depends on the board and its weighting of speed and cost.
- The Hermes approval plugin with a plain-HTTP local server: it accepts custom endpoints only as HTTPS on the default
  port (needs a local TLS proxy or a patch). The Hermes routing plugin talks to TypeSafe only (needs a base-URL patch).
- llama.cpp builds without the `/v1/systemone` route (proposed in llama.cpp PR #30361); decider runs through its own
  Python wrapper meanwhile.

## Bruchindikator
On the own test set the local model does not beat embedding kNN in coverage at 5 % error, or shadow mode shows
confident wrong approvals: then keep kNN routing and human approvals.

## Nachtrag 2026-10-19 evening: own measurement on Alita (CPU, 8 threads)
Local service for both models in the `/v1/systemone` format, measured on own cases against bge-m3 kNN
(leave-one-out, k = 5). Own run 2026-10-19; the cases stay private (real commands with paths).

| family | method | accuracy | coverage at 5 % error | p >= 0.8: cases / errors | approval-needed caught | confident wrong "auto" |
|---|---|---|---|---|---|---|
| routing, 60 requests, 3 targets | kNN | 0.80 | 0.13 | 29 / 2 | - | - |
| | decider-4b v2.1 Q4_K_M | 0.83 | 0.62 | 23 / 0 | - | - |
| | H2O-Lightning-4B Q8_0 | 0.88 | 0.80 | 31 / 0 | - | - |
| approval, 154 real shell commands, 36 need approval | kNN | 0.82 | 0.00 | 130 / 17 | 11 of 36 | 16 |
| | decider-4b | 0.92 | 0.94 | 113 / 3 | 26 of 36 | 1 |
| | H2O-Lightning-4B | 0.92 | 0.91 | 93 / 2 | 25 of 36 | 0 |

- Both models beat kNN mainly in confidence, not in accuracy: kNN is confidently wrong (16 confident "auto" on
  commands that need approval), the models put almost all their misses below p = 0.8. Approval vs kNN: McNemar
  p = 0.004 (decider) and 0.006 (H2O); routing differences are not significant (n = 60).
- A gate "auto only at p >= 0.8, otherwise ask" would have let through 1 (decider, a borderline delete) and 0 (H2O)
  of the 36 approval-needed commands, while deciding 73 % / 60 % of all commands without a human.
- Misses cluster on commands that act on a remote host over ssh and on edits of another agent's configuration: such
  classes belong in the fixed rule layer before the model.
- Labels: one labeller (the agent) with a rubric written before any model ran; no second rater yet.
- Practical: the H2O stock GGUF needs a llama.cpp build from October 2026 (older builds stop at the missing
  next-token-prediction layer `blk.32`); the readout through llama-server `/completion` with an equal logit bias on
  the labels reproduced the vendor card example (0.9654 vs 0.9657). The vendor's yes/no floor (0.801) must be off for
  thresholding: with it every yes/no answer reports at least 0.801. CPU latency median 1.3-4.6 s (decider) and
  3.9-9.5 s (H2O) per decision: a live gate needs the GPU.

## Ablesung
Web research 2026-10-19, each source opened:
- TypeSafe AI, Jev product page, https://typesafe.ai/ (accessed 2026-10-19): Jev as "System One Model" for automation,
  thresholds for autonomous action vs review, 42 USD per billion input tokens; no JEPA.
- width.ai, "What Is Jev AI? TypeSafe's System One Model, and Where It Fits in an Agent Harness",
  https://www.width.ai/post/what-is-jev-ai-typesafe : routing, context selection, tool approval, scoring; all speed and
  cost numbers vendor-reported; nine documented failure modes ("context rot").
- awesome-jev-tools, https://github.com/v-modal/awesome-jev-tools : curated list (>100 tools) of harness plugins for
  routing, approvals, compaction, evaluation, and local replacements.
- anpicasso/hermes-jev-approvals (MIT), https://github.com/anpicasso/hermes-jev-approvals : replaces the Hermes smart
  approval reviewer; six typed questions, fixed rule chain, self-reported 4.4x fewer prompts on 153 commands.
- punkcanyang/hermes-jev-router (MIT), https://github.com/punkcanyang/hermes-jev-router : per-turn tier routing plus
  trim-then-compress; no published measurements.
- ReallyArtificial/stuntdouble (MIT), https://github.com/ReallyArtificial/stuntdouble : shadow proxy that runs local
  doubles (Kev, Laya) beside Jev and logs agreement (against Jev, not ground truth).
- h2oai/h2o-lightning-4b model card, https://huggingface.co/h2oai/h2o-lightning-4b : JevBench 72.5 vs 71.5, ECE 0.017,
  `/v1/systemone` via vLLM or llama-server GGUF.
- Anyesh, "The open Jev clones: three ways to read a decision, and a leaderboard that does not transfer", DEV Community,
  https://dev.to/anyesh/the-open-jev-clones-three-ways-to-read-a-decision-and-a-leaderboard-that-does-not-transfer-4aea :
  pointer head (Kev), mask-marker encoder (Laya), first-token logits; 11-task panel numbers above.
- Barbosa JAS, 2026, "Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System
  One Decision Layers", arXiv:2609.28940 : position paper, four decision points, one case study without significance.
- unverified: JevBench leaderboard https://benchmarkheaven.com/jev-models (page too large to load; reportedly
  Quyet-1.0-Large leads on another score); JEPA timeline (V-JEPA 2.1 March 2026, AMI Labs) only from secondary
  coverage, https://startuphub.ai/ai-news/ai-figures/2026/figure-yann-lecun-jepa-release-cadence-2026-08-20 .
Own: decider-4b v2.1 Q4_K_M on 60 routing cases, 2026-10-08 (see decision-model-as-profile-orchestrator).
