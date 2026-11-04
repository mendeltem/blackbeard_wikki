"""The hidden part of the film: voice timing, the look, and small drawing helpers. Each chapter only says what happens when."""
import json, os
from pathlib import Path
from manim import *

HERE = Path(os.environ["FILM_DIR"]).resolve()
FONT = "CMU Serif"
BG, INK, DIM = "#0b0d12", "#ece9e1", "#8d929a"
BLUE_, TEAL_, YELLOW_, GREEN_, ORANGE_, RED_, PURPLE_ = "#58C4DD", "#5CD0B3", "#FFE14D", "#83C167", "#FC8B3C", "#FC6255", "#9A72AC"
config.background_color = BG; config.pixel_width = int(os.environ.get("W", 1280)); config.pixel_height = int(os.environ.get("H", 720)); config.frame_rate = int(os.environ.get("FPS", 30)); config.disable_caching = True; config.verbosity = "ERROR"; config.progress_bar = "none"
config.media_dir = str(HERE / "media"); config.output_file = None
STATE = json.loads((HERE / "audio_beats/state.json").read_text())


def T(text, size=28, color=INK, bold=False):
    """Text; several lines are centred. No ligatures, so that letters transform cleanly."""
    lines = VGroup(*[Text(l, font=FONT, font_size=size, color=color, weight=BOLD if bold else NORMAL, disable_ligatures=True) for l in text.split("\n")])
    return lines.arrange(DOWN, buff=size * .0045) if len(lines) > 1 else lines


class Box(VGroup):
    """A rounded rectangle with a label. It can light up."""
    def __init__(self, label, color=BLUE_, w=2.6, h=1.1, size=26, **k):
        super().__init__(**k); self.col = color
        self.rect = RoundedRectangle(corner_radius=.14, width=w, height=h, stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=.08)
        self.glow = self.rect.copy().set_fill(opacity=0).set_stroke(color, width=16, opacity=0)
        self.text = T(label, size).move_to(self.rect)
        if self.text.width > w - .3: self.text.scale_to_fit_width(w - .3)
        if self.text.height > h - .16: self.text.scale_to_fit_height(h - .16)
        self.add(self.glow, self.rect, self.text)

    def on(self):
        return AnimationGroup(self.rect.animate.set_fill(self.col, .5).set_stroke(self.col, 4.5, 1), self.glow.animate.set_stroke(self.col, 16, .28), self.text.animate.set_opacity(1).set_color(WHITE))

    def off(self):
        return AnimationGroup(self.rect.animate.set_fill(self.col, .08).set_stroke(self.col, 3, 1), self.glow.animate.set_stroke(self.col, 16, 0), self.text.animate.set_opacity(1).set_color(INK))

    def mute(self):
        return AnimationGroup(self.rect.animate.set_fill(self.col, .03).set_stroke(self.col, 2, .35), self.glow.animate.set_stroke(self.col, 16, 0), self.text.animate.set_opacity(.4))


def link(a, b, color=DIM, da=RIGHT, db=LEFT, width=3, **k):
    p = a.get_critical_point(da) if hasattr(a, "get_critical_point") else a; q = b.get_critical_point(db) if hasattr(b, "get_critical_point") else b
    return Arrow(p, q, buff=.08, color=color, stroke_width=width, tip_length=.18, max_tip_length_to_length_ratio=.25, max_stroke_width_to_length_ratio=20, **k)


def tick(color=GREEN_, s=.3):
    return VMobject(stroke_color=color, stroke_width=6).set_points_as_corners([[-.5 * s, 0, 0], [-.12 * s, -.4 * s, 0], [.6 * s, .5 * s, 0]])


def cross(color=RED_, s=.3):
    return VGroup(Line([-s / 2, -s / 2, 0], [s / 2, s / 2, 0], color=color, stroke_width=6), Line([-s / 2, s / 2, 0], [s / 2, -s / 2, 0], color=color, stroke_width=6))


def dots(n, cols, r=.09, gap=.1, color=DIM):
    return VGroup(*[Dot(radius=r, color=color) for _ in range(n)]).arrange_in_grid(cols=cols, buff=gap)


def bar(length, color, h=.34):
    return Rectangle(width=max(length, .001), height=h, stroke_width=0, fill_color=color, fill_opacity=.85)


class Film(Scene):
    key = ""; number = 0; title = ""

    def setup(self):
        beats = json.loads((HERE / f"beats/{self.key}_beats.json").read_text()); d = [STATE[f"{self.key}_{i}.wav"]["seconds"] for i in range(len(beats))]
        self.starts = [sum(d[:i]) for i in range(len(d))]; self.lens = d; self.current = 0; self.caption = None

    def now(self):
        return self.renderer.time

    def beat(self, i):
        """Start of a beat: wait until the voice gets there."""
        self.current = i; self.until(self.starts[i])

    def until(self, t):
        if t > self.now() + 1 / config.frame_rate:
            self.wait(t - self.now())
        elif t < self.now() - .25:
            print(f"LATE {self.key} beat {self.current}: {self.now() - t:.2f} s", flush=True)

    def to(self, share):
        """Wait until this share of the current beat has been spoken."""
        self.until(self.starts[self.current] + share * self.lens[self.current])

    def finish(self):
        self.until(self.starts[-1] + self.lens[-1])

    def open(self):
        """Chapter title: written large, then it moves to the corner."""
        big = T(f"{self.number}. {self.title}", 44, bold=True); small = T(f"{self.number}. {self.title}", 24, DIM, bold=True).to_corner(UL, buff=.3)
        self.play(Write(big), run_time=1.1); self.wait(.2); self.play(Transform(big, small), run_time=.7); self.head = big

    def clear_all(self, run_time=.6):
        keep = [m for m in self.mobjects if m is not self.head]
        if keep:
            self.play(*[FadeOut(m) for m in keep], run_time=run_time)
        self.caption = None

    def say(self, text, color=INK, y=-3.3, size=28):
        """One short line at the bottom, replacing the one before."""
        new = T(text, size, color).move_to([0, y, 0]); old = self.caption; self.caption = new
        self.play(*([FadeOut(old, shift=UP * .15)] if old else []), FadeIn(new, shift=UP * .15), run_time=.5)

    def send(self, a, b, color=YELLOW_, label=None, run_time=1.0, keep=False, r=.09):
        """A dot (or label) travels from a to b and leaves a passing light on the way."""
        p = a.get_center() if hasattr(a, "get_center") else np.array(a); q = b.get_center() if hasattr(b, "get_center") else np.array(b)
        thing = label if label is not None else Dot(p, radius=r, color=color); thing.move_to(p); path = Line(p, q, color=color, stroke_width=5)
        self.play(thing.animate.move_to(q), ShowPassingFlash(path, time_width=.5), run_time=run_time, rate_func=smooth)
        if not keep:
            self.play(FadeOut(thing), run_time=.15)
        return thing

    def ring(self, m):
        """Red ring: only for the few moments that need it. It goes away again, so it never sits on text."""
        self.play(Circumscribe(m, shape=Rectangle, color=RED_, stroke_width=5, buff=.14, time_width=1.2), run_time=1.3)
