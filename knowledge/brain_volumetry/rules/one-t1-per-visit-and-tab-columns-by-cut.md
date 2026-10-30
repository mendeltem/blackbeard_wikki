---
id: one-t1-per-visit-and-tab-columns-by-cut
typ: regel
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-30
herkunft: DEMDAS HPC pilot (65 sessions, FreeSurfer 8.1.0), 2026-10-13
verweist_auf: [demdas-pipeline-protocol-v1, euler-number-needs-the-binary-not-the-log]
---

# One T1 per visit, and TSV columns by `cut`, never by `read`

## Aussage
Two list bugs produced 5 of 14 "failed" recon-all jobs in the DEMDAS HPC pilot (Slurm arrays 11179269/70, 13.10.2026):

1. **Empty TSV columns vanish with `read`.** `IFS=$'\t' read -r a b c ...` collapses consecutive tabs, so a row with an empty `run` or `pair` field shifts every later column: recon-all received the DWI path as `-i` ("ERROR: cannot find ...dwi..."; array ids 49, 57, 64). Rule: parse each column with `cut -f N` (keeps empty fields) or in Python with `csv`.
2. **Two T1 files of the same visit under one id.** A DEMDAS session can hold the distortion-corrected MPRAGE (`run-2_T1w`) and the uncorrected ND copy (`_T1w`, no run). The list treated them as two rows with the same id, so two jobs wrote into one working directory and destroyed each other (`MRIsplineNormalize(): npeaks = 1`, line-search failure). On the HPC copy only the ND file existed for the two sessions, and recon-all 8.1.0 failed on the ND image while Alita (8.2.0, run-2) succeeded. Rule: a "pair" is only run-1 + run-2 (two acquisitions); otherwise take exactly one T1, run-2 preferred, as `gm_beispiel.py` does.

A third failure class is a finding, not a bug: `-FLAIRpial` dies with "Numerical result out of range" in the vertex loop of `mris_place_surface` for 3 of 65 sessions whose base run succeeds (array ids 10, 44, 47). The base variant is kept for those.

**Update 2026-10-30: the jobs that "succeeded" were wrong too.** The same `read` shift hit every row whose `run` field was empty, but only the rows where the shifted path was a DWI crashed. Where the shifted path was the FLAIR, recon-all ran to the end on the FLAIR as its T1 input: 49 of 50 kept pilot sessions (FS 8.1.0) show `mri_convert ..._FLAIR.nii.gz` in `scripts/recon-all.log`. Nothing failed; the outputs simply looked like recon-all outputs. It surfaced two weeks later in a method check: cortex about 28 % smaller than the T1-based run of the same session (FS 8.2.0), and Euler numbers of the two runs uncorrelated (rho -0.19). Two rules follow:

3. **After fixing an input-parsing bug, audit the jobs that succeeded, not only the ones that failed.** Grep the input actually used (`mri_convert` line in `recon-all.log`, `-i` in the command) for every finished job.
4. **A resumable array skips finished outputs, including wrong ones.** The fixed script tests `surf/rh.thickness` and exits "done", so the bad runs stay in place, and the longitudinal stream (`-base`/`-long`) picks them up as time points. Delete wrong outputs explicitly before re-submitting, and rebuild every template that used them.

## Trägt
- Local re-run of both list scripts on the 24-participant example set: old 115 rows with 57 duplicate ids, new 58 rows with 0 duplicates; full cohort unchanged (1528 rows, 0 duplicates).
- `hpc/make_session_list.py`, `hpc_py/01_make_session_list.py`, all four `*.sbatch` patched; copies on the stick (HPC_SCRIPTS, HPC_SCRIPTS_PY) and transfer folder HPC_TRANSFER with the two run-2 T1.

## Trägt nicht
- Whether recon-all 8.2.0 also fails on the ND image is untested (the ND copy is only a fallback).

## Bruchindikator
- Any `recon-all.log` whose first `mri_convert` input is not a `*_T1w.nii.gz`.
- A session id occurring twice in `lists/sessions.tsv`, or `-i` pointing outside `anat/`.

## Ablesung
- 2026-10-30: own check, FS 8.1.0 vs 8.2.0 on 47 shared sessions; input audit of 50 pilot `recon-all.log` files (Tier: own data).
- Slurm logs `log/reconall_<array>_<idx>.out`, `sacct` (FAILED 1:0, 52-88 min), user-pasted terminal output 13.10.2026 (Tier: own data).
- FreeSurfer recon-all documentation on `-FLAIRpial` (https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all), FreeSurfer 8.1.0 module on the Charité HPC.

## Verknüpft
- [demdas-pipeline-protocol-v1](../findings/demdas-pipeline-protocol-v1.md)
