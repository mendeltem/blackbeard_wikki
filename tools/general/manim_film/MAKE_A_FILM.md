# How to make a film (for an agent working alone)

Goal: a narrated film as good as `examples/clara_working_station`. Read `README.md`, then `src/engine.py`, then `examples/clara_working_station/chapters_a.py` (class What and class Parts) before writing anything. Copy the way those chapters think, not their text.

## Order of work
1. Read the source. Write `beats/<key>_beats.json`: 4 to 6 spoken blocks per chapter, 1 to 3 short sentences each. Plain words. Numbers only if they stand in the source. Say abbreviations as a listener would hear them. No claim that is not in the source.
2. `python <tool>/src/voice.py .` with the tts env, to get the exact durations.
3. Write `chapters.py` and `chapters.txt`.
4. `AUDIT=1 Q=low <tool>/src/render.sh .`, then `python <tool>/src/film_gate.py . source.md`. Fix what it reports.
5. `python <tool>/src/sheets.py .` and look at every `check/sheet_*.png`. The gate cannot see beauty; you can.
6. Full render without Q, then `<tool>/src/finish.sh . film`.

## What makes it good
- **One picture grows.** Start a chapter with one idea on screen and add to it. Keep objects across beats. Clear the screen only when the idea really changes.
- **Picture follows voice.** Use `self.to(share)` so that each thing appears as it is named. Something should move at least every 10 seconds.
- **Light up, do not point.** `b.on()` for the box being talked about, `b.off()` for the one before. A red `self.ring` at most once in a chapter, for the one thing that must not be missed.
- **Show the idea, do not write the sentence.** Do not print the narration on screen. A label has few words. Show amounts as bars or dots at true scale, flows as arrows with a moving dot, choices as branches, overlap as two circles.
- **Real numbers only.** A picture without real values says "schematic".
- **Fill the frame.** x from -6.8 to 6.8, y from -3.6 to 3.0. No small cluster in a corner, no text on text, no line through text.

## Common mistakes
- Text rectangles are only fitted inside `Box`; a long `T(...)` can run off the frame, so split it with `\n`.
- `self.say` replaces the caption. After `clear_all` the old one is gone.
- Keep your own list of boxes on screen. Do not test `box in self.mobjects`.
