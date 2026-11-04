#!/bin/bash
# render.sh <film folder>   Every chapter in chapters.txt, at most 4 at a time, CPU only. Q=low: quick check render.
export FILM_DIR=$(realpath "$1"); T=$(dirname "$(realpath "$0")"); export PYTHONPATH=$T:$FILM_DIR OMP_NUM_THREADS=1 CUDA_VISIBLE_DEVICES=""; M=${MANIM:-$HOME/miniconda3/envs/manim/bin/manim}; cd "$FILM_DIR"; mkdir -p check
if [ "$Q" = low ]; then export W=640 H=360 FPS=12; fi
grep -E "${ONLY:-.}" chapters.txt | xargs -P 4 -L 1 sh -c '"$0" render --disable_caching --format mp4 --media_dir media -o "$2" "$1" "$2" > "check/$2.log" 2>&1; echo "$2 exit $?"; grep -E "LATE|Error" "check/$2.log" | head -8' "$M"
