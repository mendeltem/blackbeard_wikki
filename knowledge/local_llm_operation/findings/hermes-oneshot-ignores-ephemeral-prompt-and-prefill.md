---
id: hermes-oneshot-ignores-ephemeral-prompt-and-prefill
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-21
herkunft: Alita, installed Hermes Agent v0.20.5 (local commit f0daf560), recording stub server, 2026-10-21
verweist_auf: [hermes-keeps-every-conversation-in-state-db, lean-hermes-toolsets]
---

# Hermes one-shot mode (-z) drops the ephemeral system prompt and the prefill messages

## Aussage
"Prefill" means three different things around a local agent, and only one of them is a file you configure:
1. **Hermes prefill messages** (`prefill_messages_file` or `HERMES_PREFILL_MESSAGES_FILE`): a JSON list of
   `{role, content}` turns. Hermes inserts them on every API call right after the system prompt and before the real
   history, and never saves them to the session, logs or trajectories. Use: few-shot examples ("answer like this").
2. **Prompt processing** in llama.cpp: before the first output token the server computes the KV cache for every new
   input token. A prefix identical to the last request is not computed again, and `--slot-save-path` stores a slot's
   cache as a file. Own log, 479 requests with more than 2000 new tokens: median 747 tokens/s on an RTX A5000 with a
   27B Q4 model, so an 8.6k-token prefix costs about 12 s.
3. **Thinking-only continuation**: when a reasoning model returns only thinking and no answer, Hermes puts that turn
   back as an assistant message and lets the model continue (at most 2 times).

Measured with a stub OpenAI server that records every request, both markers set through environment variables:
- `hermes -z "..."` (one-shot): neither the `HERMES_EPHEMERAL_SYSTEM_PROMPT` text nor the prefill turns reach the
  model. `hermes_cli/oneshot.py` passes only the preloaded skills (`-s/--skills`) as the ephemeral prompt and loads no
  prefill file.
- `hermes chat -q "..."`: both arrive. The ephemeral text sits at the very end of the system message, after the
  volatile tail (skills index, memory, "Conversation started: <date>"). The prefill turns come right after the system
  message.

A theme brief handed over through `HERMES_EPHEMERAL_SYSTEM_PROMPT` therefore never reached a one-shot agent. The
three per-theme KV-cache files warmed in one-shot mode in September 2026 contain the Hermes core and that day's date,
and no brief text (token lists read from the slot files and detokenised).

## Traegt
- One-shot workers (cron jobs, drivers, warm-up calls) on Hermes v0.20.5: context that must reach them goes in with
  `-s <skill>` (preloaded skill) or at the start of the task text.
- Interactive and gateway sessions: the ephemeral prompt and prefill turns work, but behind the date line. A cached
  prefix that includes them matches only on the same day with an unchanged memory and skills index.

## Traegt nicht
- Other Hermes versions: the one-shot path may change. Check again with the stub after an update.
- Whether `--cache-reuse` (KV shifting of matching chunks) still reuses the brief after the date changed was not
  measured.
- Whether the September core prefix still matches today's Hermes core was not checked.

## Bruchindikator
The stub shows the ephemeral marker in a `-z` request, or a slot file warmed in one-shot mode contains the brief.

## Ablesung
- Nous Research, Hermes Agent, https://github.com/NousResearch/hermes-agent (MIT; accessed 2026-10-21). Own reading
  of the installed v0.20.5: `hermes_cli/oneshot.py` (`ephemeral_system_prompt=skills_prompt`), `cli.py`
  (`HERMES_EPHEMERAL_SYSTEM_PROMPT`, `_load_prefill_messages`), `agent/conversation_loop.py` (prefill insert after the
  system message, ephemeral appended to it), `agent/system_prompt.py` (stable, context, volatile order),
  `hermes_cli/config_defaults.py` (`prefill_messages_file`: "never saved to sessions, logs, or trajectories").
- llama.cpp server, https://github.com/ggml-org/llama.cpp/tree/master/tools/server (MIT; accessed 2026-10-21):
  `--slot-save-path`, `POST /slots/{id}?action=save|restore`, `--cache-reuse`.
- Own run 2026-10-21: stub server probe (`-z` vs `chat -q`), detokenised slot files, prompt-eval timings from the
  server log.
