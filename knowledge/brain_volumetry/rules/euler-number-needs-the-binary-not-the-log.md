---
id: euler-number-needs-the-binary-not-the-log
typ: regel
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: QC gate of the DEMDAS pilot, 13.10.2026: 6 of 61 finished sessions reported Euler = 2
verweist_auf: [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort]
---

# Take the Euler number from `mris_euler_number` on `?h.orig.nofix`; a log fallback can return the post-fix value 2

## Aussage
The QC-relevant Euler number is that of the UNCORRECTED surface (`surf/lh.orig.nofix`, `rh.orig.nofix`), read with
`mris_euler_number`. In FreeSurfer 8.2 the binary needs the ITK libraries (`libitkvnl_algo-5.3.so.1`) on LD_LIBRARY_PATH; without
them it fails silently in a subprocess and a fallback that greps `recon-all.log` can pick the LAST "euler #" line, which is the
topology-fixed surface (always 2). In the pilot this produced 6 sessions with Euler 2 and a wrong "recon-all pending" state; with the
library path set, all 61 sessions had values between -142 and -15, cohort cutoff Q1 - 1.5 IQR = -109.5, no session flagged.

## Traegt
Every QC gate built on the Euler number (Rosen 2018); every tool that wraps FreeSurfer 8 binaries from a conda Python.

## Traegt nicht
FreeSurfer installations whose binaries find their libraries on the default path.

## Bruchindikator
An Euler number of exactly 2 or an empty value for a finished session.

## Ablesung
13.10.2026 14:20-14:35, qc_gate.py before/after the LD_LIBRARY_PATH fix (61 sessions).

## Quellen
- Rosen AFG et al. 2018. Quantitative assessment of structural image quality. NeuroImage 169:407-418. DOI 10.1016/j.neuroimage.2017.12.059. PMID 29278774.
- Monereo-Sanchez J et al. 2021. Quality control strategies for brain MRI segmentation and parcellation: insights from the Maastricht Study. NeuroImage 237:118174. DOI 10.1016/j.neuroimage.2021.118174. PMID 34000406.

## Verknuepft
- [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort](../findings/freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort.md)
