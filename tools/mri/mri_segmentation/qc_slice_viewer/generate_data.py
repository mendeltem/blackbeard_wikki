#!/usr/bin/env python3
"""generate_data.py -- extend the qc_slice_viewer generator with per-finding geometry
and TP/FP/FN assignment.

Part of the plan 2026-10-12 10:54 "beende den offenen Kasten im Pruefpunkt
slice-viewer-as-shared-tool" (Auftrag 2, "generator-erweitern").

The shared slice-viewer tool (src/qc_slice_viewer.py) already labels every
reference and predicted connected component and forms per-component hit maps,
but it collapses them to counts before data.json is written, so the front-end
can neither show coordinates nor count the assignment per finding. This script
is the self-contained, runnable extension: it reads the (reference, prediction)
pair packed in each synthetic volume and emits, for EVERY finding (sphere),

    bounding_box            [min_i, min_j, min_k, max_i, max_j, max_k]  (voxel / image coords)
    centroid_voxel_image    [i, j, k]                                   (voxel / image coords)
    centroid_voxel_patient  [x, y, z] mm  (RAS, via the NIfTI affine header)
    label                   one of {TP, FP, FN}

plus per-finding volume (voxels + mm3), number of slices it spans, the IoU that
decided the label, and the id of the paired ground-truth / predicted component.

TP/FP/FN logic (IoU based, threshold 0.5):
    TP = a predicted component with IoU > 0.5 against a ground-truth sphere
    FP = a predicted component with no ground-truth hit (max IoU <= threshold)
    FN = a ground-truth sphere with no predicted hit (max IoU <= threshold)

Input volumes: each .nii.gz is a 4-D volume of shape (I, J, K, 2):
    channel 0 = reference (ground truth) mask, > 0 = lesion
    channel 1 = prediction probability map, 0..1 (float) or uint8 0..255
The two synthetic volumes are the ones materialised from
tests/test_synthetic.py (3 reference spheres each; the prediction has two true
hits, one false alarm and one sub-size blob). See build_synth.py in this folder.

Usage:
    python generate_data.py --volumes data/synth_a.nii.gz data/synth_b.nii.gz \
        --out tools/mri/mri_segmentation/qc_slice_viewer/data/

Output: one <stem>.json per volume with the case id, cohort, the iou threshold,
the aggregate stats (tp/fp/fn/n/dice) and the `findings` list (one entry per
detected or missed sphere) carrying the four new fields above.

No patient data. No GPU. Conda env "dl": nibabel, scipy, numpy.
"""
from __future__ import annotations
import argparse, json, os
import nibabel as nib
import numpy as np
from scipy import ndimage

CONNECTIVITY_26 = np.ones((3, 3, 3), bool)
IOU_THRESHOLD = 0.5          # TP iff IoU(pred, gt) > 0.5
PROB_THRESHOLD = 0.3         # prediction probability threshold (matches test)
MIN_MM3 = 1.0                # drop prediction components smaller than this (matches test)


def as_prob(a):
    a = np.asarray(a, dtype=np.float32)
    return a / 255.0 if a.max() > 1.5 else a


def post_process(prob, vox_mm3):
    """Threshold + size rule + 26-connectivity, exactly as the real tool does."""
    lab, n = ndimage.label(prob > PROB_THRESHOLD, structure=CONNECTIVITY_26)
    size = np.bincount(lab.ravel(), minlength=n + 1)
    keep = np.ones(n + 1, bool); keep[0] = False
    keep &= size * vox_mm3 >= MIN_MM3
    return keep[lab]


def iou(a, b):
    inter = int(np.logical_and(a, b).sum())
    union = int(np.logical_or(a, b).sum())
    return inter / union if union else 0.0


def component_geometry(mask, affine):
    """bounding_box, image centroid, patient centroid, volume, n_slices for one component."""
    idx = np.argwhere(mask)                       # rows are (i, j, k)
    mn = idx.min(axis=0).tolist()
    mx = idx.max(axis=0).tolist()
    cent_img = ndimage.center_of_mass(mask)       # (i, j, k) float
    cent_img = [float(v) for v in cent_img]
    cent_pat = np.asarray(affine) @ np.array(cent_img + [1.0])
    return {
        "bounding_box": mn + mx,
        "centroid_voxel_image": cent_img,
        "centroid_voxel_patient": [float(v) for v in cent_pat[:3]],
        "volume_voxels": int(mask.sum()),
        "n_slices": int(np.count_nonzero(mask.any(axis=(1, 2)))),
    }


def assign(ref_labels, ref_ids, pred_labels, pred_ids, ref_mask, pred_mask, shape):
    """Greedy IoU matching. Returns (ref_state, pred_state) dicts: id -> (label, paired_id, iou)."""
    ref_geom = {c: (ref_labels == c) for c in ref_ids}
    pred_geom = {c: (pred_labels == c) for c in pred_ids}
    # candidate pairs sorted by descending IoU
    pairs = []
    for pc in pred_ids:
        for rc in ref_ids:
            v = iou(pred_geom[pc], ref_geom[rc])
            if v > IOU_THRESHOLD:
                pairs.append((v, pc, rc))
    pairs.sort(key=lambda t: -t[0])
    ref_state = {c: ("FN", None, 0.0) for c in ref_ids}
    pred_state = {c: ("FP", None, 0.0) for c in pred_ids}
    used_r, used_p = set(), set()
    for v, pc, rc in pairs:
        if pc in used_p or rc in used_r:
            continue
        pred_state[pc] = ("TP", rc, round(v, 4))
        ref_state[rc] = ("TP", pc, round(v, 4))
        used_p.add(pc); used_r.add(rc)
    return ref_state, pred_state


def build_case(vol_path, cohort):
    nii = nib.load(vol_path)
    arr = np.asarray(nii.dataobj)
    affine = np.asarray(nii.affine)
    if arr.ndim == 4 and arr.shape[-1] == 2:
        ref = (arr[..., 0] > 0)
        prob = as_prob(arr[..., 1])
    elif arr.ndim == 3:
        ref = arr > 0
        prob = np.zeros(arr.shape, np.float32)
    else:
        raise SystemExit(f"{vol_path}: unsupported shape {arr.shape}")
    vox_mm3 = float(np.prod(nii.header.get_zooms()[:3]))
    pred = post_process(prob, vox_mm3)

    ref_labels, n_ref = ndimage.label(ref, structure=CONNECTIVITY_26)
    pred_labels, n_pred = ndimage.label(pred, structure=CONNECTIVITY_26)
    ref_ids = list(range(1, n_ref + 1))
    pred_ids = list(range(1, n_pred + 1))
    ref_state, pred_state = assign(ref_labels, ref_ids, pred_labels, pred_ids, ref, pred, ref.shape)

    findings = []
    for c in pred_ids:                                  # detected lesions: TP or FP
        m = pred_labels == c
        label, paired, iou = pred_state[c]
        g = component_geometry(m, affine)
        g.update(id=f"pred-{c}", source="prediction", label=label,
                 iou_with_ref=iou, paired_ref_id=(f"ref-{paired}" if paired else None))
        findings.append(g)
    for c in ref_ids:                                   # missed ground truth: FN (TP ones already covered)
        label, paired, iou = ref_state[c]
        if label == "TP":
            continue
        m = ref_labels == c
        g = component_geometry(m, affine)
        g.update(id=f"ref-{c}", source="reference", label=label,
                 iou_with_ref=iou, paired_pred_id=(f"pred-{paired}" if paired else None))
        findings.append(g)

    both = int(np.logical_and(ref, pred).sum())
    den = int(pred.sum()) + int(ref.sum())
    dice = round(2 * both / den, 4) if den else 1.0
    tp = sum(1 for c in pred_ids if pred_state[c][0] == "TP")
    fp = sum(1 for c in pred_ids if pred_state[c][0] == "FP")
    fn = sum(1 for c in ref_ids if ref_state[c][0] == "FN")
    return {
        "id": os.path.splitext(os.path.basename(vol_path))[0],
        "cohort": cohort,
        "shape": list(arr.shape[:-1] if arr.ndim == 4 else arr.shape),
        "vox_mm3": round(vox_mm3, 6),
        "iou_threshold": IOU_THRESHOLD,
        "n_ref": int(n_ref),
        "n_pred": int(n_pred),
        "stats": {"tp": int(tp), "fp": int(fp), "fn": int(fn), "n": int(n_pred),
                  "dice": dice,
                  "ref_ml": round(float(ref.sum()) * vox_mm3 / 1000.0, 3),
                  "pred_ml": round(float(pred.sum()) * vox_mm3 / 1000.0, 3)},
        "findings": findings,
    }


def main():
    ap = argparse.ArgumentParser(description="Extend data.json with per-finding geometry + TP/FP/FN.")
    ap.add_argument("--volumes", nargs="+", required=True, help="4-D (I,J,K,2) .nii.gz, ch0=ref ch1=pred")
    ap.add_argument("--out", required=True, help="output directory for the .json files")
    ap.add_argument("--cohort", default="synth")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    for v in args.volumes:
        case = build_case(v, args.cohort)
        out = os.path.join(args.out, case["id"] + ".json")
        with open(out, "w") as f:
            json.dump(case, f, indent=2)
        print(f"{case['id']}: n_ref={case['n_ref']} n_pred={case['n_pred']} "
              f"tp/fp/fn={case['stats']['tp']}/{case['stats']['fp']}/{case['stats']['fn']} "
              f"dice={case['stats']['dice']} findings={len(case['findings'])} -> {out}")


if __name__ == "__main__":
    main()

# ============================================================================
# VALIDATION REPORT -- extended generator run on the two synthetic volumes
# (synth_a, synth_b; each 3 reference spheres, prediction = 2 hits + 1 false
#  alarm + 1 sub-size blob, so the expected assignment is tp/fp/fn = 2/1/1).
# Every number below is from the real run (script + generated .json files), not
# invented. See the run log at the path quoted per section.
# ============================================================================

## Fields Present
# The step-4 assertion (all 4 keys in every finding) passed on BOTH volumes:
#   python -c "import json; d=json.load(open('<v>.json')); \
#     assert all(k in f for f in d['findings'] for k in \
#     ['bounding_box','centroid_voxel_image','centroid_voxel_patient','label'])"
# -> synth_a.nii.json OK, findings= 4 ; synth_b.nii.json OK, findings= 4
# Required per-finding fields (all present in all 8 findings):
#   bounding_box            [min_i, min_j, min_k, max_i, max_j, max_k]  (voxel/image)
#   centroid_voxel_image    [i, j, k]                                   (voxel/image)
#   centroid_voxel_patient  [x, y, z] mm, RAS via NIfTI affine
#   label                   TP | FP | FN
# Extra per-finding fields: volume_voxels, n_slices, iou_with_ref,
#   paired_ref_id / paired_pred_id, id, source.
# Spot check (synth_a, affine = diag(0.5, 0.5, 1.0)): pred-1 centroid image
#   (20.0, 30.0, 15.0) -> patient (10.0, 15.0, 15.0)  [x*0.5, y*0.5, z*1.0]. CORRECT.

## IoU Threshold
# Threshold used: IOU_THRESHOLD = 0.5  (TP iff IoU(pred, gt) > 0.5).
# Observed per-finding IoU (both volumes identical):
#   pred-1 (TP) = 1.0   pred-2 (TP) = 1.0
#   pred-3 (FP) = 0.0   ref-2  (FN) = 0.0
# The two true hits sit exactly on their ground-truth spheres (IoU 1.0 > 0.5 ->
# TP); the false alarm and the missed sphere are disjoint from everything
# (IoU 0.0 <= 0.5 -> FP / FN). No finding sits in the ambiguous 0.0<IoU<=0.5 band.

## Label Distribution
# Per volume (synth_a and synth_b identical), 4 findings each:
#   TP = 2   (pred-1, pred-2)   true hits
#   FP = 1   (pred-3)           false alarm
#   FN = 1   (ref-2)            missed ground-truth sphere
# Aggregate stats per volume: tp=2 fp=1 fn=1 n_pred=3 dice=0.6667
#   (3 equal reference spheres, 2 hit + 1 false alarm: 2*2N / 6N = 2/3).
# Matches the reference expectation of tests/test_synthetic.py (tp/fp/fn = 2/1/1).
# Source of all numbers: qc_slice_viewer/generate_data.py + build_synth.py,
# outputs qc_slice_viewer/data/synth_a.nii.json, synth_b.nii.json (run 2026-10-12).
