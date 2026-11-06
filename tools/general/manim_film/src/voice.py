"""Voice for every beat (Kokoro; GPU when one is free, else CPU). Beats whose text did not change are skipped.   python voice.py <film folder>   (env tts)"""
import os
import json, sys
from pathlib import Path
import numpy as np, soundfile as sf
from kokoro import KPipeline
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

F = Path(sys.argv[1]).resolve(); (F / "audio_beats").mkdir(exist_ok=True); path = F / "audio_beats/state.json"; st = json.loads(path.read_text()) if path.exists() else {}; pipe = KPipeline(lang_code="a", device=_device())
for line in (F / "chapters.txt").read_text().split("\n"):
    if not line.strip(): continue
    key = line.split()[2]
    for i, text in enumerate(json.loads((F / f"beats/{key}_beats.json").read_text())):
        name = f"{key}_{i}.wav"
        if st.get(name, {}).get("text") == text: continue
        y = np.concatenate([np.asarray(a) for _, _, a in pipe(text, voice="af_heart", speed=1.0)] + [np.zeros(int(24000 * .45), np.float32)]); sf.write(F / "audio_beats" / name, y, 24000); st[name] = {"seconds": len(y) / 24000, "text": text}
path.write_text(json.dumps(st)); print("seconds", round(sum(v["seconds"] for v in st.values())))
