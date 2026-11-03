---
id: gsp1000-leaddbs-header-left-right-mirror
typ: pruefpunkt
status: vorschlag
thema: knowledge/lesion_detection_method
stand: 2026-11-03
herkunft: own check 2026-11-03 of two public Harvard Dataverse releases
verweist_auf: []
---

# GSP1000 connectome: the Lead-DBS release header has x mirrored against the NIfTI release

## Aussage
`vol/space/mat` in `dataset_volsurf.mat` of "GSP1000 Preprocessed Connectome for Lead DBS" says x = +2i - 90 (0-based index i). The NIfTI release of the
same connectome has x = -2i + 90. The time courses have the same voxel index in both (median same-voxel r = 1.00, 100 subjects; 0.38 when mirrored). So at most one header can be right, and the data support the NIfTI one:
T1 of the NIfTI release vs the FSL MNI152 template r = 0.920 as stored, 0.868 mirrored; inferior frontal to posterior temporal connectivity, read with the NIfTI header, is stronger on the left (Fisher z 0.26 vs 0.15, t = 6.0, n = 300).
**Own lesion network code must map through the NIfTI orientation, and test it with a check that would come out differently under a mirror image.**

## Traegt
- Cohen, Al-Fatly, Horn: GSP1000 Preprocessed Connectome for Lead DBS, Harvard Dataverse, doi:10.7910/DVN/KKTJQC.
- GSP1000 Preprocessed Connectome (NIfTI), Harvard Dataverse, doi:10.7910/DVN/ILXIKS.
- Holmes et al. 2015, Brain Genomics Superstruct Project initial data release, Sci Data 2:150031.

## Traegt nicht
- **Whether Lead Mapper itself produces mirrored maps is unverified:** its code was not read and not run. It may handle this internally. Test with a one-sided seed before concluding anything.
- A brain-mask Dice test could not separate the two orientations (0.888 both ways), and a within- vs across-hemisphere test would not either.

## Bruchindikator
Lead-DBS documentation or code shows a deliberate flip for this file, or a one-sided seed in Lead Mapper gives correctly lateralised maps.

## Ablesung
Do not treat this as a bug report until Lead Mapper was tested. Do treat it as a required check for any code reading these `.mat` files directly. Files are compressed MATLAB v5, 120 volumes per run, 285,903 voxels; `scipy.io.loadmat` reads them from inside the tar archives without unpacking.
