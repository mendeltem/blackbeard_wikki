---
id: remote-model-gets-only-data-free-skills-and-redacted-text
typ: regel
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-16
herkunft: Alita 2026-10-16: agent skills shared between Claude Code, Hermes (Clara) and OpenCode; Clé (institutional model hub) as fallback for the morning report while the GPU runs a cohort job
verweist_auf: [readme-for-a-research-package, dataset-handover-one-folder-per-case-no-copies]
---

# A remote model gets only data-free skills and redacted text

## Aussage
1. Shared skills folder split by data: `~/.agents/skills/` holds only skills that touch no patient data (wiki update,
   install check); skills that move or show patient data (data-drive storage, data-set handover, QC pages) live only
   where a vetted agent reads them (`~/.claude/skills/`).
2. Agents read more folders than their own: OpenCode loads `~/.agents/skills/` AND the Claude Code folder
   `~/.claude/skills/`. With a remote model it must start with `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1`; check the
   visible set with `opencode debug skill`, not by asking the model (that request timed out after 5 min). Hermes takes
   extra folders via `skills.external_dirs` in the profile's `config.yaml` and follows symlinks.
3. Unattended jobs that fall back to a remote model when the local one is off (here: the morning status report while
   the GPU is reserved for a cohort run) redact identifiers before sending: subject/session ids, pseudonym codes,
   e-mail addresses. Wait for the local model a few minutes, not half an hour (the old version waited 30 min and failed).
4. The report and the board say which model wrote the interpretation.

## Trägt
`opencode debug skill`: 10 skills without the switch (incl. the three patient-data ones), 3 with it. Hermes
`skills list`: exactly the two shared skills. Trigger tests through both agents loaded the right skill. Morning report
interpreted by the hub's model in 10 s instead of a 30-minute wait and a failure.

## Trägt nicht
Redaction by pattern catches ids of known formats only; free-text names or new id formats need a review of what the
report contains (here: 0 id-like tokens in the day's report and board excerpt).

## Bruchindikator
A skill or report line that reaches the remote model with an identifier.

## Ablesung
Agent Skills specification: https://agentskills.io/specification. OpenCode skills docs: https://opencode.ai/docs/skills/
(version 1.18.35; switch names from its binary). Hermes agent `agent/skill_utils.py` (`get_external_skills_dirs`,
`os.walk(..., followlinks=True)`). kibotu/agent-skill-creation (commit 88dadd6, MIT). Own runs 2026-10-16.
