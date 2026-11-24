#!/usr/bin/env python3
"""Deliver folder of a finished film: the film and index.html on top, everything else in parts/.

    python film_page.py <film folder> <name> --title "..." --out <deliver folder> [--intro "one sentence"] [--body fragment.html] [--top other.mp4 ...]

Needs video/<name>.mp4 (finish.sh), chapters.txt, audio_beats/state.json and a "## Sources" list in source.md.
The page has one big video, the chapter list with clickable times, an optional body (an HTML fragment, e.g. a report)
and every source as a link that opens in a new tab. Standard library only; ffprobe is used when it is there.
Exit 1 when something the page needs is missing; nothing is deleted, existing files in --out are overwritten by name."""
import argparse, html, json, re, shutil, subprocess, sys
from pathlib import Path

URL = re.compile(r"https?://[^\s<>)\]]+[^\s<>)\].,;]")


def chapters(film):
    """-> [(key, title, start seconds, length seconds)] from chapters.txt, the chapter files and the voice timing."""
    state = json.loads((film / "audio_beats/state.json").read_text()); out, t = [], 0.0
    for line in (film / "chapters.txt").read_text().splitlines():
        if not line.strip(): continue
        file, cls, key = line.split()[:3]
        m = re.search(rf'class {cls}\b.*?title\s*=\s*"([^"]*)"', (film / file).read_text(), re.S)
        n = len(json.loads((film / f"beats/{key}_beats.json").read_text()))
        d = sum(state[f"{key}_{i}.wav"]["seconds"] for i in range(n))
        out.append((key, m.group(1) if m else key, t, d)); t += d
    return out


def sources(film):
    """Lines of the list under the heading that contains 'Sources' in source.md."""
    lines, on = [], False
    for l in (film / "source.md").read_text().splitlines():
        if l.startswith("#"): on = "source" in l.lower() and l.lstrip("#").strip().lower().startswith("sources"); continue
        if on and l.strip().startswith(("-", "*")) or (on and re.match(r"\s*\d+\.", l)): lines.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s*", "", l))
    return lines


def linked(text):
    """Escaped text with every web address turned into a link that opens in a new tab."""
    out, last = [], 0
    for m in URL.finditer(text):
        u = m.group(0); out.append(html.escape(text[last:m.start()])); out.append(f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(u)}</a>'); last = m.end()
    return "".join(out) + html.escape(text[last:])


def clock(s):
    return f"{int(s) // 60}:{int(s) % 60:02d}"


CSS = """:root{--bg:#f6f4ee;--ink:#1c1e22;--dim:#5d636b;--line:#d9d5ca;--card:#fffdf8;--acc:#0f6e8c}
@media (prefers-color-scheme:dark){:root{--bg:#0b0d12;--ink:#ece9e1;--dim:#9aa0a8;--line:#262a33;--card:#12151c;--acc:#58C4DD}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 Georgia,'CMU Serif',serif}
main{max-width:1000px;margin:0 auto;padding:24px 16px 64px}h1{font-size:1.9rem;line-height:1.2;margin:.2em 0 .3em}h2{font-size:1.35rem;margin:2em 0 .5em;border-bottom:1px solid var(--line);padding-bottom:.25em}h3{font-size:1.1rem;margin:1.4em 0 .3em}
p.intro{color:var(--dim);margin:0 0 1em}video{width:100%;border-radius:8px;background:#000;display:block}
ol.ch{list-style:none;padding:0;margin:.8em 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:8px}
ol.ch button{width:100%;text-align:left;font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:6px;padding:8px 10px;cursor:pointer}
ol.ch button:hover,ol.ch button.now{border-color:var(--acc)}ol.ch b{color:var(--acc);font-variant-numeric:tabular-nums;margin-right:.5em}
a{color:var(--acc)}ol.src li{margin:.45em 0;overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;margin:.6em 0;font-size:.95em}th,td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}th{background:var(--card)}
.wrap{overflow-x:auto}code{font:.88em ui-monospace,Menlo,Consolas,monospace;background:var(--card);border:1px solid var(--line);border-radius:4px;padding:0 .3em}
.note{background:var(--card);border-left:4px solid var(--acc);padding:.6em .9em;margin:1em 0}.small{color:var(--dim);font-size:.9em}"""

JS = """const v=document.getElementById('film'),bs=[...document.querySelectorAll('ol.ch button')];
bs.forEach(b=>b.onclick=()=>{v.currentTime=+b.dataset.t;v.play()});
v.ontimeupdate=()=>{let k=-1;bs.forEach((b,i)=>{if(v.currentTime>=+b.dataset.t-.05)k=i});bs.forEach((b,i)=>b.classList.toggle('now',i===k))};"""


def main():
    a = argparse.ArgumentParser(); a.add_argument("film"); a.add_argument("name"); a.add_argument("--title", required=True); a.add_argument("--out", required=True)
    a.add_argument("--intro", default=""); a.add_argument("--body"); a.add_argument("--top", nargs="*", default=[]); A = a.parse_args()
    film, out = Path(A.film).resolve(), Path(A.out).resolve(); mp4 = film / f"video/{A.name}.mp4"
    need = [mp4, film / "chapters.txt", film / "audio_beats/state.json", film / "source.md"] + [Path(t) for t in A.top] + ([Path(A.body)] if A.body else [])
    missing = [str(p) for p in need if not p.exists()]
    if missing: sys.exit("missing: " + ", ".join(missing))
    if len(A.top) > 2: sys.exit("at most 3 mp4 on top (the film and two more)")
    ch, src = chapters(film), sources(film)
    if not src: sys.exit('source.md has no list under a "## Sources" heading: every film names its sources')
    parts = out / "parts"; parts.mkdir(parents=True, exist_ok=True); shutil.copy2(mp4, out / mp4.name)
    for t in A.top: shutil.copy2(t, out / Path(t).name)
    keep = [p for p in sorted((film / "video").glob("[0-9][0-9]_*.mp4"))] + [film / "source.md", film / "chapters.txt"] + sorted(film.glob("chapters*.py")) + [p for p in (film / "check/say_check.mp3", film / "check/say_check.md", film / "check/see_report.md") if p.exists()]
    for p in keep: shutil.copy2(p, parts / p.name)
    (parts / "beats").mkdir(exist_ok=True)
    for p in sorted((film / "beats").glob("*_beats.json")): shutil.copy2(p, parts / "beats" / p.name)
    total = sum(c[3] for c in ch); body = Path(A.body).read_text() if A.body else ""
    items = "".join(f'<li><button data-t="{c[2]:.2f}"><b>{clock(c[2])}</b>{i + 1}. {html.escape(c[1])}</button></li>' for i, c in enumerate(ch))
    more = "".join(f'<p><a href="{html.escape(Path(t).name)}">{html.escape(Path(t).name)}</a></p>' for t in A.top)
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(A.title)}</title><style>{CSS}</style></head><body><main>
<h1>{html.escape(A.title)}</h1>{f'<p class="intro">{html.escape(A.intro)}</p>' if A.intro else ''}
<video id="film" src="{html.escape(mp4.name)}" controls preload="metadata"></video>
<ol class="ch">{items}</ol>{more}
{body}
<h2 id="sources">Sources</h2><ol class="src">{''.join(f'<li>{linked(s)}</li>' for s in src)}</ol>
<p class="small">Film: {clock(total)} min, {len(ch)} chapters. Chapter files, the script (beats), the source sheet and the pronunciation check are in <a href="parts/">parts/</a>.</p>
</main><script>{JS}</script></body></html>"""
    (out / "index.html").write_text(page)
    real = None
    try: real = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out / mp4.name)], capture_output=True, text=True).stdout)
    except Exception: pass
    print(f"{out}/index.html: {len(ch)} chapters, {clock(total)} by voice timing" + (f", file {clock(real)}" if real else ", file length not measured (no ffprobe)") + f", {len(src)} sources, {len(list(parts.rglob('*')))} files in parts/")
    if real and abs(real - total) > 1.5: print(f"WARNING: file length and voice timing differ by {abs(real - total):.1f} s: chapter times may be off")
    top = [p.name for p in out.iterdir() if p.is_file()]
    if len([t for t in top if t.endswith('.mp4')]) > 3: print("WARNING: more than 3 mp4 on top; move the others to parts/")


if __name__ == "__main__":
    main()
