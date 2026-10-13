---
id: recon-all-8-memory-peak-is-a-15-minute-phase
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: DEMDAS GM line on Alita, recon-all logs of 89 finished sessions (bids/demdas, FreeSurfer 8.2.0), 13.10.2026
verweist_auf: [synthseg-in-freesurfer-8-runs-on-cpu-only, schedule-recon-all-8-by-phase-not-by-run, demdas-segmentation-method-benchmark-wd6]
---

# recon-all 8.2: the memory peak is a 15-minute phase, not the whole run

## Aussage
A FreeSurfer 8.2.0 `recon-all -all` run on a DEMDAS T1w needs its memory only at the start.
Measured in `scripts/recon-all.log` of finished sessions (sub-PDDISDJ1V39UH6_ses-M0 as the profiled case):

| phase | wall time | memory |
|---|---|---|
| MotionCor + SynthStrip + SynthSeg + SynthMorph (affine x2, deform) | first ~15 min (16:14 to 16:30) | SynthSeg VmPeak 43 GB virtual, 26 GB resident; SynthMorph deform VmPeak 20 GB |
| Nu correction to surfaces, registration, parcellation | remaining ~50 min | 2 to 4 GB |

Whole-run wall time per session (89 finished runs, 24-core box, 62 GB RAM):

| parallel runs (MAX_P) | threads | mean per session | throughput | outcome |
|---|---|---|---|---|
| 5 | 4 | 29 min | ~10 per h | 174 OOM kills (signal 9), 31 of 61 aborted |
| 3 | 6 | 48 min | 3.75 per h | ran, RAM-bound |
| 2 | 6 | ~36 min (resume run) | ~3.4 per h | stable, half of the 24 cores idle |

Consequence for the full cohort (586 subjects, 1616 sessions, 1652 T1w incl. 40 run-1/run-2 pairs):
sequential on the workstation at MAX_P=2 ~20 days; gating only the 15-minute Synth phase (2 at a time) and
letting 6 to 8 surface phases run beside it gives ~7.5 sessions per hour, ~9 days; stopping the local
LLM server (18 GB RAM) at night allows 3 in the Synth phase, ~6 to 7 days. On a Slurm cluster each
session is an independent task: 36 GB, 4 CPUs, 6 h limit is a safe request; 100 concurrent tasks finish
the cohort in 12 to 15 h wall time.

Also measured: the 24-case example set finished 61 of 65 sessions (4 without usable input progress);
the recon_alle_v2 night run ended 13.10. 00:01 "ENDE: 61/61 fertig".

## Trägt
- recon-all 8.2.0 with the bundled fspython (TensorFlow 2.13 CPU, see linked finding); T1w 1 mm DEMDAS data.
- Per-run memory gates (MIN_GB) measured on this box; numbers transfer to other hosts as a ratio, not as constants.

## Trägt nicht
- recon-all 7.x: no Synth phase, peak 2 to 3 GB, run-count gating is the right model there.
- FastSurfer: the segmentation runs on the GPU in about a minute, the surface part is CPU-bound for 60 to 90 min;
  the thickness is a different method and must be validated against recon-all before mixing.
- Runs with `-no-isrunning` resume: a stale `recon-all.done` makes recon-all skip everything; delete it first
  (handled in recon_alle_v2.sh).

## Bruchindikator
- A profiled run whose VmPeak after the SynthMorph deform step still exceeds 10 GB.
- A FreeSurfer release that moves SynthSeg to the GPU or drops it from recon-all (then the phase disappears).

## Ablesung
Tier 1 (own logs): `derivatives/demdas/freesurfer/alle.log`, `*/scripts/recon-all.log` ("#@# mri_synthseg vmpeak",
"#@# mri_synthmorph ... VmPeak"), `demdas-gm/recon_alle_v2.sh` header (OOM count, MAX_P history).

## Verknüpft
[synthseg-in-freesurfer-8-runs-on-cpu-only](synthseg-in-freesurfer-8-runs-on-cpu-only.md),
[schedule-recon-all-8-by-phase-not-by-run](../rules/schedule-recon-all-8-by-phase-not-by-run.md),
[demdas-segmentation-method-benchmark-wd6](demdas-segmentation-method-benchmark-wd6.md)
