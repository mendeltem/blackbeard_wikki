# Deliver: film page, YouTube package, storage

## Contents
- The deliver folder
- YouTube package (tutorial films without patient data)
- Storage and copies
- What the final message names

## The deliver folder

```
<topic>_<yyyymmdd>/
  <name>.mp4            the film (at most 3 mp4 on top, e.g. film + two tutorials)
  index.html            one big video, chapter list with clickable times, sources as links (new tab)
  parts/                one mp4 per chapter, source.md, beats/, chapters*.py, say_check.mp3
```

`scripts/film_page.py` writes this. `--body fragment.html` puts a longer text (a report, a method description) between the chapter list and the sources; write it as an HTML fragment with `<h2>` sections. `--top a.mp4 b.mp4` adds up to two more films on top.
After it ran: open `index.html` in a browser once, click two chapter times, and check that the page has no web address that is not a link.

## YouTube package (tutorial films without patient data)

Five files next to the film: 1080p video with a title card of about 4 s that shows the result first, thumbnail 1280x720 JPG, description with chapter times (first `0:00`, shifted by the card length), quiz, README with the upload title. The exact commands and limits are in the section "YouTube package" of `MAKE_A_FILM.md` in the tool folder; follow them there. Render at `W=1920 H=1080` for this.
The user uploads; an agent never uploads. Atlas or data licences that exclude commercial use mean: no ads on the video; say so in the README.

## Storage and copies

- Work folder stays where the film was built. Results go to the group drive with a checksum comparison (in Claude Code: skill `alita-storage`, target RESULTS). Report the file count on both sides.
- Films with patient data: group drive only. No public page, no YouTube, no vision check.
- Nothing is deleted by an agent, also not old versions: move a replaced film to `parts/old_<yyyymmdd>/`.

## What the final message names

The path of `index.html`, the film length, the gate result and the number of rounds, the vision check result (or "not run" with the reason), the words whose pronunciation the user has not heard, every guessed decision (length, language, resolution), and what was not checked.
