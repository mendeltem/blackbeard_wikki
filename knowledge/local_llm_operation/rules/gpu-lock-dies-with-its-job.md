---
id: gpu-lock-dies-with-its-job
typ: regel
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-20
herkunft: Alita (RTX A5000 24 GB), incident 2026-10-15 to 2026-10-20; tool gpu-sperre built and tested 2026-10-20
verweist_auf: [model-server-start-checks-card-and-picks-profile, foreign-gpu-process-before-measuring, every-agent-crash-becomes-a-lesson]
---

# A GPU lock dies with its job, expires, and an expired idle lock stops blocking

## Aussage
When a language model server and GPU jobs share one card, the lock that keeps the model off the card must
(1) be held by the job itself, (2) carry an expiry, and (3) stop counting once it has expired and no GPU job process has
run for a while. "Is the holder PID alive?" alone is not a lock check.

Incident: a queue held the lock through a separate transient unit running `sleep infinity`. The queue ended after
about 14 h; the unit kept running. Ten tools asked only whether the PID in the lock file was alive, one health check
reported it as intended, and the local agent could not load its model for five days.

Fix on Alita (own run 2026-10-20):
- `gpu-sperre lauf "<what>" --bis 30h [--platz MIB] -- <command>` holds a kernel `flock` on a lock file while the command
  runs. The lock belongs to the open file description, so children that inherit the descriptor keep it and it is
  released when all of them are gone, also after `kill -9` of the wrapper (flock(2)). `--platz` stops the model server
  when the card is too full; the model watchdog brings it back after the job.
- Every lock expires (`--bis`; a legacy lock file 24 h after it was written). An expired lock is ORPHANED when no GPU
  process other than the model server runs now and none was seen for 2 h. Orphaned locks do not block, are reported once
  to the user's phone, and nothing is killed; the status line says how to end the holder (stop the transient unit or
  kill the PID).
- If `nvidia-smi` fails, no lock is ever orphaned. Readers fall back to the old check if the tool fails.
- All readers ask one tool instead of ten copies of the PID logic; legacy writers keep working during the transition.

## Traegt
Single-user workstations where queues, ad-hoc trainings and an agent's model server compete for one GPU. Test script with
a fake `nvidia-smi`: 24 checks (free, held, refused second job, rc passed through, wrapper killed, expired and idle,
GPU job keeps an expired lock, model server is not a job, nvidia-smi failure, legacy holder like the incident, take-over,
`--platz`), all passed 2026-10-20.

## Traegt nicht
- A job that needs the card but sits in a CPU phase for more than 2 h after its own `--bis`: its lock counts as
  orphaned. Give `--bis` generously.
- Jobs that never take the lock: then only free VRAM protects them (see the model-server start rule).
- Several users on one machine: the holder scan reads `/proc/*/fd` of the own user only.

## Bruchindikator
A Telegram report of an orphaned lock while a job was in fact still working, or the model server loading into a running
job (CUDA OOM in the job): then lengthen the idle window or require `--bis` on every GPU job.

## Ablesung
- flock(2), Linux man-pages, https://man7.org/linux/man-pages/man2/flock.2.html (accessed 2026-10-20): locks belong to
  the open file description; duplicates from fork(2)/dup(2) share the lock, released by LOCK_UN or when all duplicate
  descriptors are closed.
- Own incident and fix, Alita 2026-10-15 to 2026-10-20 (lock held 5 days by a `sleep infinity` transient unit; tool
  `gpu-sperre` with test `gpu-sperre-test`, 24/24 checks).
