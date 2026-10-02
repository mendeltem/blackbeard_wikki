# -*- coding: utf-8 -*-
"""Tests mit synthetischen Labelbildern. Keine Bilddaten, kein FreeSurfer.

Aufruf:  python -m unittest discover -s tests -v
"""
import csv
import os
import subprocess
import sys
import tempfile
import unittest

import numpy as np
import nibabel as nib

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src")
sys.path.insert(0, SRC)
import aseg_tissue as at  # noqa: E402

SCRIPT = os.path.join(SRC, "run_aseg_tissue_volumes.py")


def block(vol, x0, n, label):
    """n Voxel entlang z in Spalte (x0, 0) mit label fuellen."""
    vol[x0, 0, :n] = label


def phantom(parc=True):
    """20x4x40-Volumen. Voxelzahlen sind die erwarteten Volumina bei 1 mm."""
    a = np.zeros((20, 4, 40), dtype=np.int16)
    block(a, 0, 30, 2)                       # WM links        30
    block(a, 1, 30, 41)                      # WM rechts       30
    block(a, 2, 20, 1028 if parc else 3)     # Kortex links    20
    block(a, 3, 20, 2028 if parc else 42)    # Kortex rechts   20
    block(a, 4, 10, 10)                      # Thalamus        10
    block(a, 5, 5, 13)                       # Pallidum         5
    block(a, 6, 5, 28)                       # Ventral DC       5
    block(a, 7, 8, 4)                        # Seitenventrikel  8
    block(a, 8, 12, 24)                      # CSF             12
    block(a, 9, 6, 16)                       # Hirnstamm        6
    block(a, 10, 3, 31)                      # Plexus, keine Gruppe
    return a


def volumes(aseg, convention="gm", wmh=None, vox=1.0):
    cls = at.class_of(at.CONVENTIONS[convention])
    lab = at.tissue_label_image(aseg, cls, wmh)
    rows = at.tissue_volumes(lab, vox, wmh)
    return {r["structure"]: r["volume_mm3"] for r in rows}, rows


class TestGruppierung(unittest.TestCase):
    def test_volumina_exakt(self):
        v, _ = volumes(phantom())
        self.assertEqual(v["GM"], 20 + 20 + 10 + 5 + 5)
        self.assertEqual(v["WM"], 30 + 30 + 6)
        self.assertEqual(v["CSF"], 8 + 12)
        self.assertEqual(v["sum_GM_WM_CSF"], v["GM"] + v["WM"] + v["CSF"])

    def test_voxelgroesse_skaliert(self):
        v, _ = volumes(phantom(), vox=0.4 ** 3)
        self.assertAlmostEqual(v["WM"], 66 * 0.4 ** 3)

    def test_konvention_verschiebt_pallidum_und_vdc(self):
        gm, _ = volumes(phantom(), "gm")
        wm, _ = volumes(phantom(), "wm")
        self.assertEqual(gm["GM"] - wm["GM"], 10)
        self.assertEqual(wm["WM"] - gm["WM"], 10)
        self.assertEqual(gm["sum_GM_WM_CSF"], wm["sum_GM_WM_CSF"])

    def test_dk_parzellen_zaehlen_als_gm(self):
        mit, _ = volumes(phantom(parc=True))
        ohne, _ = volumes(phantom(parc=False))
        self.assertEqual(mit["GM"], ohne["GM"])

    def test_plexus_in_keiner_gruppe(self):
        cls = at.class_of(at.CONVENTIONS["gm"])
        self.assertNotIn(31, cls)
        self.assertNotIn(77, cls)

    def test_corpus_callosum_parzelle_nicht_gemappt(self):
        self.assertNotIn(1004, at.TISSUE_MAP)
        self.assertNotIn(2004, at.TISSUE_MAP)


class TestFeineKlassen(unittest.TestCase):
    def test_unbekanntes_label_wird_gemeldet(self):
        a = phantom()
        block(a, 11, 7, 999)
        rows, unmapped = at.fine_volumes(a, 1.0)
        self.assertEqual(unmapped, [999])
        hit = [r for r in rows if r["structure"] == "unmapped_label_999"]
        self.assertEqual(hit[0]["volume_mm3"], 7)
        v, _ = volumes(a)
        self.assertEqual(v["GM"], 60)        # nicht still mitgezaehlt

    def test_summe_fein_gleich_alle_voxel(self):
        a = phantom()
        rows, _ = at.fine_volumes(a, 1.0)
        self.assertEqual(sum(r["volume_mm3"] for r in rows), np.count_nonzero(a))

    def test_seite(self):
        rows, _ = at.fine_volumes(phantom(), 1.0)
        side = {r["label"]: r["side"] for r in rows}
        self.assertEqual(side[2], "left")
        self.assertEqual(side[41], "right")
        self.assertEqual(side[2028], "right")
        self.assertEqual(side[16], "both")


class TestWMH(unittest.TestCase):
    def setUp(self):
        self.a = phantom()
        self.w = np.zeros(self.a.shape, dtype=np.uint8)
        self.w[0, 0, :4] = 1      # 4 Voxel im WM
        self.w[4, 0, :2] = 1      # 2 Voxel im Thalamus (GM)
        self.w[7, 0, :1] = 1      # 1 Voxel im Ventrikel
        self.w[15, 0, :3] = 1     # 3 Voxel im Hintergrund

    def test_wmh_wird_addiert_nicht_ueberschrieben(self):
        ohne, _ = volumes(self.a)
        mit, _ = volumes(self.a, wmh=self.w)
        for k in ("GM", "WM", "CSF"):
            self.assertEqual(ohne[k], mit[k])

    def test_wmh_zerlegung(self):
        v, _ = volumes(self.a, wmh=self.w)
        self.assertEqual(v["WMH_in_WM"], 4)
        self.assertEqual(v["WMH_in_GM"], 2)
        self.assertEqual(v["WMH_in_CSF"], 1)
        self.assertEqual(v["WMH_outside_classes"], 3)
        self.assertEqual(v["WM_minus_WMH"] + v["WMH_in_WM"], v["WM"])

    def test_form_muss_passen(self):
        cls = at.class_of(at.CONVENTIONS["gm"])
        with self.assertRaises(ValueError):
            at.tissue_label_image(self.a, cls, np.zeros((2, 2, 2)))


class TestWarnungen(unittest.TestCase):
    def test_fehlender_kortex_faellt_auf(self):
        a = phantom(parc=True)
        tm = {k: v for k, v in at.TISSUE_MAP.items() if k < 1000}
        cls = at.class_of(at.CONVENTIONS["gm"], tm)
        rows = at.tissue_volumes(at.tissue_label_image(a, cls), 1.0)
        _, unmapped = at.fine_volumes(a, 1.0, tm)
        text = " ".join(at.sanity_warnings(rows, unmapped))
        self.assertIn("GM/WM", text)
        self.assertIn("nicht in TISSUE_MAP", text)

    def test_plausibles_bild_ohne_warnung(self):
        rows = [{"structure": "GM", "volume_mm3": 650e3},
                {"structure": "WM", "volume_mm3": 500e3},
                {"structure": "CSF", "volume_mm3": 350e3},
                {"structure": "sum_GM_WM_CSF", "volume_mm3": 1500e3}]
        self.assertEqual(at.sanity_warnings(rows, []), [])


class TestDatei(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name
        self.aff = np.diag([2.0, 2.0, 2.0, 1.0])

    def tearDown(self):
        self.tmp.cleanup()

    def save(self, name, data, affine=None):
        p = os.path.join(self.d, name)
        nib.save(nib.Nifti1Image(data, self.aff if affine is None else affine), p)
        return p

    def run_cli(self, *extra):
        return subprocess.run([sys.executable, SCRIPT] + list(extra),
                              capture_output=True, text=True)

    def test_float_labels_werden_gerundet(self):
        p = self.save("f.nii.gz", phantom().astype(np.float32) + 0.0004)
        _, a = at.load_labels(p)
        self.assertTrue(np.array_equal(a, phantom()))

    def test_mgz_wird_gelesen(self):
        p = os.path.join(self.d, "s.mgz")
        nib.save(nib.MGHImage(phantom().astype(np.int32), self.aff), p)
        img, a = at.load_labels(p)
        self.assertTrue(np.array_equal(a, phantom()))
        self.assertAlmostEqual(at.voxel_mm3(img), 8.0)

    def test_cli_schreibt_csv_und_labelbild(self):
        seg = self.save("seg.nii.gz", phantom())
        out = os.path.join(self.d, "v.csv")
        lab = os.path.join(self.d, "lab.nii.gz")
        r = self.run_cli("--seg", seg, "--out", out, "--labels-out", lab)
        self.assertIn(r.returncode, (0, 1), r.stderr)   # Phantom ist winzig -> Warnung
        with open(out) as fh:
            rows = {x["structure"]: float(x["volume_mm3"])
                    for x in csv.DictReader(fh) if x["measure"] == "tissue_volume"}
        self.assertEqual(rows["WM"], 66 * 8.0)          # 2 mm Voxel
        self.assertEqual(set(np.unique(nib.load(lab).get_fdata())), {0.0, 1.0, 2.0, 3.0})

    def test_cli_lehnt_fremdes_grid_ab(self):
        seg = self.save("seg.nii.gz", phantom())
        wmh = self.save("wmh.nii.gz", np.ones(phantom().shape, dtype=np.uint8),
                        affine=np.diag([1.0, 1.0, 1.0, 1.0]))
        r = self.run_cli("--seg", seg, "--out", os.path.join(self.d, "v.csv"),
                         "--wmh", wmh)
        self.assertEqual(r.returncode, 2)
        self.assertFalse(os.path.exists(os.path.join(self.d, "v.csv")))
