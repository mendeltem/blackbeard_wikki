"""Voice for every beat (Kokoro, CPU). Beats whose text did not change are skipped.   python voice.py <film folder>   (env tts)"""
import json, sys
from pathlib import Path
import numpy as np, soundfile as sf
from kokoro import KPipeline
F = Path(sys.argv[1]).resolve(); (F / "audio_beats").mkdir(exist_ok=True); path = F / "audio_beats/state.json"; st = json.loads(path.read_text()) if path.exists() else {}; pipe = KPipeline(lang_code="a", device="cpu")
for line in (F / "chapters.txt").read_text().split("\n"):
    if not line.strip(): continue
    key = line.split()[2]
    for i, text in enumerate(json.loads((F / f"beats/{key}_beats.json").read_text())):
        name = f"{key}_{i}.wav"
        if st.get(name, {}).get("text") == text: continue
        y = np.concatenate([np.asarray(a) for _, _, a in pipe(text, voice="af_heart", speed=1.0)] + [np.zeros(int(24000 * .45), np.float32)]); sf.write(F / "audio_beats" / name, y, 24000); st[name] = {"seconds": len(y) / 24000, "text": text}
path.write_text(json.dumps(st)); print("seconds", round(sum(v["seconds"] for v in st.values())))
