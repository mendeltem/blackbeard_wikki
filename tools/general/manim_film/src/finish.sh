#!/bin/bash
# finish.sh <film folder> <final name>   (RES=1080p30 after a W=1920 H=1080 render)  Joins each chapter's picture with its voice, then all chapters. Run after the full render.
set -e; cd "$1"; FF=${FFMPEG:-$HOME/miniconda3/envs/tts/bin/ffmpeg}; mkdir -p video; : > video/list.txt; i=0
while read -r _ n k; do
  [ -n "$k" ] || continue; i=$((i+1)); v=$(ls media/videos/*/${RES:-720p30}/"$n".mp4); list=$(mktemp)
  for w in $(ls audio_beats/"$k"_*.wav | sed -E 's/.*_([0-9]+)\.wav/\1/' | sort -n); do echo "file '$PWD/audio_beats/${k}_$w.wav'" >> "$list"; done
  out=video/$(printf %02d $i)_$k.mp4; "$FF" -nostdin -loglevel error -y -i "$v" -f concat -safe 0 -i "$list" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 128k -shortest -movflags +faststart "$out"; echo "file '$PWD/$out'" >> video/list.txt; rm "$list"
done < chapters.txt
"$FF" -loglevel error -y -f concat -safe 0 -i video/list.txt -c copy -movflags +faststart "video/$2.mp4"; ls -la "video/$2.mp4"
