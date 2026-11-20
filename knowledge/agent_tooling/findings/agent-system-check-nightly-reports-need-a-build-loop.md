---
id: agent-system-check-nightly-reports-need-a-build-loop
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-20
herkunft: own check and repair of a local agent system (chat agent, relay, exit guard, memory job, watchers) on one workstation, 2026-11-20
verweist_auf: []
---

# A nightly error report does not repair anything: known faults stayed open for 8 days; a memory rewrite must be measured by what it keeps

## Aussage
1. A full check of a running agent system (own run, 2026-11-20) found seven faults that the nightly reports had named for up to 8 days. Nobody built the fixes, because the report ended in proposals and no step turned a repeated proposal into a decision.
2. The watcher itself was partly blind: it read a log path that did not exist and skipped the log of the memory job. Its failure count swung without meaning (0 to 166 per night). A watcher has to be tested against the log it claims to read: the path exists and its last line is younger than a day.
3. A fixed model alias in one tool broke when the model hub dropped the alias; a second tool that asked the hub for its model list kept working. One place should resolve model names, and every caller uses it.
4. A timer that stops a model server must look at the server's slots first. Here an approval timer killed the server in the middle of an answer ten times in seven days. Waiting while a slot computes, with an upper limit (30 min), removed the kills in the stand-in test.
5. Rewriting a long memory page in one model call fails once the page is at its length limit: every draft comes back too long and is rejected, and the job repeats this every hour. Updating one section per call works (450-line page, 36 new entries: 7 calls, about 16 min on a local 27B model).
6. The section-wise rewrite brought a new risk that the format check does not see: a section draft can drop most of the old source pointers (one section lost 59 of 74, twice in a row). A loss guard fixed it: a draft that drops more than half of the old pointers is asked once more, then the old section stays. With the guard, 96 of 96 old pointers were kept.
7. A job whose draft was rejected should not retry with the same input. Skipping a page until new input or a code change arrives, and one alarm after three nights without progress, stops the silent hourly GPU use.
8. A service restart loop without a start check can run for hours (222 failed starts in 2 h, one every 30 s, because the GPU memory was taken). A check of free GPU memory and of the port before the start, growing waits between tries, a SIGTERM handler and a short stop timeout are the repair.
9. A test that counts a run with only empty answers as a result hides an outage. Such a run is "invalid", not "0 of n".

## Trägt
Own run 2026-11-20 on one workstation: logs of 7 to 30 days, unit states, test runs of each fix (stand-in tests, one real run of the memory rewrite on a copy of the largest page). Software: [systemd 255](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html) (`KillMode=mixed`, `TimeoutStopSec`, `RestartSteps`, `RestartMaxDelaySec`), [logrotate 3.21.0](https://github.com/logrotate/logrotate) (`copytruncate` for logs held open by a server), [llama.cpp server](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) (`/slots`, field `is_processing`; build of the workstation, commit 7584430). The links were not opened again for this entry: unverified.

## Trägt nicht
One system, one day. The fixes were tested with stand-ins and one real run each, not over weeks. The numbers for the memory rewrite come from one page and one batch; other pages and models can lose more or less. No comparison with other ways to shorten a page (for example a summary of the oldest part only).

## Bruchindikator
A fault appears in three nightly reports in a row again; the section-wise rewrite loses pointers although the guard is on; the restart loop returns although the start check is in place.

## Ablesung
After two nightly reports with the same fault: decide (build, or write down why not now). Test every watcher against its log. Measure every automatic rewrite of a memory page by the pointers it keeps, per section. Give every start path a check and a timeout, and every model stop a look at the slots.
