# tools/skills

Agent Skills: one folder per recurring kind of work, with a `SKILL.md` (name, description, rules, steps) and optional
scripts, in the open format of <https://agentskills.io/specification>. The agent sees only name and description at the
start and opens the rest when a task matches. Why and with which limits: finding
[agent-skills-what-they-give-and-what-they-cost-2026-11](../../knowledge/agent_tooling/findings/agent-skills-what-they-give-and-what-they-cost-2026-11.md).

| Skill | Language | Purpose |
|---|---|---|
| [film-making/](film-making/README.md) | markdown, bash, python | Order of work, house rules, checks and deliver folder for a narrated animated film with `tools/general/manim_film` |
| [mri-overlay-pages/](mri-overlay-pages/README.md) | markdown, python, javascript | Fixed colours (ground truth, second rater, TP, FP, FN) and picture quality for MRI slices with masks drawn on top |

Rules for this folder: only skills without patient data, without dataset names and without data paths (agents with
remote models read them). One skill, one job. Every skill has `evals/evals.json` and its README states what was tested.
Install: copy the folder to the place your agent reads (`~/.agents/skills/<name>` for Codex, OpenCode and Hermes with
an external folder; link or copy to `~/.claude/skills/<name>` for Claude Code).
