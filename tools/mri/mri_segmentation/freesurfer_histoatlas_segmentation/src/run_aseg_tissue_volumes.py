#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kommandozeile zu aseg_tissue.py. Linear, ohne main().

    python run_aseg_tissue_volumes.py --seg SEG --out CSV
                                      [--wmh MASKE] [--pallidum-vdc gm|wm]
                                      [--labels-out NIFTI]

Rueckgabewert: 0 ok, 1 ok mit Warnungen, 2 Eingabefehler.
"""
import argparse
import csv
import os
import sys

import numpy as np
import nibabel as nib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aseg_tissue as at  # noqa: E402

parser = argparse.ArgumentParser(description="GM/WM/CSF aus einem aseg-Labelbild")
parser.add_argument("--seg", required=True,
                    help="aseg-Labelbild: SynthSeg, SuperSynth oder aseg (.nii.gz, .mgz)")
parser.add_argument("--out", required=True, help="Ausgabe-CSV, long format")
parser.add_argument("--wmh", default="",
                    help="binaere WMH-Maske im SELBEN Grid wie --seg (optional)")
parser.add_argument("--pallidum-vdc", choices=sorted(at.CONVENTIONS), default="gm",
                    help="wohin Pallidum und Ventral DC zaehlen (Standard: gm)")
parser.add_argument("--labels-out", default="",
                    help="optional: Gewebe-Labelbild als .nii.gz schreiben")
args = parser.parse_args()

seg_img, aseg = at.load_labels(args.seg)
vox = at.voxel_mm3(seg_img)

wmh = None
if args.wmh:
    wmh_img = nib.load(args.wmh)
    if not at.same_grid(seg_img, wmh_img):
        print("FEHLER: --wmh liegt nicht im Grid von --seg. Erst resamplen "
              "(nearest), dann erneut aufrufen. Hier wird nicht geraten.",
              file=sys.stderr)
        sys.exit(2)
    wmh = np.asanyarray(wmh_img.dataobj)

groups = at.CONVENTIONS[args.pallidum_vdc]
label_class = at.class_of(groups)

fine_rows, unmapped = at.fine_volumes(aseg, vox)
lab = at.tissue_label_image(aseg, label_class, wmh)
tissue_rows = at.tissue_volumes(lab, vox, wmh)
warnings = at.sanity_warnings(tissue_rows, unmapped)

with open(args.out, "w", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=["measure", "label", "structure",
                                            "side", "volume_mm3"])
    writer.writeheader()
    writer.writerows(tissue_rows + fine_rows)

if args.labels_out:
    out_img = nib.Nifti1Image(lab, seg_img.affine)
    out_img.set_data_dtype(np.uint8)
    out_img.header.set_slope_inter(1, 0)
    nib.save(out_img, args.labels_out)

print("Konvention: Pallidum und Ventral DC -> %s" % args.pallidum_vdc.upper())
for row in tissue_rows:
    print("  %-22s %10.2f ml" % (row["structure"], row["volume_mm3"] / 1000.0))
for text in warnings:
    print("WARNUNG: " + text, file=sys.stderr)

sys.exit(1 if warnings else 0)
