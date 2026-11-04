"""Contact sheets: frames at 55 % and 97 % of every beat. Look at them before the full render.   python sheets.py <film folder>   (env manim)"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image
H = Path(sys.argv[1]).resolve(); st = json.loads((H / "audio_beats/state.json").read_text()); FF = sys.argv[2] if len(sys.argv) > 2 else str(Path.home() / "miniconda3/envs/tts/bin/ffmpeg")
for line in (H / "chapters.txt").read_text().split("\n"):
    if not line.strip(): continue
    _, name, key = line.split(); v = next(iter(H.glob(f"media/videos/**/{name}.mp4")), None)
    if v is None: print("missing", name); continue
    t = 0; ims = []
    for i in range(len(json.loads((H / f"beats/{key}_beats.json").read_text()))):
        s = st[f"{key}_{i}.wav"]["seconds"]
        for share in (.55, .97):
            out = H / f"check/{name}_{i}_{int(share * 100)}.png"; subprocess.run([FF, "-loglevel", "error", "-y", "-ss", str(t + s * share), "-i", str(v), "-frames:v", "1", str(out)], check=True); ims.append(Image.open(out).convert("RGB") if out.exists() else ims[-1])   # the very end of a short film may hold no frame
        t += s
    w, h = ims[0].size; sheet = Image.new("RGB", (2 * w + 6, len(ims) // 2 * (h + 6)), "#444")
    for j, im in enumerate(ims):
        sheet.paste(im, ((j % 2) * (w + 6), (j // 2) * (h + 6)))
    sheet.save(H / f"check/sheet_{name}.png"); print(name, sheet.size)
