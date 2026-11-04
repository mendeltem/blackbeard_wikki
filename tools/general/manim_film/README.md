# manim_film

Narrated films in the style of 3Blue1Brown, drawn with Manim Community. Boxes light up with the voice, objects stay on screen across beats, and the timing follows the audio exactly. This is the house standard for animated explanations since 2026-11-04 (user: "das video ist sehr gut geworden, daran halten"). Rule: `knowledge/agent_tooling/rules/explanation-video-is-the-standard.md`.

A film folder holds `chapters.txt` (one line per chapter: file, class, key), `chapters*.py`, and `beats/<key>_beats.json` (a list of spoken blocks).

```bash
python src/voice.py my_film                         # env tts, CPU; only changed text
Q=low src/render.sh my_film                         # seconds: quick check
python src/sheets.py my_film                        # env manim; look at check/sheet_*.png
src/render.sh my_film                               # 1280x720, 30 fps, CPU
src/finish.sh my_film my_final_name                 # video/my_final_name.mp4 plus one file per chapter
```

## Writing a chapter
`class X(Film)` with `key`, `number`, `title`. `self.beat(i)` waits for the voice to reach block i, `self.to(.4)` waits for 40 % of the block, `self.finish()` runs to the end. `self.open()` writes the chapter title and moves it to the corner.
- `Box(label, color, w, h, size)` fits its label. `b.on()` lights it, `b.off()` returns it to normal, `b.mute()` dims it.
- `self.say(text)` is one line at the bottom, `self.send(a, b)` sends a dot along a path, `link(a, b)` is an arrow, `self.clear_all()` empties the screen but keeps the title.
- `self.ring(m)`: a red ring that goes away again. Use it rarely. The Clara film uses two in ten minutes.

## Quality gate
`AUDIT=1 Q=low src/render.sh my_film`, then `python src/film_gate.py my_film source.md`. It measures text off the frame, text on text, lines through text, rings, lit boxes, screen clears, motion, how full the screen is, voice sync and numbers not in the source. Controls: the approved film passes (0 problems), `tests/bad` fails. It cannot judge beauty; a person decides. For agents working alone: `MAKE_A_FILM.md`.

## Can an agent do this alone?
Own test 2026-11-04: Clara with the hub model made five 3-minute films on new topics with `MAKE_A_FILM.md`, no edits to any film; each took 22 to 45 minutes. The last two passed the gate in a row, with the guide unchanged between them. Still weaker than the reference: plainer pictures, and its image tool gives only a text description, so it cannot judge the look. A person decides. Status: not yet judged by the user.

## Traps
- Manim sets `dim` on every object, so a method called `dim` fails with "'int' object is not callable".
- Animating parts of a group splits it in `scene.mobjects`, so keep your own list of what is on screen.
- `LATE` in the log means an animation overran its voice mark; a second or so at a title card is fine.
- No LaTeX is needed: `DecimalNumber` and `MathTex` need it, so numbers count with a text updater (`counter` in the example).

`examples/clara_working_station` is the full film the user approved: 8 chapters, 10:20, rendered in 36 s on 24 CPU cores.

Sources: Manim Community, https://www.manim.community/ . Kokoro-82M, https://huggingface.co/hexgrad/Kokoro-82M . CMU Serif (cm-unicode), https://ctan.org/pkg/cm-unicode . Style reference only: 3Blue1Brown, https://www.3blue1brown.com/ ; no code from it is used.
