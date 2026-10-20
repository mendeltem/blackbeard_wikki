---
id: hermes-keeps-every-conversation-in-state-db
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-20
herkunft: Alita, source reading of Hermes Agent v0.20.5 (2026.8.19) and the local launch chain, 2026-10-20; user question about a private mode for the local agent
verweist_auf: [pre-tool-hook-blocks-data-paths-for-remote-model, remote-model-gets-only-data-free-skills-and-redacted-text, hermes-agent-local-qwen-benchmark]
---

# Hermes keeps every conversation in its profile database; a no-record session needs a throwaway profile home

## Aussage
Hermes Agent writes every message of a session to SQLite `$HERMES_HOME/state.db` (`_persist_session` in
`run_agent.py`, called on every exit path "so conversations are never lost"). Per-session JSON snapshots exist too, but
only when `sessions.write_json_snapshots` is on (default off). No CLI flag turns the session store off: `--safe-mode`
and `--ignore-rules` drop user config, memory injection, plugins and MCP servers, not persistence; `--source tool` only
hides sessions from the session lists.

Around a local agent there are usually more recorders than the database. On Alita:
- the session database and the Hermes logs and readline history (`.hermes_history`) in the profile;
- a terminal recording of the tmux wrapper (`pipe-pane`) in the profile;
- the outbound guard's log, holding up to 2000 characters of each text that was checked before leaving the machine;
- not the model server: llama-server does not log prompt text at default verbosity and saves KV slots only on an
  explicit request.

A session without a record therefore needs a throwaway `HERMES_HOME`: a fresh folder in RAM (`/dev/shm`, mode 700)
holding copies of config, rules (SOUL.md), memory and skills, deleted on exit. Start it through the normal launcher so
the protection layers (guard, network block, PATH wrappers) stay, and without the terminal recording. The launcher must
accept a home override, because it hard-codes the profile path.

## Traegt
A local model on the same machine. What the agent learns in such a session (memory, skills) is thrown away with the
folder; files it writes with its tools stay where it wrote them.

## Traegt nicht
- A hosted model profile: the provider's server logs are out of reach.
- The outbound guard log: keep it, it is the record of what left the machine.
- RAM is not a guarantee: pages can be swapped to disk.
- Not built yet: Claude Code's auto-mode classifier refused the one-line launcher change as "Logging/Audit Tampering";
  it needs an explicit decision by the user.

## Bruchindikator
After a private session, files under the real profile (state.db, logs, sessions) changed during its run, or the
throwaway folder is still in `/dev/shm` after exit.

## Ablesung
- Nous Research, Hermes Agent, https://github.com/NousResearch/hermes-agent (MIT; accessed 2026-10-20): the README
  describes FTS5 session search over past conversations and names no option to disable persistence.
- Own reading 2026-10-20 of the installed v0.20.5: `run_agent.py` `_persist_session` and `_save_session_log`
  (`sessions.write_json_snapshots`, default False), `hermes chat --help` (no persistence flag), `hermes_constants.py`
  (`HERMES_HOME` override).
