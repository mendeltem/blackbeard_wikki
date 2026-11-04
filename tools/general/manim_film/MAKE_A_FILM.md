# How to make a film (for an agent working alone)

Goal: a narrated film as good as `examples/clara_working_station`. Read `README.md`, then `src/engine.py`, then `examples/clara_working_station/chapters_a.py` (class What and class Parts) before writing anything. Copy the way those chapters think, not their text.

## Order of work
1. Read the source. Write `beats/<key>_beats.json`: 4 to 6 spoken blocks per chapter, 1 to 3 short sentences each. Plain words. Numbers only if they stand in the source. Say abbreviations as a listener would hear them. No claim that is not in the source.
2. `python <tool>/src/voice.py .` with the tts env, to get the exact durations.
3. Write `chapters.py` and `chapters.txt`.
4. `AUDIT=1 Q=low <tool>/src/render.sh .`, then `python <tool>/src/film_gate.py . source.md`. Fix what it reports.
5. `python <tool>/src/sheets.py .` and look at every `check/sheet_*.png`. The gate cannot see beauty; you can.
6. Full render without Q, then `<tool>/src/finish.sh . film`.
7. Public films only: `python <tool>/src/film_see.py . --public` (env manim). A vision model looks at every beat. Fix everything under "Confirmed" in `check/see_report.md`, render again, and repeat, at most 3 times. Read the hints too: fix a hint only if you agree, because many are moments caught in the middle of an animation. Exit 2 means the eye missed its planted flaws: say so in your report and do not call the film seen. The tool cannot judge beauty and does not hear the voice. Never use it on a film with patient data: the frames go to the hub.

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

## A topic without data (physics, a method)
Own build 2026-11-04, double quantum coherence in MRS, 8 chapters, 6.6 min, gate passed after three rounds.
- Compute the numbers instead of drawing ideas: a small simulation (here a density-matrix model of the filter) gives real curves and values, and the film says "simulated" or "schematic" on screen.
- Write `source.md` first, with every number the film uses, also axis ticks and labels such as "pulse 1"; the gate checks speech and on-screen text against it.
- Check every physics sentence against the source before the voice is made; rephrase what the sources do not say (e.g. "keeps more signal" was cut because no source gave it).

## YouTube package
User standard since 2026-11-04 (first: double quantum coherence film). Deliver five files next to the film; films with patient data never go to YouTube.
1. **Video** `<name>_youtube_1080p.mp4`: a title card of about 4 s in front that shows the result first (no logo, no "subscribe"), then the film. Render the card with the engine at `W=1920 H=1080` (the engine sets the size from these variables; manim's `-r` is ignored), then join and encode:
   `ffmpeg -i card.mp4 -f lavfi -t <card s> -i anullsrc=r=48000:cl=stereo -i film.mp4 -filter_complex "[0:v]fps=30,format=yuv420p,setsar=1[v0];[2:v]scale=1920:1080:flags=lanczos,setsar=1[v1];[v0][1:a][v1][2:a]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart out.mp4`, then decode-check with `ffmpeg -i out.mp4 -f null -`.
2. **Thumbnail** `youtube_thumbnail.jpg`: 1280x720 JPG under 2 MB (YouTube Help 72431); 2 to 5 large words and one picture of the result (before -> after); nothing in the bottom-right corner, where the duration badge sits; look at it at phone size. Custom thumbnails need a verified account.
3. **Description** `youtube_description.txt`: one-sentence explanation, chapter list, a note on what is simulated or schematic, sources with DOI or PubMed link, software line. Chapters: the first must be `0:00`, at least 3, each at least 10 s, in the description (not a comment). Shift every chapter time after the first by the length of the title card.
4. **Quiz** `youtube_quiz.txt`: about 6 questions, each shown at the end of the chapter it tests; 3 answers of at most 80 characters, the correct one not always first; explanation under 350 characters. These limits are those reported for quiz posts; YouTube does not document the in-video quiz limits (checked 2026-11-04), so check in Studio.
5. **README**: which file to upload, title under 100 characters plus two alternatives, how to post ("not made for kids", category Education), and a course (playlist) name for the series.

Sources (looked up 2026-11-04): YouTube Help, thumbnails https://support.google.com/youtube/answer/72431 ; chapter rules https://gling.ai/blog/creating-youtube-chapters-a-complete-guide ; intro length (2 to 5 s for teaching, rule of thumb, not from YouTube) https://www.teleprompter.com/blog/how-long-should-a-youtube-intro-be ; quiz post limits https://cordcuttersnews.com/youtube-is-rolling-out-quizzes-to-see-if-you-are-learning-anything/ (unverified against YouTube's own help).

## Common mistakes
- Text rectangles are only fitted inside `Box`; a long `T(...)` can run off the frame, so split it with `\n`.
- `self.say` replaces the caption. After `clear_all` the old one is gone.
- Keep your own list of boxes on screen. Do not test `box in self.mobjects`.
- `group.scale(k)` also shrinks the text in it, and the gate fails labels under 18 pt. Build axes and curves at their final size (give the helper a width factor and an offset) instead of scaling.
- A zoom with `scale` pushes tick labels off the frame: fade the labels out before the zoom and back in after it.
- Dark text (`BG`) on a fill with low opacity is unreadable; use `INK` or `WHITE` unless the fill is nearly solid.
- A box from an early beat that is never faded collides with later labels ("text on text"); fade every helper box in the beat where its job ends.
- A label placed `next_to` a row of arrows can sit on the arrows; put it above or below the thing it names.
