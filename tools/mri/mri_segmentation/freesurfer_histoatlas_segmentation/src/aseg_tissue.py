#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GM / WM / CSF aus einem aseg-Labelbild (SynthSeg, SuperSynth, FreeSurfer aseg).

Nur Tabellen und Funktionen, keine Seiteneffekte beim Import. Der Aufruf von der
Kommandozeile steht in run_aseg_tissue_volumes.py.

Die Gruppierung der aseg-Labels zu GM/WM/CSF ist eine Konvention, keine Messung.
Zwei Konventionen aus der Literatur sind eingebaut, sie unterscheiden sich in
Pallidum und Ventral DC (Quellen in PAPERS.md):
    "gm"  Pallidum und Ventral DC zaehlen zu GM
    "wm"  Pallidum und Ventral DC zaehlen zu WM

Abhaengigkeiten: numpy, nibabel.
"""
import numpy as np
import nibabel as nib

# ----------------------------------------------------------------------------
# aseg-Label -> (feine Klasse, Seite). FreeSurfer-Labelwerte.
# ----------------------------------------------------------------------------
TISSUE_MAP = {
    2:  ("cerebral_WM",        "left"),  41: ("cerebral_WM",        "right"),
    3:  ("cerebral_cortex",    "left"),  42: ("cerebral_cortex",    "right"),
    4:  ("lateral_ventricle",  "left"),  43: ("lateral_ventricle",  "right"),
    5:  ("inf_lat_ventricle",  "left"),  44: ("inf_lat_ventricle",  "right"),
    7:  ("cerebellar_WM",      "left"),  46: ("cerebellar_WM",      "right"),
    8:  ("cerebellar_cortex",  "left"),  47: ("cerebellar_cortex",  "right"),
    10: ("thalamus",           "left"),  49: ("thalamus",           "right"),
    11: ("caudate",            "left"),  50: ("caudate",            "right"),
    12: ("putamen",            "left"),  51: ("putamen",            "right"),
    13: ("pallidum",           "left"),  52: ("pallidum",           "right"),
    17: ("hippocampus",        "left"),  53: ("hippocampus",        "right"),
    18: ("amygdala",           "left"),  54: ("amygdala",           "right"),
    26: ("accumbens",          "left"),  58: ("accumbens",          "right"),
    28: ("ventral_DC",         "left"),  60: ("ventral_DC",         "right"),
    31: ("choroid_plexus",     "left"),  63: ("choroid_plexus",     "right"),
    14: ("third_ventricle",    "both"),
    15: ("fourth_ventricle",   "both"),
    16: ("brainstem",          "both"),
    24: ("CSF_extracerebral",  "both"),
    77: ("WM_hypointensities", "both"),
}

# Desikan-Killiany-Parzellen. Index = Label - 1000 (links) bzw. - 2000 (rechts).
# Mit Parzellierung segmentiert steckt der Kortex in 1001-1035 / 2001-2035 und
# NICHT in 3 / 42. Fehlen diese Zeilen, faellt der gesamte Kortex aus GM heraus.
# 4 (corpuscallosum) vergibt aparc nicht und steht darum bewusst nicht hier:
# taucht 1004 / 2004 doch auf, wird es als unmapped gemeldet statt still als GM
# gezaehlt.
DK_PARCELS = {
    1: "bankssts",                  2: "caudalanteriorcingulate",
    3: "caudalmiddlefrontal",       5: "cuneus",
    6: "entorhinal",                7: "fusiform",
    8: "inferiorparietal",          9: "inferiortemporal",
    10: "isthmuscingulate",         11: "lateraloccipital",
    12: "lateralorbitofrontal",     13: "lingual",
    14: "medialorbitofrontal",      15: "middletemporal",
    16: "parahippocampal",          17: "paracentral",
    18: "parsopercularis",          19: "parsorbitalis",
    20: "parstriangularis",         21: "pericalcarine",
    22: "postcentral",              23: "posteriorcingulate",
    24: "precentral",               25: "precuneus",
    26: "rostralanteriorcingulate", 27: "rostralmiddlefrontal",
    28: "superiorfrontal",          29: "superiorparietal",
    30: "superiortemporal",         31: "supramarginal",
    32: "frontalpole",              33: "temporalpole",
    34: "transversetemporal",       35: "insula",
}
for _i, _name in DK_PARCELS.items():
    TISSUE_MAP[1000 + _i] = ("ctx_" + _name, "left")
    TISSUE_MAP[2000 + _i] = ("ctx_" + _name, "right")

_CORTEX = ["cerebral_cortex"] + ["ctx_" + n for n in DK_PARCELS.values()]
_GM_CORE = _CORTEX + ["cerebellar_cortex", "thalamus", "caudate", "putamen",
                      "hippocampus", "amygdala", "accumbens"]
_WM_CORE = ["cerebral_WM", "cerebellar_WM", "brainstem"]
_CSF = ["lateral_ventricle", "inf_lat_ventricle", "third_ventricle",
        "fourth_ventricle", "CSF_extracerebral"]
_SWING = ["pallidum", "ventral_DC"]      # die zwei strittigen Strukturen

# choroid_plexus und WM_hypointensities stehen bewusst in KEINER Gruppe.
CONVENTIONS = {
    "gm": {"GM": _GM_CORE + _SWING, "WM": _WM_CORE,          "CSF": _CSF},
    "wm": {"GM": _GM_CORE,          "WM": _WM_CORE + _SWING, "CSF": _CSF},
}

TISSUE_CODE = {"GM": 1, "WM": 2, "CSF": 3}
WMH_OFFSET = 10      # 11 GM&WMH, 12 WM&WMH, 13 CSF&WMH

# Plausibilitaetsgrenzen fuer Erwachsene. Verletzung = Warnung, kein Abbruch.
GM_WM_RATIO_RANGE = (0.8, 1.8)
SUM_ML_RANGE = (1000.0, 2200.0)


def load_labels(path):
    """Labelbild als int32. Floats werden gerundet, nicht abgeschnitten."""
    img = nib.load(path)
    data = np.asanyarray(img.dataobj)
    if data.dtype.kind == "f":
        data = np.rint(data)
    return img, data.astype(np.int32, copy=False)


def voxel_mm3(img):
    return float(np.prod(img.header.get_zooms()[:3]))


def same_grid(img_a, img_b, atol=1e-4):
    return (img_a.shape[:3] == img_b.shape[:3]
            and np.allclose(img_a.affine, img_b.affine, atol=atol))


def class_of(groups, tissue_map=None):
    """{Label: 'GM'|'WM'|'CSF'}. Labels ohne Gruppe fehlen im Ergebnis."""
    tissue_map = TISSUE_MAP if tissue_map is None else tissue_map
    out = {}
    for label, (fine, _side) in tissue_map.items():
        for coarse, members in groups.items():
            if fine in members:
                out[int(label)] = coarse
    return out


def fine_volumes(aseg, vox_mm3, tissue_map=None):
    """Eine Zeile je vorkommendem Label. -> (rows, unmapped_labels).

    Labels, die nicht in tissue_map stehen, bekommen eine eigene Zeile
    'unmapped_label_<n>' und werden zurueckgemeldet. Sie verschwinden nicht.
    """
    tissue_map = TISSUE_MAP if tissue_map is None else tissue_map
    labels, counts = np.unique(aseg[aseg > 0], return_counts=True)
    rows, unmapped = [], []
    for label, count in zip(labels.tolist(), counts.tolist()):
        if label in tissue_map:
            name, side = tissue_map[label]
        else:
            name, side = "unmapped_label_%d" % label, "both"
            unmapped.append(label)
        rows.append({"measure": "tissue_fine", "label": label, "structure": name,
                     "side": side, "volume_mm3": count * vox_mm3})
    return rows, unmapped


def tissue_label_image(aseg, label_class, wmh=None):
    """uint8-Bild: 1 GM, 2 WM, 3 CSF, plus WMH_OFFSET wo die WMH-Maske liegt.

    Die WMH wird addiert, nicht ueberschrieben. Dadurch bleibt count(2) das
    WM ohne WMH und count(12) das WMH im WM.
    """
    lab = np.zeros(aseg.shape, dtype=np.uint8)
    for label, coarse in label_class.items():
        lab[aseg == label] = TISSUE_CODE[coarse]
    if wmh is not None:
        if wmh.shape != aseg.shape:
            raise ValueError("WMH-Maske %s passt nicht zum Labelbild %s"
                             % (wmh.shape, aseg.shape))
        lab[(wmh > 0) & (lab > 0)] += WMH_OFFSET
    return lab


def tissue_volumes(lab, vox_mm3, wmh=None):
    """Zeilen measure=tissue_volume aus dem Bild von tissue_label_image()."""
    counts = np.bincount(lab.ravel(), minlength=WMH_OFFSET + 4)
    rows, total = [], {}
    for coarse, code in TISSUE_CODE.items():
        total[coarse] = (counts[code] + counts[code + WMH_OFFSET]) * vox_mm3
        rows.append(_row(coarse, total[coarse]))
    rows.append(_row("sum_GM_WM_CSF", sum(total.values())))
    if wmh is not None:
        rows.append(_row("WM_minus_WMH", counts[TISSUE_CODE["WM"]] * vox_mm3))
        inside = 0                       # in Voxeln, damit die Differenz exakt bleibt
        for coarse, code in TISSUE_CODE.items():
            inside += int(counts[code + WMH_OFFSET])
            rows.append(_row("WMH_in_" + coarse, counts[code + WMH_OFFSET] * vox_mm3))
        outside = int(np.count_nonzero(wmh > 0)) - inside
        rows.append(_row("WMH_outside_classes", outside * vox_mm3))
    return rows


def _row(structure, volume_mm3):
    return {"measure": "tissue_volume", "label": "", "structure": structure,
            "side": "both", "volume_mm3": float(volume_mm3)}


def sanity_warnings(tissue_rows, unmapped):
    """Liste von Warntexten. Leer, wenn nichts auffaellt."""
    vol = {r["structure"]: r["volume_mm3"] for r in tissue_rows}
    out = []
    if unmapped:
        out.append("%d Labels nicht in TISSUE_MAP, eigene tissue_fine-Zeile, aber "
                   "in keiner Gewebeklasse: %s" % (len(unmapped), sorted(unmapped)))
    if vol.get("WM", 0) > 0:
        ratio = vol["GM"] / vol["WM"]
        lo, hi = GM_WM_RATIO_RANGE
        if not lo <= ratio <= hi:
            out.append("GM/WM = %.2f liegt ausserhalb %.1f bis %.1f. Meist fehlt "
                       "eine Labelklasse in TISSUE_MAP oder sie steht in der "
                       "falschen Gruppe." % (ratio, lo, hi))
    total_ml = vol.get("sum_GM_WM_CSF", 0) / 1000.0
    lo, hi = SUM_ML_RANGE
    if total_ml and not lo <= total_ml <= hi:
        out.append("GM+WM+CSF = %.0f ml liegt ausserhalb %.0f bis %.0f ml. "
                   "Voxelgroesse im Header pruefen." % (total_ml, lo, hi))
    if vol.get("WMH_outside_classes", 0) > 0:
        out.append("%.2f ml der WMH-Maske liegen in keiner Gewebeklasse."
                   % (vol["WMH_outside_classes"] / 1000.0))
    return out
