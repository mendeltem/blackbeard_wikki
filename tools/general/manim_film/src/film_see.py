"""Lets an agent look at its own film: frames of every beat go to a vision model, which reports what it sees. Public films only.
    python film_see.py <film folder> --public [--model vision] [--only chapter_key] [--max-beats N]    (env manim)
Exit 0 = no confirmed flaw and the eye is working; 1 = confirmed flaws, see check/see_report.md; 2 = the eye failed its planted flaws, so "no flaw" would mean nothing.
Every run also shows the model frames with flaws drawn in on purpose. A missed plant fails the run. The tool sees still frames in order; it does not hear the voice and it cannot judge beauty.
Own calibration 2026-11-04: on an approved film most raw answers were false alarms from frames caught mid-animation. So a layout flaw counts only if a second look at the settled frame at the end of the beat confirms it; "mismatch", "empty" and "misleading_chart" stay hints for the agent and never fail a film."""
import base64, io, json, os, random, re, subprocess, sys, time, urllib.request
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); import beats as B   # 09.11.2026: beats may be objects
from PIL import Image, ImageDraw, ImageFont
F = Path(sys.argv[1]).resolve(); arg = lambda n, d=None: sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
MODEL = arg("--model", "vision"); ONLY = arg("--only"); MAX = int(arg("--max-beats", 0)); PLANTS = 3; FF = os.environ.get("FFMPEG", str(Path.home() / "miniconda3/envs/tts/bin/ffmpeg"))
KEY = os.environ.get("CLE_API_KEY") or (Path.home() / ".config/cle/api_key").read_text().strip() if os.environ.get("CLE_API_KEY") or (Path.home() / ".config/cle/api_key").exists() else None
URL = os.environ.get("FILM_SEE_URL") or ("https://cle.charite.de/api/chat/completions" if KEY else "http://127.0.0.1:8770/v1/chat/completions")
beats_all = " ".join(p.read_text() for p in F.glob("beats/*.json"))
if "--public" not in sys.argv: sys.exit("film_see sends frames to the hub. Say --public only for a film without patient data.")
if any(next(F.rglob(x), None) for x in ("*.nii", "*.nii.gz", "*.dcm")) or re.search(r"\bsub-[A-Za-z0-9]+", beats_all) or str(F).startswith((str(Path.home() / "data") + "/", "/media/")): sys.exit("Refused: this folder looks like patient data.")
ASK = """These are 4 moments, in time order, from one short beat of an animated explanation film (top left, top right, bottom left, bottom right).
The voice says in this beat: "%s"
Look hard. Report only what you can see. Kinds of flaw: overlap (text on text, box on box), line_through_text, cut_off (anything past the frame edge), unreadable (too small, too faint, poor contrast), misleading_chart (a picture that suggests something false, unlabelled or confusing amounts), empty (most of the frame unused without reason), mismatch (the picture does not show what the voice says).
A word that is fading in or out for one moment is not a flaw. Answer with JSON only: {"flaws":[{"kind":"...","where":"which moment and where","fix":"one short concrete fix"}]}. No flaw: {"flaws":[]}."""
HARD = ("overlap", "line_through_text", "cut_off", "unreadable")  # misleading_chart stays a hint: all 3 confirmed cases were true-scale charts or dot grids the model miscounted
CHECK = """This is one settled frame of an animated film. Another reader claims: %s flaw, at "%s". Fix proposed: "%s".
Look only at this frame and be sceptical. Is that flaw clearly visible here? Answer with JSON only: {"flaws":[{"kind":"%s"}]} if it is clearly there, {"flaws":[]} if not."""
op = urllib.request.build_opener(urllib.request.ProxyHandler({})); used = Counter()


def ask(img, text):
    b = io.BytesIO(); img.save(b, "PNG"); body = {"model": MODEL, "max_tokens": 700, "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}, "messages": [{"role": "user", "content": [{"type": "text", "text": text}, {"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()}}]}]}
    head = {"Content-Type": "application/json"}; head.update({"Authorization": "Bearer " + KEY} if KEY else {}); last = None
    for wait in (0, 5, 20):
        time.sleep(wait)
        try:
            o = json.load(op.open(urllib.request.Request(URL, data=json.dumps(body).encode(), headers=head), timeout=180)); c = o["choices"][0]["message"]["content"] or ""; m = re.search(r"\{.*\}", c, re.S); used["calls"] += 1
            if m: return json.loads(m.group(0)).get("flaws", [])
            last = "no JSON: " + c[:80]
        except Exception as e: last = str(e)[:120]
    raise RuntimeError(f"model did not answer: {last}")


def frame(video, t):
    p = subprocess.run([FF, "-nostdin", "-v", "error", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(p)).convert("RGB").resize((640, 360))


def strip(ims):
    s = Image.new("RGB", (1286, 726), "#555")
    for i, m in enumerate(ims): s.paste(m, ((i % 2) * 646, (i // 2) * 366))
    return s


def plant(ims, rng):
    """Draws a flaw that is really there: a line through a word and a sentence on top of the picture, in all 4 moments."""
    out = []; x = rng.randint(40, 200); y = rng.randint(90, 240); col = rng.choice([(255, 60, 60), (255, 255, 255), (255, 230, 0)])
    try: f = ImageFont.truetype("DejaVuSans-Bold.ttf", 30)
    except OSError: f = ImageFont.load_default()
    for m in ims:
        c = m.copy(); d = ImageDraw.Draw(c); d.text((x, y), "OVERLAPPING WORDS HERE", font=f, fill=col); d.text((x + 14, y + 12), "MORE WORDS ON TOP", font=f, fill=col); d.line([(20, y + 30), (620, y - 30)], fill=col, width=5); out.append(c)
    return out


st = json.loads((F / "audio_beats/state.json").read_text()); rows = []; strips = []; (F / "check").mkdir(exist_ok=True)
for line in (F / "chapters.txt").read_text().splitlines():
    if not line.strip(): continue
    _, name, key = line.split()
    if ONLY and key != ONLY: continue
    vids = sorted(F.glob(f"media/videos/**/{name}.mp4"), key=lambda p: p.stat().st_mtime)
    if not vids: sys.exit(f"no video for {name}: render first")
    texts = [B.plain(b["say"]) for b in B.load(F, key)]; t = 0
    for i, spoken in enumerate(texts):
        s = st[f"{key}_{i}.wav"]["seconds"]; strips.append((key, i, spoken, [frame(vids[-1], t + s * x) for x in (.25, .5, .75, .97)])); t += s
if MAX: strips = strips[:MAX]
rng = random.Random(len(strips)); caught = 0; pick = rng.sample(strips, min(PLANTS, len(strips)))
for key, i, spoken, ims in pick:
    fl = ask(strip(plant(ims, rng)), ASK % spoken); hit = any(x.get("kind") in ("overlap", "line_through_text") for x in fl); caught += hit; print(f"plant {key} beat {i}: {'caught' if hit else 'MISSED'}", flush=True)
eye_ok = caught == len(pick)
for key, i, spoken, ims in strips:
    fl = ask(strip(ims), ASK % spoken); end = ims[-1].resize((1280, 720), Image.LANCZOS)
    for x in fl:
        x["confirmed"] = x.get("kind") in HARD and bool(ask(end, CHECK % (x.get("kind"), x.get("where"), x.get("fix"), x.get("kind"))))
    rows.append({"chapter": key, "beat": i, "voice": spoken, "flaws": fl}); print(f"{key} beat {i}: {sum(x['confirmed'] for x in fl)} confirmed, {len(fl)} raw", flush=True)
kinds = Counter(x.get("kind", "?") for r in rows for x in r["flaws"] if x["confirmed"]); hints = sum(not x["confirmed"] for r in rows for x in r["flaws"]); n = sum(kinds.values())
(F / "check/see.json").write_text(json.dumps({"model": MODEL, "plants": len(pick), "caught": caught, "beats": len(rows), "flaws": n, "hints": hints, "kinds": kinds, "rows": rows}, indent=1))
rep = [f"# What the vision model saw ({MODEL})", f"Eye check: {caught} of {len(pick)} planted flaws caught.", f"{len(rows)} beats, {n} confirmed flaws: {dict(kinds)}. {hints} hints.", "", "## Confirmed: fix these"]
line = lambda r, x: f"- {r['chapter']} beat {r['beat']}: **{x.get('kind')}** at {x.get('where')}. Fix: {x.get('fix')}"
rep += [line(r, x) for r in rows for x in r["flaws"] if x["confirmed"]] + ["", "## Hints: look, and ignore what is only a moment in an animation"] + [line(r, x) for r in rows for x in r["flaws"] if not x["confirmed"]]; (F / "check/see_report.md").write_text("\n".join(rep) + "\n")
print(rep[1], rep[2]); print("EYE FAILED" if not eye_ok else ("FLAWS" if n else "CLEAN")); sys.exit(2 if not eye_ok else (1 if n else 0))
