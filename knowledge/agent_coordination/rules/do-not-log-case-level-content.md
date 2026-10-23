---
id: do-not-log-case-level-content
typ: regel
status: vorschlag
thema: agent_coordination
stand: 2026-10-21
herkunft: user instruction 2026-10-21 ("wichtig logs da nicht machen"), own runs 2026-10-21
verweist_auf: [three-data-classes-decide-what-may-leave-the-institution, remote-model-gets-only-data-free-skills-and-redacted-text]
---

# Do not log case-level content

## Aussage
A log is a copy. Write no case-level content into logs, caches or agent session stores - not for class 3, not for class
2, and not into a temporary directory that sits next to the data. Case-level means anything that identifies or
reconstructs an individual record: subject or session ids, file paths, image headers, individual values, names, image
files, unredacted report text.

Rule of thumb: **if it must not be committed, it must not be logged either.** The same content that is too sensitive for
a repository is too sensitive for a text file that happens to be called a log. A log is usually easier to find and
harder to forget than the data itself.

What is allowed and wanted: counts, durations, exit codes, decision outcomes, error classes, aggregate numbers, file
names of *code* (not of data). "23 files processed, 4 skipped, exit 0" is a good log line. "sub-XXXX ses-YY image
malformed" is not.

## Trägt
It settles a whole class of small decisions without a judgement call each time: no debug output on by default, no
"Vorgang gespeichert" file, no keeping last night's output "in case it is useful", no session store collecting the ids
that were inside a prompt. The place for the run's own intermediate state is a temporary directory owned by that run,
deleted when it ends - not a persistent history.

It also protects against the case that is easy to miss: the log of a *program we did not write*. An agent harness, a
service, a scheduler or a database keeps its own history. With Hermes, conversations land in the profile's state
database by design. That is one more reason not to put the content in the prompt or the tool output in the first place -
what never arrives cannot be stored.

Standing check, own runs 2026-10-21: `/tmp` held exactly this kind of leftover from the day's work (image test logs, a
background-visibility probe file, dispatcher output). None of it contained patient data because the work happened on
the Cle side, but a probe file in a working directory is precisely the habit this rule forbids.

## Trägt nicht
It does not forbid logging the *decision*. An audit trail is wanted and, for class 2 and 3, often required: which
dataset, which class, which rule, what was decided, and when - about the data, never from the data. The guard log is
not a violation, it is the point, as long as it records the decision and not the content (no excerpt field, no "logged
value").

It also does not forbid a short-lived in-memory trace while debugging one run, if that run is local and the trace dies
with the process. What it forbids is the persistence: the file that outlives the run, the cache that is still there next
week, the shared directory that someone else can read.

## Bruchindikator
A log, cache or session store contains subject ids, session ids, data or image paths, individual values, image headers
or unredacted report text. A debug output file or probe file is left in a working directory. Intermediate state is put
next to the data instead of in the run's own temporary space. A log line is defended with "it is only the file name" -
file names are case-level content. A tool is used with its default history on a class-2 or class-3 job.

## Ablesung
User instruction, 2026-10-21, verbatim: "wichtig logs da nicht machen". Decided in the same session as the class rule, so
it is written next to it: [three-data-classes-decide-what-may-leave-the-institution](three-data-classes-decide-what-may-leave-the-institution.md).
Content that may not leave the institution at all: [remote-model-gets-only-data-free-skills-and-redacted-text](../../local_llm_operation/rules/remote-model-gets-only-data-free-skills-and-redacted-text.md).
Existing finding that an agent harness keeps its own history: [hermes-keeps-every-conversation-in-state-db](../../local_llm_operation/findings/hermes-keeps-every-conversation-in-state-db.md).
