---
id: rules-that-repeat-become-checks
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-02
herkunft: Claude-Code-Sitzung Alita, error catalogue over all session transcripts and system logs 2026-09 to 2026-11-02 (two read-only agents), 2026-11-01/02
verweist_auf: [no-silent-fallback-values, restart-loop-is-an-alarm-not-a-repair, empty-is-not-missing, tests-prove-claims-not-plumbing]
---

# A written rule that is broken twice becomes a check -- and a watchdog measures progress, not state

## Aussage
A catalogue of 88 incidents from the session transcripts plus the system logs (34 of 429 queue entries failed, 29 stuck
agent jobs, 457 model-server restarts) showed: only 8 of 88 surfaced as a crash; 69 were found by a deliberate check, 11
by the user, many days to weeks late. Eleven kinds of error came back although a written rule against them already existed
(memory note or error book). The five root causes:
1. silent fallbacks and success codes without a result (a "zero candidates" fallback fired in every block for 1.5 days
   because of a wrong path; rc 0 with empty output);
2. acceptance checks that test for files or words, not for plausible content (placeholders, a stand-in model, a metric
   artefact accepted as "a real finding");
3. "waiting" read as "running": dependencies bound to "started" instead of "finished", an idle session holding a queue
   for 10-15 h, a model restore waiting forever for memory;
4. shared resources without one owner (one GPU for training, language model and a small decision model; orphan and
   duplicate processes after an abort);
5. operator habits (a process search that matches its own shell, in-place sed with '#' on scripts), repeated after the rule.

## Traegt
Agent systems that run unattended. Turn each repeated rule into an enforced check within a week:
- enqueue-time smoke test (program exists and is executable, folder exists, Python compiles, module importable, shell
  parses) -- 21 of 34 queue failures had died within 30 s, often after hours of waiting;
- a progress watchdog that compares signals (open queue vs live worker vs CPU time of the job tree vs GPU load vs log
  growth) and alarms by message, not by a status line;
- a fallback counter: the same fallback in at least half of a driver's blocks is a bug, not data;
- plausibility in acceptance (threshold at the grid edge, sensitivity near 1 with high F1, F1 far above any own model);
- restart back-off with an alarm;
- a pre-command hook for the assistant's own habits.
Log every new error the same day (what, cause, how found, fix).

## Traegt nicht
Judgement errors (wrong scientific choice, wrong question); those need review, not a check. A check that raises false
alarms trains people to ignore it -- test each one on known good and known bad cases before enabling it.

## Bruchindikator
After the checks are live, a repeat of one of the five causes slips through unnoticed for more than a day.

## Ablesung
Own catalogue 2026-11-01/02 (aggregates only, no case identifiers). Implemented 2026-11-02 on Alita: grossauftrag
--einreihen smoke test, fortschrittswache (systemd timer, 15 min), spec_check plausibility block, wache back-off (3 starts
in 2 h, then 2 h pause and one alarm), hub retries on 502/503/504, Claude Code PreToolUse hook. Tier 2 (one system).

## Verknuepft
- [no-silent-fallback-values](no-silent-fallback-values.md)
- [restart-loop-is-an-alarm-not-a-repair](restart-loop-is-an-alarm-not-a-repair.md)
- [empty-is-not-missing](empty-is-not-missing.md)
- [tests-prove-claims-not-plumbing](tests-prove-claims-not-plumbing.md)
