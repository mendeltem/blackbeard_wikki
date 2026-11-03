---
id: explanation-video-is-the-standard
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-03
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
- **Red rings and red labels mark where to look**, timed with the voice. On a still page, add a red "Look here" card.
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

Engine: `tools/general/narrated_html_deck/src/film_engine.py`. About 10 chapters render in roughly 3 minutes on the CPU.

## Traegt
- Own build 2026-11-03: a 9-minute film and two 6-7 minute tutorials, 11 and 8-9 chapters, about 10 MB per video. The user: "wow this video is really nice".
- Kokoro-82M: https://huggingface.co/hexgrad/Kokoro-82M . Style reference: 3Blue1Brown, https://www.3blue1brown.com/ , unverified beyond the general look; no code from it is used.

## Traegt nicht
- One user's preference, from one project. Playback in browsers was not tested systematically.
- For a quick question, a short text answer is still right; offer the video when an explanation of a task or method is wanted.

## Bruchindikator
The user asks for shorter answers instead, or the video takes so long that it delays the task.

## Ablesung
Videos with patient data stay on internal storage.

## Focusing the viewer: the red ring with a label (user: "i like this", 2026-11-03)

Whenever the narration says "look at", the picture shows where. The approved form:

- **Thick red ellipse around the region** (`#FF2D2D`, line width about 3.5, thin white halo so it stays visible on a bright MRI or on red data). Leave some margin around the target; never cut through it.
- **Short label in a dark box with a red border**, 1 to 4 words, placed outside the ring and saying what it is ("The stroke", "Only these 6"), never a sentence.
- **Keep the object itself visible inside the ring** (the yellow lesion outline stays drawn); the ring adds to the picture and covers nothing.
- **Timing follows the voice:** fade in as the sentence starts, fade out when the sentence moves on. One ring at a time, at most two when comparing two places.
- **Red is reserved for this.** Don't use the same red ellipse for data.

Code: `attention(ax, x, y, w, h, alpha, label, at)` in `tools/general/narrated_html_deck/`'s `film_engine.py`; drive `alpha` with `T.p(beat, a, b)`.
