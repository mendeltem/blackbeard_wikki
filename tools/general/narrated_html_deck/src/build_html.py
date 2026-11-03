"""Step 2: the page: one slide at a time, the voice per slide, keys and buttons. No external files.

    python build_html.py <deck folder> [--title "Name"] [--label internal]

Writes index.html into the deck folder. Keep the page next to figures/ and audio/.
"""
import argparse
import html
import json
import sys
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("deck")
p.add_argument("--title", default="Presentation")
p.add_argument("--label", default="")
args = p.parse_args()
HERE = Path(args.deck).resolve()
sys.path.insert(0, str(HERE))
from slides import SLIDES

seconds = json.loads((HERE / "audio/durations.json").read_text())
sections = ""
for i, s in enumerate(SLIDES, 1):
    body = s.get("html", "")
    if "fig" in s:
        body = f"<figure><img src='figures/{s['fig']}' alt='{html.escape(s['title'])}'><figcaption>{html.escape(s['cap'])}</figcaption></figure>"
    sections += (f"<section class='slide' data-audio='audio/slide{i:02d}.mp3'><h1>{html.escape(s['title'])}</h1><div class='body'>{body}</div>"
                 f"<div class='transcript'><b>Transcript</b><br>{html.escape(s['speech'])}</div></section>\n")
total = sum(v["seconds"] for v in seconds.values()) / 60
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(args.title)}</title><style>
:root{{--bg:#fcfcfb;--ink:#0b0b0b;--mut:#52514e;--line:#dedcd5;--card:#f3f2ee;--blue:#2a78d6;--orange:#eb6834;--ok:#0a7a3c;--bad:#b3261e;--mid:#8a6a00}}
*{{box-sizing:border-box}}html,body{{height:100%}}body{{margin:0;background:var(--bg);color:var(--ink);font:18px/1.45 system-ui,sans-serif;display:flex;flex-direction:column}}
main{{flex:1;overflow:auto;padding:22px 16px}}.slide{{display:none;max-width:1050px;margin:0 auto}}.slide.on{{display:block}}
h1{{font-size:clamp(23px,3.2vw,34px);line-height:1.2;margin:0 0 16px}}h3{{margin:0 0 8px}}.lead{{font-size:clamp(20px,2.4vw,26px);margin:0 0 16px}}
.body li{{margin:8px 0}}figure{{margin:0}}figure img{{display:block;width:100%;max-height:62vh;object-fit:contain}}figcaption,.mut{{color:var(--mut);font-size:15px}}figcaption{{margin-top:8px}}
.eq{{background:var(--card);padding:14px 16px;border-radius:6px;font-size:clamp(16px,2.1vw,21px);margin:0 0 16px;overflow-wrap:anywhere}}
table{{border-collapse:collapse;width:100%}}td,th{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}
.big{{font-size:clamp(17px,2vw,20px)}}.big li{{margin:10px 0}}.yes{{color:var(--ok);font-weight:600;white-space:nowrap}}.no{{color:var(--bad);font-weight:600;white-space:nowrap}}.mid{{color:var(--mid);font-weight:600}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:12px}}.card{{background:var(--card);padding:14px 16px;border-radius:6px;border-top:4px solid}}.card p{{margin:6px 0}}.pos{{border-color:#b2182b}}.neg{{border-color:#2166ac}}
.transcript{{display:none;margin-top:16px;padding:12px 14px;background:var(--card);border-radius:6px;font-size:16px}}body.tr .transcript{{display:block}}
footer{{border-top:1px solid var(--line);padding:10px 16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;background:var(--bg)}}
button,select{{font:inherit;font-size:15px;padding:7px 12px;border:1px solid #bdbbb3;background:#fff;color:var(--ink);border-radius:5px;cursor:pointer}}#play{{background:var(--blue);border-color:var(--blue);color:#fff;min-width:96px}}
#bar{{flex:1 1 180px;height:8px;background:var(--line);border-radius:4px;cursor:pointer;min-width:120px}}#fill{{height:100%;width:0;background:var(--blue);border-radius:4px}}#count{{color:var(--mut);font-size:15px;min-width:60px}}
label{{font-size:15px;color:var(--mut);display:inline-flex;gap:5px;align-items:center}}@media (max-width:680px){{.two{{grid-template-columns:1fr}}body{{font-size:16px}}}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#1a1a19;--ink:#f0efec;--mut:#c3c2b7;--line:#3a3a37;--card:#262624;--ok:#5fd16f;--bad:#ff8a80;--mid:#ffcc33}}button,select{{background:#2c2c2a;color:#f0efec;border-color:#555}}figure img{{background:#fcfcfb;border-radius:4px}}}}
</style></head><body>
<main>{sections}</main>
<footer><button id="prev" title="Previous slide (left arrow)">← Back</button><button id="play" title="Play or pause (space)">▶ Play</button><button id="next" title="Next slide (right arrow)">Next →</button>
<span id="count"></span><div id="bar" title="Click to jump within this slide"><div id="fill"></div></div>
<label><input type="checkbox" id="auto" checked> Auto-advance</label><label>Speed <select id="speed"><option>0.8</option><option selected>1</option><option>1.25</option><option>1.5</option></select></label>
<button id="tr" title="Show the spoken text (T)">Transcript</button><span class="mut">about {total:.0f} min{" &middot; " + html.escape(args.label) if args.label else ""}</span></footer>
<audio id="a" preload="auto"></audio>
<script>
const S=[...document.querySelectorAll('.slide')],a=document.getElementById('a'),pb=document.getElementById('play'),sp=document.getElementById('speed'),au=document.getElementById('auto');let i=0,want=false;
function show(n,play){{i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,k)=>s.classList.toggle('on',k===i));document.querySelector('main').scrollTop=0;document.getElementById('count').textContent=(i+1)+' / '+S.length;a.src=S[i].dataset.audio;a.playbackRate=+sp.value;fill.style.width='0';location.hash=i+1;if(play)start();else stop();}}
const fill=document.getElementById('fill');
function start(){{want=true;a.playbackRate=+sp.value;a.play().catch(()=>{{want=false;pb.textContent='▶ Play';}});pb.textContent='❚❚ Pause';}}
function stop(){{want=false;a.pause();pb.textContent='▶ Play';}}
pb.onclick=()=>a.paused?start():stop();document.getElementById('next').onclick=()=>show(i+1,want);document.getElementById('prev').onclick=()=>show(i-1,want);
a.ontimeupdate=()=>{{if(a.duration)fill.style.width=(100*a.currentTime/a.duration)+'%';}};
a.onended=()=>{{if(au.checked&&i<S.length-1)show(i+1,true);else stop();}};sp.onchange=()=>{{a.playbackRate=+sp.value;}};
document.getElementById('bar').onclick=e=>{{const r=e.currentTarget.getBoundingClientRect();if(a.duration)a.currentTime=a.duration*(e.clientX-r.left)/r.width;}};
document.getElementById('tr').onclick=()=>document.body.classList.toggle('tr');
document.addEventListener('keydown',e=>{{if(e.target.tagName==='SELECT')return;if(e.key===' '){{e.preventDefault();a.paused?start():stop();}}else if(e.key==='ArrowRight')show(i+1,want);else if(e.key==='ArrowLeft')show(i-1,want);else if(e.key==='t'||e.key==='T')document.body.classList.toggle('tr');}});
show((parseInt(location.hash.slice(1))||1)-1,false);
</script></body></html>"""
(HERE / "index.html").write_text(page)
print("wrote", HERE / "index.html", len(SLIDES), "slides,", f"{total:.1f} min")
