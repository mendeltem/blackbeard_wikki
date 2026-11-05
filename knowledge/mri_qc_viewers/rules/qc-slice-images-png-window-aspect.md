---
id: qc-slice-images-png-window-aspect
typ: regel
status: vorschlag
thema: knowledge/mri_qc_viewers
stand: 2026-11-05
herkunft: own QC page (grey matter, clinical vs research T1, 2026-11-05); a rater called the images squashed and of poor quality
verweist_auf: [qc-slice-viewer-conventions, qc-build-order-for-a-new-lesion-type]
---

# QC slice images: window first, then 8-bit PNG, size from the rotated array

## Aussage
- **Map to 0-255, do not store raw values.** Browsers and monitors show 8 bits per channel. A 16-bit PNG of raw
  intensities is drawn without any window (dark, flat). Window in float (0.5-99.5th percentile inside the brain),
  interpolate in float, round to uint8 last. 256 grey levels inside a brain window exceed what a rater can tell apart.
- **Width and height from the rotated array.** After `np.rot90(slice)` the PIL size is `(rot.shape[1], rot.shape[0])`.
  The page fixed here passed the unrotated extents, so every slice was stretched sideways (366x278 instead of 278x366).
- **Lossless PNG, not JPEG.** JPEG rings at label borders and blurs thin cortex.
- **Upscale in the generator, show 1:1.** Grey image: Lanczos 3x from the windowed float; labels: nearest (borders stay
  on voxel edges). No CSS `image-rendering:pixelated` stretching to the column width.
- **Overlay as a separate transparent palette PNG** (index 0 clear, 25 % tint, solid 1-px outline), stacked by the browser.
  The overlay switch just hides the layer; the anatomy under the label stays visible. Size: 11 MB per pair of 47-slice
  stacks instead of 27 MB for RGB overlay images (measured 2026-11-05).
- **Check native voxel size first.** If the T1 is 1 mm isotropic, resampling to the 1 mm segmentation grid costs nothing;
  with thick or anisotropic slices, render on the native grid with the voxel aspect.

## Traegt
Measured on public DLBS T1 (OpenNeuro ds004856) with SynthSeg 2 labels; PIL 11, numpy; Firefox headless screenshot.

## Traegt nicht
Display of FLAIR with bright lesions needs its own window (see LOG 2026-11-05, qc_slice_viewer grey_window).

## Bruchindikator
Image width/height ratio differs from the brain's left-right / anterior-posterior extent; blocky edges at normal zoom.

## Ablesung
`assert img.size == (rot.shape[1]*U, rot.shape[0]*U)` after every resize; look at one public image before delivery.
Sources: Pillow docs, Image.resize and PNG transparency (https://pillow.readthedocs.io, version 11); PNG spec
W3C 2003 (https://www.w3.org/TR/png/), 8/16-bit depths and tRNS chunk.
