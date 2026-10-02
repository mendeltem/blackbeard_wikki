#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wmh_post.py  -  Rechenkern des WMH-Postprocessings, ohne FSL und ohne Pipeline

Nimmt eine BIANCA-Wahrscheinlichkeitskarte (LPM) im FLAIR-Raum und die Masken
aus der Segmentierung (WM, Ventrikel) in ihrem eigenen Gitter und liefert:

    raw    LPM >= Schwelle
    wm     raw UND WM-Maske            <- das berichtete Ergebnis
    pv     wm UND Distanz zum Ventrikel <= pv_dist_mm
    deep   wm OHNE pv

pv + deep ergibt per Konstruktion genau wm. Es gibt keine Cluster-Verarbeitung.

Braucht nur numpy, scipy und nibabel. Alle Funktionen arbeiten auf
nibabel-Bildern im Speicher; Laden und Speichern macht der Aufrufer.
"""

import numpy as np
import nibabel as nib
from nibabel.processing import resample_from_to
from scipy import ndimage


def threshold_tag(thr):
    """0.90 -> '090', 0.85 -> '085'. So heissen die Dateien je Schwelle."""
    return "0" + f"{float(thr):.2f}".split(".")[1]


def canonical(img):
    """Bild in RAS-Orientierung. Ohne das stimmen Achsen zweier Bilder nicht
    ueberein, auch wenn beide im selben Weltraum liegen."""
    return nib.as_closest_canonical(img)


def resample_to(img, ref_img, order=0):
    """Bild auf das Gitter von ref_img legen, ueber Weltkoordinaten.

    order=0 (nearest) fuer Masken, order=1 (trilinear) fuer die Distanzkarte.
    Masken aus dem isotropen 1-mm-Gitter der Segmentierung liegen sonst nicht
    auf der anisotropen FLAIR und verschwinden im Overlay oder im Masking.
    """
    img = canonical(img)
    if img.shape[:3] != ref_img.shape[:3] or not np.allclose(img.affine, ref_img.affine):
        img = resample_from_to(img, (ref_img.shape[:3], ref_img.affine), order=order)
    return np.asarray(img.dataobj)


def ventricle_distance_mm(vent_img):
    """Euklidische Distanz in mm zur Ventrikelmaske, im Gitter der Maske.

    Gerechnet wird im isotropen Segmentierungsgitter, nicht auf der FLAIR:
    eine Distanztransformation auf 3- bis 5-mm-Schichten waere in z so grob
    wie die Schichtdicke. Resampelt wird erst danach.

    Leere Ventrikelmaske -> None. Kein Ersatzwert: ohne Ventrikel gibt es
    keine PV/tief-Aufteilung, und das soll sichtbar bleiben.
    """
    vent = np.asarray(vent_img.dataobj) > 0
    if not vent.any():
        return None
    dist = ndimage.distance_transform_edt(~vent, sampling=vent_img.header.get_zooms()[:3])
    return nib.Nifti1Image(dist.astype(np.float32), vent_img.affine)


def volume_ml(mask, zooms):
    """Voxelzahl mal Voxelvolumen, in ml. Identisch zu fslstats -V."""
    if mask is None:
        return None
    return round(float(np.count_nonzero(mask)) * float(np.prod(zooms[:3])) / 1000.0, 4)


def save_mask_like(arr, ref_img, out_path, dtype=np.uint8):
    """Array im Gitter von ref_img speichern.

    scl_slope und scl_inter werden zurueckgesetzt. Der Header der LPM kann
    eine Skalierung tragen; die Ursprungspipeline setzt sie zurueck, weil dort
    Masken nach dem Laden bei 1/slope statt bei 1 lagen. Mit nibabel 5.4.2
    liess sich das am 2026-10-02 NICHT nachstellen (die Maske kommt auch ohne
    Reset als 1 zurueck). Der Reset bleibt als Vorsicht fuer aeltere Versionen.
    """
    hdr = ref_img.header.copy()
    hdr.set_data_dtype(dtype)
    hdr.set_slope_inter(1.0, 0.0)
    nib.save(nib.Nifti1Image(np.asarray(arr).astype(dtype), ref_img.affine, hdr), out_path)
    return out_path


def postprocess(lpm_img, wm_img, vent_img, thr=0.90, pv_dist_mm=10.0,
                lesion_img=None, lesion_dilate_vox=1):
    """LPM -> raw, wm, pv, deep plus Volumina.

    lpm_img     BIANCA-LPM im FLAIR-Raum
    wm_img      WM-Maske, beliebiges Gitter im selben Weltraum
    vent_img    Ventrikelmaske, beliebiges Gitter im selben Weltraum
    lesion_img  optionale Infarktmaske. Wird um lesion_dilate_vox Voxel
                dilatiert (26er-Nachbarschaft) und in der LPM auf 0 gesetzt.

    Rueckgabe: dict mit den Arrays im LPM-Gitter, dem kanonisierten
    Referenzbild 'ref' und den Volumina in ml.
    """
    ref = canonical(lpm_img)
    lpm = np.asarray(ref.dataobj, dtype=np.float32)
    zooms = ref.header.get_zooms()[:3]

    wm = resample_to(wm_img, ref, order=0) > 0

    dist_img = ventricle_distance_mm(vent_img)
    dist = resample_to(dist_img, ref, order=1) if dist_img is not None else None

    lesion = None
    if lesion_img is not None:
        lesion = resample_to(lesion_img, ref, order=0) > 0
        if lesion_dilate_vox > 0:
            lesion = ndimage.binary_dilation(lesion, structure=np.ones((3, 3, 3), dtype=int),
                                             iterations=lesion_dilate_vox)
        lpm = np.where(lesion, 0.0, lpm).astype(np.float32)

    raw = lpm >= thr
    wmh = raw & wm

    if dist is not None:
        pv = wmh & (dist <= pv_dist_mm)
        deep = wmh & ~pv
    else:
        pv, deep = None, None

    return {
        "ref": ref,
        "threshold": thr,
        "tag": threshold_tag(thr),
        "pv_dist_mm": pv_dist_mm,
        "raw": raw, "wm": wmh, "pv": pv, "deep": deep,
        "wm_mask": wm, "dist": dist, "lesion": lesion,
        "raw_ml": volume_ml(raw, zooms),
        "wm_ml": volume_ml(wmh, zooms),
        "pv_ml": volume_ml(pv, zooms),
        "deep_ml": volume_ml(deep, zooms),
        "wm_mask_ml": volume_ml(wm, zooms),
        # Volumen der dilatierten Infarktmaske. NICHT das Volumen an WMH,
        # das dadurch entfernt wurde.
        "lesion_mask_ml": volume_ml(lesion, zooms),
    }
