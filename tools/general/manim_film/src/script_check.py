"""Script check before the voice step (2026-11-09).   python script_check.py <film folder> [--no-reader] [--only key1,key2] [--context earlier,keys]   (any python 3)

1. Shape. A teaching chapter follows: question -> guess (the intuitive wrong idea) -> fails (why it breaks) -> idea ->
   example (real numbers) -> recap; a "predict" beat (pause and predict) may replace the guess, "reveal" answers it.
   Beats carry this as "role". Checked: every chapter opens with a question, ends with a recap, and the film has a
   wrong idea that is broken (guess + fails, or predict + reveal) in at least every second chapter.
2. Pace. Spoken words per minute per beat (needs voice.py): flagged outside 120-175.
3. Novice reader. A first-year student model (Cle, alias frontier) reads the whole script and lists jargon used before it
   is explained, missing "why", jumps, and sentences that are hard to follow by ear. The script leaves Alita for the
   Charite hub: pass --no-reader for any film whose narration names patients, case IDs or unpublished cohort numbers.
Writes check/script_check.md. Exit 1 when the shape fails.
"""
import json, os, re, ssl, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import beats as B

F = Path(sys.argv[1]).resolve(); arg = lambda n, d=None: sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
ONLY = set(arg("--only", "").split(",")) - {""}; keys = [k for k in B.keys(F) if not ONLY or k in ONLY]
st = json.loads((F / "audio_beats/state.json").read_text()) if (F / "audio_beats/state.json").exists() else {}
out, bad, broken = [f"# Script check: {F.name}", ""], [], 0

out += ["## Shape", "", "| chapter | roles | problems |", "|---|---|---|"]
for k in keys:
    bs = B.load(F, k); roles = [b["role"] or "-" for b in bs]; p = []
    if roles[0] not in ("question", "predict"): p.append("does not open with a question")
    if roles[-1] != "recap": p.append("no recap at the end")
    if ("guess" in roles and "fails" in roles) or ("predict" in roles and "reveal" in roles): broken += 1
    if "predict" in roles and not any(b["pause"] >= 3 for b in bs if b["role"] == "predict"): p.append("predict beat without a pause of 3 s or more")
    if p: bad.append(k)
    out.append(f"| {k} | {' > '.join(roles)} | {'; '.join(p) or 'ok'} |")
need = (len(keys) + 1) // 2
out += ["", f"Wrong idea broken in {broken} of {len(keys)} chapters (need {need})."]
if broken < need: bad.append("too few wrong ideas broken")

out += ["", "## Pace (spoken words per minute)", ""]
slow = []
for k in keys:
    for i, b in enumerate(B.load(F, k)):
        s = st.get(f"{k}_{i}.wav"); n = len(B.WORD.findall(B.plain(b["say"])))
        if s and s.get("text") == b["raw"] and n > 6:          # only a voice made from this very text
            wpm = n / max(s.get("speech", s["seconds"] - .45), .1) * 60
            if not 120 <= wpm <= 175: slow.append(f"- {k} beat {i}: {wpm:.0f} words per minute")
out += slow or ["all beats between 120 and 175 (or no voice yet)."]

if "--no-reader" not in sys.argv:
    script = "\n".join(f"[{k} {i}] {B.plain(b['say'])}" for k in keys for i, b in enumerate(B.load(F, k)))
    ctx = [k for k in arg("--context", "").split(",") if k]   # chapters the listener heard before (explained there): context only, not checked
    if ctx: script = "ALREADY HEARD EARLIER IN THE FILM (terms explained here count as known; do not report these lines):\n" + "\n".join(B.plain(b["say"]) for k in ctx for b in B.load(F, k)) + "\n\nCHECK THIS PART:\n" + script
    ask = ("You are a first-year medical student who knows basic anatomy but no image analysis or statistics. You HEAR this film "
           "narration once, without seeing the pictures. List the places where you would get lost. Types: jargon (a term used before it is explained), "
           "why (a step is done but the reason is not given), jump (a missing link between two sentences), ear (a sentence too long or nested to follow by ear), "
           "number (a number without what it counts). Be strict but list only real problems, at most 15, most serious first. "
           'Answer ONLY a JSON list: [{"where": "<chapter> <beat>", "type": "...", "quote": "<few words>", "fix": "<short suggestion>"}]\n\nNARRATION:\n' + script)
    key = (Path.home() / ".config/cle/api_key").read_text().strip(); os.environ["NO_PROXY"] = "cle.charite.de"
    req = urllib.request.Request("https://cle.charite.de/api/chat/completions", json.dumps({"model": arg("--model", "frontier"), "messages": [{"role": "user", "content": ask}], "max_tokens": 6000, "temperature": .2, "stream": True, "chat_template_kwargs": {"enable_thinking": False}}).encode(),
                                 {"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    txt = ""   # streamed: the hub cuts a silent call after about 50 s
    for line in op.open(req, timeout=300):
        line = line.decode().strip()
        if line.startswith("data:") and line[5:].strip() not in ("", "[DONE]"):
            ch = json.loads(line[5:]).get("choices") or [{}]; txt += (ch[0].get("delta", {}).get("content") or "")
    m = re.search(r"\[.*\]", txt, re.S)
    try: items = json.loads(m.group(0)) if m else None
    except ValueError: items = None
    cut = items is None
    if cut: items = [json.loads(x) for x in re.findall(r"\{[^{}]*\}", txt) if x.strip().startswith('{"') or '"where"' in x]   # answer cut off: keep the complete items
    (F / "check").mkdir(exist_ok=True); (F / "check/script_reader_raw.txt").write_text(txt)   # the raw answer, to see what the reader said
    out += ["", f"## Novice reader ({arg('--model', 'frontier')} on Cle; a hint list, the author decides)", "", "| where | type | quote | fix |", "|---|---|---|---|"]
    if cut: out.append("(the reader's answer was cut off or not clean JSON; complete items kept, see check/script_reader_raw.txt)")
    out += [f"| {x.get('where')} | {x.get('type')} | {x.get('quote')} | {x.get('fix')} |" for x in items] or ["| - | - | nothing found | - |"]

out += ["", "PASS" if not bad else "FAIL: " + ", ".join(bad)]
(F / "check").mkdir(exist_ok=True); (F / "check/script_check.md").write_text("\n".join(out) + "\n"); print("\n".join(out)); sys.exit(1 if bad else 0)
