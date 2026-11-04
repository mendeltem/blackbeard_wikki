#!/bin/bash
# Self-test: voice, check render, sheets, full render and final film for tests/mini in a throwaway folder.
set -e; R=$(dirname "$(realpath "$0")")/..; D=$(mktemp -d "$HOME/.manim_film_test.XXXX"); cp -r "$R/tests/mini/." "$D/"; TTS=${TTS:-$HOME/miniconda3/envs/tts}; MP=${MANIM_ENV:-$HOME/miniconda3/envs/manim}
CUDA_VISIBLE_DEVICES="" HF_HUB_OFFLINE=1 OMP_NUM_THREADS=4 "$TTS/bin/python" -W ignore "$R/src/voice.py" "$D" 2>&1 | tail -1
Q=low "$R/src/render.sh" "$D"; "$MP/bin/python" "$R/src/sheets.py" "$D"; rm -rf "$D/media"; "$R/src/render.sh" "$D"; "$R/src/finish.sh" "$D" final
want=$(python3 -c "import json;print(sum(v['seconds'] for v in json.load(open('$D/audio_beats/state.json')).values()))"); got=$("$TTS/bin/ffmpeg" -i "$D/video/final.mp4" 2>&1 | grep -oE 'Duration: [0-9:.]+' | cut -d' ' -f2 | awk -F: '{print $1*3600+$2*60+$3}')
python3 -c "import sys;a,b=$want,$got;print('audio',round(a,2),'film',b);sys.exit(0 if abs(a-b)<.25 else 1)"; rm -rf "$D"; echo PASSED
