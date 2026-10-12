---
id: cohort-copies-need-a-gzip-sweep
typ: regel
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-12
herkunft: DEMDAS pilot, 12.10.2026: one T1w was a truncated copy (508 KB of 5.2 MB) since 03.09.
verweist_auf: [synthseg-in-freesurfer-8-runs-on-cpu-only]
---

# After copying a cohort, run `gzip -t` over every NIfTI and compare file counts and byte totals with the source

## Aussage
A truncated `.nii.gz` is silent until a tool reads past the cut: in the DEMDAS pilot one T1w (508 KB instead of 5.2 MB) sat in
the BIDS tree for five weeks; SynthSeg failed with `zlib.error: invalid distance code` deep in a log, the session simply
vanished from the QC page ("31 of 63"), and recon-all would have failed the same way. The sweep is cheap: 886 NIfTI (12 GB)
in under two minutes. For a cohort copy, also compare file count and summed bytes of source and target, and run an `rsync -c`
dry run; `du -sh` is useless on exFAT (cluster inflation: 67 GB shown for 43.7 GB of data).

## Traegt
Every copy of imaging data from USB drives, network shares or sticks; the inventory step of a new cohort.

## Traegt nicht
Uncompressed files; corruption inside a valid gzip stream (that needs a hash from the source).

## Bruchindikator
A session missing from a QC page without a stated reason; a `.nii.gz` far smaller than its siblings.

## Ablesung
12.10.2026 16:16-16:25 (gzip sweep, inventory size 5.221 MB vs local 508 KB, replacement from the external SSD).

## Verknuepft
- [synthseg-in-freesurfer-8-runs-on-cpu-only](../findings/synthseg-in-freesurfer-8-runs-on-cpu-only.md)
