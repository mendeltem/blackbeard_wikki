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
