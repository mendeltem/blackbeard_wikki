# -*- coding: utf-8 -*-
"""Tests fuer wafer_ramp. Keine privaten Daten, alle Werte stehen hier."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

import wafer_ramp as wr  # noqa: E402


class TestHochlauf(unittest.TestCase):

    def test_eckpunkte_werden_getroffen(self):
        for form in ("s", "linear"):
            werte = wr.hochlauf(10, 57.5, 11, form)
            self.assertAlmostEqual(werte[0], 10, places=9)
            self.assertAlmostEqual(werte[-1], 57.5, places=9)
            self.assertEqual(len(werte), 11)

    def test_linear_hat_gleiche_schritte(self):
        werte = wr.hochlauf(10, 57.5, 11, "linear")
        schritte = [werte[i] - werte[i - 1] for i in range(1, len(werte))]
        for s in schritte:
            self.assertAlmostEqual(s, 4.75, places=9)

    def test_s_kurve_steigt_monoton_und_ist_am_steilsten_in_der_mitte(self):
        werte = wr.hochlauf(10, 57.5, 11, "s")
        schritte = [werte[i] - werte[i - 1] for i in range(1, len(werte))]
        self.assertTrue(all(s > 0 for s in schritte))
        self.assertEqual(schritte.index(max(schritte)), 5)  # Zuwachs auf Monat 7
        self.assertAlmostEqual(werte[8], 53.692, places=3)  # Monat 9

    def test_zu_wenige_monate(self):
        with self.assertRaises(ValueError):
            wr.hochlauf(10, 57.5, 1)


class TestErloes(unittest.TestCase):

    def test_gb_je_wafer_und_erloes(self):
        self.assertAlmostEqual(wr.gb_je_wafer(3.0), 933.3333, places=4)
        self.assertAlmostEqual(wr.erloes_je_wafer(15.0, 3.0), 14000.0, places=6)
        self.assertAlmostEqual(wr.erloes_je_wafer(15.0, 4.0), 10500.0, places=6)

    def test_monatserloes_in_milliarden(self):
        # 53.692 Tausend Wafer zu 14.000 USD sind rund 0,7517 Mrd. USD
        self.assertAlmostEqual(wr.monatserloes(53.692, 15.0, 3.0), 0.751688, places=6)


class TestVerlauf(unittest.TestCase):

    def test_tabelle_hat_zuwachs_und_versatz(self):
        zeilen = wr.verlauf(10, 57.5, 11, "s", 15.0, 3.0)
        self.assertIsNone(zeilen[0]["zuwachs"])
        self.assertEqual(zeilen[0]["umsatz_ab_monat"], 5)
        self.assertEqual(zeilen[-1]["monat"], 11)
        self.assertAlmostEqual(zeilen[-1]["wafer"], 57.5, places=9)


if __name__ == "__main__":
    unittest.main()
