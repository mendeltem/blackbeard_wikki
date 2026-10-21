---
id: local-agent-harness-review-2026-10
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-21
herkunft: Alita, review of the running Hermes setup against published practice; own log counts 2026-10-21
verweist_auf: [hermes-oneshot-ignores-ephemeral-prompt-and-prefill, system-one-decision-layer-for-agent-harnesses]
---

# Review of the local agent harness: sandbox and critic matter more than caching

## Aussage
A local agent (27B hybrid model on one llama-server slot) works a job queue with a driver loop, a same-model critic
and an acceptance checklist; it runs with approvals bypassed, behind a loopback-only network rule. A Telegram agent
uses LLM-judged approvals, with a 4B classifier in shadow mode. Compared with published practice, ranked by risk:

1. **No filesystem sandbox while approvals are bypassed.** The network is locked, the filesystem is not. Hermes'
   hard floor only blocks damage rooted at `/`, raw disks and shutdown, so `rm -rf` of a data folder in the home
   directory passes. OWASP LLM06 and Anthropic's sandboxing post both ask for filesystem and network isolation
   together. Landlock (kernel ABI 8 here) restricts writes without root; bubblewrap fails on this Ubuntu because
   unprivileged user namespaces are restricted by AppArmor; Hermes also has a Docker terminal backend.
2. **The critic is the same model.** Without external feedback, self-correction does not reliably help and can hurt
   (Huang 2024, Kamoi 2024); models evaluate their own output too kindly (Panickssery 2024); models of 13B or less
   need a strong verifier (Zhang 2024). Own log: of 106 finished jobs, 6 ended after round 1, and 30 (28 %) used all
   4 rounds with the critic still reporting serious findings, yet passed the checklist. Critic and checklist disagree.
   Better: checks that can fail (run the script, count the files, compare the numbers), agreed before the work
   starts, or a judge from another model family.
3. **Approval classifier.** Rules first, classifier only for the rest, never auto-deny: this matches Anthropic's auto
   mode design, where even the large classifier missed 17 % of 52 real overeager actions. A 4B model should stay in
   shadow until its misses on the own log are counted.
4. **Caching is mostly fine.** Of the last 2601 requests with more than 8k tokens in the slot, 89 % reused the prefix
   and 4 % were computed cold (median 35 s each). `--cache-reuse` is disabled by the server for this hybrid model on
   every load. The host-memory prompt cache (`--cache-ram`, default 8 GiB) is on and full; with one slot it saves
   and loads only when less than half of the slot is kept (`--slot-prompt-similarity` path), see open PR #22083.

## Traegt
One GPU workstation, one llama-server slot, one hybrid 27B model, Hermes v0.20.5, job queue with critic rounds.

## Traegt nicht
- The critic numbers come from 108 driver logs up to 2026-08-28 (half of the finished jobs have no log); they show
  disagreement, not which side is right.
- The 17 % miss rate is Anthropic's figure for their classifier, not a measurement of the 4B model.

## Bruchindikator
A job that the critic passes in round 1 fails a real executable check, or a sandboxed run breaks a job that needs
to write outside the allowed folders.

## Ablesung
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", ICLR 2024, arXiv:2310.01798: without
  external feedback, accuracy fell after self-correction (GPT-4 on GSM8K 95.5 to 89.0 over two rounds).
- Kamoi et al., "When Can LLMs Actually Correct Their Own Mistakes?", TACL 2024, arXiv:2406.01297: self-correction
  works with reliable external feedback or fine-tuning, not with prompted self-feedback in general.
- Panickssery, Bowman, Feng, "LLM Evaluators Recognize and Favor Their Own Generations", NeurIPS 2024,
  arXiv:2404.13076: self-recognition correlates linearly with self-preference.
- Zhang et al., "Small Language Models Need Strong Verifiers to Self-Correct Reasoning", Findings of ACL 2024,
  arXiv:2404.17140: small models gain only with a strong verifier.
- Gou et al., "CRITIC", ICLR 2024, arXiv:2305.11738: tool-interactive critique beats critique without tools.
- Anthropic Engineering, "Making Claude Code safer with sandboxing" (2025),
  https://www.anthropic.com/engineering/claude-code-sandboxing: filesystem plus network isolation, 84 % fewer
  permission prompts (internal figure).
- Anthropic Engineering, "How we built Claude Code auto mode" (2026),
  https://www.anthropic.com/engineering/claude-code-auto-mode: rules first, two-stage classifier, 0.4 % false
  positives, 17 % misses on 52 real overeager actions.
- OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency,
  https://genai.owasp.org/llmrisk/llm062025-excessive-agency/: least privilege, authorisation outside the LLM.
- Anthropic, "Effective harnesses for long-running agents" (2025),
  https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, and "Harness design for
  long-running apps" (2026), https://www.anthropic.com/research/harness-design-long-running-apps: progress file,
  one task at a time, done only after end-to-end tests, a separate skeptical evaluator tuned by reading its logs,
  remove one harness component at a time to test it.
- Manus, "Context Engineering for AI Agents" (2025),
  https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus, and Anthropic prompt caching
  docs, https://platform.claude.com/docs/en/build-with-claude/prompt-caching: static first, timestamps last.
- llama.cpp PR #16391 "server : host-memory prompt caching" (merged 2025-10-09), PR #9866 "server : reuse context
  chunks" (merged 2024-10-13), PR #22083 (open): https://github.com/ggml-org/llama.cpp. Own source reading
  `tools/server/server-context.cpp` (save to RAM only if f_keep < 0.5 on the similarity path).
- Own run 2026-10-21: server log (cache_reuse disabled message on each load, prompt-eval counts), driver logs,
  Landlock ABI query, `kernel.apparmor_restrict_unprivileged_userns = 1`.
