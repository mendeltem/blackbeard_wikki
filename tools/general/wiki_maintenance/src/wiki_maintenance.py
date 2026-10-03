# -*- coding: utf-8 -*-
"""Pflege der Blackboard-Wiki: TODO-Sammlung, tote Links, fehlende Indexzeilen.

    python wiki_maintenance.py --root /pfad/zur/wiki --todo TODO.md
    python wiki_maintenance.py --root /pfad/zur/wiki --check

--todo schreibt eine Sammelliste aller offenen Punkte aus knowledge/.
--check meldet tote interne Links und Einträge, die in keiner INDEX.md stehen,
und endet mit Exit-Code 1, wenn es etwas findet.
Offen ist ein Eintrag mit `status: offen`, dazu jede Zeile unter einer
Überschrift "## Zu prüfen" oder "## Zu pruefen" in beliebigen Einträgen.
"""
import argparse
import os
import re
import sys

_FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)
_LINK = re.compile(r"\]\(([^)\s]+)\)")
_TODO_HEAD = re.compile(r"^## Zu pr(?:ü|ue)fen\s*$", re.M)


def parse_entry(text):
    """Frontmatter-Felder, Titel und Zeilen unter "Zu prüfen" eines Eintrags."""
    meta = {}
    m = _FRONT.match(text)
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    t = re.search(r"^# (.+)$", text, re.M)
    meta["titel"] = t.group(1).strip() if t else ""
    todos = []
    h = _TODO_HEAD.search(text)
    if h:
        rest = text[h.end():]
        nxt = re.search(r"^## ", rest, re.M)
        block = rest[:nxt.start()] if nxt else rest
        for line in block.split("\n"):
            s = line.strip()
            if re.match(r"^(\d+\.|-|\*)\s+", s):
                todos.append(re.sub(r"^(\d+\.|-|\*)\s+", "", s))
    meta["todos"] = todos
    return meta


def entry_files(root):
    """Alle Einträge unter knowledge/<bereich>/<typ>/*.md, sortiert."""
    base = os.path.join(root, "knowledge")
    out = []
    for area in sorted(os.listdir(base)):
        ad = os.path.join(base, area)
        if not os.path.isdir(ad):
            continue
        for sub in sorted(os.listdir(ad)):
            sd = os.path.join(ad, sub)
            if not os.path.isdir(sd):
                continue
            for f in sorted(os.listdir(sd)):
                if f.endswith(".md"):
                    out.append((area, sub, os.path.join(sd, f)))
    return out


def rebase_links(text, entry_dir, root):
    """Relative Links aus einem Eintrag so umschreiben, dass sie von der Wurzel aus gelten."""
    def fix(m):
        target = m.group(1)
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, frag = target.partition("#")
        new = os.path.relpath(os.path.normpath(os.path.join(entry_dir, path)), root).replace(os.sep, "/")
        return "](%s%s)" % (new, "#" + frag if frag else "")
    return _LINK.sub(fix, text)


def collect_open(root):
    """Offene Punkte je Bereich: Einträge mit status offen und alle Zu-prüfen-Zeilen."""
    items = []
    for area, sub, path in entry_files(root):
        meta = parse_entry(open(path, encoding="utf-8").read())
        if meta.get("status") == "offen" or meta["todos"]:
            items.append({
                "bereich": area,
                "pfad": os.path.relpath(path, root).replace(os.sep, "/"),
                "titel": meta["titel"],
                "typ": meta.get("typ", ""),
                "status": meta.get("status", ""),
                "stand": meta.get("stand", ""),
                "todos": [rebase_links(t, os.path.dirname(path), root) for t in meta["todos"]],
            })
    return items


def render_todo(items, datum):
    """Markdown der Sammelliste, gruppiert nach Bereich."""
    lines = ["# TODO", "",
             "Automatisch erzeugt von `tools/general/wiki_maintenance` am %s. Nicht von Hand bearbeiten:" % datum,
             "Änderungen gehören in den jeweiligen Eintrag, danach Liste neu erzeugen.", "",
             "%d offene Einträge." % len(items), ""]
    area = None
    for it in items:
        if it["bereich"] != area:
            area = it["bereich"]
            if lines[-1] != "":
                lines.append("")
            lines += ["## %s" % area, ""]
        lines.append("- [%s](%s) (%s, %s, Stand %s)" % (it["titel"], it["pfad"], it["typ"], it["status"], it["stand"]))
        for t in it["todos"]:
            lines.append("  - [ ] %s" % t)
    return "\n".join(lines) + "\n"


def dead_links(root):
    """Interne Markdown-Links, deren Ziel nicht existiert: Liste (Datei, Ziel)."""
    bad = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(d, f)
            for target in _LINK.findall(open(p, encoding="utf-8").read()):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                target = target.split("#")[0]
                if not os.path.exists(os.path.normpath(os.path.join(d, target))):
                    bad.append((os.path.relpath(p, root).replace(os.sep, "/"), target))
    return bad


def unindexed(root):
    """Einträge, die in der INDEX.md ihres Bereichs nicht verlinkt sind."""
    missing = []
    for area, sub, path in entry_files(root):
        idx = os.path.join(root, "knowledge", area, "INDEX.md")
        text = open(idx, encoding="utf-8").read() if os.path.exists(idx) else ""
        rel = "%s/%s" % (sub, os.path.basename(path))
        if rel not in text:
            missing.append(os.path.relpath(path, root).replace(os.sep, "/"))
    return missing


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", required=True, help="Wurzel der Wiki")
    ap.add_argument("--todo", help="Zieldatei der Sammelliste, relativ zur Wurzel")
    ap.add_argument("--datum", default=None, help="Datum im Kopf der Liste, Standard heute")
    ap.add_argument("--check", action="store_true", help="tote Links und fehlende Indexzeilen prüfen")
    a = ap.parse_args()
    if a.todo:
        import datetime
        datum = a.datum or datetime.date.today().isoformat()
        items = collect_open(a.root)
        open(os.path.join(a.root, a.todo), "w", encoding="utf-8").write(render_todo(items, datum))
        print("%d offene Einträge nach %s" % (len(items), a.todo))
    if a.check:
        bad = dead_links(a.root)
        miss = unindexed(a.root)
        for p, t in bad:
            print("toter Link: %s -> %s" % (p, t))
        for p in miss:
            print("nicht im Index: %s" % p)
        print("%d tote Links, %d Einträge ohne Indexzeile" % (len(bad), len(miss)))
        sys.exit(1 if bad or miss else 0)
