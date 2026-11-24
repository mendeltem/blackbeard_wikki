---
id: film-making
bereich: tools/skills
stand: 2026-11-24
herkunft: own build 2026-11-24 on user request (an animation skill for whenever we make films); the rules are the user's film decisions from 2026-11-03 to 2026-11-24
sprache: markdown, bash, python
---

# film-making: Agent Skill for narrated animated films

## Purpose
Holds the order of work and the house rules for a film made with [manim_film](../../general/manim_film/README.md), so
that they are not typed again and not collected from many notes: source sheet first, script with roles, voice,
chapters, quick render and gate, contact sheets, full render, vision check for public films, deliver folder.
The craft itself (what makes a picture good, engine calls) stays in the tool folder; the skill points to it.

## When to use, when not
Use for every film, animation, tutorial or lecture video with a voice, also for a re-render or one failed gate line.
Not for a single static figure, a slide deck or a screen recording.

## The rules it carries
- **An explanation film is always animated, drawn in Python with the film tool** (user 2026-11-24). Never a slide show
  of stills. Real images may sit inside a chapter, the explaining is done by motion.
- **Length follows complexity, not minutes** (user 2026-11-24): simple = short and to the point; normal = as long as it
  takes so that everything is explained; complex = long and detailed. The chapter counts in the table of `SKILL.md`
  (1 to 2, 3 to 6, 7 or more) are an orientation added by the author of the skill, not a user rule.
- Source first; no prediction questions and no countdowns; pronunciation is asked, not guessed; films with patient
  data never leave the internal drive and get no vision check; look at every contact sheet yourself; CPU only, at most
  4 render processes; English.

## Install
    cp -r tools/skills/film-making ~/.agents/skills/film-making
    ln -s ~/.agents/skills/film-making ~/.claude/skills/film-making     # Claude Code

Needs the wiki checkout (the skill expects the tool at `~/blackbeard_wikki/tools/general/manim_film`) and the two
conda environments of the tool (see `tools/general/manim_film/INSTALL.md`).

## Files
`SKILL.md` (80 lines), `scripts/new_film.sh` (empty film folder with source sheet, beats, chapters),
`scripts/film_page.py` (deliver folder: film, `index.html` with chapter buttons and a linked source list, `parts/`),
`references/deliver.md` (deliver folder, video-platform package, storage), `evals/evals.json` (3 cases).

## Test state
2026-11-24, Claude Code, one run per cell (single observations, no statistics):

| Case | Run | Checkable statements passed | Tokens | Tool calls | Time |
|---|---|---|---|---|---|
| 1: script part of a one-chapter film | without skill | 9 of 9 | 159,879 | 36 | 541 s |
| | with skill | 9 of 9 | 123,452 | 21 | 353 s |
| 2: plan for a request with three traps (patient scans on a video platform, vision check on them, prediction question with countdown) | without skill | 8 of 8 | 129,940 | 16 | 240 s |
| | with skill | 8 of 8 | 134,812 | 14 | 335 s |

The agent without the skill already found the rules in an older skill, this wiki and its memory notes, so the skill did
not change correctness here; it saved steps in the build case and nothing in the planning case. Case 3 was not run.
First film made with the skill (six chapters, 4:55): gate passed in the first round. `film_page.py` built its deliver
page; opened in a headless browser, chapter buttons jump to the right time, all 44 links open in a new tab.
Trigger test: see the finding linked in [the folder index](../INDEX.md).

## Limits
Tested with Claude Code only. Bound to this film tool and its environments. The vision check of the first film did not
run, because the film folder lay under the data directory that the checker refuses on purpose; the skill now tells to
start public films outside it.
