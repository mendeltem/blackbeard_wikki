"""Automatic quality gate for a film. Exit 0 = passes. It measures what can be measured; a person still watches and decides.
    AUDIT=1 Q=low render.sh <film>; python film_gate.py <film> [source.md]"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); import beats as B
F = Path(sys.argv[1]).resolve(); src = Path(sys.argv[2]).read_text() if len(sys.argv) > 2 else None
LIMITS = dict(problems=0, rings_per_5min=3, late_seconds=2.5, max_still_seconds=14, min_lit_per_beat=1.0, max_clears_per_beat=.5, min_fill=.3, min_motion_share=.22, off_centre_share=.25, min_travel_per_minute=.5)
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
m = dict(problems=len(problems), rings_per_5min=round(sum(a["rings"] for a in A) / sec * 300, 2), late_seconds=round(max(a["late"] for a in A), 2), max_still_seconds=round(still, 1), min_lit_per_beat=round(lit / beats, 2), max_clears_per_beat=round(sum(a["clears"] for a in A) / beats, 2), min_fill=round(sum(fills) / max(len(fills), 1), 3), min_motion_share=round(moving / sec, 3), min_travel_per_minute=round(sum(a.get("travel", 0) for a in A) / sec * 60, 2), marks_used=sum(a.get("marks_used", 0) for a in A), predicts=sum(a.get("predicts", 0) for a in A), off_centre_share=round(sum(x > .35 for a in A for x in a.get("off", [])) / max(sum(len(a.get("off", [])) for a in A), 1), 3))
bad = [k for k, v in LIMITS.items() if (m[k] < v if k.startswith("min_") else m[k] > v)]
if src is not None:
    words = " ".join(B.MARK.sub("", b["say"]) for k in keys for b in B.load(F, k)) + " " + " ".join(s for p in F.glob("chapters*.py") for s in re.findall(r'(?:T|Box|self\.say)\("([^"]*)"', p.read_text()))
    known = set(re.findall(r"\d[\d,.]*\d|\d", src)); new = sorted(set(re.findall(r"\d[\d,.]*\d|\d", words)) - known); m["numbers_not_in_source"] = new
    if new: bad.append("numbers_not_in_source")
    comma = sorted(set(re.findall(r"\b0,\d+", words))); m["decimal_commas"] = comma
    if comma: bad.append("decimal_commas")
print(json.dumps({"seconds": round(sec), "beats": beats, "measured": m, "limits": LIMITS, "failed": bad}, indent=1)); [print(" ", p) for p in problems[:40]]; print("PASS" if not bad else "FAIL: " + ", ".join(bad)); sys.exit(1 if bad else 0)
