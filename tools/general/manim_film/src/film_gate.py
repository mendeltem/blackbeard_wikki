"""Automatic quality gate for a film. Exit 0 = passes. It measures what can be measured; a person still watches and decides.
    AUDIT=1 Q=low render.sh <film>; python film_gate.py <film> [source.md]"""
import json, re, sys
from pathlib import Path
F = Path(sys.argv[1]).resolve(); src = Path(sys.argv[2]).read_text() if len(sys.argv) > 2 else None
LIMITS = dict(problems=0, rings_per_5min=3, late_seconds=2.5, max_still_seconds=14, min_lit_per_beat=1.0, max_clears_per_beat=.65, min_fill=.3, min_motion_share=.22)
keys = [l.split()[2] for l in (F / "chapters.txt").read_text().splitlines() if l.strip()]; A = []
for k in keys:
    p = F / f"check/{k}.audit.json"
    if not p.exists(): print("FAIL no audit for", k, "(a crash, or render without AUDIT=1)"); sys.exit(1)
    A.append(json.loads(p.read_text()))
sec = sum(a["seconds"] for a in A); beats = sum(a["beats"] for a in A); problems = sorted({x for a in A for x in a["problems"]}); still = moving = 0
for a in A:
    last = 0
    for s, e in a["plays"]:
        still = max(still, s - last); moving += e - s; last = e
    still = max(still, a["seconds"] - last)
lit = sum(a["lit"] for a in A); fills = [x for a in A for x in a["fill"]]
m = dict(problems=len(problems), rings_per_5min=round(sum(a["rings"] for a in A) / sec * 300, 2), late_seconds=round(max(a["late"] for a in A), 2), max_still_seconds=round(still, 1), min_lit_per_beat=round(lit / beats, 2), max_clears_per_beat=round(sum(a["clears"] for a in A) / beats, 2), min_fill=round(sum(fills) / max(len(fills), 1), 3), min_motion_share=round(moving / sec, 3))
bad = [k for k, v in LIMITS.items() if (m[k] < v if k.startswith("min_") else m[k] > v)]
if src is not None:
    words = " ".join(" ".join(json.loads((F / f"beats/{k}_beats.json").read_text())) for k in keys) + " " + " ".join(s for p in F.glob("chapters*.py") for s in re.findall(r'(?:T|Box|self\.say)\("([^"]*)"', p.read_text()))
    known = set(re.findall(r"\d[\d,.]*\d|\d", src)); new = sorted(set(re.findall(r"\d[\d,.]*\d|\d", words)) - known); m["numbers_not_in_source"] = new
    if new: bad.append("numbers_not_in_source")
print(json.dumps({"seconds": round(sec), "beats": beats, "measured": m, "limits": LIMITS, "failed": bad}, indent=1)); [print(" ", p) for p in problems[:40]]; print("PASS" if not bad else "FAIL: " + ", ".join(bad)); sys.exit(1 if bad else 0)
