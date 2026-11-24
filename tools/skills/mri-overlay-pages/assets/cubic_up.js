// Cubic B-spline upsampling of a grey picture in the browser. Source: wmh_trainer (MIT, Uchralt Temuulen), commit 06e8190.
// Use: const fine = cubicUp(grey, w, h, 4);  grey = Uint8 values row by row; returns (w*f) x (h*f) values.
// Masks and all measures (Dice, counts) stay on the native voxels; only the shown scan is upsampled.
// Cubic B-spline interpolation of a grey picture to f times the size (f = whole number).
// The same method as scipy.ndimage.zoom(order=3, grid_mode=True): every voxel becomes f x f
// smooth points instead of one square. The outline of the picture stays where it is, so the
// voxel grid of the mask still fits. Returns the grey values row by row (0 .. 255).
function cubicUp(grey, w, h, f){
  const Z = Math.sqrt(3) - 2;                      // pole of the cubic spline filter
  const c = new Float32Array(w * h);
  for (let i = 0; i < c.length; i++) c[i] = grey[i];
  // 1. spline coefficients: filter one line (a row or a column) in place, mirrored at the ends
  const filterLine = (off, n, step) => {
    if (n < 2) return;
    let sum = 0, zk = 1;
    for (let k = 0; k < n; k++) c[off + k * step] *= 6;
    for (let k = 0; k < Math.min(n, 28); k++){ sum += c[off + k * step] * zk; zk *= Z; }
    c[off] = sum;
    for (let k = 1; k < n; k++) c[off + k * step] += Z * c[off + (k - 1) * step];
    const last = off + (n - 1) * step;
    c[last] = Z / (Z * Z - 1) * (c[last] + Z * c[last - step]);
    for (let k = n - 2; k >= 0; k--) c[off + k * step] = Z * (c[off + (k + 1) * step] - c[off + k * step]);
  };
  for (let y = 0; y < h; y++) filterLine(y * w, w, 1);
  for (let x = 0; x < w; x++) filterLine(x, h, w);
  // 2. for every new point: its 4 neighbours on the old grid and their weights
  const taps = n => {
    const idx = new Int32Array(n * f * 4), wt = new Float32Array(n * f * 4);
    for (let j = 0; j < n * f; j++){
      const pos = (j + 0.5) / f - 0.5, i = Math.floor(pos), t = pos - i;
      const weights = [(1 - t) ** 3 / 6, (3 * t ** 3 - 6 * t * t + 4) / 6, (-3 * t ** 3 + 3 * t * t + 3 * t + 1) / 6, t ** 3 / 6];
      for (let k = 0; k < 4; k++){
        let q = i - 1 + k;
        if (q < 0) q = -q;
        if (q > n - 1) q = 2 * (n - 1) - q;
        idx[j * 4 + k] = Math.max(0, q); wt[j * 4 + k] = weights[k];
      }
    }
    return { idx, wt };
  };
  const W = w * f, H = h * f, tx = taps(w), ty = taps(h);
  // 3. first along the rows, then along the columns
  const wide = new Float32Array(W * h);
  for (let y = 0; y < h; y++){
    const row = y * w;
    for (let j = 0, o = y * W; j < W; j++, o++){
      const a = j * 4;
      wide[o] = c[row + tx.idx[a]] * tx.wt[a] + c[row + tx.idx[a + 1]] * tx.wt[a + 1] +
                c[row + tx.idx[a + 2]] * tx.wt[a + 2] + c[row + tx.idx[a + 3]] * tx.wt[a + 3];
    }
  }
  const out = new Uint8ClampedArray(W * H);         // rounds, and keeps the values in 0 .. 255
  for (let j = 0; j < H; j++){
    const a = j * 4;
    const r0 = ty.idx[a] * W, r1 = ty.idx[a + 1] * W, r2 = ty.idx[a + 2] * W, r3 = ty.idx[a + 3] * W;
    const w0 = ty.wt[a], w1 = ty.wt[a + 1], w2 = ty.wt[a + 2], w3 = ty.wt[a + 3];
    for (let x = 0, o = j * W; x < W; x++, o++)
      out[o] = wide[r0 + x] * w0 + wide[r1 + x] * w1 + wide[r2 + x] * w2 + wide[r3 + x] * w3;
  }
  return out;
}
