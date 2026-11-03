"""Step 1: one audio file per slide, with Kokoro-82M on the CPU.

    CUDA_VISIBLE_DEVICES="" python speech.py <deck folder> [--force true]

The deck folder holds slides.py (list SLIDES, see tests/example_deck). Skips slides whose text did not change.
Writes audio/slideNN.mp3 and audio/durations.json. Needs kokoro, soundfile, ffmpeg with libmp3lame.
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline

p = argparse.ArgumentParser()
p.add_argument("deck")
p.add_argument("--voice", default="af_heart")
p.add_argument("--lang", default="a", help="Kokoro language code, a = American English")
p.add_argument("--force", default="false")
args = p.parse_args()
HERE = Path(args.deck).resolve()
sys.path.insert(0, str(HERE))
from slides import SLIDES

FFMPEG = shutil.which("ffmpeg") or Path(sys.executable).parent / "ffmpeg"
(HERE / "audio").mkdir(exist_ok=True)
state_file = HERE / "audio/durations.json"
state = json.loads(state_file.read_text()) if state_file.exists() else {}
pipe = KPipeline(lang_code=args.lang, device="cpu")
for i, s in enumerate(SLIDES, 1):
    name = f"slide{i:02d}.mp3"
    key = hashlib.md5(s["speech"].encode()).hexdigest()
    if args.force != "true" and state.get(name, {}).get("key") == key and (HERE / "audio" / name).exists():
        continue
    parts = [np.asarray(a) for _, _, a in pipe(s["speech"], voice=args.voice, speed=1.0)]
    y = np.concatenate(parts + [np.zeros(int(24000 * .3), np.float32)])
    wav = HERE / "audio/tmp.wav"
    sf.write(wav, y, 24000)
    subprocess.run([str(FFMPEG), "-loglevel", "error", "-y", "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "64k", str(HERE / "audio" / name)], check=True)
    wav.unlink()
    state[name] = {"key": key, "seconds": round(len(y) / 24000, 1)}
    print(name, state[name]["seconds"], "s", flush=True)
state_file.write_text(json.dumps(state, indent=1))
print(f"total {sum(v['seconds'] for v in state.values()) / 60:.1f} min")
