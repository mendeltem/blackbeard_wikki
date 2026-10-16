---
id: clara-cle-agents-solve-bounded-code-tasks-slower
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-17
herkunft: Agent benchmark on Alita 2026-10-16/17: four tasks from the same day's work (bug fix with test, feature with tests, code review, wiki entry with sources), Claude Code vs Hermes and OpenCode on an institutional model hub (Clé, model clea), fresh clone at the commit before each fix, 45 min limit, hidden checks
verweist_auf: [remote-model-gets-only-data-free-skills-and-redacted-text, release-test-means-fresh-machine-with-release-assets]
---

# Agents on the institutional model hub solve bounded code tasks correctly, 6-18 times slower; long reviews time out

## Aussage
1. Bug fix with a test that fails on the old code, feature change with tests, and a wiki entry with correct DOIs:
   all three agents passed every hidden check (README-style test, five seeds of the held-out behaviour, full test
   suite, wiki maintenance check, both DOIs right).
2. Time per task: Claude Code 1.3-9.4 min; OpenCode + hub 1.4-18.7 min; Hermes + hub 2.0-38.6 min (bug fix 2.0 vs 18.7
   vs 38.6 min). Hermes needed 92 model calls for the bug fix; every call resends 22-80k tokens of prompt and history.
3. Open-ended code review (find real bugs, reproduce them): Claude Code found both planted bugs plus six further real
   ones, all reproduced; OpenCode + hub found both plus one documentation bug; Hermes + hub ran out of time (45 min)
   without a report.
4. Harness facts that change results: OpenCode `run` auto-rejects commands outside its folder unless
   `OPENCODE_PERMISSION` grants `external_directory`; a data-guard plugin that masks image file names also slows an agent
   on synthetic data; a scorer that runs training in the repository can itself break a test (writes into examples/).

## Trägt
Same prompts, fresh sessions, identical starting commits, hidden checks added only after the runs; cost of the Claude
Code runs 3.4 USD in total, hub runs without charge.

## Trägt nicht
One run per agent and task, one model on the hub (clea), German prompts, a single repository; no long multi-system
tasks (data, cluster, GPU) and no image judgement were tested.

## Bruchindikator
A repeat with three runs per cell where the hub agents miss hidden checks, or where Hermes finishes the review in time
with a larger context setting.

## Ablesung
Hermes agent (Nous Research): https://github.com/NousResearch/hermes-agent; OpenCode 1.18.35: https://opencode.ai/docs/;
model hub benchmark of the same night (context up to 359k tokens, 104-340 tokens/s): local llm_api bench, 2026-10-16.
Own runs 2026-10-16/17 (prompts, scorer and scores kept with the benchmark).
