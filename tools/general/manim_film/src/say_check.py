"""Pronunciation check before a film is shown (2026-11-09).   python say_check.py <film folder> [--no-audio]   (env tts, after voice.py)

Kokoro reads a word from its dictionary, or guesses it with espeak when the word is unknown; the guesses are where films
go wrong (a name like "Kuijf", a tool like "robustfov", a long term like "hyperintensities"). This lists, once per word:
  unknown   not in Kokoro's dictionary: espeak guessed it
  letters   capitals read letter by letter (WMH -> double-u em aitch): fine for real acronyms, wrong for names
  mixed     letters and digits mixed (T1, cu12)
  unheard   respelled by pronounce.json but never confirmed by the user
Words the user already confirmed (pronounce.json "confirmed" spoken forms and "ok") are left out.
Writes check/say_check.md (table with the phonemes) and check/say_check.mp3: for every word "word N" and then the
sentence around it, so the user can answer "3 is wrong, should sound like ...". Exit 1 while anything is listed.
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np, soundfile as sf
sys.path.insert(0, str(Path(__file__).resolve().parent))
import beats as B
from misaki import en

F = Path(sys.argv[1]).resolve(); AUDIO = "--no-audio" not in sys.argv; SR = 24000
P = json.loads((B.TOOL / "pronounce.json").read_text()); unheard = P.get("unheard", {})
fine = {w.lower() for w in P.get("ok", [])} | {x.lower() for v in P.get("confirmed", {}).values() for x in B.WORD.findall(v)}
strict = en.G2P(trf=False, british=False, fallback=None)            # unknown words come back with ❓
st = json.loads((F / "audio_beats/state.json").read_text()); seen, rows = set(), []

for key in B.keys(F):
    for i, b in enumerate(B.load(F, key)):
        text, _ = B.spoken(b["say"]); _, toks = strict(text); s = st.get(f"{key}_{i}.wav", {}); words = s.get("words", [])
        for w, v in unheard.items():   # respelled written forms that the user never confirmed: found in the written text
            if w.lower() in seen or not re.search(rf"(?<![A-Za-z0-9_]){re.escape(w)}(?![A-Za-z0-9_])", b["say"]): continue
            seen.add(w.lower()); first = B.WORD.findall(v)[0].lower(); hit = next((x for x in words if x[0].lower() == first), None)
            rows.append({"word": v, "why": "unheard", "written": w, "chapter": key, "beat": i, "at": hit[1] if hit else None, "end": hit[2] + 1.0 if hit else None, "speech": s.get("speech", s.get("seconds", 0))})
        for t in toks:
            w = t.text; lw = w.lower(); base = re.sub(r"'s$", "", lw)
            if not B.WORD.fullmatch(w) or lw in seen or lw in fine or base in fine: continue
            why = ("unknown" if (t.phonemes is None or "❓" in t.phonemes) else "letters" if re.fullmatch(r"[A-Z]{2,}s?", w) and len(t.phonemes or "") > 2 * len(w)
                   else "mixed" if re.search(r"[A-Za-z]\d|\d[A-Za-z]", w) else None)
            if not why: continue
            seen.add(lw); hit = next((x for x in words if x[0].lower() == lw), None)
            rows.append({"word": w, "why": why, "written": w, "chapter": key, "beat": i, "at": hit[1] if hit else None, "end": hit[2] if hit else None, "speech": s.get("speech", s.get("seconds", 0))})

if rows:
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a", device="cpu", repo_id="hexgrad/Kokoro-82M")
    for r in rows:
        r["phonemes"] = " ".join(x.phonemes or "?" for x in pipe.g2p(r["word"])[1] if x.phonemes)   # what the voice really used (espeak guess included)
order = {"unknown": 0, "letters": 1, "mixed": 2, "unheard": 3}; rows.sort(key=lambda r: (order[r["why"]], r["chapter"], r["beat"]))
(F / "check").mkdir(exist_ok=True)
md = [f"# Pronunciation check: {F.name}", "", f"{len(rows)} words to hear. Listen to `check/say_check.mp3` (each one: \"word N\", then its sentence) and answer like \"3 wrong, say it like ...\" or \"all fine\". "
      "Confirmed answers go into pronounce.json (confirmed / ok) and PRONUNCIATION.md.", "",
      "| N | word | why | phonemes the voice used | chapter, beat, second |", "|---|---|---|---|---|"]
for n, r in enumerate(rows, 1):
    md.append(f"| {n} | {r['word']}" + (f" (for {r['written']})" if r["written"] != r["word"] else "") + f" | {r['why']} | `{r['phonemes']}` | {r['chapter']} {r['beat']}, {r['at'] if r['at'] is not None else '?'} |")
md += ["", "Why: unknown = espeak guessed it; letters = read letter by letter; mixed = letters with digits; unheard = respelled but never confirmed."]
(F / "check/say_check.md").write_text("\n".join(md) + "\n"); print("\n".join(md))

if AUDIO and rows:
    out = []
    for n, r in enumerate(rows, 1):
        lab = np.concatenate([np.asarray(x.audio) for x in pipe(f"Word {n}.", voice="am_michael")]); out += [lab, np.zeros(int(SR * .35), np.float32)]
        y, _ = sf.read(F / "audio_beats" / f"{r['chapter']}_{r['beat']}.wav", dtype="float32")
        a = 0 if r["at"] is None else max(0, r["at"] - 1.6); e = r["speech"] if r["end"] is None else min(r["speech"], r["end"] + 1.2)
        out += [y[int(a * SR):int(e * SR)], np.zeros(int(SR * .9), np.float32)]
    wav = F / "check/say_check.wav"; sf.write(wav, np.concatenate(out), SR)
    ff = str(Path.home() / "miniconda3/envs/tts/bin/ffmpeg"); subprocess.run([ff, "-loglevel", "error", "-y", "-i", str(wav), "-b:a", "96k", str(F / "check/say_check.mp3")], check=True); wav.unlink()
    print("listen:", F / "check/say_check.mp3")
sys.exit(1 if rows else 0)
