# -*- coding: utf-8 -*-
"""Tests ohne Netz fuer die reinen Textfunktionen, plus ein optionaler Netztest.

Aufruf:  python -m unittest discover -s tests -v
Netztest zusaetzlich:  WAYBACK_NETZ=1 python -m unittest discover -s tests -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import wayback_snapshot as w  # noqa: E402

HTML = """<!doctype html><html><head><title>Preise</title>
<style>.a{color:red}</style><script>var x = "<b>nicht</b> sichtbar";</script></head>
<body><!-- Kommentar --><h1>Pricing</h1>
<table><tr><td>gpt-4</td><td>$0.03 &nbsp;/ 1K tokens</td></tr>
<tr><td>gpt-3.5-turbo</td><td>$0.002 / 1K tokens</td></tr></table>
<p>A &amp; B</p></body></html>"""


class TestZuText(unittest.TestCase):
    def test_entfernt_script_und_style(self):
        t = w.zu_text(HTML)
        self.assertNotIn("color:red", t)
        self.assertNotIn("nicht", t)

    def test_entfernt_kommentar_und_tags(self):
        t = w.zu_text(HTML)
        self.assertNotIn("Kommentar", t)
        self.assertNotIn("<", t)

    def test_behaelt_inhalt_und_loest_entitaeten(self):
        t = w.zu_text(HTML)
        self.assertIn("gpt-4", t)
        self.assertIn("$0.03", t)
        self.assertIn("A & B", t)

    def test_normalisiert_leerraum(self):
        self.assertEqual(w.zu_text("<p>a\n\n   b</p>"), "a b")


class TestAusschnitt(unittest.TestCase):
    def setUp(self):
        self.t = w.zu_text(HTML)

    def test_findet_stichwort(self):
        teile = w.ausschnitt(self.t, "gpt-3.5-turbo", vor=0, nach=40)
        self.assertEqual(len(teile), 1)
        self.assertTrue(teile[0].startswith("gpt-3.5-turbo"))
        self.assertIn("$0.002", teile[0])

    def test_ohne_treffer_leer(self):
        self.assertEqual(w.ausschnitt(self.t, "claude-opus"), [])

    def test_ohne_stichwort_ganzer_text(self):
        self.assertEqual(w.ausschnitt(self.t, None), [self.t])

    def test_alle_treffer(self):
        t = "preis a preis b preis c"
        self.assertEqual(len(w.ausschnitt(t, "preis", vor=0, nach=5, alle=True)), 3)

    def test_gross_klein_egal(self):
        self.assertEqual(len(w.ausschnitt(self.t, "PRICING", vor=0, nach=10)), 1)


@unittest.skipUnless(os.environ.get("WAYBACK_NETZ"), "Netztest nur mit WAYBACK_NETZ=1")
class TestNetz(unittest.TestCase):
    def test_schnappschuss_bekannter_seite(self):
        su, st = w.schnappschuss("example.com", "20200101")
        self.assertTrue(su and su.startswith("http"))
        self.assertEqual(len(st), 14)


if __name__ == "__main__":
    unittest.main()
