"""The hidden part of the film: timing, drawing helpers, video writing. Each chapter only says what appears when."""
import json, subprocess, tempfile
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

BG, INK, MUTED, BLUE, YELLOW, ORANGE, GREEN, RED, GREY = "#0e1116", "#f2f2ee", "#9aa0a6", "#58C4DD", "#FFE14D", "#FC8B3C", "#83C167", "#FC6255", "#7c828a"
FPS = 24; HERE = Path.cwd(); FFMPEG = "ffmpeg"     # run from the film folder (audio_beats/, video/, frames_check/)
plt.rcParams.update({"figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG, "text.color": INK, "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED, "axes.edgecolor": "#444", "font.size": 15,
                     "axes.spines.top": False, "axes.spines.right": False, "mathtext.fontset": "dejavusans"})


def smooth(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)


def attention(ax, x, y, w, h, alpha=1.0, label=None, at=None, size=15, transform=None):
    """Red ring: look here."""
    from matplotlib.patches import Ellipse
    import matplotlib.patheffects as pe
    if alpha <= 0:
        return
    tr = transform or ax.transData
    ax.add_patch(Ellipse((x, y), w, h, fill=False, edgecolor="#FF2D2D", lw=3.5, alpha=alpha, transform=tr, zorder=20, clip_on=False, path_effects=[pe.Stroke(linewidth=6, foreground="white", alpha=.7 * alpha), pe.Normal()]))
    if label:
        lx, ly = at or (x, y)
        ax.text(lx, ly, label, color="#FF2D2D", fontsize=size, weight="bold", alpha=alpha, transform=tr, ha="center", va="center", zorder=21, bbox=dict(facecolor=BG, edgecolor="#FF2D2D", boxstyle="round,pad=.25", lw=1.2, alpha=.92 * alpha))


class Time:
    """Where we are in the chapter. p(2) goes smoothly from 0 to 1 during beat 2."""
    def __init__(self, ends, frame):
        self.t = frame / FPS; self.ends = ends; self.starts = [0] + ends[:-1]

    def p(self, beat, a=0.0, b=1.0):
        s, e = self.starts[beat], self.ends[beat]; return float(smooth((self.t - (s + a * (e - s))) / max((b - a) * (e - s), 1e-6)))

    def local(self, beat):
        return self.t - self.starts[beat]

    def beat(self):
        return int(np.searchsorted(self.ends, self.t, side="right")) if self.t < self.ends[-1] else len(self.ends) - 1


def render(key, title, nbeats, draw, check_only=False, out=None):
    """Run draw(fig, time) for every frame, join it with the voice, write video/<out or key>.mp4."""
    out = out or key
    state = json.loads((HERE / "audio_beats/state.json").read_text()); ends = list(np.cumsum([state[f"{key}_{i}.wav"]["seconds"] for i in range(nbeats)]))
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100); total = int(ends[-1] * FPS) + 1
    def frame_rgb(n):
        fig.clf(); tm = Time(ends, n); fig.text(.03, .945, title, fontsize=21, weight="bold", color=INK); draw(fig, tm); fig.canvas.draw(); return np.asarray(fig.canvas.buffer_rgba())[..., :3].copy()
    for i, e in enumerate(ends):
        plt.imsave(HERE / f"frames_check/{out}_{i}.png", frame_rgb(max(int(e * FPS) - 3, 0)))
    if check_only:
        return
    with tempfile.TemporaryDirectory() as d:
        wav = Path(d) / "a.wav"; sf.write(wav, np.concatenate([sf.read(HERE / f"audio_beats/{key}_{i}.wav")[0] for i in range(nbeats)]), 24000)
        p = subprocess.Popen([FFMPEG, "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1280x720", "-r", str(FPS), "-i", "-", "-i", str(wav), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "24", "-preset", "medium", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", "-shortest", str(HERE / f"video/{out}.mp4")], stdin=subprocess.PIPE)
        for n in range(total):
            p.stdin.write(frame_rgb(n).tobytes())
        p.stdin.close(); p.wait()
    print(out, "done", round(ends[-1]), "s", flush=True)
