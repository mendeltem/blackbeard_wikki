"""Voice for every beat (Kokoro; GPU when one is free, else CPU). Beats whose text did not change are skipped.   python voice.py <film folder>   (env tts)
Since 2026-11-09 it also keeps the time of every word (Kokoro token timestamps), so a chapter can wait for a word marked {name}
(self.at("name")), and it adds the silence a beat asks for ("pause"). Spoken forms come from pronounce.json (beats.py)."""
import os, sys, json, difflib
from pathlib import Path
import numpy as np, soundfile as sf
sys.path.insert(0, str(Path(__file__).resolve().parent))
import beats as B
from kokoro import KPipeline
SR, TAIL = 24000, .45


def _device():
    # 06.11.2026: Kokoro on the GPU when one is free (much faster); KOKORO_DEVICE=cpu forces the old behaviour
    want = os.environ.get("KOKORO_DEVICE", "")
    if want:
        return want
    try:
        import torch
        if torch.cuda.is_available() and torch.cuda.mem_get_info()[0] > 2 * 1024**3:
            return "cuda"
    except Exception:  # noqa: BLE001
        pass
    return "cpu"


def norm(w):
    return "".join(c for c in w.lower() if c.isalnum())


def speak(pipe, text):
    """-> (audio, [[word, start, end], ...]) with times from the start of the beat."""
    parts, words, off = [], [], 0.0
    for r in pipe(text, voice=os.environ.get("VOICE", "af_heart"), speed=float(os.environ.get("SPEED", 1.0))):
        a = np.asarray(r.audio); parts.append(a)
        for t in (r.tokens or []):
            if norm(t.text) and t.start_ts is not None: words.append([t.text, round(off + t.start_ts, 3), round(off + (t.end_ts or t.start_ts), 3)])
        off += len(a) / SR
    return (np.concatenate(parts) if parts else np.zeros(1, np.float32)), words


def mark_times(text, marks, words):
    """Word index in our text -> time of the matching Kokoro word (difflib alignment; numbers and odd tokens may split)."""
    ours = [norm(w) for w in B.WORD.findall(text)]; theirs = [norm(w[0]) for w in words]; at = {}
    for a, b, n in difflib.SequenceMatcher(None, ours, theirs, autojunk=False).get_matching_blocks():
        for k in range(n): at[a + k] = words[b + k][1]
    out = {}
    for name, i in marks.items():
        later = [at[j] for j in range(i, len(ours)) if j in at]; out[name] = later[0] if later else (words[-1][2] if words else 0.0)
    return out


if __name__ == "__main__":
    F = Path(sys.argv[1]).resolve(); (F / "audio_beats").mkdir(exist_ok=True); path = F / "audio_beats/state.json"; st = json.loads(path.read_text()) if path.exists() else {}
    pipe = KPipeline(lang_code="a", device=_device(), repo_id="hexgrad/Kokoro-82M"); lex = B.lexicon()
    for key in B.keys(F):
        for i, b in enumerate(B.load(F, key)):
            name = f"{key}_{i}.wav"; text, marks = B.spoken(b["say"], lex)
            if st.get(name, {}).get("text") == b["raw"] and st[name].get("spoken") in (None, text): continue
            y, words = speak(pipe, text); speech = len(y) / SR
            y = np.concatenate([y, np.zeros(int(SR * (TAIL + b["pause"])), np.float32)]); sf.write(F / "audio_beats" / name, y, SR)
            st[name] = {"seconds": len(y) / SR, "speech": round(speech, 3), "text": b["raw"], "spoken": text, "words": words, "marks": mark_times(text, marks, words)}
            print(name, round(speech, 1), "s", f"marks {st[name]['marks']}" if marks else "", flush=True)
    path.write_text(json.dumps(st)); print("seconds", round(sum(v["seconds"] for v in st.values())))
