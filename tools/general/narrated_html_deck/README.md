# narrated_html_deck

A slide presentation as a plain HTML page, with a spoken voice per slide. Works offline from a folder; no server, no external files.

```bash
python src/speech.py my_deck              # slides.py -> audio/slideNN.mp3 (only changed slides)
python src/build_html.py my_deck --title "My talk" --label internal
```

`my_deck/slides.py` holds the list `SLIDES`; see `tests/example_deck/slides.py`. Images go in `my_deck/figures/`. Open `my_deck/index.html`
and press Play: browsers block sound until the first click, so the page never starts by itself.

Keys: space = play / pause, arrows = slide, T = transcript. Auto-advance, speed and a seek bar are on the page. It follows the system dark mode.

Install and test: see INSTALL.md. Rule for using it: `knowledge/agent_tooling/rules/narrated-html-deck-one-audio-per-slide.md`.

## Animated film, in the style of 3Blue1Brown

`src/film_engine.py`: dark theme, smooth motion, voice in sync. Split the speech into beats and write one audio file per beat (`audio_beats/<key>_<i>.wav` and `state.json` with the seconds); a chapter is then a function `draw(fig, time)` in which `time.p(2)` moves smoothly from 0 to 1 during beat 2. `render(key, title, nbeats, draw)` writes `video/<key>.mp4` and one check frame per beat. No outside video library; matplotlib frames are piped into ffmpeg (libx264, aac). Show the video beside a detailed text.

Use `attention(ax, x, y, w, h, alpha, label)` for a red ring that shows where to look. Rule and full recipe: `knowledge/agent_tooling/rules/explanation-video-is-the-standard.md`.
