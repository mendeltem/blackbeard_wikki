"""Synthetic test: two volumes with spheres, a reference and a probability map with two hits and one false alarm.
Checks that data.json counts TP/FP/FN as the metric would, that the comparison wording and the verdict mode build."""
import json, os, subprocess, sys, tempfile
import nibabel as nib, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "src", "qc_slice_viewer.py")


def sphere(shape, centre, r):
    z, y, x = np.ogrid[:shape[0], :shape[1], :shape[2]]
    return (x - centre[2]) ** 2 + (y - centre[1]) ** 2 + (z - centre[0]) ** 2 <= r * r


def make_case(d, cid, seed):
    rng = np.random.default_rng(seed)
    shape = (64, 72, 40)
    img = np.zeros(shape, np.float32)
    brain = sphere(shape, (32, 36, 20), 26); img[brain] = 100 + 20 * rng.standard_normal(brain.sum())
    ref = np.zeros(shape, bool); centres = [(20, 30, 15), (40, 40, 22), (30, 50, 28)]
    for c in centres:
        ref |= sphere(shape, c, 2)
    prob = np.zeros(shape, np.float32)
    for c in centres[:2]:                       # two hits
        prob[sphere(shape, c, 2)] = 0.9
    prob[sphere(shape, (44, 20, 12), 2)] = 0.8  # one false alarm
    prob[sphere(shape, (12, 60, 30), 0.6)] = 0.7  # a tiny blob below the size rule (1 voxel)
    aff = np.diag([0.5, 0.5, 1.0, 1.0])
    paths = {}
    for name, arr in (("image", img), ("reference", ref.astype(np.uint8)), ("prob", (prob * 255).astype(np.uint8))):
        p = os.path.join(d, f"{cid}_{name}.nii.gz"); nib.save(nib.Nifti1Image(arr, aff), p); paths[name] = p
    return dict(id=cid, image=paths["image"], reference=paths["reference"], runs={"model": paths["prob"]})


def run(manifest, out, extra=()):
    subprocess.run([sys.executable, TOOL, manifest, "--out", out, *extra], check=True, capture_output=True)
    return json.load(open(os.path.join(out, "data.json"))), open(os.path.join(out, "quality_control.html")).read()


def test_counts_and_pages():
    with tempfile.TemporaryDirectory() as d:
        cases = [make_case(d, "case-a", 1), make_case(d, "case-b", 2)]
        m = dict(dataset="synthetic", cohort="synth", reference_is="reference", image_as_acquired=True,
                 runs=[dict(name="model", kind="prob", threshold=0.3, min_mm3=1.0, info="synthetic model")], cases=cases)
        mp = os.path.join(d, "manifest.json"); json.dump(m, open(mp, "w"))
        data, html = run(mp, os.path.join(d, "out"))
        assert len(data) == 2
        for c in data:
            s = c["stats"]["model"]
            assert (s["tp"], s["fp"], s["fn"]) == (2, 1, 1), s
            assert c["n_ref"] == 3 and len(c["tiles"]) > 0
        assert "Reference (blue)" in html and "synthetic model" in html
        # verdict mode and comparison wording
        data_v, html_v = run(mp, os.path.join(d, "out_v"), ["--verdict"])
        assert os.path.exists(os.path.join(d, "out_v", "img", "case-a_TP.png")) and "by verdict" in html_v
        m["reference_is"] = "comparison"; json.dump(m, open(mp, "w"))
        _, html_c = run(mp, os.path.join(d, "out_c"))
        assert "NOT a reference" in html_c and "only comparison" in html_c
        # mask runs and a case without a reference
        m["runs"].append(dict(name="maskrun", kind="mask")); m["cases"][0]["runs"]["maskrun"] = cases[0]["reference"]; m["cases"][1]["reference"] = None
        json.dump(m, open(mp, "w"))
        data_m, _ = run(mp, os.path.join(d, "out_m"))
        assert data_m[0]["stats"]["maskrun"]["tp"] == 3 and data_m[1]["n_ref"] == 0


if __name__ == "__main__":
    test_counts_and_pages(); print("ok")
