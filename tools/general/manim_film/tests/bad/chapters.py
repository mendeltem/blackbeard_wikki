from engine import *


class Bad(Film):
    key = "bad"; number = 1; title = "Deliberately bad"
    def construct(self):
        self.beat(0); self.open(); a = T("this text runs far off the right edge of the frame for sure and keeps on going", 40).move_to([5, 0, 0]); b = T("text on text", 30).move_to(a.get_center() + LEFT * 1); c = T("line through me", 30).move_to([0, 2, 0]); l = Line([-3, 2, 0], [3, 2, 0], color=RED_); self.add(a, b, c, l)
        self.beat(1); self.finish()
