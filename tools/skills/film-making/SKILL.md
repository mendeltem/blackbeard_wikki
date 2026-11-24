---
name: film-making
description: Makes a narrated animated film with the Manim film tool - script, voice, chapters, checks, render, deliver folder. Use when asked to make, change or re-render a film, animation, tutorial or lecture video, also for "Film", "Animation", "Erklaerfilm", "Video mit Stimme", a film page or a YouTube package. Load it before planning or touching such work, also for one failed gate line or a late animation. Not for a single static figure, a slide deck, or a screen recording.
license: CC-BY-4.0
compatibility: Needs the wiki tool folder manim_film and the conda envs tts (Kokoro voice, ffmpeg) and manim on this workstation. CPU only.
metadata:
  author: Uchralt Temuulen
  version: "1.2"
  since: "2026-11-24"
---

# Film making

Tool: `T=~/blackbeard_wikki/tools/general/manim_film`. Approved reference film: `$T/examples/clara_working_station`.
This skill holds the order of work and the user's rules. The craft (what makes a picture good, engine calls, common mistakes) is in the tool folder; read it there, do not copy it here.

## Rules that always hold

0. **An explanation film is animated, drawn in Python with this tool** (user 24.11.2026: explainer films always with animations; the Python-made animations so far were good). Things move and light up with the voice. Never a slide show of stills, never a talking text page. Real images (a scan, a screenshot) may sit inside a chapter, but the explaining is done by motion.
1. **Source first.** Every number that is spoken or shown stands in `source.md` before the script is written, with where it comes from. A drawing whose shape is not data says "schematic" on screen.
2. **No prediction questions and no thinking countdowns** (user 17.11.2026), also when a request asks for them: say the naive expectation as a `guess` beat and break it in a `fails` beat. Tell the user you did this.
3. **Pronunciation is asked, not guessed.** Words that `say_check.py` lists as unknown go to the user (send `check/say_check.mp3` and the table) before the final render. Do not tune the voice otherwise: sound is secondary, the first version should come fast.
4. **Patient data.** A film that shows scans or per-case values of own cohorts: never YouTube, never `film_see.py` (its frames leave the machine), never a published page; `script_check.py` only with `--no-reader`; store on the group drive only.
5. **Look yourself.** The gate measures layout, it cannot see whether a picture is good. Open every `check/sheet_*.png` before the full render.
6. **CPU only, at most 4 render processes** (`render.sh` does this). Several films at once: serialise the renders with `flock ~/ablage/tmp_render/tutorial_render.lock <command>`.
7. Films, pages and file names are in English.
8. A frame that shows a scan with masks or outlines takes its colours and picture quality from the skill `mri-overlay-pages`.

## Length follows complexity, not minutes

User 24.11.2026: the length of a film is set by how complex the topic is, not by a minute count. Pick the level from the request; if it names none, take normal and say so in the report.

| Level | The film is | Orientation, not a limit |
|---|---|---|
| simple | short and to the point: the one idea, one example | 1 to 2 chapters |
| normal | as long as it takes so that everything is explained | 3 to 6 chapters |
| complex | long and detailed: every step, every term, the limits | 7 or more chapters, or several films |

A minute count in a request is a hint for the level, never a reason to drop a step that the explanation needs.

## Before the first film of a session

Read, in this order: `$T/MAKE_A_FILM.md` (88 lines: what makes it good, layout, common mistakes), `$T/README.md` (engine calls and traps), and the classes `What` and `Parts` in `$T/examples/clara_working_station/chapters_a.py`. Copy how those chapters think, not their text.

## Steps

Run every command from the film folder. `PT=~/miniconda3/envs/tts/bin/python`, `PM=~/miniconda3/envs/manim/bin/python`.

| # | Do | Command | Passed when |
|---|---|---|---|
| 0 | New folder; a film with only public content gets a folder outside `~/data` (for example `~/ablage/films/<name>`), or step 8 refuses it | `bash scripts/new_film.sh <folder> <key1> <key2> ...` (in this skill's folder) | folder has `source.md`, `beats/`, `chapters.py`, `chapters.txt` |
| 1 | Fill `source.md` | by hand: every number, label and source link | nothing in the plan is missing from it |
| 2 | Write `beats/<key>_beats.json` | 4 to 6 beats per chapter, 1 to 3 short sentences, each `{"say": ..., "role": ...}`; roles question, guess, fails, idea, example, recap; `{name}` before a word a picture must wait for | `python3 $T/src/script_check.py .` exits 0 (`--no-reader` for non-public content) |
| 3 | Voice | `$PT $T/src/voice.py .` then `$PT $T/src/say_check.py .` | open words are listed for the user (rule 3) |
| 4 | Write `chapters.py` | one class per chapter; plan where every box stands at the end of each beat | file imports |
| 5 | Quick render + gate | `AUDIT=1 Q=low $T/src/render.sh .` then `python3 $T/src/film_gate.py . source.md` | gate exits 0; no `LATE` over about 1 s in `check/*.log` |
| 6 | Sheets | `$PM $T/src/sheets.py .` and look at each `check/sheet_*.png` | no overlap, no empty frame, lit box = the thing being named |
| 7 | Full render | `$T/src/render.sh .` then `$T/src/finish.sh . <name>`; for 1080p: `W=1920 H=1080 $T/src/render.sh .` then `RES=1080p30 $T/src/finish.sh . <name>` | `video/<name>.mp4` exists and decodes |
| 8 | Vision check, public films only | `$PM $T/src/film_see.py . --public` | exit 0; exit 2 = the eye failed, say so and do not call the film seen |
| 9 | Deliver | `$PM scripts/film_page.py <film folder> <name> --title "..." --out <deliver folder>` (in this skill's folder) | see below |

If step 5 fails, fix `chapters.py` and repeat 5; a text change means step 3 again for that chapter (unchanged beats are skipped).

## Deliver

One folder: the film as `.mp4` and `index.html` on top (at most 3 mp4 on top), everything else in `parts/`. The page has one big video, a chapter list with clickable times, and every source as a link that opens in a new tab. `scripts/film_page.py` builds exactly this from `chapters.txt`, the voice timing and the `## Sources` list in `source.md`.
Tutorial films for YouTube need five more files, and results belong on the group drive: read `references/deliver.md` for both.

## Report

Say: the level (simple, normal, complex) and the length, number of gate rounds and the gate result, whether the vision check ran and what it confirmed, which words the user has not heard yet, what you guessed, and what you did not check.

## When it fails

- `LATE <key> beat n` in the log: an animation runs longer than its voice mark; shorten `run_time` or move the mark.
- Gate: "number not in source": add the number with its origin to `source.md`, or remove it from the film. Never add a number to `source.md` only to pass.
- Gate: "text on text" / "box on box": an old helper box was never faded; fade it in the beat where its job ends.
- `predict()` raises: rule 2; rewrite as guess and fails.
- `'int' object is not callable`: a method named `dim` collides with Manim; rename it.
- `film_see.py` refuses a folder under `~/data`: that guard is on purpose; do not copy the film elsewhere to get around it. Report "vision check not run" and start the next public film outside `~/data` (step 0). First seen 24.11.2026.
