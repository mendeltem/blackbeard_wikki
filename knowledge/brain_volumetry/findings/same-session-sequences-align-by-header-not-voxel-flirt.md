---
id: same-session-sequences-align-by-header-not-voxel-flirt
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-16
herkunft: FLAIR onto T2*/SWI for an in-house microbleed cohort (40 cases), Alita 2026-10-16; visual QC and brain-mask overlap
verweist_auf: []
---

# Sequences of one session align by their headers; a voxel-space FLIRT start can rotate them by 90-180 degrees

## Aussage
1. FLAIR and T2* of the same session were stored with different axis orders (T2* LPS, FLAIR after
   `fslreorient2std` RAS). FLIRT (6 dof, normalised mutual information, search +-20 degrees) starts in FSL's
   scaled-voxel space, not in scanner space: the needed 180-degree flip lay outside the search range and the
   result was rotated (visible only on the image; the cost value looked unremarkable). `-usesqform` did not
   rescue it either.
2. The two headers already share the scanner frame (same centre to 0.1 mm): resampling the FLAIR onto the T2*
   matrix by world coordinates (`nibabel.processing.resample_from_to`, trilinear) overlays exactly; brain-mask
   overlap Dice median 0.98 over 40 cases. One case (0.84) had a smaller FLAIR field of view / motion: flagged,
   its SynthSeg taken from the T2*/SWI instead.
3. SynthSeg on the FLAIR (better tissue contrast, 2.5 mm instead of 5 mm slices) carried over the same way
   (nearest neighbour); keep it only where it covers the brain mask (Dice >= 0.85), else SynthSeg of the scan.

## Traegt
Visual checkerboard QC of the corrected version, overlap numbers for all 40 cases; identical header centres.

## Traegt nicht
Sequences from different sessions or with patient motion need a real registration (header start + small search,
e.g. FLIRT with `-usesqform` after both files share one orientation, or ANTs).

## Bruchindikator
A checkerboard that breaks at tissue borders after header resampling.

## Ablesung
FLIRT: Jenkinson M, Smith S. A global optimisation method for robust affine registration of brain images.
Med Image Anal 2001;5(2):143-156, doi:10.1016/S1361-8415(01)00036-6. Jenkinson M, Bannister P, Brady M, Smith S.
NeuroImage 2002;17(2):825-841, doi:10.1006/nimg.2002.1132. FLIRT user guide (`-usesqform`):
https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT/UserGuide. NIfTI qform/sform: https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/qsform.html.
SynthSeg robust: Billot B, Magdamo C, Cheng Y, Arnold SE, Das S, Iglesias JE. PNAS 2023;120(9):e2216399120,
doi:10.1073/pnas.2216399120. Own runs 2026-10-16 (FSL 6.0.7.23, FreeSurfer 8.2.0).
