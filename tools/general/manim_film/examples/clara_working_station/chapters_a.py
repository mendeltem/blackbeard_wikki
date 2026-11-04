from engine import *


class What(Film):
    key = "what"; number = 1; title = "What this thing is, in one breath"
    def construct(self):
        self.beat(0); self.open()
        alita = RoundedRectangle(corner_radius=.25, width=8.2, height=5.2, stroke_color=TEAL_, stroke_width=3, fill_color=TEAL_, fill_opacity=.04).move_to([.6, -.35, 0])
        name = T("Alita", 32, TEAL_, bold=True).next_to(alita.get_corner(UL), DR, buff=.2)
        phone, term = Box("phone", GREY_B, 1.8, .8, 24).move_to([-5.5, .6, 0]), Box("terminal", GREY_B, 1.8, .8, 24).move_to([-5.5, -1.1, 0])
        self.to(.3); self.play(Create(alita), Write(name), run_time=1.1); self.play(FadeIn(phone, shift=RIGHT * .3), FadeIn(term, shift=RIGHT * .3), run_time=.5)
        self.to(.62); self.play(phone.on(), run_time=.3); self.send(phone, alita, label=T("a question", 22, YELLOW_), run_time=1.1); self.play(phone.off(), run_time=.2)
        self.to(.86); self.play(alita.animate.set_fill(TEAL_, .16), run_time=.6)

        self.beat(1); self.play(alita.animate.set_fill(TEAL_, .04), run_time=.3)
        clara = Box("Clara", GREEN_, 2.4, 1, 32).move_to([.6, .75, 0]); self.play(DrawBorderThenFill(clara), run_time=.8)
        chips = VGroup(Box("writes code", GREEN_, 2.1, .7, 22), Box("trains the model", GREEN_, 2.5, .7, 22), Box("inspects results", GREEN_, 2.5, .7, 22)).arrange(RIGHT, buff=.2).move_to([.6, -.45, 0])
        self.to(.1); 
        for c in chips:
            self.play(FadeIn(c, shift=UP * .2), run_time=.35); self.play(c.on(), run_time=.3)
        self.to(.48); data = Box("patient data", ORANGE_, 2.2, .7, 22).move_to([.6, -2.0, 0]); net = Box("network", RED_, 1.5, .8, 24).move_to([6.0, .75, 0]); self.play(FadeIn(data), FadeIn(net), *[c.off() for c in chips], run_time=.5)
        d = Dot(data.get_center(), radius=.11, color=ORANGE_); self.add(d); self.play(d.animate.move_to([4.55, -1.5, 0]), run_time=.8, rate_func=smooth); self.play(d.animate.move_to(data), run_time=.6, rate_func=rush_from); self.remove(d)
        self.to(.72); wire = DashedLine(clara.get_right(), net.get_left(), color=RED_, stroke_width=3); x = cross().move_to(wire); self.play(Create(wire), run_time=.5); self.play(GrowFromCenter(x), run_time=.4)

        self.beat(2); self.play(FadeOut(chips), FadeOut(data), FadeOut(wire), FadeOut(x), FadeOut(net), FadeOut(phone), FadeOut(term), run_time=.4)
        relay = Box("relay", YELLOW_, 1.7, 1, 30).move_to([-1.9, .75, 0]); inlet = link(relay.get_left() + LEFT * 1.6, relay, YELLOW_); self.play(DrawBorderThenFill(relay), GrowArrow(inlet), clara.animate.move_to([2.7, .75, 0]), run_time=.8)
        self.play(relay.on(), run_time=.4)
        local, cle = Box("local model", GREEN_, 2.3, .85, 24).move_to([-1.9, -1.95, 0]), Box("Clé", BLUE_, 1.5, .85, 30).move_to([5.9, 2.5, 0])
        la, lb = link(relay, local, GREEN_, DOWN, UP), link(relay, cle, BLUE_, UP + RIGHT * .2, LEFT); self.to(.17); self.play(FadeIn(local), GrowArrow(la), run_time=.5)
        tokens = ["data path", "subject id", "cohort name", "image file"]; self.to(.2)
        for t in tokens:
            tag = T(t, 22, ORANGE_).move_to([-5.4, .75, 0]); self.play(FadeIn(tag), run_time=.2); self.play(tag.animate.move_to(relay), run_time=.42); self.play(tag.animate.move_to(local).set_opacity(0), run_time=.42)
        self.to(.7); self.play(local.on(), run_time=.3); self.play(FadeIn(cle), GrowArrow(lb), local.off(), run_time=.5)
        tag = T("data-free work", 22, BLUE_).move_to([-5.2, .75, 0]); self.play(FadeIn(tag), run_time=.2); self.play(tag.animate.move_to(relay), run_time=.5); self.play(tag.animate.move_to(cle).set_opacity(0), cle.on(), run_time=.7)

        self.beat(3); self.clear_all(.35)
        left = Box("", BLUE_, 5.6, 4.6).move_to([-3.45, -.35, 0]); right = Box("", GREEN_, 5.6, 4.6).move_to([3.45, -.35, 0]); wall = Line([0, 2.1, 0], [0, -2.8, 0], color=YELLOW_, stroke_width=9); wl = T("relay", 26, YELLOW_, bold=True).next_to(wall, UP, buff=.1)
        lt = VGroup(T("network side", 30, BLUE_, bold=True), T("Clé\nresearch agents", 28), T("never see data", 24, DIM)).arrange(DOWN, buff=.4).move_to(left); rt = VGroup(T("data side", 30, GREEN_, bold=True), T("Clara", 28), T("never reaches the network", 24, DIM)).arrange(DOWN, buff=.4).move_to(right)
        self.play(FadeIn(left), FadeIn(right), run_time=.4); self.play(Write(lt[0]), Write(rt[0]), FadeIn(lt[1:]), FadeIn(rt[1:]), run_time=.6)
        self.to(.1); self.play(left.on(), right.mute(), lt.animate.set_opacity(1), rt.animate.set_opacity(.4), run_time=.5)
        self.to(.48); self.play(right.on(), left.mute(), rt.animate.set_opacity(1), lt.animate.set_opacity(.4), run_time=.5)
        self.to(.8); self.play(left.mute(), right.mute(), lt.animate.set_opacity(.4), rt.animate.set_opacity(.4), Create(wall), Write(wl), run_time=.7); self.play(wall.animate.set_stroke(width=16), run_time=.3); self.play(wall.animate.set_stroke(width=9), run_time=.3)

        self.beat(4); self.clear_all(.35)
        steps = VGroup(Box("question", YELLOW_, 1.9, .95, 24), Box("shortlist\nof methods", BLUE_, 2.2, .95, 24), Box("one job\nper method", TEAL_, 2.2, .95, 24), Box("countable\ncriteria", PURPLE_, 2.2, .95, 24), Box("harness", GREEN_, 1.9, .95, 26)).arrange(RIGHT, buff=.5).move_to([0, .4, 0])
        arrows = [link(steps[i], steps[i + 1]) for i in range(4)]; self.play(FadeIn(steps[0], shift=UP * .2), run_time=.3)
        for i, s in enumerate(steps[1:]):
            self.to([.12, .3, .47, .68][i]); self.play(steps[i].off(), GrowArrow(arrows[i]), FadeIn(s, shift=LEFT * .3), s.on(), run_time=.55)
        self.to(.78); loop = CurvedArrow(steps[4].get_corner(DR) + LEFT * .3, steps[4].get_corner(DL) + RIGHT * .3, angle=-TAU * .55, color=GREEN_, stroke_width=3, tip_length=.16); lab = T("one job at a time,\nuntil the check passes", 24, DIM).move_to([3.9, -1.95, 0])
        self.play(Create(loop), FadeIn(lab), run_time=.6); d = Dot(loop.get_start(), color=YELLOW_, radius=.09); self.add(d); self.play(MoveAlongPath(d, loop), run_time=1.1); self.remove(d)

        self.beat(5); self.play(FadeOut(lab), FadeOut(loop), *[FadeOut(a) for a in arrows], FadeOut(steps[:4]), steps[4].animate.move_to([-4.7, .4, 0]), run_time=.5)
        out = VGroup(Box("trained model", GREEN_, 3.2, .9, 26), Box("comparison table", GREEN_, 3.2, .9, 26), Box("QC page", GREEN_, 3.2, .9, 26)).arrange(DOWN, buff=.3).move_to([1.8, .4, 0]); links = [link(steps[4].get_right(), o, DIM) for o in out]
        for o, l, t in zip(out, links, (.08, .2, .32)):
            self.to(t); self.play(GrowArrow(l), FadeIn(o, shift=RIGHT * .2), run_time=.3); self.play(o.on(), run_time=.2)
        self.to(.55); self.say("One question in, one checked result out, all on Alita."); self.finish()


class Why(Film):
    key = "why"; number = 2; title = "Why not just use the cluster?"
    def construct(self):
        self.beat(0); self.open()
        wait = bar(.02, RED_, .55).move_to([-5.3, 1.6, 0], aligned_edge=LEFT); la = T("a whole GPU: about 9 hours in the queue", 28).next_to([-5.3, 2.1, 0], RIGHT, buff=0); self.to(.2); self.play(FadeIn(la), run_time=.3); self.play(wait.animate.stretch_to_fit_width(10.6).move_to([-5.3, 1.6, 0], aligned_edge=LEFT), run_time=1.6, rate_func=linear)
        cards = VGroup(*[Box("80 GB", BLUE_, 1.1, .62, 19) for _ in range(7)]).arrange(RIGHT, buff=.14).move_to([-.9, -.1, 0]); lb = T("only seven cards have 80 GB", 28).next_to(cards, UP, buff=.2).align_to(la, LEFT); cards.align_to(la, LEFT)
        self.to(.42); self.play(FadeIn(lb), LaggedStart(*[FadeIn(c, scale=.8) for c in cards], lag_ratio=.12), run_time=.9); self.play(*[c.on() for c in cards], run_time=.4)
        small = bar(.15, GREEN_, .55).move_to([-5.3, -1.95, 0], aligned_edge=LEFT); lc = T("a small share: starts in seconds, fits only small trainings", 28).next_to([-5.3, -1.45, 0], RIGHT, buff=0); self.to(.68); self.play(FadeIn(lc), GrowFromEdge(small, LEFT), *[c.off() for c in cards], run_time=.6)

        self.beat(1); self.clear_all(.35)
        ring_ = Circle(radius=1.45, color=YELLOW_, stroke_width=3).move_to([-3.9, -.25, 0]); ws = ["build", "train", "fix", "retry"]; labs = VGroup(*[T(w, 26).move_to(ring_.get_center() + np.array([np.cos(a) * 2.3, np.sin(a) * 1.85, 0])) for w, a in zip(ws, (PI / 2, 0, -PI / 2, PI))]); rounds = T("dozens of\nrounds a day", 25, YELLOW_).move_to(ring_)
        self.play(Create(ring_), FadeIn(labs), FadeIn(rounds), run_time=.7); d = Dot(ring_.point_at_angle(PI / 2), color=YELLOW_, radius=.12); self.add(d); self.play(MoveAlongPath(d, ring_), run_time=1.6, rate_func=linear)
        x0 = -.6; q = bar(.02, RED_, .55).move_to([x0, .9, 0], aligned_edge=LEFT); ql = T("cluster queue: each round costs hours", 27).next_to([x0, 1.45, 0], RIGHT, buff=0)
        self.to(.34); self.play(FadeIn(ql), run_time=.3); self.play(q.animate.stretch_to_fit_width(6.5).move_to([x0, .9, 0], aligned_edge=LEFT), run_time=1.2, rate_func=linear)
        w = bar(.3, GREEN_, .55).move_to([x0, -1.0, 0], aligned_edge=LEFT); wl = T("workstation, one fold on an A5000: about 25 min", 27); wl.scale_to_fit_width(min(wl.width, 6.7)).next_to([x0, -.45, 0], RIGHT, buff=0)
        self.to(.62); self.play(FadeIn(wl), GrowFromEdge(w, LEFT), run_time=.7); self.to(.86); self.play(MoveAlongPath(d, ring_), run_time=.8, rate_func=linear); self.say("Rounds cost minutes.", GREEN_)

        self.beat(2); self.clear_all(.35)
        ws_box = RoundedRectangle(corner_radius=.25, width=6.4, height=5, stroke_color=GREEN_, stroke_width=3, fill_color=GREEN_, fill_opacity=.05).move_to([-3, -.3, 0]); name = T("workstation", 28, GREEN_, bold=True).next_to(ws_box, UP, buff=.14)
        clara = Box("Clara", GREEN_, 1.9, .85, 28).move_to([-3, 1.35, 0]); scans = dots(48, 12, .1, .17, ORANGE_).move_to([-3, -1.05, 0]); sl = T("every scan and mask", 24, ORANGE_).next_to(scans, UP, buff=.16)
        cloud = Box("cloud model", BLUE_, 2.6, 1, 26).move_to([4.5, .5, 0]); self.play(Create(ws_box), Write(name), run_time=.6); self.play(FadeIn(clara), FadeIn(scans), FadeIn(sl), run_time=.5)
        self.to(.32); self.play(FadeIn(cloud), run_time=.3); wire = DashedLine(cloud.get_left(), [0, .5, 0], color=RED_, stroke_width=3); x = cross().move_to(wire); self.play(Create(wire), GrowFromCenter(x), run_time=.6);
        cn = T("cannot see them", 25, DIM).next_to(cloud, DOWN, buff=.2); self.play(FadeIn(cn), run_time=.3)
        self.to(.55); self.play(clara.on(), LaggedStart(*[d_.animate.set_color(YELLOW_).scale(1.25) for d_ in scans], lag_ratio=.05), run_time=3)
        cohort = T("the whole cohort", 25, YELLOW_).next_to(scans, DOWN, buff=.2); self.play(FadeIn(cohort), run_time=.3)

        self.beat(3); self.clear_all(.35)
        doc = Box("data agreement", YELLOW_, 3.4, 1.2, 30).move_to([0, 1.6, 0]); ask = T("may an AI system process this dataset?", 26, DIM).next_to(doc, DOWN, buff=.15); self.play(DrawBorderThenFill(doc), run_time=.6); self.play(FadeIn(ask), doc.on(), run_time=.4)
        a, b = Box("clause forbids it", RED_, 3.6, .95, 26).move_to([-3.6, -1.15, 0]), Box("allowed", GREEN_, 3.6, .95, 26).move_to([3.6, -1.15, 0]); start = ask.get_bottom() + DOWN * .1; la = link(start, a, RED_, DOWN, UP); lb = link(start, b, GREEN_, DOWN, UP)
        self.to(.48); self.play(doc.off(), GrowArrow(la), FadeIn(a), run_time=.5); self.play(a.on(), run_time=.3); r1 = T("the local model may not either", 25).next_to(a, DOWN, buff=.2); self.play(FadeIn(r1), run_time=.3)
        self.to(.76); self.play(a.off(), GrowArrow(lb), FadeIn(b), run_time=.5); self.play(b.on(), run_time=.3); r2 = T("local keeps the data inside", 25).next_to(b, DOWN, buff=.2); self.play(FadeIn(r2), run_time=.3); 

        self.beat(4); self.clear_all(.35)
        c1 = Circle(radius=2.2, color=BLUE_, fill_opacity=.12, stroke_width=3).move_to([-1.35, -.35, 0]); c2 = Circle(radius=2.2, color=ORANGE_, fill_opacity=.12, stroke_width=3).move_to([1.35, -.35, 0]); t1 = T("the loop\nis fast", 30).move_to([-2.5, -.35, 0]); t2 = T("data\nmay stay", 30).move_to([2.5, -.35, 0])
        self.play(DrawBorderThenFill(c1), FadeIn(t1), run_time=.8); self.play(DrawBorderThenFill(c2), FadeIn(t2), run_time=.8)
        self.to(.42); both = Intersection(c1, c2, color=YELLOW_, fill_opacity=.75, stroke_width=0); lab = T("work-\nstation", 26, BG, bold=True).move_to(both); self.play(FadeIn(both), FadeIn(lab), run_time=.8); self.play(both.animate.set_fill(opacity=1), rate_func=there_and_back, run_time=.7)
        self.to(.72); self.say("That is why we do not just use the cluster."); self.finish()


class Request(Film):
    key = "request"; number = 3; title = "One request, start to finish"
    def construct(self):
        self.beat(0); self.open()
        phone = RoundedRectangle(corner_radius=.3, width=7.4, height=2.6, stroke_color=GREY_B, stroke_width=3).move_to([0, -.2, 0]); ask = T("I want a WMH segmentation model.\nCan you research it?", 31).move_to(phone)
        self.play(Create(phone), run_time=.5); self.play(AddTextLetterByLetter(ask[0]), run_time=1.4); self.play(AddTextLetterByLetter(ask[1]), run_time=1.0)

        self.beat(1); q = Box("the question", YELLOW_, 2.2, .9, 25).move_to([-5.3, .3, 0]); self.play(ReplacementTransform(VGroup(phone, ask), q), run_time=.7)
        cle = Box("Clé", BLUE_, 1.5, 1, 30).move_to([-1.9, .3, 0]); hub = T("Charité hub", 22, DIM).next_to(cle, UP, buff=.12); l0 = link(q, cle, YELLOW_); self.play(GrowArrow(l0), FadeIn(cle), FadeIn(hub), run_time=.5); self.play(cle.on(), run_time=.3)
        self.to(.42); agents = VGroup(*[Box(t, TEAL_, 2.5, .6, 22) for t in ("agent: papers", "agent: code", "agent: methods")]).arrange(DOWN, buff=.3).move_to([2.3, .3, 0]); ls = [link(cle, a, TEAL_) for a in agents]; self.play(cle.off(), LaggedStart(*[GrowArrow(l) for l in ls], lag_ratio=.2), LaggedStart(*[FadeIn(a, shift=RIGHT * .2) for a in agents], lag_ratio=.2), run_time=1); self.play(LaggedStart(*[a.on() for a in agents], lag_ratio=.25), run_time=1)

        self.beat(2); self.play(*[a.off() for a in agents], run_time=.2)
        names = ["2D U-Net", "3D U-Net", "nnU-Net", "BIANCA"]; cards = VGroup(*[Box(n, YELLOW_, 2.2, .8, 24) for n in names]).arrange(DOWN, buff=.17).move_to([5.3, .05, 0]); self.to(.12)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * .3) for c in cards], lag_ratio=.25), run_time=1.2)
        self.to(.62); ticks = VGroup(*[VGroup(*[tick(GREEN_, .2) for _ in range(3)]).arrange(RIGHT, buff=.07).next_to(c, LEFT, buff=.15) for c in cards]); ticks_lab = T("an acceptance\nlist for each", 26, GREEN_).next_to(ticks, LEFT, buff=.35)
        self.play(FadeOut(agents), *[FadeOut(l) for l in ls], FadeOut(q), FadeOut(l0), FadeOut(cle), FadeOut(hub), VGroup(cards, ticks, ticks_lab).animate.shift(LEFT * 3.2), run_time=.8); self.play(LaggedStart(*[FadeIn(t) for t in ticks], lag_ratio=.2), FadeIn(ticks_lab), run_time=.7)

        self.beat(3); self.play(FadeOut(ticks), FadeOut(ticks_lab), cards.animate.scale(.85).arrange(RIGHT, buff=.14).move_to([2.2, 1.8, 0]), run_time=.7)
        harness = Box("harness", GREEN_, 2.4, 1, 28).move_to([-4.3, 1.8, 0]); self.play(FadeIn(harness), run_time=.3); l = link(cards[0], harness, GREEN_, LEFT, RIGHT); self.play(GrowArrow(l), harness.on(), cards[0].on(), *[c.mute() for c in cards[1:]], run_time=.6)
        self.to(.62); self.say("It moves on only when the current one is done.", DIM, y=.6, size=26)

        self.beat(4); self.play(FadeOut(self.caption), FadeOut(l), harness.off(), run_time=.3); self.caption = None
        c = Box("Clara writes code\nin the sandbox", GREEN_, 3.2, 1.1, 24).move_to([-4.3, -.6, 0]); g = Box("GPU trains\non open data", ORANGE_, 3, 1.1, 24).move_to([0, -.6, 0]); ch = Box("acceptance check\ncounts facts", PURPLE_, 3.2, 1.1, 24).move_to([4.3, -.6, 0])
        a1, a2 = link(c, g), link(g, ch); fail = CurvedArrow(ch.get_bottom() + DOWN * .05, c.get_bottom() + DOWN * .05, angle=-PI / 5, color=RED_, stroke_width=3, tip_length=.18); ft = T("failed: back to Clara", 24, RED_).move_to([0, -2.85, 0])
        self.play(FadeIn(c), c.on(), run_time=.5); self.to(.22); self.play(c.off(), GrowArrow(a1), FadeIn(g), g.on(), run_time=.5); self.to(.42); self.play(g.off(), GrowArrow(a2), FadeIn(ch), ch.on(), run_time=.5)
        self.to(.58); nm = T("no model is asked", 24, DIM).next_to(ch, UP, buff=.15); self.play(FadeIn(nm), run_time=.3); self.to(.76); self.play(ch.off(), Create(fail), FadeIn(ft), run_time=.7); d = Dot(fail.get_start(), color=RED_, radius=.11); self.add(d); self.play(MoveAlongPath(d, fail), c.on(), run_time=.9); self.remove(d)

        self.beat(5); self.clear_all(.35)
        cols = VGroup(T("Dice", 28, BLUE_), T("lesion F1", 28, BLUE_)).arrange(RIGHT, buff=1.0).move_to([-.8, 2.0, 0]); rows = VGroup(*[T(n, 27) for n in names + ["public leaderboard"]]).arrange(DOWN, buff=.3, aligned_edge=LEFT).move_to([-4.4, .2, 0]); rows[-1].set_color(DIM)
        cells = VGroup(*[VGroup(*[Dot(radius=.07, color=DIM).move_to([cols[j].get_x(), r.get_y(), 0]) for j in range(2)]) for r in rows]); self.play(FadeIn(cols), FadeIn(rows), run_time=.6); self.play(LaggedStart(*[FadeIn(x, scale=.3) for x in cells], lag_ratio=.25), run_time=1.3)
        sch = T("schematic: scored on the test set", 22, DIM).next_to(rows, DOWN, buff=.28).align_to(rows, LEFT); self.play(FadeIn(sch), run_time=.3)
        out = VGroup(Box("best model", GREEN_, 3.2, .9, 26), Box("comparison table", GREEN_, 3.2, .9, 26), Box("QC page", GREEN_, 3.2, .9, 26)).arrange(DOWN, buff=.3).move_to([4.6, .2, 0])
        self.to(.62); 
        for o in out:
            self.play(FadeIn(o, shift=LEFT * .2), o.on(), run_time=.55)
        self.finish()


class Parts(Film):
    key = "parts"; number = 4; title = "The parts"
    def construct(self):
        self.beat(0); self.open()
        P = {"prompt": Box("prompt", GREY_B, 1.8, .85, 26).move_to([-5.7, 1.0, 0]), "relay": Box("relay\n:8770", YELLOW_, 1.8, 1.05, 25).move_to([-2.6, 1.0, 0]), "cle": Box("Clé", BLUE_, 1.8, .85, 28).move_to([.6, 2.35, 0]), "agents": Box("research\nagents", BLUE_, 1.9, .95, 23).move_to([3.5, 2.35, 0]), "one": Box("System One", PURPLE_, 2.2, .85, 25).move_to([.6, 1.0, 0]),
             "clara": Box("Clara", GREEN_, 2.2, 1.0, 30).move_to([.6, -.5, 0]), "guard": Box("exit guard\n:8899", RED_, 2.0, 1.0, 24).move_to([3.7, -.5, 0]), "board": Box("blackboard", TEAL_, 2.1, .85, 24).move_to([-2.6, -.5, 0]), "out": Box("outside", GREY_B, 1.5, .85, 24).move_to([6.1, -.5, 0])}
        L = [link(P["prompt"], P["relay"]), link(P["relay"], P["cle"], BLUE_, UP + RIGHT * .0, LEFT), link(P["cle"], P["agents"], BLUE_), link(P["relay"], P["one"]), link(P["one"], P["clara"], DIM, DOWN, UP), link(P["clara"], P["guard"]), link(P["guard"], P["out"]), link(P["clara"], P["board"], DIM, LEFT, RIGHT)]
        def facts(*lines):
            return VGroup(*[T(t, 26) for t in lines]).arrange(DOWN, buff=.13).move_to([0, -2.65, 0])
        cur = facts("Clara runs on the workstation: writes code, trains, inspects", "sees patient data only through the local model", "network: loopback only, enforced by the kernel sandbox")
        self.play(DrawBorderThenFill(P["clara"]), run_time=.7); self.play(P["clara"].on(), run_time=.3); self.to(.1); self.play(FadeIn(cur[0]), run_time=.4); self.to(.5); self.play(FadeIn(cur[1]), run_time=.4); self.to(.72); self.play(FadeIn(cur[2]), run_time=.4)
        seen = [P["clara"]]
        def show(new, lit, links, lines):
            nonlocal cur
            f = facts(*lines); self.play(FadeOut(cur), FadeIn(f), *[n.off() for n in seen], *[FadeIn(n) for n in new], *[GrowArrow(l) for l in links], run_time=.6); seen.extend(new); self.play(*[x.on() for x in lit], run_time=.35); cur = f
        self.beat(1); show([P["prompt"]], [P["prompt"]], [], ["the prompt states the goal, from phone, desktop or browser", "no patient data, has network access"])
        self.beat(2); show([P["cle"], P["agents"]], [P["cle"]], [L[2]], ["Clé: on-premise model hub at Charité, splits the request", "no patient data. Research agents use it for papers and code"]); self.to(.7); self.play(P["cle"].off(), P["agents"].on(), run_time=.4)
        self.beat(3); show([P["relay"]], [P["relay"]], [L[0], L[1]], ["the relay checks every request on port 8770", "fixed rules first: data paths, subject ids, cohort names, image files,", "privacy markers go to the local model"]); self.to(.68); self.play(FadeIn(P["one"]), GrowArrow(L[3]), run_time=.4); self.play(P["one"].on(), run_time=.3)
        self.beat(4); show([], [P["one"]], [L[4]], ["System One: a small decision model on the workstation", "picks the model, gives a verdict, gates Clara's commands", "no patient data, no network"])
        self.beat(5); show([P["guard"], P["out"]], [P["guard"]], [L[5], L[6]], ["the exit guard on port 8899 blocks anything with a data reference", "only checked technical questions pass out"]); self.to(.7); self.play(P["guard"].off(), FadeIn(P["board"]), GrowArrow(L[7]), run_time=.5); self.play(P["board"].on(), run_time=.3); self.finish()
