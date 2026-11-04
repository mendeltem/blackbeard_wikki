# Install

```bash
conda create -y -n manim -c conda-forge --override-channels python=3.11 manim
mkdir -p ~/.fonts; for f in cmunrm cmunbx; do curl -sSL -o ~/.fonts/$f.otf https://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/$f.otf; done; fc-cache -f ~/.fonts
```
Voice needs a second environment with kokoro, soundfile and ffmpeg (`FFMPEG=` to point at another ffmpeg). Tested with manim 0.22.1.

Self-test from zero, in a throwaway copy: `tests/run.sh`. It makes voice, renders the mini film and checks that the length matches.
