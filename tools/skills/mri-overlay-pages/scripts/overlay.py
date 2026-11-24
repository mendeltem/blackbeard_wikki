"""House colours and picture quality for masks drawn over an MRI slice (user rule 24.11.2026).
Import the functions or copy them; never retype the colours.

    python overlay.py --demo OUT_DIR     builds a small page from a synthetic phantom (no patient data)

Needs numpy, scipy, Pillow."""
import argparse, os
import numpy as np
from scipy import ndimage
from PIL import Image

# role -> (colour, words for the legend, how it is drawn)
COL = dict(gt=(46, 134, 171), rater2=(232, 135, 30), tp=(59, 178, 115), fp=(232, 23, 138), fn=(235, 60, 60))
WORDS = dict(gt="ground truth", rater2="second rater", tp="true positive (found)", fp="false positive (false alarm)", fn="false negative (missed)")
COLOUR_NAME = dict(gt="blue", rater2="orange", tp="green", fp="pink", fn="red")
INNER = ("gt", "rater2")          # rater marks: ring inside the mask
OUTER = ("tp", "fn", "fp")        # verdicts: ring around the mask, so a red ring around a blue lesion reads "missed"
LEGEND = ("gt", "rater2", "tp", "fp", "fn")
FULL = {2: np.ones((3, 3), bool), 3: np.ones((3, 3, 3), bool)}


def verdict(found, truth):
    """Split into TP, FP, FN by connected clusters (8-neighbourhood in 2-D, 26 in 3-D); hit = the clusters touch.
    tp, fp = clusters of `found`; fn = clusters of `truth` that no found cluster touches."""
    st = FULL[found.ndim]
    lab_f, _ = ndimage.label(found, st); lab_t, _ = ndimage.label(truth, st)
    near_t = ndimage.binary_dilation(truth, st); near_f = ndimage.binary_dilation(found, st)
    hit_f = np.unique(lab_f[near_t & (lab_f > 0)]); hit_t = np.unique(lab_t[near_f & (lab_t > 0)])
    tp = np.isin(lab_f, hit_f) & found
    return dict(tp=tp, fp=found & ~tp, fn=truth & ~np.isin(lab_t, hit_t))


def grey_up(a, scale, lo, hi, hide=False):
    """Window first, then upsample with a cubic spline (order 3). scale = (rows, columns), whole numbers.
    hide=True gives a flat grey picture of the same size: layout check without showing a patient scan."""
    if hide: return np.full((a.shape[0] * scale[0], a.shape[1] * scale[1]), 128, np.uint8)
    w = np.clip((a.astype(np.float32) - lo) / max(hi - lo, 1e-6), 0, 1)
    u = ndimage.zoom(w, scale, order=3, mode="nearest", grid_mode=True)
    return (np.clip(u, 0, 1) * 255).round().astype(np.uint8)


def ring(m, width, outer, inset=0):
    """outer: ring around the mask. inner: ring inside it; inset moves it further in, so two raters on the same lesion both show."""
    if not m.any(): return m
    if outer: return ndimage.binary_dilation(m, iterations=width) & ~m
    if inset: m = ndimage.binary_erosion(m, iterations=inset, border_value=0)
    return m & ~ndimage.binary_erosion(m, iterations=width, border_value=0)


def overlay_rgba(layers, scale, width=2):
    """layers: role -> 2-D boolean mask on the native voxels. Masks are enlarged by repeating voxels (never smoothed),
    then drawn as crisp rings. Returns an RGBA picture of the same size as grey_up(...)."""
    unknown = set(layers) - set(COL)
    assert not unknown, f"no house colour for {unknown}: give extra layers their own picture and a colour that is none of the five"
    up = {k: np.repeat(np.repeat(v.astype(bool), scale[0], 0), scale[1], 1) for k, v in layers.items()}
    o = np.zeros(next(iter(up.values())).shape + (4,), np.uint8)
    for k in INNER + OUTER:
        if k not in up: continue
        e = ring(up[k], width, k in OUTER)
        if k == "rater2" and "gt" in up:          # a second-rater mark on a ground-truth lesion: ring one step further in, both show
            lab, _ = ndimage.label(up[k], FULL[2]); shared = np.isin(lab, np.unique(lab[up["gt"] & (lab > 0)])) & up[k]
            e = ring(up[k] & ~shared, width, False) | ring(shared, width, False, inset=width)
        o[e, :3] = COL[k]; o[e, 3] = 255
    return o


def save_pair(stem, a, layers, scale, lo, hi, hide=False):
    """Writes <stem>.png (scan, 8-bit grey) and <stem>_o.png (transparent overlay, same size). Lossless, no JPEG."""
    Image.fromarray(grey_up(a, scale, lo, hi, hide)).save(stem + ".png", optimize=True)
    Image.fromarray(overlay_rgba(layers, scale), "RGBA").save(stem + "_o.png", optimize=True)


def legend_html(roles):
    """Swatch plus words for the roles on the page, in the fixed order."""
    sw = '<span style="display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;margin-right:6px;background:rgb({})"></span>'
    return " &nbsp; ".join(f'<span title="{COLOUR_NAME[k]}">{sw.format(",".join(map(str, COL[k])))}{COLOUR_NAME[k]} = {WORDS[k]}</span>' for k in LEGEND if k in roles)


PAGE = """<!doctype html><html lang="en"><meta charset="utf-8"><title>{title}</title>
<style>body{{margin:0;background:#111;color:#ddd;font:16px system-ui,sans-serif}}header{{position:sticky;top:0;background:#111;padding:10px 16px;border-bottom:1px solid #333;z-index:5}}
button{{font-size:15px;padding:4px 10px;margin-right:14px}}.view{{position:relative;width:{w}px;height:{h}px;margin:16px}}.view img{{position:absolute;left:0;top:0;width:{w}px;height:{h}px}}p{{margin:8px 16px;color:#aaa;max-width:{w}px}}</style>
<header><button id="b" title="switch all outlines on or off">Overlays: ON (O)</button>{legend}</header>
<div class="view"><img src="{stem}.png" alt="scan"><img id="o" src="{stem}_o.png" alt="outlines"></div>
<p>{note}</p>
<script>const b=document.getElementById('b'),o=document.getElementById('o');function t(){{const on=o.style.display==='none';o.style.display=on?'':'none';b.textContent='Overlays: '+(on?'ON':'OFF')+' (O)';}}
b.onclick=t;document.addEventListener('keydown',e=>{{if(e.key==='o'||e.key==='O')t();}});</script></html>"""


def demo(out):
    """Synthetic phantom with all five roles. Not a scan: every value is invented."""
    os.makedirs(out, exist_ok=True); rng = np.random.default_rng(20261124); n = 128
    y, x = np.mgrid[:n, :n]; r = np.hypot((x - 64) / 50, (y - 64) / 58)
    a = 0.02 + ndimage.gaussian_filter((r < 1).astype(float), 1.2) * (0.6 + 0.12 * np.cos(r * 9) + ndimage.gaussian_filter(rng.normal(0, 0.5, (n, n)), 2))
    def blob(cx, cy, rad): return np.hypot(x - cx, y - cy) <= rad
    spots = dict(a=blob(44, 50, 2.6), b=blob(84, 46, 1.6), c=blob(60, 84, 3.2), d=blob(90, 84, 1.2), e=blob(40, 90, 2.0), b2=blob(85, 46, 1.9))
    for m in spots.values(): a[m] -= 0.45
    truth = spots["a"] | spots["b"] | spots["c"]; rater2 = spots["a"] | spots["b2"] | spots["e"]; found = blob(45, 50, 2.4) | blob(60, 85, 2.6) | spots["d"]
    layers = dict(gt=truth, rater2=rater2, **verdict(found, truth)); scale = (6, 6)
    save_pair(f"{out}/demo", a, layers, scale, 0.0, 0.95)
    note = ("Synthetic phantom, no patient data. Scan: windowed 0 to 0.95, then cubic spline (order 3), 6 x 6 points per voxel. "
            "Outlines: voxels repeated, never smoothed. Verdict: connected clusters, 8-neighbourhood, hit = the clusters touch.")
    open(f"{out}/index.html", "w").write(PAGE.format(title="Overlay demo", w=n * 6, h=n * 6, stem="demo", legend=legend_html(layers), note=note))
    print("wrote", out, {k: int(v.sum()) for k, v in layers.items()})


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--demo", metavar="OUT_DIR", required=True); demo(os.path.expanduser(ap.parse_args().demo))
