#!/usr/bin/env python3
"""Render the blackbeard_wikki Markdown sources into a browsable HTML site.

Markdown stays the source of truth (agents write it). This tool builds, for humans,
a site with an index.html that links to every other page: one page per area
(SUMMARY on top, entries as collapsible details), one page per entry, tools,
log, open checks, rules. Plus search.js for client-side search and a JSON index
for machines. Only the standard library and python-markdown are used.

Usage: python wiki_html.py --root <wiki root> --out <output dir> [--base-url URL]
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    sys.exit("python-markdown fehlt: pip install markdown")

GITHUB = "https://github.com/mendeltem/blackbeard_wikki/blob/main/"
TYPE_LABEL = {"axioms": "Axiom", "mechanisms": "Mechanismus", "risks": "Risiko", "rules": "Regel",
              "open_checks": "Prüfpunkt", "findings": "Befund", "assets": "Material"}
TYPE_ORDER = ["axioms", "rules", "mechanisms", "findings", "risks", "open_checks", "assets"]
STATUS_CLASS = {"getragen": "ok", "vorschlag": "warn", "offen": "info", "gebrochen": "bad", "widerlegt": "bad"}

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])


# ----------------------------------------------------------------- parsing

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str):
    meta, body = {}, text
    if text.startswith("---"):
        parts = text.split("\n---", 1)
        if len(parts) == 2:
            for line in parts[0].splitlines()[1:]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    v = v.strip()
                    if v.startswith("[") and v.endswith("]"):
                        v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
                    meta[k.strip()] = v
            body = parts[1].lstrip("\n")
    return meta, body


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def strip_heading(body: str) -> str:
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:i] + lines[i + 1:])
    return body


def section(body: str, name: str) -> str:
    """Text under '## <name>' until the next '## '."""
    m = re.search(r"^## " + re.escape(name) + r"\s*$(.*?)(?=^## |\Z)", body, re.M | re.S)
    return m.group(1).strip() if m else ""


def parse_table_rows(text: str):
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows[1:] if rows else []


LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def link_target(cell: str):
    m = LINK_RE.search(cell)
    return (m.group(1), m.group(2)) if m else (cell, None)


def git_history(root: Path):
    """Return (last_change per file, commits list, commits per day)."""
    try:
        out = subprocess.run(["git", "log", "--format=%H\t%ci\t%s", "--name-only"],
                             cwd=root, capture_output=True, text=True, check=True).stdout
    except Exception:
        return {}, [], Counter()
    last, commits, per_day, cur = {}, [], Counter(), None
    for line in out.splitlines():
        if "\t" in line and len(line.split("\t")[0]) == 40:
            h, ci, s = line.split("\t", 2)
            cur = {"hash": h, "date": ci[:10], "time": ci[11:16], "msg": s, "files": []}
            commits.append(cur)
            per_day[ci[:10]] += 1
        elif line.strip() and cur is not None:
            cur["files"].append(line.strip())
            last.setdefault(line.strip(), (cur["date"], cur["msg"]))
    return last, commits, per_day


# ------------------------------------------------------------------ model

class Wiki:
    def __init__(self, root: Path):
        self.root = root
        self.map = {}       # md source (relative) -> html output (relative)
        self.entries = []   # dicts
        self.areas = []     # dicts
        self.tools = []     # dicts
        self.last, self.commits, self.per_day = git_history(root)
        self.scan()

    def register(self, src: str, out: str):
        self.map[src] = out

    def scan(self):
        r = self.root
        self.register("README.md", "rules.html")
        self.register("INDEX.md", "index.html")
        self.register("TODO.md", "todo.html")
        self.register("updates/LOG.md", "log.html")
        self.register("knowledge/INDEX.md", "index.html#bereiche")
        self.register("tools/INDEX.md", "tools/index.html")
        # areas from knowledge/INDEX.md
        desc = {}
        for cells in parse_table_rows(read(r / "knowledge/INDEX.md")):
            if len(cells) >= 3:
                name, _ = link_target(cells[0])
                desc[name] = {"inhalt": cells[1], "stichwoerter": cells[2]}
        for d in sorted((r / "knowledge").iterdir()):
            if not d.is_dir():
                continue
            area = {"name": d.name, "dir": d, "entries": [], **desc.get(d.name, {"inhalt": "", "stichwoerter": ""})}
            self.register(f"knowledge/{d.name}/INDEX.md", f"{d.name}/index.html")
            self.register(f"knowledge/{d.name}/SUMMARY.md", f"{d.name}/index.html#kurzstand")
            area["summary"] = read(d / "SUMMARY.md") if (d / "SUMMARY.md").exists() else ""
            area["intro"] = ""
            inhalt = {}
            if (d / "INDEX.md").exists():
                idx = read(d / "INDEX.md")
                area["intro"] = "\n".join(l for l in idx.split("\n|")[0].splitlines()[1:]).strip()
                for cells in parse_table_rows(idx):
                    if len(cells) >= 3:
                        _, tgt = link_target(cells[1])
                        if tgt:
                            inhalt[Path(tgt).stem] = cells[2]
            for td in sorted(d.iterdir()):
                if not td.is_dir():
                    continue
                for f in sorted(td.glob("*.md")):
                    if f.name == "INDEX.md":
                        self.register(f"knowledge/{d.name}/{td.name}/INDEX.md", f"{d.name}/index.html#{td.name}")
                        continue
                    meta, body = parse_frontmatter(read(f))
                    rel = f.relative_to(r).as_posix()
                    e = {"id": meta.get("id", f.stem), "file": f, "rel": rel, "area": d.name,
                         "type": td.name, "typ": meta.get("typ", TYPE_LABEL.get(td.name, td.name).lower()),
                         "status": str(meta.get("status", "")), "stand": str(meta.get("stand", "")),
                         "herkunft": str(meta.get("herkunft", "")),
                         "verweist": meta.get("verweist_auf", []) if isinstance(meta.get("verweist_auf"), list) else [],
                         "title": first_heading(body, f.stem), "body": strip_heading(body),
                         "inhalt": inhalt.get(f.stem, ""), "out": f"{d.name}/{td.name}/{f.stem}.html"}
                    e["aussage"] = section(body, "Aussage") or section(body, "Frage") or ""
                    e["changed"] = self.last.get(rel, ("", ""))
                    self.register(rel, e["out"])
                    area["entries"].append(e)
                    self.entries.append(e)
            self.areas.append(area)
        # tools: every directory under tools/ with a README.md
        for readme in sorted((r / "tools").rglob("README.md")):
            td = readme.parent
            rel_dir = td.relative_to(r).as_posix()
            meta, body = parse_frontmatter(read(readme))
            t = {"name": td.name, "rel_dir": rel_dir, "dir": td, "title": first_heading(body, td.name),
                 "body": strip_heading(body), "out": f"{rel_dir}/index.html",
                 "changed": self.last.get(f"{rel_dir}/README.md", ("", "")), "extra": []}
            self.register(f"{rel_dir}/README.md", t["out"])
            for extra in sorted(td.glob("*.md")):
                if extra.name not in ("README.md", "INDEX.md"):
                    out = f"{rel_dir}/{extra.stem.lower()}.html"
                    self.register(f"{rel_dir}/{extra.name}", out)
                    t["extra"].append((extra, out))
            self.tools.append(t)
        for idx in (r / "tools").rglob("INDEX.md"):
            rel = idx.relative_to(r).as_posix()
            self.map.setdefault(rel, "tools/index.html")
        self.by_id = {e["id"]: e for e in self.entries}
        self.backlinks = defaultdict(list)
        for e in self.entries:
            for v in e["verweist"]:
                if v in self.by_id:
                    self.backlinks[v].append(e)


# ---------------------------------------------------------------- rendering

def rel_href(from_out: str, to_out: str) -> str:
    frag = ""
    if "#" in to_out:
        to_out, frag = to_out.split("#", 1)
        frag = "#" + frag
    p = os.path.relpath(to_out, os.path.dirname(from_out) or ".")
    return p.replace(os.sep, "/") + frag


def md_to_html(wiki: Wiki, text: str, src_rel: str, out_rel: str) -> str:
    """Convert Markdown, rewriting relative links to the HTML site or GitHub."""
    MD.reset()
    h = MD.convert(text)
    src_dir = Path(src_rel).parent

    def fix(m):
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", href):
            return m.group(0)
        path, frag = (href.split("#", 1) + [""])[:2]
        target = os.path.normpath((src_dir / path).as_posix()).replace(os.sep, "/")
        if target.startswith("../") or target == "..":
            return m.group(0)
        if target in wiki.map:
            dest = wiki.map[target]
            if frag and "#" not in dest:
                dest += "#" + frag
            return f'href="{rel_href(out_rel, dest)}"'
        return f'href="{GITHUB}{target}{("#" + frag) if frag else ""}"'

    return re.sub(r'href="([^"]+)"', fix, h)


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def badge(status: str) -> str:
    key = status.split()[0].lower() if status else ""
    return f'<span class="badge {STATUS_CLASS.get(key, "")}">{esc(status or "ohne Status")}</span>'


def svg_bars(series, width=640, height=90, label=""):
    """Simple inline SVG bar chart; series = list of (label, value)."""
    if not series:
        return ""
    mx = max(v for _, v in series) or 1
    n = len(series)
    bw = width / n
    bars = []
    for i, (lab, v) in enumerate(series):
        bh = (height - 20) * v / mx
        bars.append(f'<rect x="{i*bw:.1f}" y="{height-20-bh:.1f}" width="{max(bw-1,1):.1f}" height="{bh:.1f}" rx="1">'
                    f'<title>{esc(lab)}: {v}</title></rect>')
    ticks = [f'<text x="0" y="{height-5}">{esc(series[0][0])}</text>',
             f'<text x="{width}" y="{height-5}" text-anchor="end">{esc(series[-1][0])}</text>']
    return (f'<figure class="plot"><svg viewBox="0 0 {width} {height}" preserveAspectRatio="none" role="img" '
            f'aria-label="{esc(label)}">{"".join(bars)}{"".join(ticks)}</svg>'
            f'<figcaption>{esc(label)} (max {mx})</figcaption></figure>')


CSS = """
:root{--bg:#f7f6f2;--fg:#1d1d1b;--muted:#6b6a64;--card:#ffffff;--line:#e2e0d8;--accent:#1f5f8b;--ok:#2e7d32;--warn:#b26a00;--bad:#b3261e;--info:#1f5f8b;--bar:#9fb7c9;--font:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15171a;--fg:#e8e6e0;--muted:#9a9890;--card:#1e2126;--line:#30343a;--accent:#7fb3d8;--ok:#7bc67e;--warn:#e0a84b;--bad:#ef7b74;--info:#7fb3d8;--bar:#4c6a80}}
:root[data-theme="dark"]{--bg:#15171a;--fg:#e8e6e0;--muted:#9a9890;--card:#1e2126;--line:#30343a;--accent:#7fb3d8;--ok:#7bc67e;--warn:#e0a84b;--bad:#ef7b74;--info:#7fb3d8;--bar:#4c6a80}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 var(--font)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header.top{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);z-index:5}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px}
nav.main{display:flex;flex-wrap:wrap;gap:4px 16px;align-items:center;padding:10px 0}
nav.main a.brand{font-weight:700;color:var(--fg)}nav.main input{margin-left:auto;min-width:160px;flex:1 1 160px;max-width:360px;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg)}
#hits{position:absolute;right:16px;left:16px;max-width:1068px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.15);max-height:60vh;overflow:auto;display:none}
#hits a{display:block;padding:8px 12px;border-bottom:1px solid var(--line);color:var(--fg)}#hits a small{color:var(--muted);display:block}
main{padding:20px 0 60px}h1{font-size:1.6rem;line-height:1.25;margin:.4em 0}h2{font-size:1.25rem;margin-top:1.6em;border-bottom:1px solid var(--line);padding-bottom:4px}h3{font-size:1.05rem}
.crumbs{color:var(--muted);font-size:.9rem}.crumbs a{color:var(--muted)}
.muted{color:var(--muted)}.small{font-size:.9rem}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:16px 0}
.tile{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}.tile b{font-size:1.5rem;display:block}.tile span{color:var(--muted);font-size:.85rem}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:6px}
.card h3{margin:0}.card .kw{color:var(--muted);font-size:.82rem}.card .counts{font-size:.85rem;display:flex;flex-wrap:wrap;gap:6px 10px}
.stripe{display:flex;height:6px;border-radius:3px;overflow:hidden;background:var(--line)}.stripe i{display:block}
.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}.info{color:var(--info)}
.stripe .ok{background:var(--ok)}.stripe .warn{background:var(--warn)}.stripe .bad{background:var(--bad)}.stripe .info{background:var(--info)}
.badge{display:inline-block;font-size:.75rem;padding:1px 8px;border-radius:999px;border:1px solid currentColor;line-height:1.5;white-space:nowrap}
.type{display:inline-block;font-size:.75rem;padding:1px 8px;border-radius:4px;background:var(--line);color:var(--fg);white-space:nowrap}
details.entry{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:8px 0;padding:0}
details.entry>summary{cursor:pointer;padding:10px 14px;list-style:none;display:flex;flex-wrap:wrap;gap:6px 10px;align-items:baseline}
details.entry>summary::-webkit-details-marker{display:none}details.entry>summary::before{content:"▸";color:var(--muted);margin-right:2px}details.entry[open]>summary::before{content:"▾"}
details.entry>summary .t{font-weight:600;flex:1 1 60%}details.entry>summary .i{flex-basis:100%;color:var(--muted);font-size:.9rem;font-weight:400}
details.entry>.body{padding:0 14px 12px;border-top:1px solid var(--line)}
.summary{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:10px;padding:4px 16px;margin:12px 0}
table{border-collapse:collapse;max-width:100%;display:block;overflow-x:auto;font-size:.92rem}th,td{border:1px solid var(--line);padding:4px 8px;text-align:left;vertical-align:top}th{background:var(--line)}
pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px;overflow-x:auto;font-size:.85rem}code{font-size:.9em}
.meta{font-size:.9rem;color:var(--muted);display:grid;grid-template-columns:max-content 1fr;gap:2px 12px;margin:10px 0}
.plot svg{width:100%;height:auto;fill:var(--bar)}.plot svg text{fill:var(--muted);font-size:11px}.plot{margin:12px 0}.plot figcaption{color:var(--muted);font-size:.85rem}
ul.changes{list-style:none;padding:0}ul.changes li{padding:6px 0;border-bottom:1px solid var(--line)}ul.changes .d{color:var(--muted);font-variant-numeric:tabular-nums;margin-right:8px}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px}
footer{color:var(--muted);font-size:.85rem;border-top:1px solid var(--line);padding:12px 0}
@media (max-width:600px){body{font-size:15px}h1{font-size:1.3rem}}
"""

SEARCH_JS = """
(function(){var q=document.getElementById('q'),h=document.getElementById('hits');if(!q||!window.WIKI_INDEX)return;
var root=q.getAttribute('data-root');
function run(){var v=q.value.trim().toLowerCase();if(v.length<2){h.style.display='none';h.innerHTML='';return;}
var terms=v.split(/\\s+/),out=[];for(var i=0;i<WIKI_INDEX.length&&out.length<40;i++){var e=WIKI_INDEX[i],hay=(e.t+' '+e.x+' '+e.a+' '+e.y+' '+e.s).toLowerCase(),ok=true;
for(var j=0;j<terms.length;j++){if(hay.indexOf(terms[j])<0){ok=false;break;}}if(ok)out.push(e);}
h.innerHTML=out.length?out.map(function(e){return '<a href="'+root+e.p+'">'+e.t+'<small>'+e.a+' · '+e.y+' · '+e.s+(e.d?' · '+e.d:'')+'</small></a>';}).join(''):'<a>keine Treffer</a>';h.style.display='block';}
q.addEventListener('input',run);q.addEventListener('focus',run);document.addEventListener('click',function(ev){if(!h.contains(ev.target)&&ev.target!==q)h.style.display='none';});
document.addEventListener('keydown',function(ev){if(ev.key==='/'&&document.activeElement!==q){ev.preventDefault();q.focus();}});})();
"""


class Site:
    def __init__(self, wiki: Wiki, out: Path, base_url: str):
        self.w, self.out, self.base_url = wiki, out, base_url
        self.built = date.today().isoformat()

    def page(self, out_rel: str, title: str, body: str, crumbs=None):
        root = rel_href(out_rel, "index.html")
        root = "" if root == "index.html" else root[:-len("index.html")]
        nav = [("index.html", "Start"), ("rules.html", "Regeln"), ("todo.html", "Offen"),
               ("log.html", "Protokoll"), ("tools/index.html", "Werkzeuge")]
        links = "".join(f'<a href="{rel_href(out_rel, p)}">{t}</a>' for p, t in nav)
        crumb_html = ""
        if crumbs:
            crumb_html = '<div class="crumbs">' + " › ".join(
                f'<a href="{rel_href(out_rel, p)}">{esc(t)}</a>' if p else esc(t) for p, t in crumbs) + "</div>"
        doc = f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title>
<style>{CSS}</style></head><body>
<header class="top"><div class="wrap"><nav class="main"><a class="brand" href="{rel_href(out_rel, 'index.html')}">blackbeard_wikki</a>{links}
<input id="q" type="search" placeholder="Suchen ( / )" data-root="{root}" autocomplete="off"></nav></div><div id="hits"></div></header>
<main><div class="wrap">{crumb_html}{body}</div></main>
<footer><div class="wrap">Erzeugt {self.built} aus Markdown mit tools/general/wiki_html. Quelle bleibt Markdown, diese Seite ist die Lesefassung.</div></footer>
<script src="{rel_href(out_rel, 'search.js')}"></script></body></html>"""
        p = self.out / out_rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(doc, encoding="utf-8")

    # ---- pieces
    def entry_summary_line(self, e, out_rel):
        return (f'<span class="type">{esc(TYPE_LABEL.get(e["type"], e["typ"]))}</span>'
                f'<span class="t"><a href="{rel_href(out_rel, e["out"])}">{esc(e["title"])}</a></span>'
                f'{badge(e["status"])}<span class="muted small">{esc(e["stand"])}</span>'
                + (f'<span class="i">{esc(e["inhalt"])}</span>' if e["inhalt"] else ""))

    def status_stripe(self, entries):
        c = Counter((e["status"].split() or ["?"])[0].lower() for e in entries)
        n = max(len(entries), 1)
        parts = "".join(f'<i class="{STATUS_CLASS.get(k, "")}" style="width:{100*v/n:.1f}%" title="{esc(k)}: {v}"></i>'
                        for k, v in c.most_common())
        counts = " ".join(f'<span class="{STATUS_CLASS.get(k, "")}">{v} {esc(k)}</span>' for k, v in c.most_common())
        return f'<div class="stripe">{parts}</div><div class="counts">{counts}</div>'

    # ---- pages
    def build(self):
        self.out.mkdir(parents=True, exist_ok=True)
        self.build_index()
        for a in self.w.areas:
            self.build_area(a)
            for e in a["entries"]:
                self.build_entry(e)
        self.build_tools()
        self.build_simple("README.md", "rules.html", "Regeln der Wiki")
        self.build_simple("TODO.md", "todo.html", "Offene Punkte")
        self.build_simple("updates/LOG.md", "log.html", "Änderungsprotokoll")
        self.build_search()

    def build_index(self):
        w = self.w
        open_checks = [e for e in w.entries if e["status"].startswith("offen") or e["type"] == "open_checks"]
        last_commit = w.commits[0] if w.commits else None
        tiles = [(len(w.areas), "Bereiche"), (len(w.entries), "Einträge"), (len(open_checks), "offene Prüfpunkte"),
                 (len(w.tools), "Werkzeuge"), (f'{last_commit["date"]}' if last_commit else "–", "letzter Commit")]
        tiles_html = "".join(f'<div class="tile"><b>{esc(v)}</b><span>{t}</span></div>' for v, t in tiles)
        # recent changes: entries by last commit
        recent = sorted([e for e in w.entries if e["changed"][0]], key=lambda e: e["changed"][0], reverse=True)[:15]
        rec_html = "".join(f'<li><span class="d">{esc(e["changed"][0])}</span><a href="{e["out"]}">{esc(e["title"])}</a>'
                           f' <span class="muted small">{esc(e["area"])} · {esc(e["changed"][1])[:90]}</span></li>' for e in recent)
        # activity plot: commits per day, last 60 days
        today = date.today()
        series = [((today - timedelta(days=i)).isoformat(), w.per_day.get((today - timedelta(days=i)).isoformat(), 0))
                  for i in range(59, -1, -1)]
        plot = svg_bars(series, label="Commits je Tag, letzte 60 Tage")
        # area cards
        cards = []
        for a in sorted(w.areas, key=lambda a: max([e["changed"][0] for e in a["entries"]] or [""]), reverse=True):
            tc = Counter(e["type"] for e in a["entries"])
            counts = " · ".join(f'{v} {TYPE_LABEL.get(k, k)}' for k, v in sorted(tc.items(), key=lambda kv: TYPE_ORDER.index(kv[0]) if kv[0] in TYPE_ORDER else 99))
            newest = max([e["changed"][0] for e in a["entries"]] or [""])
            cards.append(f'<div class="card"><h3><a href="{a["name"]}/index.html">{esc(a["name"])}</a></h3>'
                         f'<div>{esc(a["inhalt"])}</div><div class="kw">{esc(a["stichwoerter"])}</div>'
                         f'{self.status_stripe(a["entries"])}<div class="muted small">{counts or "keine Einträge"}'
                         f'{(" · zuletzt " + newest) if newest else ""}</div></div>')
        open_by_area = Counter(e["area"] for e in open_checks)
        open_html = ", ".join(f'<a href="{a}/index.html#open_checks">{esc(a)} ({n})</a>' for a, n in open_by_area.most_common())
        body = f"""<h1>blackbeard_wikki</h1>
<p>Gemeinsames Wissen aller Agenten und Chats. Lesereihenfolge: Bereich wählen, dort zuerst den <b>Kurzstand</b>, dann die Einträge aufklappen.
Agenten schreiben weiter Markdown, diese Seiten werden daraus erzeugt (<a href="rules.html">Regeln</a>).</p>
<div class="tiles">{tiles_html}</div>
{plot}
<div class="two"><section><h2>Zuletzt geändert</h2><ul class="changes">{rec_html}</ul></section>
<section><h2>Offen</h2><p>{open_html or "nichts offen"}</p><p><a href="todo.html">Alle offenen Punkte</a> · <a href="log.html">Änderungsprotokoll</a> · <a href="tools/index.html">Werkzeuge</a></p>
<h2>Legende</h2><p>{badge("getragen")} belegt und tragend · {badge("vorschlag")} unbestätigt oder mit Annahme · {badge("offen")} Prüfpunkt · {badge("gebrochen")} widerlegt, bleibt stehen</p>
<p class="small muted">Typen: Axiom (Setzung), Regel, Mechanismus (Wirkungskette), Befund (belegt, mit Quelle), Risiko (Gegenkraft), Prüfpunkt (offener Schritt).</p></section></div>
<h2 id="bereiche">Bereiche</h2><div class="cards">{"".join(cards)}</div>"""
        self.page("index.html", "blackbeard_wikki", body)

    def build_area(self, a):
        out_rel = f'{a["name"]}/index.html'
        intro = md_to_html(self.w, a["intro"], f'knowledge/{a["name"]}/INDEX.md', out_rel) if a["intro"] else ""
        summary = md_to_html(self.w, strip_heading(a["summary"]), f'knowledge/{a["name"]}/SUMMARY.md', out_rel) if a["summary"] else "<p class='muted'>kein Kurzstand</p>"
        # timeline of entries by stand
        by_month = Counter(e["stand"][:7] for e in a["entries"] if e["stand"])
        months = sorted(by_month)
        plot = svg_bars([(m, by_month[m]) for m in months], height=70, label="Einträge je Monat (Stand)") if len(months) > 1 else ""
        sections = []
        for t in TYPE_ORDER + sorted(set(e["type"] for e in a["entries"]) - set(TYPE_ORDER)):
            es = [e for e in a["entries"] if e["type"] == t]
            if not es:
                continue
            es.sort(key=lambda e: e["stand"], reverse=True)
            items = []
            for e in es:
                body = md_to_html(self.w, e["body"], e["rel"], out_rel)
                items.append(f'<details class="entry" id="{esc(e["id"])}"><summary>{self.entry_summary_line(e, out_rel)}</summary>'
                             f'<div class="body"><p class="small muted">Herkunft: {esc(e["herkunft"])} · <a href="{rel_href(out_rel, e["out"])}">eigene Seite</a>'
                             f' · <a href="{GITHUB}{e["rel"]}">Markdown</a></p>{body}</div></details>')
            sections.append(f'<h2 id="{t}">{TYPE_LABEL.get(t, t)} <span class="muted small">({len(es)})</span></h2>{"".join(items)}')
        body = f"""<h1>{esc(a["name"])}</h1><p>{esc(a["inhalt"])}</p><p class="muted small">{esc(a["stichwoerter"])}</p>
{self.status_stripe(a["entries"])}{intro and '<div class="small">' + intro + '</div>'}
<h2 id="kurzstand">Kurzstand</h2><div class="summary">{summary}</div>{plot}
<p class="small muted">Einträge aufklappen: Klick auf die Zeile. Alle <a href="#" onclick="document.querySelectorAll('details.entry').forEach(d=>d.open=true);return false">öffnen</a> / <a href="#" onclick="document.querySelectorAll('details.entry').forEach(d=>d.open=false);return false">schließen</a>.</p>
{"".join(sections)}"""
        self.page(out_rel, a["name"], body, crumbs=[("index.html", "Start"), (None, a["name"])])

    def build_entry(self, e):
        out_rel = e["out"]
        body = md_to_html(self.w, e["body"], e["rel"], out_rel)
        refs = []
        for v in e["verweist"]:
            if v in self.w.by_id:
                t = self.w.by_id[v]
                refs.append(f'<a href="{rel_href(out_rel, t["out"])}">{esc(t["title"])}</a> <span class="muted small">({esc(t["area"])})</span>')
            else:
                refs.append(f'<span class="muted">{esc(v)}</span>')
        back = [f'<a href="{rel_href(out_rel, b["out"])}">{esc(b["title"])}</a> <span class="muted small">({esc(b["area"])})</span>'
                for b in self.w.backlinks.get(e["id"], [])]
        meta = (f'<div class="meta"><span>Typ</span><span>{esc(TYPE_LABEL.get(e["type"], e["typ"]))}</span>'
                f'<span>Status</span><span>{badge(e["status"])}</span><span>Stand</span><span>{esc(e["stand"])}</span>'
                f'<span>Herkunft</span><span>{esc(e["herkunft"])}</span>'
                f'<span>Zuletzt geändert</span><span>{esc(e["changed"][0])} {esc(e["changed"][1])}</span>'
                + (f'<span>Verweist auf</span><span>{"<br>".join(refs)}</span>' if refs else "")
                + (f'<span>Verwiesen von</span><span>{"<br>".join(back)}</span>' if back else "")
                + f'<span>Quelle</span><span><a href="{GITHUB}{e["rel"]}">{esc(e["rel"])}</a></span></div>')
        self.page(out_rel, e["title"], f'<h1>{esc(e["title"])}</h1>{meta}{body}',
                  crumbs=[("index.html", "Start"), (f'{e["area"]}/index.html', e["area"]),
                          (f'{e["area"]}/index.html#{e["type"]}', TYPE_LABEL.get(e["type"], e["type"]))])

    def build_tools(self):
        out_rel = "tools/index.html"
        rows = "".join(f'<li><a href="{rel_href(out_rel, t["out"])}">{esc(t["rel_dir"])}</a> — {esc(t["title"])}'
                       f'<span class="muted small"> · zuletzt {esc(t["changed"][0])}</span></li>' for t in self.w.tools)
        idx = self.w.root / "tools/INDEX.md"
        intro = md_to_html(self.w, strip_heading(read(idx)), "tools/INDEX.md", out_rel) if idx.exists() else ""
        self.page(out_rel, "Werkzeuge", f"<h1>Werkzeuge</h1>{intro}<ul>{rows}</ul>", crumbs=[("index.html", "Start"), (None, "Werkzeuge")])
        for t in self.w.tools:
            body = md_to_html(self.w, t["body"], f'{t["rel_dir"]}/README.md', t["out"])
            extra = " · ".join(f'<a href="{rel_href(t["out"], o)}">{esc(f.stem)}</a>' for f, o in t["extra"])
            self.page(t["out"], t["title"], f'<h1>{esc(t["title"])}</h1><p class="small muted">{esc(t["rel_dir"])}'
                      f'{(" · " + extra) if extra else ""} · <a href="{GITHUB}{t["rel_dir"]}">GitHub</a></p>{body}',
                      crumbs=[("index.html", "Start"), ("tools/index.html", "Werkzeuge"), (None, t["name"])])
            for f, o in t["extra"]:
                b = md_to_html(self.w, read(f), f'{t["rel_dir"]}/{f.name}', o)
                self.page(o, f"{t['name']} – {f.stem}", b, crumbs=[("index.html", "Start"), ("tools/index.html", "Werkzeuge"), (t["out"], t["name"]), (None, f.stem)])

    def build_simple(self, src, out_rel, title):
        p = self.w.root / src
        if not p.exists():
            return
        self.page(out_rel, title, md_to_html(self.w, read(p), src, out_rel), crumbs=[("index.html", "Start"), (None, title)])

    def build_search(self):
        idx = []
        for e in self.w.entries:
            snippet = (e["inhalt"] or re.sub(r"\s+", " ", e["aussage"]))[:240]
            idx.append({"t": e["title"], "p": e["out"], "a": e["area"], "y": TYPE_LABEL.get(e["type"], e["typ"]),
                        "s": e["status"], "d": e["stand"], "x": snippet, "id": e["id"], "src": e["rel"]})
        for t in self.w.tools:
            idx.append({"t": t["title"], "p": t["out"], "a": "tools", "y": "Werkzeug", "s": "", "d": t["changed"][0],
                        "x": t["rel_dir"], "id": t["name"], "src": f'{t["rel_dir"]}/README.md'})
        (self.out / "search.js").write_text("window.WIKI_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";\n" + SEARCH_JS, encoding="utf-8")
        (self.out / "index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=0), encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", required=True, help="Wurzel der Wiki (enthält knowledge/, tools/)")
    ap.add_argument("--out", required=True, help="Zielordner, z. B. docs")
    ap.add_argument("--base-url", default="", help="optional, Basis-URL der veröffentlichten Seite")
    args = ap.parse_args(argv)
    root, out = Path(args.root).resolve(), Path(args.out).resolve()
    if not (root / "knowledge").is_dir():
        sys.exit(f"kein knowledge/ unter {root}")
    wiki = Wiki(root)
    Site(wiki, out, args.base_url).build()
    n_pages = sum(1 for _ in out.rglob("*.html"))
    print(f"{len(wiki.areas)} Bereiche, {len(wiki.entries)} Einträge, {len(wiki.tools)} Werkzeuge -> {n_pages} Seiten unter {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
