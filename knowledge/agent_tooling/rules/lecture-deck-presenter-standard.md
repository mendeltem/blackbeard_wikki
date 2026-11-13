---
id: lecture-deck-presenter-standard
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-13
herkunft: user requests 2026-11-13 while preparing the lecture of 18.11.2026 (clicker, presenter view, timers, PDF); own build, deck v19 to v29 in github.com/mendeltem/mri-segmentation-lectures
verweist_auf: [narrated-html-deck-one-audio-per-slide, explanation-video-is-the-standard]
---

# Live lecture deck: one click = one point, with its animation and its own voice; presenter view with timing to the second

## Aussage
A deck for a live lecture (lecturer with a laser-pointer clicker, projector plus a second window on the laptop) follows this standard.
It extends the [narrated explanation deck](narrated-html-deck-one-audio-per-slide.md) and uses the [Manim film look](explanation-video-is-the-standard.md) for the clips.

**Content pipeline (numbered scripts, rerun in this order after any slide change)**
1. Slide text and voice text in one list (`slides_data.py`); points per slide with a marked word (`deck_layout.py`: a point lights up when the voice says its `{mark}`).
2. Voice per beat with word times (Kokoro, voice `af_heart`), a Manim clip per slide timed to the marks.
3. `03_make_deck_media`: point times on the slide timeline.
4. `16_step_notes`: the voice text split into steps, whole sentences per point (a sentence belongs to the point whose mark falls inside it); written spelling for the screen, spoken spelling kept for the voice.
5. `17_step_audio`: one recording per step from whole sentences (unchanged texts are skipped).
6. `15_pdf_handout`: PDF from screenshots of every slide's final state.
7. `06_sync_repo`: copy only the files the deck uses into the public repo, then commit as the owner and push (GitHub Pages).

**Interaction standard**
- **One mode button, not separate boxes:** "Clicker" (point by point, default) or "Auto" (every slide plays in full and the deck goes on by itself; pauses at interactive pages and exercises); key A switches. Separate Autoplay / Auto-advance / Point-by-point boxes confused the lecturer, because point by point silently overrode the other two (2026-11-13).
- **Point by point is the default.** Clicker PageDown / → = next point, after the last point the next slide; PageUp / ← = back one point (back shows the finished state, no animation); ↓ / ↑ = whole slide. Unticking "Point by point" gives plain autoplay through each slide (self-study).
- **Each click plays the animation of its point**: the clip runs from the end of the previous point to 0.12 s before the next mark, then stops. Seeking to the mark itself shows the previous point, because a clip draws a point only after its mark.
- **Each click plays its own recording** of whole sentences. Cutting the slide voice at the marks cuts words, because marks often sit mid-sentence. The "Voice" box switches it on or off (V); the clip stays muted while the step voice plays.
- **Text first, then the voice** (lecturer 2026-11-13): on each click the clip starts just before the point's mark, draws its box, and the step voice starts 1.4 s later (the slowest builds, a curve plus its label, take about 1.4 s). Step texts: a sentence belongs to the point whose mark falls inside it; a sentence with the marks of several points is cut at each marked word, moved back to the nearest phrase boundary (after , ; : or before and/or/but; else keep a, the, into ... with the marked word) but never before the previous point's own mark; a sentence without a mark at the start of a beat (new picture) leads in to that beat's first point, otherwise it continues the point already shown. Check every step: click through headless, screenshot at voice start with the spoken text under it, look at all contact sheets (found 5 places where the voice named the next picture early).
- **The first click forward starts the lecture clock** and plays point 1 with its voice (it stays on point 1); every later click moves on.
- **Exercise slides:** a click starts that exercise's countdown, which **stops at 0:00** (red, "time is up"); the next click goes on. S pauses, "reset" refills.
- **Restart** (bar and presenter view, with a confirmation asked in the window where it was pressed): slide 1, point 1, lecture clock off, all exercise timers full.

**Presenter view (second window, opened with N)**
- Header "step g / N · slide · point k / n"; the point heading and its sentences in large type (about 34 px); the whole slide text, background and Q&A folded below.
- Right: the next point with its sentences, after the last point the next slide.
- Status line: "▶ animation running · 2.4 s" until the longer of clip piece and step voice ends, then "■ animation finished"; on exercise slides the countdown in large type.
- Clock and plan **per step to the second**: a slide's planned time is split over its points by where each point falls in the voice; "step planned at m:ss · ahead / behind by m:ss" (colour beyond 30 s) and "this slide: m:ss left / over".

**Handout PDF**: cover, linked contents by section with interactive pages and exercises marked, one page per slide (screenshot of the final state, every point with what is said at it, sources with one line each), all sources with the slides that use them, PDF bookmarks. Written spelling, not the voice spelling ("BIANCA", not "Bianka").

**Checks before every push**: syntax check of the page script; headless Chromium (Playwright) with projector and presenter window together, pressing the clicker keys and reading slide, point, video time, clock and presenter text after each key; look at rendered screenshots, not only at numbers.

## Traegt
- Own build 2026-11-13, lecture "Brain region segmentations using FSL, FreeSurfer and Python" (18.11.2026): 50 slides, 184 steps, 3 exercises, plan 83 min; deck v19 to v29, each version tested headless before the push. Repo: https://github.com/mendeltem/mri-segmentation-lectures ; live deck https://mendeltem.github.io/mri-segmentation-lectures/lecture_1118/deck/
- Faults found this way, each fixed: a clip that loaded late reset the slide to "no point" (the clock was zeroed before the keep-point check); projector one point behind the presenter view (seek to the mark); voice cut mid-sentence (per-step recording); point mode off by default made the voice run through the whole slide.
- Kokoro-82M https://huggingface.co/hexgrad/Kokoro-82M ; Playwright 1.62 https://playwright.dev (page.pdf with outline, headless keyboard tests) ; browser autoplay rules https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay

## Traegt nicht
- Not yet used in front of an audience; timing per step is a plan, not a measurement of a real lecture.
- Tested in headless Chromium; the lecturer uses Firefox. Clicker models that send other keys (b, period) are not mapped.

## Bruchindikator
The lecturer still waits for animations, or the per-step plan is off by minutes in a real lecture.

## Ablesung
Only public data in public decks. Lecture decks with patient images stay on the internal drive.
