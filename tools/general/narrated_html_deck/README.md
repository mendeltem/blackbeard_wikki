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
