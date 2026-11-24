#!/bin/bash
# new_film.sh <film folder> <key1> [key2 ...]   Skeleton of a film: source.md, beats/<key>_beats.json (six roles), chapters.py, chapters.txt.
# One key per chapter, lower case (letters, digits, _). Refuses to write into a folder that already exists.
set -e
[ $# -ge 2 ] || { echo "usage: new_film.sh <film folder> <key1> [key2 ...]"; exit 2; }
D=$1; shift
[ -e "$D" ] && { echo "exists already, nothing written: $D"; exit 1; }
for k in "$@"; do [[ $k =~ ^[a-z][a-z0-9_]*$ ]] || { echo "bad key (lower case letters, digits, _): $k"; exit 2; }; done
mkdir -p "$D/beats"
cat > "$D/source.md" <<'S'
# Source

Every number, name and label the film says or shows stands here first, each with where it comes from. The gate compares the film against this file.

## Facts

- TODO: fact with its number (source 1)

## Sources

- TODO: Author, year, title. https://...
S
printf '"""TODO film title: each chapter says what happens when. Read MAKE_A_FILM.md in the tool folder before writing."""\nfrom engine import *\n' > "$D/chapters.py"
: > "$D/chapters.txt"; n=0
for k in "$@"; do
  n=$((n + 1)); cls=$(echo "$k" | sed -E 's/(^|_)([a-z0-9])/\U\2/g')
  cat > "$D/beats/${k}_beats.json" <<'J'
[
 {"say": "TODO question: what are we trying to find out?", "role": "question"},
 {"say": "TODO guess: the first idea most people have, said kindly.", "role": "guess"},
 {"say": "TODO fails: why that idea breaks, with a number from source.md.", "role": "fails"},
 {"say": "TODO idea: the thing that works. Put {mark} before a word a picture must wait for.", "role": "idea"},
 {"say": "TODO example: real numbers from source.md.", "role": "example"},
 {"say": "TODO recap: one sentence for the picture that sums it up.", "role": "recap"}
]
J
  cat >> "$D/chapters.py" <<P


class $cls(Film):
    key = "$k"; number = $n; title = "TODO"

    def construct(self):
        self.beat(0); self.open()   # question: one idea on screen
        self.beat(1)                # guess
        self.beat(2)                # fails
        self.beat(3)                # idea: self.at("mark") waits for the marked word
        self.beat(4)                # example
        self.beat(5)                # recap: the picture that sums it up
        self.finish()
P
  echo "chapters.py $cls $k" >> "$D/chapters.txt"
done
echo "made $D with $n chapter(s): fill source.md first, then the beats"
