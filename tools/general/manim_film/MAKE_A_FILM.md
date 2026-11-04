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

## Make room before you add
Plan each chapter on paper first: where does every box stand at the end of each beat? Boxes must not touch or overlap unless one lies wholly inside the other, and a label must not cross a box edge. Nothing above y = 3.0, where the title sits. If a new thing has no room, move or remove the old things first with an animation; never drop it on top. The gate checks this after every `self.to` and at every beat end.

## Charts tell the truth
A signed value grows from a zero line: positive up, negative down, on one scale. Every bar has its name and value in the same place relative to the bar, all of them. Use a chart when the source gives numbers, and put the numbers on it.

## Endings and belonging
End a chapter on the picture that sums it up, not on a row of leftover boxes. Things that belong together stand together: an optional file belongs inside the case folder it is part of, not under the list of cases.

## Tell the story with motion
Do not clear the screen between most beats. Let the last picture turn into the next one: `Transform` an object into its next form, move old boxes aside, send a dot along an arrow to show that something travels. A film of boxes appearing is a slide show. The gate counts travelling and clearing.

## Say only what the picture proves
- A new number replaces the old one at the same moment. Never leave one cohort's number beside another cohort's label, not even for a beat.
- A drawing whose shape is not real data says "schematic" on screen, also bars that only show an idea.
- English decimals with a point: 0.136, even if the source writes 0,136.
- Do not say "the numbers are on the screen". Say the number that matters.

## Words on screen stay true to this moment
- A caption belongs to its beat. When the voice moves on, replace it or `FadeOut` it; `self.caption = None` after a fade. The gate fails a caption that stays two beats.
- A list that lights up must light the item the voice is naming now, not the one before.
- Text at font size 22 or more; the gate fails anything below 18. If a box shrinks its label that far, make the box bigger.
- Keep a clear gap between labels and axes or box edges. A number alone ("seventeen") means nothing: say what it counts.

## Common mistakes
- Text rectangles are only fitted inside `Box`; a long `T(...)` can run off the frame, so split it with `\n`.
- `self.say` replaces the caption. After `clear_all` the old one is gone.
- Keep your own list of boxes on screen. Do not test `box in self.mobjects`.
