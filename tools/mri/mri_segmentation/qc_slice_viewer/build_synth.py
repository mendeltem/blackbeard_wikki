#!/usr/bin/env python3
"""build_synth.py -- materialise the two synthetic volumes for the extended generator.

Recipe is 1:1 from tests/test_synthetic.py (make_case): a 64x72x40 volume, an
ellipsoid "brain", 3 reference spheres (r=2), a prediction probability map with
two true hits (0.9), one false alarm (0.8) and one 1-voxel sub-size blob (0.7).
The affine is diag([0.5, 0.5, 1.0, 1.0]) so patient (RAS) coordinates are
non-trivial and the affine math can be checked by hand.

Each output volume is 4-D (I, J, K, 2): channel 0 = reference mask, channel 1 =
prediction probability (float 0..1).
"""
import os, sys
import nibabel as nib
import numpy as np


def sphere(shape, centre, r):
    z, y, x = np.ogrid[:shape[0], :shape[1], :shape[2]]
    return (x - centre[2]) ** 2 + (y - centre[1]) ** 2 + (z - centre[0]) ** 2 <= r * r


def make_volume(d, stem, seed):
    rng = np.random.default_rng(seed)
    shape = (64, 72, 40)
    img = np.zeros(shape, np.float32)
    brain = sphere(shape, (32, 36, 20), 26)
    img[brain] = 100 + 20 * rng.standard_normal(brain.sum())
    ref = np.zeros(shape, bool)
    centres = [(20, 30, 15), (40, 40, 22), (30, 50, 28)]
    for c in centres:
        ref |= sphere(shape, c, 2)
    prob = np.zeros(shape, np.float32)
    for c in centres[:2]:                      # two true hits
        prob[sphere(shape, c, 2)] = 0.9
    prob[sphere(shape, (44, 20, 12), 2)] = 0.8   # one false alarm
    prob[sphere(shape, (12, 60, 30), 0.6)] = 0.7  # sub-size 1-voxel blob
    vol = np.stack([ref.astype(np.uint8), prob], axis=-1)   # (I,J,K,2)
    aff = np.diag([0.5, 0.5, 1.0, 1.0])
    p = os.path.join(d, f"{stem}.nii.gz")
    nib.save(nib.Nifti1Image(vol, aff), p)
    return p


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(d, exist_ok=True)
    for stem, seed in (("synth_a", 1), ("synth_b", 2)):
        print(make_volume(d, stem, seed))
