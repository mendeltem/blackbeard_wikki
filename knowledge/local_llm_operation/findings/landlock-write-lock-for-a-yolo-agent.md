---
id: landlock-write-lock-for-a-yolo-agent
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-21
herkunft: Alita (Ubuntu, kernel 7.0, Landlock ABI 8), own launcher and tests, one real agent run, 2026-10-21
verweist_auf: [local-agent-harness-review-2026-10, hermes-oneshot-ignores-ephemeral-prompt-and-prefill]
---

# A Landlock write lock for an agent that runs without approvals, built without root

## Aussage
A local agent that runs with approvals bypassed (`--yolo`) can be limited to writing in a short list of folders
with Landlock, a Linux security module any process can apply to itself without root. A launcher of about 150
lines of Python (ctypes, no packages) does it in four steps:
1. Create a ruleset that handles only the write rights: write, truncate, create, remove and rename (refer).
2. Add one rule per allowed folder (all write rights beneath it). Add file-only rules (write, truncate) for single
   files and for `/dev` and `/proc`, so `/dev/null`, terminals and GPU device nodes stay writable but nothing can be
   created there.
3. Set `no_new_privs` and call `landlock_restrict_self`.
4. `exec` the agent.

Reading and executing stay allowed everywhere. Every child inherits the lock, and the agent cannot lift it.

Measured on 2026-10-21:
- 20 of 20 checks pass in a throwaway folder. The allowed folder can create, rename and delete. The forbidden
  folder cannot create, overwrite or delete, and `rm -rf` on it removes nothing. Children, including `setsid` ones,
  inherit the lock. Reading works everywhere, and `nvidia-smi` reaches the GPU.
- Real run of the agent (Hermes v0.20.5, local 27B model): writing in the work folder works. The home root and the
  code tree are denied ("Permission denied"). A decoy file outside the list survived `rm -f`. The agent's own
  profile (memory, sessions) stays writable.
- Order matters with a setgid helper. The launcher must run inside `sg <group>`, because `no_new_privs` would
  otherwise stop the group change.
- Pitfall when testing: Hermes gives the agent's shell its own HOME inside the profile, so `~` in a test command
  points into an allowed folder and proves nothing. Use absolute paths.

## Traegt
Accidents by an agent working as the same user: a wrong `rm -rf`, overwriting raw data, editing its own guard
scripts or launcher.

## Traegt nicht
- Anything run by a service outside the process tree is not locked. `systemd-run` without `--scope` escapes; with
  `--scope` the command stays a child and is locked (both measured). A PATH wrapper blocks the escape but can be
  bypassed with the full path. An already running tmux server and other user daemons are not locked either.
- Landlock ABI 8 does not mediate connects to pathname Unix sockets.
- No read restriction: the lock says nothing about which data the agent may read.
- bubblewrap is no alternative on this Ubuntu: `kernel.apparmor_restrict_unprivileged_userns = 1` blocks
  unprivileged user namespaces.

## Bruchindikator
A write outside the list succeeds under the launcher, or a normal job fails because a needed folder is missing from
the list. The launcher warns about missing paths on stderr.

## Ablesung
- Linux kernel documentation, "Landlock: unprivileged access control",
  https://docs.kernel.org/userspace-api/landlock.html (accessed 2026-10-21): ruleset, path-beneath rules,
  `landlock_restrict_self`, `no_new_privs`, inheritance by children, file-only access rights.
- Anthropic Engineering, "Making Claude Code safer with sandboxing" (2025),
  https://www.anthropic.com/engineering/claude-code-sandboxing: filesystem and network isolation together.
- OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency,
  https://genai.owasp.org/llmrisk/llm062025-excessive-agency/: least privilege, enforcement outside the model.
- Own run 2026-10-21: launcher test suite (20 checks), one agent run with absolute paths and a decoy file,
  `systemd-run` with and without `--scope` under the lock.
