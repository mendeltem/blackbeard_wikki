#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Archivierte Fassung einer Seite zu einem Stichtag holen und als Text ausgeben.

Für Preis- und Spezifikationsarchäologie: Anbieter überschreiben ihre Preis- und
Datenblattseiten ohne Versionierung. Die Wayback Machine hat oft einen
Schnappschlag, und dessen Zeitstempel ist ein belegbares Datum für die Zahl.

Nur Standardbibliothek, kein pip.
"""
import argparse
import json
import re
import sys
import urllib.request

API = "http://archive.org/wayback/available?url={url}&timestamp={ts}"
UA = {"User-Agent": "Mozilla/5.0 (wayback_snapshot)"}


def hole(url, timeout=90):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def schnappschuss(url, stichtag, timeout=60):
    """Nächstgelegener Schnappschuss. Gibt (archiv_url, zeitstempel) oder (None, None)."""
    d = json.loads(hole(API.format(url=url, ts=stichtag), timeout))
    c = d.get("archived_snapshots", {}).get("closest")
    if not c or not c.get("available"):
        return None, None
    return c["url"], c["timestamp"]


def zu_text(html):
    """HTML grob zu Fließtext. Entfernt script und style, dann alle Tags."""
    t = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&")
          .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"'))
    return re.sub(r"\s+", " ", t).strip()


def ausschnitt(text, stichwort, vor=200, nach=1200, alle=False):
    """Textausschnitte um ein Stichwort. Ohne Treffer: leere Liste."""
    if not stichwort:
        return [text]
    out = []
    for m in re.finditer(re.escape(stichwort), text, re.I):
        out.append(text[max(0, m.start() - vor):m.start() + nach])
        if not alle:
            break
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("url", help="Seite ohne Schema, z. B. openai.com/api/pricing")
    p.add_argument("stichtag", help="JJJJMMTT, z. B. 20240601")
    p.add_argument("-s", "--stichwort", default=None, help="Text, um den herum ausgeschnitten wird")
    p.add_argument("--vor", type=int, default=200)
    p.add_argument("--nach", type=int, default=1200)
    p.add_argument("--alle", action="store_true", help="alle Treffer statt nur dem ersten")
    p.add_argument("--timeout", type=int, default=90)
    a = p.parse_args(argv)

    su, st = schnappschuss(a.url, a.stichtag, a.timeout)
    if not su:
        print("kein Schnappschuss gefunden fuer %s @ %s" % (a.url, a.stichtag), file=sys.stderr)
        return 2
    print("# quelle: %s" % su)
    print("# zeitstempel: %s" % st)
    text = zu_text(hole(su, a.timeout))
    teile = ausschnitt(text, a.stichwort, a.vor, a.nach, a.alle)
    if not teile:
        print("# stichwort nicht gefunden, %d Zeichen Text geholt" % len(text), file=sys.stderr)
        return 3
    for t in teile:
        print(t)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
