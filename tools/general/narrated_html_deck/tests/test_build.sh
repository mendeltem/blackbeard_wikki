#!/bin/bash
# From zero: example deck -> audio -> page, in a temporary copy.  bash tests/test_build.sh <python with kokoro>
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"; PY="${1:-python}"; D="$(mktemp -d)"; trap 'rm -rf "$D"' EXIT
cp "$HERE/tests/example_deck/slides.py" "$D/"
CUDA_VISIBLE_DEVICES="" "$PY" "$HERE/src/speech.py" "$D"
"$PY" "$HERE/src/build_html.py" "$D" --title "Example deck"
test "$(ls "$D"/audio/*.mp3 | wc -l)" = 2
grep -q "audio/slide02.mp3" "$D/index.html"
A=$(stat -c %Y "$D/audio/slide01.mp3"); CUDA_VISIBLE_DEVICES="" "$PY" "$HERE/src/speech.py" "$D"; test "$A" = "$(stat -c %Y "$D/audio/slide01.mp3")"
echo "OK: 2 audio files, page refers to them, unchanged text is not re-spoken"
