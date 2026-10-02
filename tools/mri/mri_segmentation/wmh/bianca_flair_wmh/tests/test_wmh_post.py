# -*- coding: utf-8 -*-
"""
Tests fuer wmh_post.py. Laufen ohne private Daten und ohne FSL: jedes Phantom
wird im Test selbst gebaut, einschliesslich der leeren Varianten.

    python -m unittest discover -s tests

Zwei Gitter wie in echten Daten: FLAIR anisotrop (2 x 2 x 5 mm), Segmentierung
isotrop 1 mm, gleicher Weltraum.
"""
import os
import sys
import tempfile
import unittest

import numpy as np
import nibabel as nib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import wmh_post as wp

FLAIR_SHAPE, FLAIR_ZOOMS = (96, 96, 24), (2.0, 2.0, 5.0)
SEG_SHAPE, SEG_ZOOMS = (192, 192, 120), (1.0, 1.0, 1.0)


def affine(zooms, shape):
    a = np.diag(list(zooms) + [1.0])
    a[:3, 3] = -np.array(zooms) * np.array(shape) / 2.0
    return a


FLAIR_AFF, SEG_AFF = affine(FLAIR_ZOOMS, FLAIR_SHAPE), affine(SEG_ZOOMS, SEG_SHAPE)


def ball(shape, center, r_vox):
    g = np.ogrid[:shape[0], :shape[1], :shape[2]]
    return sum((g[i] - center[i]) ** 2 for i in range(3)) <= r_vox ** 2


def phantom(with_vent=True):
    """WM-Kugel 60 mm, Ventrikelkugel 14 mm in der Mitte, LPM mit einer Kappe
    um den Ventrikel, einem tiefen Fleck und einem Fleck in der Infarktmaske."""
    wm = ball(SEG_SHAPE, (96, 96, 60), 60).astype(np.uint8)
    vent = ball(SEG_SHAPE, (96, 96, 60), 14).astype(np.uint8)
    wm[vent > 0] = 0
    if not with_vent:
        vent[:] = 0

    lpm = np.zeros(FLAIR_SHAPE, np.float32)
    lpm[ball(FLAIR_SHAPE, (48, 48, 12), 10)] = 0.95     # um den Ventrikel
    lpm[ball(FLAIR_SHAPE, (62, 40, 12), 4)] = 0.92      # weiter aussen
    lpm[ball(FLAIR_SHAPE, (30, 48, 12), 4)] = 0.97      # in der Infarktmaske
    lpm[70, 60, 12] = 0.87                              # nur ueber 0.85

    lesion = ball(FLAIR_SHAPE, (30, 48, 12), 6).astype(np.uint8)
    return (nib.Nifti1Image(lpm, FLAIR_AFF), nib.Nifti1Image(wm, SEG_AFF),
            nib.Nifti1Image(vent, SEG_AFF), nib.Nifti1Image(lesion, FLAIR_AFF))


class TestPostprocess(unittest.TestCase):

    def test_threshold_tag(self):
        self.assertEqual(wp.threshold_tag(0.90), "090")
        self.assertEqual(wp.threshold_tag(0.85), "085")
        self.assertEqual(wp.threshold_tag(0.9), "090")

    def test_masks_reach_the_flair_grid(self):
        lpm, wm, vent, _ = phantom()
        r = wp.postprocess(lpm, wm, vent)
        self.assertEqual(r["wm_mask"].shape, FLAIR_SHAPE)
        self.assertGreater(np.count_nonzero(r["wm_mask"]), 0)
        # Kugel 60 mm minus Kugel 14 mm, in ml. Toleranz fuer das grobe Gitter.
        expected = 4.0 / 3.0 * np.pi * (60 ** 3 - 14 ** 3) / 1000.0
        self.assertAlmostEqual(r["wm_mask_ml"], expected, delta=0.05 * expected)

    def test_pv_plus_deep_is_wm(self):
        lpm, wm, vent, _ = phantom()
        r = wp.postprocess(lpm, wm, vent)
        self.assertGreater(np.count_nonzero(r["pv"]), 0)
        self.assertGreater(np.count_nonzero(r["deep"]), 0)
        self.assertFalse(np.any(r["pv"] & r["deep"]))
        self.assertTrue(np.array_equal(r["pv"] | r["deep"], r["wm"]))
        self.assertAlmostEqual(r["pv_ml"] + r["deep_ml"], r["wm_ml"], places=3)

    def test_wm_masking_removes_ventricle_voxels(self):
        lpm, wm, vent, _ = phantom()
        r = wp.postprocess(lpm, wm, vent)
        self.assertLess(r["wm_ml"], r["raw_ml"])
        self.assertFalse(np.any(r["wm"] & ~r["wm_mask"]))

    def test_distance_is_in_mm_not_voxels(self):
        _, _, vent, _ = phantom()
        dist = wp.ventricle_distance_mm(vent)
        d = np.asarray(dist.dataobj)
        # 30 mm vom Zentrum, Ventrikelradius 14 mm -> rund 16 mm
        self.assertAlmostEqual(float(d[126, 96, 60]), 16.0, delta=1.0)
        self.assertEqual(float(d[96, 96, 60]), 0.0)

    def test_pv_boundary_follows_parameter(self):
        lpm, wm, vent, _ = phantom()
        near = wp.postprocess(lpm, wm, vent, pv_dist_mm=3.0)
        far = wp.postprocess(lpm, wm, vent, pv_dist_mm=10.0)
        self.assertLess(near["pv_ml"], far["pv_ml"])
        self.assertEqual(near["wm_ml"], far["wm_ml"])

    def test_lesion_removal(self):
        lpm, wm, vent, lesion = phantom()
        without = wp.postprocess(lpm, wm, vent)
        with_removal = wp.postprocess(lpm, wm, vent, lesion_img=lesion, lesion_dilate_vox=1)
        self.assertLess(with_removal["wm_ml"], without["wm_ml"])
        self.assertFalse(np.any(with_removal["raw"] & with_removal["lesion"]))
        # die Maske wurde dilatiert, ist also groesser als das Original
        self.assertGreater(np.count_nonzero(with_removal["lesion"]),
                           np.count_nonzero(np.asarray(lesion.dataobj)))

    def test_lower_threshold_never_gives_less(self):
        lpm, wm, vent, _ = phantom()
        r90 = wp.postprocess(lpm, wm, vent, thr=0.90)
        r85 = wp.postprocess(lpm, wm, vent, thr=0.85)
        self.assertGreater(r85["raw_ml"], r90["raw_ml"])
        self.assertTrue(np.all(r85["raw"][r90["raw"]]))

    def test_empty_ventricle_gives_no_split(self):
        lpm, wm, vent, _ = phantom(with_vent=False)
        self.assertEqual(np.count_nonzero(np.asarray(vent.dataobj)), 0)
        r = wp.postprocess(lpm, wm, vent)
        self.assertIsNone(r["pv"])
        self.assertIsNone(r["deep"])
        self.assertIsNone(r["pv_ml"])
        self.assertGreater(r["wm_ml"], 0)

    def test_empty_lpm_gives_zero_not_error(self):
        _, wm, vent, _ = phantom()
        lpm = nib.Nifti1Image(np.zeros(FLAIR_SHAPE, np.float32), FLAIR_AFF)
        r = wp.postprocess(lpm, wm, vent)
        self.assertEqual(r["raw_ml"], 0.0)
        self.assertEqual(r["wm_ml"], 0.0)
        self.assertEqual(r["pv_ml"], 0.0)

    def test_saved_mask_ignores_slope_of_reference(self):
        # Prueft die Eigenschaft, nicht den Reset: mit nibabel 5.4.2 besteht
        # dieser Test auch ohne set_slope_inter in save_mask_like.
        lpm, wm, vent, _ = phantom()
        r = wp.postprocess(lpm, wm, vent)
        ref = r["ref"]
        ref.header.set_slope_inter(0.5, 0.0)
        with tempfile.TemporaryDirectory() as tmp:
            p = wp.save_mask_like(r["wm"], ref, os.path.join(tmp, "wm.nii.gz"))
            back = np.asarray(nib.load(p).dataobj)
        self.assertEqual(float(back.max()), 1.0)
        self.assertEqual(int(np.count_nonzero(back)), int(np.count_nonzero(r["wm"])))
