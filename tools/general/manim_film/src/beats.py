"""Reading beats (stdlib only, used by voice, engine, gate and the checks).

A beat in beats/<key>_beats.json is either a plain string (old films) or an object:
    {"say": "As the cut off {knob} rises ...", "role": "guess", "pause": 5}
  say    the spoken text. {name} marks the next word: in the chapter, self.at("name") waits until that word is spoken.
  role   optional script role: question, guess, fails, idea, example, predict, reveal, recap (script_check.py reads it).
  pause  optional seconds of silence after the speech, e.g. for a pause-and-predict countdown.
Written words are turned into their spoken form with pronounce.json (whole words, case-sensitive) before the voice step.
"""
import json, re
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent
MARK = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")
WORD = re.compile(r"[A-Za-z0-9']+")


def lexicon():
    p = TOOL / "pronounce.json"
    if not p.exists(): return {}
    d = json.loads(p.read_text()); return {**d.get("unheard", {}), **d.get("confirmed", {})}


def load(film, key):
    """All beats of one chapter as dicts with say, role, pause and raw (the text that decides whether the voice is redone)."""
    out = []
    for b in json.loads((Path(film) / f"beats/{key}_beats.json").read_text()):
        if isinstance(b, str): out.append({"say": b, "role": None, "pause": 0.0, "raw": b})
        else: out.append({"say": b["say"], "role": b.get("role"), "pause": float(b.get("pause", 0)), "raw": json.dumps(b, sort_keys=True)})
    return out


def keys(film):
    return [l.split()[2] for l in (Path(film) / "chapters.txt").read_text().splitlines() if l.strip()]


def respell(text, lex=None):
    lex = lexicon() if lex is None else lex
    for w in sorted(lex, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9_]){re.escape(w)}(?![A-Za-z0-9_])", lex[w], text)
    return text


def spoken(text, lex=None):
    """-> (text for the voice, {mark: index of the word it stands before}). Markers are removed, the lexicon applied."""
    parts = MARK.split(text); clean, marks, n = [], {}, 0
    for j, part in enumerate(parts):
        if j % 2: marks[part] = n; continue
        part = respell(part, lex); clean.append(part); n += len(WORD.findall(part))
    return re.sub(r"\s{2,}", " ", "".join(clean)).strip(), marks


def plain(text):
    """Spoken text without markers, for checks that read the words."""
    return spoken(text)[0]
