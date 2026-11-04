---
id: explanation-video-is-the-standard
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-04
herkunft: user request 2026-11-03 ("this is how an explanation video should look when I want an explanation of what our task is"); own build
verweist_auf: [narrated-html-deck-one-audio-per-slide]
---

# When the user asks for an explanation of the current task, make an explanation video like this

## Aussage
This is the standard for explaining a task, method or result to the user: an animated, narrated video in the style of 3Blue1Brown, built from the real data of the task, with red rings showing where to look. Deliver plain video files that can simply be opened, and a page with detailed text beside the video.

## What to deliver
In one folder, with these plain names:
- `explanation.mp4`: the whole explanation, all chapters joined.
- `<method>_tutorial.mp4`: one longer tutorial for each method that needs teaching.
- The same names as `.mp3` for listening only, if the user wants that.
- `index.html`: chapters with the detailed text beside each video, and `tutorials.html`: tutorials with clickable parts.
- The code that made it, and a copy wherever the user works (internal drive, cluster transfer folder).

## How it should look
- **Dark background, smooth motion, no idle space.** Content fills the screen. Build one idea per spoken sentence block, so that the picture changes as the voice explains.
- **Real data whenever possible.** Illustrations are labelled as illustrations.
- **Light up the box the voice is talking about; that is the default highlight** (user 2026-11-04). Red rings only at rare key moments, and they must fade again so they never sit on text. On a still page, add a red "Look here" card.
- **Keep objects on screen across beats**, as in 3Blue1Brown, instead of drawing a new screen per beat. Manim (https://www.manim.community/, version 0.19 or newer, conda-forge) gives this directly; a 10-minute film rendered in under a minute on 24 CPU cores (own run 2026-11-04).
- **Plain words first, numbers second.** Say what a number means. Explain the reading of signs, units and colours before showing results.
- **Text and image together.** Beside each video: what we did, what we found, what it means, caution.
- **Teach the method with its own animation.** Examples that worked: correlation (time points becoming dots), one map sharpening from 1 to 1,000 people, a slider that turns a regression line, a heatmap filled in square by square, a shuffle filling up a null distribution, patients hidden one by one.
- **References are always clickable in HTML** (user rule 2026-11-03): that is the advantage of HTML over a PDF or video. Each citation links to the paper in a new tab, with a one-line hover, and a sources page lists them all.
- **Honest throughout.** Show the caveats, the failures and your own mistakes. Exploratory results are called exploratory.

## How to build it
1. Write `chapters.py`: per chapter a title, spoken beats (3 to 6 sentence blocks) and the detail text. Numbers in the speech as words; respell abbreviations for the voice.
2. Prepare one data file with real numbers and slices, so that frames render fast.
3. Generate one audio file per beat (Kokoro-82M, CPU); skip beats whose text did not change.
4. Write one `draw(fig, time)` per chapter; `time.p(beat, a, b)` moves from 0 to 1 within a beat, so the timing follows the voice.
5. Render **check frames only** first (one per beat), and look at them. Most errors are text overlaps and wrong interpretations, and they only show on rendered frames.
6. Render at most 4 chapters in parallel; join with the ffmpeg concat demuxer (`-c copy`); decode every file to verify it.
7. Build the page, store with checksums, and say what was not checked (for example, not watched to the end).

Before narrating a result, read it at predicted values, not from its sign alone. Compare every number in the speech and on the frames with the result tables. If the results change, rerun everything: old numbers must not stay in a video.

Engine since 2026-11-04: `tools/general/manim_film` (Manim, the approved look; full example in `examples/clara_working_station`). The older matplotlib `tools/general/narrated_html_deck/src/film_engine.py` stays for frames with real MRI data. About 10 chapters render in roughly 3 minutes on the CPU.

## The workstation film is the reference (user 2026-11-04: "the working station video was really good")

Watch it before building a new film: https://github.com/mendeltem/clara_working_station/blob/main/video/clara_working_station.mp4
(10 min, 8 chapters, 1280x720, 30 fps, 23 MB; narration written by the hospital hub model, animation with Manim).

**What makes it good**
- **One diagram that grows.** A chapter opens with one or two boxes and adds the next part only when the voice names it; earlier parts stay, dimmed (`mute()`), so the viewer always sees where the new piece sits.
- **The box the voice is on lights up** (`on()`: fill and glow), everything else is calm. Highlighting by light, not by arrows or rings.
- **Things move along the arrows.** A labelled dot travels from one box to the next with a passing flash on the line (`send()`), so a data flow is seen, not described. Tokens such as "data path" or "subject id" fly into a router and are sorted.
- **One colour per role, the whole film long:** teal = the machine, green = the local agent, blue = the hub model, yellow = the router, orange = patient data, red = network or failure, purple = the decision model. Colours are never reused for something else.
- **Each chapter opens with its title written large, then shrinking into the corner** (`open()`); a short caption line at the bottom replaces the previous one (`say()`).
- **Numbers as objects:** bars that grow to scale (32,768 vs 64,000 tokens), dot grids for counts (154 commands), counters for the honest log (6 crashed, 11 rewritten, 3 rewritten after the fact check).
- **An honest chapter:** what failed, what is unknown, what stays private.

**How it is built (5 small files)**
- `engine.py`: the look (dark background `#0b0d12`, CMU Serif, the colour table) and the timing. A `Film(Scene)` reads the spoken length of every beat from the audio and gives `beat(i)` (wait until the voice reaches beat i) and `to(share)` (wait until that share of the beat is spoken); an animation that overruns prints `LATE`. Helpers: `Box`, `link`, `send`, `tick`, `cross`, `dots`, `bar`, `ring` (a red Circumscribe that goes away again).
- `chapters_*.py`: one `Film` subclass per chapter that only says what happens when.
- Voice first (Kokoro, one file per beat, only changed beats re-spoken), then picture, so the picture follows the voice.
- `render.sh`: at most 4 chapters in parallel on the CPU; `Q=low` renders 640x360 at 12 fps for checks. `sheets.py`: a contact sheet per chapter with a frame at 55 % and 97 % of every beat; look at every sheet before the full render.
- `finish.sh`: joins each chapter's picture with its beat audio (ffmpeg concat), then all chapters with `-c copy`.

## Traegt
- Own build 2026-11-04: Clara Working Station film in Manim, 8 chapters, 10:20. User: "das video ist sehr gut geworden, daran halten". This is now the reference look.
- Own build 2026-11-03: a 9-minute film and two 6-7 minute tutorials, 11 and 8-9 chapters, about 10 MB per video. The user: "wow this video is really nice".
- Second Manim film without any data, 2026-11-04: double quantum coherence in MRS for students, 6.6 min, numbers from an own density-matrix simulation, sources Keltner 1997 (PMID 9055226), He 1995 (PMID 7719620), Harris 2017 (PMID 28150876); lessons added to `tools/general/manim_film/MAKE_A_FILM.md` (topic without data, scaling shrinks labels).
- Workstation film 2026-11-04 (Manim Community 0.19, https://www.manim.community/): the user called it really good and asked for it to be published; it became the reference for the CMB paper film the same day.
- Kokoro-82M: https://huggingface.co/hexgrad/Kokoro-82M . Style reference: 3Blue1Brown, https://www.3blue1brown.com/ , unverified beyond the general look; no code from it is used.

## Traegt nicht
- One user's preference, from one project. Playback in browsers was not tested systematically.
- For a quick question, a short text answer is still right; offer the video when an explanation of a task or method is wanted.

## Bruchindikator
The user asks for shorter answers instead, or the video takes so long that it delays the task.

## Ablesung
Videos with patient data stay on internal storage.

## Focusing the viewer: the red ring with a label (user: "i like this", 2026-11-03)

Since 2026-11-04: in diagrams, light up the box instead; the ring is for a rare key moment or for pointing inside an image such as an MRI. The ring must fade again and never cover a label.

Whenever the narration says "look at", the picture shows where. The approved form:

- **Thick red ellipse around the region** (`#FF2D2D`, line width about 3.5, thin white halo so it stays visible on a bright MRI or on red data). Leave some margin around the target; never cut through it.
- **Short label in a dark box with a red border**, 1 to 4 words, placed outside the ring and saying what it is ("The stroke", "Only these 6"), never a sentence.
- **Keep the object itself visible inside the ring** (the yellow lesion outline stays drawn); the ring adds to the picture and covers nothing.
- **Timing follows the voice:** fade in as the sentence starts, fade out when the sentence moves on. One ring at a time, at most two when comparing two places.
- **Red is reserved for this.** Don't use the same red ellipse for data.

Code: `attention(ax, x, y, w, h, alpha, label, at)` in `tools/general/narrated_html_deck/`'s `film_engine.py`; drive `alpha` with `T.p(beat, a, b)`.
