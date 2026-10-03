# -*- coding: utf-8 -*-
"""Synthetischer Test fuer wiki_maintenance. Baut eine Mini-Wiki im Temp-Verzeichnis."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import wiki_maintenance as w  # noqa: E402

OFFEN = """---
id: a
typ: pruefpunkt
status: offen
stand: 2026-10-03
---

# Offener Punkt

## Aussage
Text mit Link auf [b](../mechanisms/b.md).

## Zu prüfen
1. Erste Sache
2. Zweite Sache, siehe [b](../mechanisms/b.md)
- Dritte Sache

## Trägt
nichts
"""
GETRAGEN = """---
id: b
typ: mechanismus
status: getragen
stand: 2026-10-02
---

# Getragener Mechanismus

Link ins Leere: [weg](gibt-es-nicht.md) und extern [x](https://example.org).
"""


def _wiki():
    root = tempfile.mkdtemp()
    os.makedirs(os.path.join(root, "knowledge", "thema", "open_checks"))
    os.makedirs(os.path.join(root, "knowledge", "thema", "mechanisms"))
    open(os.path.join(root, "knowledge", "thema", "open_checks", "a.md"), "w", encoding="utf-8").write(OFFEN)
    open(os.path.join(root, "knowledge", "thema", "mechanisms", "b.md"), "w", encoding="utf-8").write(GETRAGEN)
    open(os.path.join(root, "knowledge", "thema", "INDEX.md"), "w", encoding="utf-8").write("[a](open_checks/a.md)\n")
    return root


def test_parse_entry():
    m = w.parse_entry(OFFEN)
    assert m["status"] == "offen"
    assert m["titel"] == "Offener Punkt"
    assert m["todos"] == ["Erste Sache", "Zweite Sache, siehe [b](../mechanisms/b.md)", "Dritte Sache"]


def test_parse_entry_ohne_todo():
    m = w.parse_entry(GETRAGEN)
    assert m["status"] == "getragen" and m["todos"] == []


def test_collect_and_render():
    root = _wiki()
    items = w.collect_open(root)
    assert len(items) == 1 and items[0]["pfad"] == "knowledge/thema/open_checks/a.md"
    md = w.render_todo(items, "2026-10-03")
    assert "## thema" in md and "1 offene Einträge" in md
    assert "- [ ] Zweite Sache, siehe [b](knowledge/thema/mechanisms/b.md)" in md


def test_dead_links():
    root = _wiki()
    bad = w.dead_links(root)
    assert bad == [("knowledge/thema/mechanisms/b.md", "gibt-es-nicht.md")]


def test_unindexed():
    root = _wiki()
    assert w.unindexed(root) == ["knowledge/thema/mechanisms/b.md"]
