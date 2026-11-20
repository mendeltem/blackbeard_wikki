---
id: log-without-text-is-a-claim-to-measure-daily-counts-instead-of-a-new-log
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-20
herkunft: own count-only scan of four decision logs of a local agent system (router, approval gate, exit guard) and the build of a daily summary from them, 2026-11-20
verweist_auf: [agent-system-check-nightly-reports-need-a-build-loop]
---

# "This log holds no text" is a claim to measure; a daily note with counts replaces a new shared log

## Aussage
1. A code comment said the routing log holds "no message text". A scan that printed counts only showed otherwise: the field with the routing reasons carried file names and folder names in about 1 line in 10, and id-like strings in a few dozen lines. The reasons were built from what the router had matched, so the matched text went into the log with them.
2. Each of the four decision logs held free text of some kind: reasons with file names (router), the task text (older router log), shell commands (approval gate), the full question (exit guard). None held a key or a password.
3. A pattern hit is a lead, not a finding. The first pass reported 55 "API keys" in one log. They were web addresses with a company name that begins like a common key prefix; none matched a secret on the machine. About a quarter of the id-like hits were invented ids from the system's own leak tests.
4. The wish was a log that every part of the system may read. A new log was not needed: a script reads the existing logs once a day and writes one short note with counts for the last 24 hours and 7 days (rounds per model and place, reasons by class, verdicts, sent or blocked, seconds per round). The agent sees the note in its local recall; the logs stay private.
5. What keeps text out of the note: only category fields are counted; a free-text reason is counted by the fixed phrase it starts with and the rest is never used; a caller label is cut at the first separator and must be a plain short word, else it counts as "other"; the finished note is checked for cohort names, case ids and paths, and on a hit nothing is written (the same when the check cannot load its word list).
6. The first note showed three things nobody had looked for: one routing signal had not arrived on any of about 2300 rounds in 7 days, one gate had not received a request for 10 days, and the quality judgements were mostly "unsure" or "no". A daily count per component shows a silent part; a log that nobody reads does not.

## Trägt
Own run 2026-11-20 on one workstation: four JSON-lines logs with about 42,000, 3300, 300 and 5200 lines; scan with regular expressions per field, output counts and field names only; summary script with 21 checks on invented logs (counts, time windows, reason classes, no free text in the note, nothing written when an id-like label appears). Python 3.12 standard library only ([json](https://docs.python.org/3/library/json.html), [re](https://docs.python.org/3/library/re.html)); timer with [systemd 255](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html). The links were not opened again for this entry: unverified.

## Trägt nicht
A pattern search finds ids and names only in the shapes it knows; a free-text name without a known shape is not found, so "no person name found" is weaker than "none there". Whether the task texts hold result numbers was not checked. The summary is one day old: whether its counts are read and acted on is not shown. The check of the finished note depends on a word list of cohort names that has to be kept current.

## Bruchindikator
The note is written with a file name, an id or a cohort name in it; a count in the note differs from a hand count of the log for the same window; a component stays at zero for a week and nobody notices.

## Ablesung
Before calling a log free of text: count pattern hits per field and look at what kind of string matched. Before building a new shared log: check whether a daily count from the logs that exist answers the question. Count free text by a fixed prefix or a closed list of classes, and let the writer refuse when its own output fails the privacy check.
