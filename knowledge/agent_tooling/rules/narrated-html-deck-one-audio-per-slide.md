---
id: narrated-html-deck-one-audio-per-slide
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-03
herkunft: user request and confirmation 2026-11-03 ("these kind of html presentation is really good"); own build, tool tools/general/narrated_html_deck
verweist_auf: [blackboard-short-protocol-long-html]
---

# Explain results as a narrated HTML deck: one audio file per slide

## Aussage
When a person needs an analysis explained, build a slide deck as a plain HTML page with a spoken voice per slide, generated from one list
that holds each slide's content and its speech. Tool: `tools/general/narrated_html_deck` (Kokoro-82M on the CPU, no server, no external files).
The user asked for this format to be kept after seeing it.

## How to build a good one
- **One idea per slide, real data first.** Start with what is being asked, then the method in plain words, then one worked example from the actual data.
- **Explain how to read the numbers.** Give signs and units their own slide; this was the question the user actually had.
- **Write the speech for the ear.** Numbers as words, abbreviations spelled out or respelled ("E Q five D"); short sentences. The voice adds the reasoning, the slide keeps the numbers.
- **Build:** one script for figures, one for speech (re-speaks only changed text), one for the page. Numbers in the text are checked against the result tables.
- **Controls:** Play starts the sound, because browsers block autoplay until the first click. Add auto-advance, transcript, speed, keys.
- **Look at the rendered slide before delivery**, not only the code.

## Next step up: animated film (user request 2026-11-03)
The user asked for the look of a 3Blue1Brown video, with image and text combined and a detailed explanation for each result. Build chapters: motion that builds one idea per spoken beat, real data, the detailed text beside the video (what we did, what we found, what it means, caution). Engine in the same tool, `src/film_engine.py`. Own build: 10 chapters, 8.2 minutes, 11 MB; check one frame per beat, because text overlaps only show on rendered frames.

## Layout rules from user feedback (2026-11-03)
- **No idle background.** Content fills the screen: no narrow centred column, no small figure in a large empty page. Text-only slides stretch to the full height, with large type.
- **One dark theme** for the page and the figures, so images do not sit in a bright box; make figures 16:9, with large fonts and tight margins.
- **Picture and text side by side.** Every result gets a picture and a short explanation: what you see, what we found, what it means, caution.
- **Explain methods with their own pictures**, using real data where possible. Example, heatmap: one test, its two lines, its number, one square; then what red, white and blue mean; then the full map.
- **Prefer longer and fuller** over short and sparse when the user wants to understand: about 30 slides, 17 minutes worked well as a request.

## Interpretation error this format caught
A positive interaction was first narrated as "those who start badly stay bad". The rendered plot showed the lines meeting at the poor end and a difference elsewhere,
and the model line ran into a range with no such patients. Interpret an interaction at **predicted values inside the range covered by data**, never from its sign alone, and draw each
group's line only where that group exists.

## Traegt
- Own build 2026-11-03: a 12-slide and a 13-slide deck, 6.5 and 8.7 minutes; `tests/test_build.sh` from zero passes (2 audio files, page refers to them, unchanged text is not re-spoken).
- Kokoro-82M: https://huggingface.co/hexgrad/Kokoro-82M . Autoplay rule: https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay

## Traegt nicht
- Not tested with an audience beyond one user; playback was checked by decoding the files and rendering slides, not by listening in each browser.
- Default voice is English; other languages need a matching Kokoro voice, unverified here.

## Bruchindikator
Listeners ask to read rather than listen, or the voice mispronounces key terms so often that corrections outweigh the benefit.

## Ablesung
Decks with patient data stay on the internal drive, not on public hosts.
