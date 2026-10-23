---
id: tmp-is-not-volatile-and-session-stores-persist
typ: befund
status: getragen
thema: agent_coordination
stand: 2026-10-21
herkunft: own runs 2026-10-21 (cleanup of /tmp scratch and Claude Code session stores on Alita)
---

# /tmp is not volatile on Alita, and agent session stores persist there

## What was found

On Alita, `/tmp` lives on the root filesystem, not on a RAM-backed `tmpfs`:

- `findmnt /tmp` resolves to `/dev/nvme0n1p2`, filesystem `ext4` (the same root partition).
- `systemctl is-enabled tmp.mount` reports `not-found`.
- Claude Code writes its session state under `/tmp/claude-1000/` and no `TMPDIR` is set for it in
  `~/.claude/settings.json`, `~/.bashrc` or `~/.profile`.

Consequence: everything an agent or a script leaves in `/tmp` survives reboots and shutdowns. It does not age out
on its own. The directory is, in practice, a durable store on a disk that also holds other people's data.

## Why it matters

1. **"It is only in /tmp" is not a containment argument.** A path under `/tmp` is not more ephemeral than a path under
   the home directory; both are the same disk. An argument that says "this copy is harmless because /tmp is cleared"
   is false here.
2. **Agent session stores grow without bound.** The Claude Code store on Alita held ~13 GB in ~59,000 files at the
   time of this check, across many session directories. Most of it was from closed sessions. This is scratch, not
   deliberate logging, but it is the same class of material a log rule is meant to bound.
3. **Cleanup is unsafe while agents run.** At check time 8 `claude` processes and 2 guard daemons were active, and
   `lsof` showed five session directories held open, one being tailed live. Deleting those would have destroyed work
   in progress.

It does not follow that the store is a leak. It follows that its lifetime is not what the name suggests, so it must be
handled deliberately rather than ignored.

## How to check (repeatable)

```
findmnt -no SOURCE,FSTYPE,OPTIONS /tmp     # tmpfs here means volatile; ext4 does not
systemctl is-enabled tmp.mount             # not-found = no systemd-managed tmpfs
df -h /tmp                                 # confirm it is the root filesystem
lsof +D /tmp/claude-1000                   # which session dirs are in use right now
pgrep -au $USER -f claude                  # is a session running at all
du -sh /tmp/claude-1000                    # size of the store
```

## Cleanup recipe (only when no agent session is running)

1. Confirm no session is active: `pgrep -au $USER -f claude` is empty and `lsof +D /tmp/claude-1000` is empty.
2. Delete only directories belonging to closed sessions; never remove a directory that `lsof` lists.
3. Better than deleting: give the tool its own temporary directory, so the store disappears with the process -
   e.g. `TMPDIR="$(mktemp -d /tmp/agent.XXXX)"` exported before the tool starts, removed afterwards. Setting `TMPDIR`
   to a directory on a real `tmpfs` (`/run/user/$UID` is RAM-backed and per-user) achieves the same for scratch.
4. Do not log what was deleted beyond counts and total size. File names and contents stay out of logs (see
   `rules/do-not-log-case-level-content.md`).

## Cost of being wrong

- Ignoring it: the store keeps growing on the root disk and old session scratch stays readable indefinitely.
- Cleaning too eagerly: work in progress is destroyed and a running agent fails for no reason - the reason to check
  `lsof` first.

Befolgen (clean up deliberately, or redirect `TMPDIR`) costs a few minutes. Ignoring it risks both a full root disk and
a long-lived copy of session material nobody chose to keep.

## Open point

Whether the session store ever held case-level content was not inspected and must not be inspected from this profile:
the guard refuses to read it. That question belongs to the local profile and to a session that is not running.
