from engine import *


def stat(text, size=26, color=INK):
    return T(text, size, color)


class Failures(Film):
    key = "failures"; number = 5; title = "Three failures that looked like success"
    def construct(self):
        self.beat(0); self.open()
        cards = VGroup(*[Box(f"failure {i}", GREEN_, 2.8, 1.5, 28) for i in (1, 2, 3)]).arrange(RIGHT, buff=.5).move_to([0, -.2, 0]); [c.text.shift(UP * .25) for c in cards]; ticks = VGroup(*[tick(GREEN_, .4).next_to(c.text, DOWN, buff=.2) for c in cards]); self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=.2), FadeIn(ticks), run_time=.5)

        self.beat(1); self.clear_all(.3)
        f = Box("a file of 3 characters: q5", ORANGE_, 5, .85, 28).move_to([-3.4, 1.8, 0]); block = T("blocked the agent for two days", 27, DIM).next_to(f, RIGHT, buff=.3); self.play(FadeIn(f), run_time=.3); self.play(f.on(), FadeIn(block), run_time=.4)
        s = 10.4 / 64000; x0 = -5.6; have = bar(32768 * s, RED_, .6).move_to([x0, .35, 0], aligned_edge=LEFT); need = bar(64000 * s, GREEN_, .6).move_to([x0, -1.15, 0], aligned_edge=LEFT); ht = T("the Q5 model's context: 32,768 tokens", 27).next_to([x0, .95, 0], RIGHT, buff=0); nt = T("the agent framework needs 64,000", 27).next_to([x0, -.55, 0], RIGHT, buff=0)
        self.to(.3); self.play(FadeIn(ht), GrowFromEdge(have, LEFT), run_time=.8); self.to(.62); self.play(FadeIn(nt), GrowFromEdge(need, LEFT), run_time=.8); self.to(.84); self.say("So it refused to start.", RED_, y=-2.5)

        self.beat(2); self.clear_all(.3)
        rows = [(22, 63), (30, 0), (9, 57)]; head = VGroup(T("minutes of work", 27, BLUE_), T("bytes of log", 27, ORANGE_)).arrange(RIGHT, buff=2.4).move_to([-1.7, 2.0, 0]); self.play(FadeIn(head), run_time=.3); xa, xb = head[0].get_left()[0], head[1].get_left()[0]; els = VGroup()
        for i, (m, b) in enumerate(rows):
            y = 1.2 - i * .9; ba = bar(m * .1, BLUE_, .46).move_to([xa, y, 0], aligned_edge=LEFT); bb = bar(b * .035, ORANGE_, .46).move_to([xb, y, 0], aligned_edge=LEFT); ta = T(str(m), 25).next_to(ba, RIGHT, buff=.1); tb = T(str(b), 25).next_to(bb, RIGHT, buff=.1); g = VGroup(ba, bb, ta, tb); self.to(.08 + i * .13); self.play(GrowFromEdge(ba, LEFT), GrowFromEdge(bb, LEFT), FadeIn(ta), FadeIn(tb), run_time=.5); els.add(g)
        self.to(.55); okc = VGroup(*[VGroup(tick(GREEN_, .25), T(w, 26)).arrange(RIGHT, buff=.15) for w in ("model", "data", "task")]).arrange(DOWN, buff=.25, aligned_edge=LEFT).move_to([5.2, 1.0, 0]); self.play(LaggedStart(*[FadeIn(o) for o in okc], lag_ratio=.3), run_time=.8)
        self.to(.8); bad = VGroup(cross(RED_, .22), T("only the file", 26, RED_)).arrange(RIGHT, buff=.15).next_to(okc, DOWN, buff=.3).align_to(okc, LEFT); self.play(FadeIn(bad), run_time=.4)

        self.beat(3); self.clear_all(.3)
        dog = Box("watchdog", YELLOW_, 2.2, .95, 28).move_to([-4.9, .7, 0]); gr = T("one misplaced bar in its grammar", 25, DIM).next_to(dog, DOWN, buff=.15).align_to(dog, LEFT); err = Box("every call:\nerror", RED_, 2.4, .95, 25).move_to([-.7, .7, 0]); okb = Box("fallback:\nok, continue", GREEN_, 2.8, .95, 25).move_to([3.7, .7, 0]); a1, a2 = link(dog, err), link(err, okb)
        self.play(FadeIn(dog), run_time=.3); self.to(.13); self.play(FadeIn(gr), run_time=.3); self.to(.3); self.play(GrowArrow(a1), FadeIn(err), err.on(), run_time=.6); self.to(.55); self.play(err.off(), GrowArrow(a2), FadeIn(okb), okb.on(), run_time=.6); self.ring(okb)
        self.to(.78); stamps = VGroup(*[T("approved", 22, GREEN_) for _ in range(12)]).arrange_in_grid(rows=2, buff=(.25, .2)).move_to([0, -1.8, 0]); self.play(LaggedStart(*[FadeIn(s, scale=1.4) for s in stamps], lag_ratio=.18), run_time=2)

        self.beat(4); self.clear_all(.3)
        ag = Box("agent", BLUE_, 1.7, .9, 26).move_to([-5.3, 1.3, 0]); sg = Box("setgid tool", ORANGE_, 2.2, .9, 25).move_to([-2.1, 1.3, 0]); ld = Box("linker drops\nLD variables", RED_, 2.5, .9, 24).move_to([1.3, 1.3, 0]); fs = Box("FreeSurfer tool:\nmissing library", RED_, 2.8, .9, 23).move_to([4.8, 1.3, 0]); ar = [link(ag, sg), link(sg, ld), link(ld, fs)]
        self.play(FadeIn(ag), run_time=.3); self.to(.27); self.play(GrowArrow(ar[0]), FadeIn(sg), sg.on(), run_time=.5); self.to(.42); self.play(sg.off(), GrowArrow(ar[1]), FadeIn(ld), ld.on(), run_time=.5); self.to(.58); self.play(ld.off(), GrowArrow(ar[2]), FadeIn(fs), fs.on(), run_time=.5)
        self.to(.8); st = Box("self test", GREEN_, 2.4, .95, 26).move_to([-1.8, -1.2, 0]); gt = T("runs without that path", 26, DIM).next_to(st, RIGHT, buff=.3); tk = tick(GREEN_, .36).next_to(st, LEFT, buff=.2); self.play(fs.off(), FadeIn(st), st.on(), Create(tk), FadeIn(gt), run_time=.6)

        self.beat(5); self.clear_all(.3)
        ck = Box("a check", BLUE_, 2, .95, 28).move_to([-4.6, 0, 0]); res = VGroup(Box("ok", GREEN_, 2.6, .85, 28), Box("undecided", YELLOW_, 2.6, .85, 28), Box("failed", RED_, 2.6, .85, 28)).arrange(DOWN, buff=.35).move_to([1.2, 0, 0]); ls = [link(ck, r) for r in res]
        self.play(FadeIn(ck), run_time=.3); self.to(.2); self.say("A component fails looking like success.", DIM, y=2.45); self.play(LaggedStart(*[GrowArrow(l) for l in ls], lag_ratio=.15), FadeIn(res[0]), FadeIn(res[2]), run_time=.6)
        self.to(.45); nn = T("cannot judge:\nmust say so", 26, YELLOW_).move_to([4.6, 0, 0]); self.play(FadeIn(res[1]), res[1].on(), FadeIn(nn), run_time=.5); self.to(.75); self.ring(res[1]); self.finish()


class Limits(Film):
    key = "limits"; number = 6; title = "What we do not know, and what stays private"
    def construct(self):
        self.beat(0); self.open()
        grid = dots(110, 22, .1, .16).move_to([0, .55, 0]); l = T("110 public test cases", 28).next_to(grid, UP, buff=.25); self.to(.12); self.play(LaggedStart(*[FadeIn(d, scale=.4) for d in grid], lag_ratio=.006), FadeIn(l), run_time=1.1)
        self.to(.27); import random as _r; _r.seed(7); pick = _r.sample(list(grid), 20); self.play(*[d.animate.set_color(YELLOW_).scale(1.35) for d in pick], run_time=.6); self.say("The method comparison uses 20 of them: a sample.", YELLOW_, y=-1.4)
        self.to(.68); self.play(*[d.animate.set_color(BLUE_) for d in grid], run_time=.7); self.say("The 2017 winner line is measured on all 110.", BLUE_, y=-1.4)

        self.beat(1); self.clear_all(.3)
        a = dots(16, 4, .13, .2, BLUE_).move_to([-5.1, .65, 0]); b = dots(16, 4, .13, .2, ORANGE_).move_to([-2.7, .65, 0]); ta, tb = T("training", 24, BLUE_).next_to(a, UP, buff=.15), T("test", 24, ORANGE_).next_to(b, UP, buff=.15); self.play(FadeIn(a), FadeIn(b), FadeIn(ta), FadeIn(tb), run_time=.4)
        self.to(.1); import random as _r; _r.seed(3); pos = [d.get_center().copy() for d in [*a, *b]]; _r.shuffle(pos); self.play(*[d.animate.move_to(p) for d, p in zip([*a, *b], pos)], run_time=1)
        self.to(.3); nl = T("Clara's U-Net numbers:\nnot a leaderboard result", 26).move_to([-3.9, -1.65, 0]); self.play(FadeIn(nl), run_time=.4)
        self.to(.5); hs = [1.1, 2.2, 3.0, 3.0, 3.0, 1.8]; base = -1.75; bs = VGroup(*[bar(.55, TEAL_, h).move_to([1.1 + i * .78, base + h / 2, 0]) for i, h in enumerate(hs)]); ceil = DashedLine([.65, base + 3, 0], [5.9, base + 3, 0], color=RED_); tl = T("32 synthetic tasks, per type (schematic)", 24).move_to([3.3, 1.75, 0]); cl = T("ceiling", 22, RED_).next_to(ceil, RIGHT, buff=.08); self.play(FadeIn(tl), LaggedStart(*[GrowFromEdge(x, DOWN) for x in bs], lag_ratio=.1), run_time=.9); self.play(Create(ceil), FadeIn(cl), run_time=.4)
        self.to(.86); self.say("It ranks hub models coarsely.", DIM)

        self.beat(2); self.clear_all(.3)
        grid = dots(60, 12, .1, .13, TEAL_).move_to([-3.8, 1.05, 0]); l = T("60 labelled jobs", 26).next_to(grid, UP, buff=.14); self.play(LaggedStart(*[FadeIn(d, scale=.4) for d in grid], lag_ratio=.01), FadeIn(l), run_time=.7)
        x0 = .7; s = 5.2; self.to(.18); fr1 = Rectangle(width=s, height=.48, stroke_color=DIM, stroke_width=2).move_to([x0, 1.45, 0], aligned_edge=LEFT); acc = bar(.68 * s, GREEN_, .48).move_to([x0, 1.45, 0], aligned_edge=LEFT); fr2 = fr1.copy().move_to([x0, .25, 0], aligned_edge=LEFT); cov = bar(.62 * s, BLUE_, .48).move_to([x0, .25, 0], aligned_edge=LEFT); t1 = T("accuracy 0.68 (six types, October 29)", 25).next_to(fr1, UP, buff=.08).align_to(fr1, LEFT); t2 = T("coverage 0.62", 25).next_to(fr2, UP, buff=.08).align_to(fr2, LEFT)
        self.play(Create(fr1), FadeIn(t1), GrowFromEdge(acc, LEFT), run_time=.7); self.play(Create(fr2), FadeIn(t2), GrowFromEdge(cov, LEFT), run_time=.7)
        self.to(.5); h = Box("hard job", ORANGE_, 1.9, .75, 24).move_to([-5.2, -1.3, 0]); r = Box("read as research", ORANGE_, 2.5, .75, 24).move_to([-1.9, -1.3, 0]); m = Box("same model", GREEN_, 2.0, .75, 24).move_to([1.3, -1.3, 0]); a1, a2 = link(h, r), link(r, m); self.play(FadeIn(h), GrowArrow(a1), FadeIn(r), r.on(), run_time=.6); self.play(GrowArrow(a2), FadeIn(m), m.on(), run_time=.5)
        self.to(.82); self.say("The 13-task test is small: it ranks, it does not benchmark.", DIM)

        self.beat(3); self.clear_all(.3)
        grid = dots(154, 22, .08, .1, PURPLE_).move_to([-2.6, 1.15, 0]); l = T("154 commands", 26).next_to(grid, UP, buff=.14); self.play(LaggedStart(*[FadeIn(d, scale=.4) for d in grid], lag_ratio=.004), FadeIn(l), run_time=.8)
        rater = Box("one rater, rubric written\nbefore any model ran", PURPLE_, 3.9, 1, 23).move_to([4.2, 1.15, 0]); self.to(.15); self.play(FadeIn(rater), rater.on(), run_time=.5)
        self.to(.47); gate = Box("the gate, live since October 29", GREEN_, 5, .8, 25).move_to([-3.6, -1.1, 0]); self.play(rater.off(), FadeIn(gate), gate.on(), run_time=.5); esc = T("still escalates many harmless commands", 25, ORANGE_).next_to(gate, RIGHT, buff=.35); self.to(.62); self.play(FadeIn(esc), gate.off(), run_time=.4)
        self.to(.82); self.say("Its answer verdicts are unchecked.", RED_, y=-2.5)

        self.beat(4); self.clear_all(.3)
        mach = RoundedRectangle(corner_radius=.25, width=6, height=4.3, stroke_color=TEAL_, stroke_width=3, fill_color=TEAL_, fill_opacity=.05).move_to([-3.5, -.4, 0]); mn = T("the machine", 26, TEAL_, bold=True).next_to(mach, UP, buff=.14); ins = VGroup(Box("patient data", ORANGE_, 3.8, .9, 26), Box("in-house cohort results", ORANGE_, 3.8, .9, 26)).arrange(DOWN, buff=.35).move_to(mach); self.play(Create(mach), FadeIn(mn), run_time=.5); self.play(LaggedStart(*[FadeIn(i) for i in ins], lag_ratio=.2), run_time=.5); self.play(*[i.on() for i in ins], run_time=.3)
        self.to(.32); pub = Box("published: only public dataset work", BLUE_, 5.6, .85, 25).move_to([3.5, 1.1, 0]); self.play(*[i.off() for i in ins], FadeIn(pub), pub.on(), run_time=.5)
        self.to(.58); sites = VGroup(*[Box(s, BLUE_, 1.75, .7, 22) for s in ("Utrecht", "Singapore", "Amsterdam")]).arrange(RIGHT, buff=.1).move_to([3.5, -.75, 0]); wl = T("WMH Segmentation Challenge: the QC data", 24, DIM).next_to(sites, UP, buff=.14); self.play(pub.off(), FadeIn(wl), LaggedStart(*[FadeIn(s, shift=UP * .15) for s in sites], lag_ratio=.25), run_time=1)

        self.beat(5); self.clear_all(.3)
        src = Box("patient data", ORANGE_, 2.5, 1.0, 26).move_to([-5.1, .75, 0]); kinds = ["mask", "embedding", "log line", "QC page", "trained model"]; ks = VGroup(*[Box(k, ORANGE_, 2.3, .55, 22) for k in kinds]).arrange(DOWN, buff=.12).move_to([-1.1, .75, 0]); ls = [link(src, k, ORANGE_) for k in ks]; self.play(FadeIn(src), src.on(), run_time=.4)
        self.to(.05); self.play(LaggedStart(*[AnimationGroup(GrowArrow(l), FadeIn(k)) for l, k in zip(ls, ks)], lag_ratio=.3), run_time=2.2); self.to(.2); lb = T("each carries its source class", 25, ORANGE_).move_to([-3, -1.4, 0]); self.play(*[k.on() for k in ks], FadeIn(lb), run_time=.5)
        self.to(.3); mis = T("Comparisons on the mixed pool: missing here, in the wiki", 24, DIM).move_to([0, -2.1, 0]); self.play(FadeIn(mis), run_time=.4)
        self.to(.62); gate = Box("check before every push", YELLOW_, 4, .9, 25).move_to([4.2, 1.6, 0]); ok = VGroup(tick(GREEN_, .26), T("every dataset has a release", 23)).arrange(RIGHT, buff=.12).next_to(gate, DOWN, buff=.22); no = VGroup(cross(RED_, .22), T("unreleased path: push aborted", 23, RED_)).arrange(RIGHT, buff=.12).next_to(ok, DOWN, buff=.18); self.play(*[k.off() for k in ks], src.off(), FadeIn(gate), gate.on(), run_time=.5); self.to(.76); self.play(FadeIn(ok), run_time=.4); self.to(.87); self.play(FadeIn(no), run_time=.4); self.finish()


class Recipe(Film):
    key = "usecase_recipe"; number = 7; title = "A use case: Clé makes a video"
    def construct(self):
        self.beat(0); self.open()
        names = [("request", YELLOW_), ("read public text\nor group totals", BLUE_), ("chapters", BLUE_), ("beats + drawing\ncode", BLUE_), ("run, one frame\nper beat", TEAL_), ("layout + fact\ncheck", PURPLE_), ("voice, frames,\nffmpeg", GREEN_), ("a person\ndecides", ORANGE_)]
        S = [Box(n, c, 2.55, 1, 24) for n, c in names]; pos = [(-4.95 + 3.3 * i, 1.3) for i in range(4)] + [(-4.95 + 3.3 * (7 - i), -.7) for i in range(4, 8)]
        for s, p in zip(S, pos):
            s.move_to([p[0], p[1], 0])
        A = [link(S[0], S[1]), link(S[1], S[2]), link(S[2], S[3]), link(S[3], S[4], DIM, DOWN, UP), link(S[4], S[5], DIM, LEFT, RIGHT), link(S[5], S[6], DIM, LEFT, RIGHT), link(S[6], S[7], DIM, LEFT, RIGHT)]
        for s in S:
            s.rect.set_fill(opacity=.03).set_stroke(opacity=.35); s.text.set_opacity(.4)
        self.play(LaggedStart(*[FadeIn(s) for s in S], lag_ratio=.1), run_time=1.0); self.to(.5); self.play(S[0].on(), run_time=.4)
        note = None
        def step(i, line):
            nonlocal note
            self.beat(i); self.play(S[i - 1].off(), GrowArrow(A[i - 1]), S[i].on(), run_time=.6)
            if line:
                self.say(line, DIM, y=-2.6, size=27)
        step(1, "Never patient data: Clé may not see it.")
        step(2, "One idea each.")
        step(3, "Each picture moment ties to a beat, with a red ring and a short label.")
        step(4, "Crashes send the error back to Clé."); back = CurvedArrow(S[4].get_top() + LEFT * .5, S[3].get_bottom() + LEFT * .5, angle=-PI / 3, color=RED_, stroke_width=3, tip_length=.15)
        self.to(.65); self.play(Create(back), run_time=.5)
        step(5, "Complaints go back: at most four rounds."); self.play(FadeOut(back), run_time=.2)
        step(6, "On the workstation CPU: Kokoro for the voice,\n24 frames per second, ffmpeg joins them.")
        step(7, "The model does not decide it is right."); self.to(.28)
        self.play(*[FadeOut(x) for s in (S[:7], A) for x in s], FadeOut(self.caption), S[7].animate.move_to([-4.6, .3, 0]), run_time=.5); self.caption = None
        props = VGroup(*[Box(t, BLUE_, 4.6, .68, 23) for t in ("explaining a segmentation result", "a tutorial with invented data", "a status report from logs", "onboarding from a README")]).arrange(DOWN, buff=.14).move_to([3.1, .9, 0]); pl = T("other uses: only proposals", 25, DIM).next_to(props, UP, buff=.12); self.play(FadeIn(pl), run_time=.3)
        self.play(LaggedStart(*[FadeIn(p, shift=LEFT * .2) for p in props], lag_ratio=.5), run_time=4.5)
        self.to(.72); self.say("Patient images and tables must not go to Clé:\nthose chapters need the local model.", ORANGE_, y=-2.5, size=27); self.finish()


def counter(scene, target, x, y, size=52, color=YELLOW_, run_time=1.0, start=0, suffix=""):
    t = ValueTracker(start); m = T(f"{start:,}{suffix}", size, color).move_to([x, y, 0]); m.add_updater(lambda o: o.become(T(f"{int(round(t.get_value())):,}{suffix}", size, color).move_to([x, y, 0]))); scene.add(m); scene.play(t.animate.set_value(target), run_time=run_time, rate_func=smooth); m.clear_updaters(); return m


class Log(Film):
    key = "usecase_log"; number = 8; title = "How it went: the honest log"
    def construct(self):
        self.beat(0); self.open()
        self.say("Counts from the full-length film Clé wrote", DIM, y=2.6, size=26)
        self.to(.42); a = VGroup(counter(self, 15, -4.3, .4, 64, run_time=.8), T("teaching chapters", 28).move_to([-4.3, -.5, 0])); self.play(FadeIn(a[1]), run_time=.2); self.to(.6); b = VGroup(counter(self, 3, 0, .4, 64, run_time=.5), T("use-case chapters", 28).move_to([0, -.5, 0])); self.play(FadeIn(b[1]), run_time=.2); self.to(.8); c = VGroup(counter(self, 54, 4.3, .4, 64, run_time=.8), T("rounds", 28).move_to([4.3, -.5, 0])); self.play(FadeIn(c[1]), run_time=.2)

        self.beat(1); self.clear_all(.3)
        items = [(6, "crashed, repaired\nfrom the error", RED_, .02), (11, "rewritten after\nthe image check", ORANGE_, .28), (3, "rewritten after\nthe fact check", YELLOW_, .54), (0, "answers empty\nor dropped", GREEN_, .76)]
        for i, (n, t, col, at) in enumerate(items):
            x = -5 + i * 3.35; self.to(at); counter(self, n, x, .5, 64, color=col, run_time=.5); self.play(FadeIn(T(t, 26).move_to([x, -.55, 0])), run_time=.3)

        self.beat(2); self.clear_all(.3)
        w = counter(self, 4501, -3.4, 1.2, run_time=1.2); self.play(FadeIn(T("words of narration", 26).move_to([-3.4, .35, 0])), run_time=.3)
        self.to(.35); s = .14; b1 = bar(26 * s, ORANGE_, .55).move_to([.5, 1.15, 0], aligned_edge=LEFT); t1 = T("26", 26).next_to(b1, RIGHT, buff=.1); lab = T("layout complaints", 26).next_to(b1, UP, buff=.12).align_to(b1, LEFT); self.play(FadeIn(lab), GrowFromEdge(b1, LEFT), FadeIn(t1), run_time=.6); self.say("A second pass repaired only drawings.", DIM, y=-1.4)
        self.to(.6); b2 = bar(20 * s, ORANGE_, .55).move_to([.5, .35, 0], aligned_edge=LEFT); t2 = T("20", 26).next_to(b2, RIGHT, buff=.1); self.play(GrowFromEdge(b2, LEFT), FadeIn(t2), run_time=.6); self.to(.8); self.play(b2.animate.set_color(RED_), run_time=.3); self.say("Twenty are still open.", RED_, y=-1.4)

        self.beat(3); self.clear_all(.3)
        c = dots(6, 6, .17, .22, RED_).move_to([-3.3, .9, 0]); tl = T("6 fact-check complaints, one chapter", 26).next_to(c, UP, buff=.2); self.play(FadeIn(c), FadeIn(tl), run_time=.5); self.to(.32); src = T("a review: the source supports them", 26, GREEN_).move_to([3.3, .9, 0]); self.play(FadeIn(src), c.animate.set_color(GREEN_), run_time=.7)
        self.to(.55); self.say("So the checker can raise false alarms.", INK, y=-.6); self.to(.8); z = T("Its zero elsewhere is no proof.", 28, ORANGE_).move_to([0, -1.5, 0]); self.play(FadeIn(z), run_time=.4)

        self.beat(4); self.clear_all(.3)
        h = Box("harness bug", RED_, 2.5, 1, 26).move_to([-5, .6, 0]); e = Box("empty source text", ORANGE_, 2.9, 1, 25).move_to([-1.5, .6, 0]); wr = Box("writer invents facts", ORANGE_, 3.2, 1, 25).move_to([2.1, .6, 0]); a1, a2 = link(h, e), link(e, wr); self.play(FadeIn(T("a first version was rejected", 28, DIM).move_to([0, 2.2, 0])), run_time=.3); self.to(.2); self.play(FadeIn(h), h.on(), run_time=.4); self.to(.36); self.play(h.off(), GrowArrow(a1), FadeIn(e), e.on(), run_time=.4); self.to(.5); self.play(e.off(), GrowArrow(a2), FadeIn(wr), wr.on(), run_time=.4)
        self.to(.62); rv = T("even reversing who may see patient data", 25, RED_).next_to(wr, DOWN, buff=.25); self.play(FadeIn(rv), run_time=.4); self.to(.8); fc = T("the fact check had nothing to compare", 26, DIM).move_to([0, -1.9, 0]); self.play(FadeIn(fc), run_time=.4)

        self.beat(5); self.clear_all(.3); self.overlap_ok = True
        pile = VGroup(*[Box(f"beat {i}", BLUE_, 2.3, .8, 24).move_to([-4.2 + .16 * i, .5 + .16 * i, 0]) for i in range(5)]); self.play(LaggedStart(*[FadeIn(p, shift=DOWN * .2) for p in pile], lag_ratio=.25), run_time=1.2); pl = T("misread timing: beats piled up", 25, RED_).move_to([-3.6, -.65, 0]); self.play(FadeIn(pl), run_time=.3)
        self.to(.22); self.play(FadeOut(pl), pile.animate.arrange(RIGHT, buff=.14).scale(.82).move_to([0, 1.1, 0]), run_time=.9); self.overlap_ok = False; self.play(LaggedStart(*[p.on() for p in pile], lag_ratio=.15), run_time=.8); self.say("Fixed: every beat is its own screen, every chapter written again.", DIM, y=.05, size=26)
        self.to(.5); parts = VGroup(Box("setup tool: harness, engine,\nsome sentences, these pictures", TEAL_, 5.2, 1.05, 24), Box("Clé: narration,\nshortened for this cut", BLUE_, 4.4, 1.05, 24)).arrange(RIGHT, buff=.4).move_to([0, -1.25, 0]); self.play(*[p.off() for p in pile], FadeIn(parts), run_time=.5); self.play(parts[0].on(), run_time=.3); self.to(.72); self.play(parts[0].off(), parts[1].on(), run_time=.3)
        self.to(.9); self.play(FadeOut(parts), FadeOut(pile), FadeOut(self.caption), run_time=.4); self.caption = None; self.play(Write(T("A person watches and decides.", 40, YELLOW_).move_to([0, 0, 0])), run_time=1.0); self.finish()
