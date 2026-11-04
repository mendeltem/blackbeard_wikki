from engine import *


class Mini(Film):
    key = "mini"; number = 1; title = "A small test"
    def construct(self):
        self.beat(0); self.open()
        a, b = Box("question", YELLOW_, 2.6, 1, 28).move_to(LEFT * 3), Box("answer", GREEN_, 2.6, 1, 28).move_to(RIGHT * 3); arrow = link(a, b); self.play(FadeIn(a), run_time=.4); self.play(a.on(), run_time=.3)
        self.beat(1); self.play(a.off(), GrowArrow(arrow), FadeIn(b), run_time=.6); self.play(b.on(), run_time=.3); self.finish()
