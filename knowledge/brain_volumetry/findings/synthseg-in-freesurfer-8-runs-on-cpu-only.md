---
id: synthseg-in-freesurfer-8-runs-on-cpu-only
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-12
herkunft: DEMDAS full cohort compute planning, 12.10.2026 (Alita)
verweist_auf: [longitudinal-volumetry-needs-error-statistics, cohort-copies-need-a-gzip-sweep]
---

# SynthSeg inside FreeSurfer 8.2 runs on the CPU only; plan 85 s per session with --robust

## Aussage
`mri_synthseg` in FreeSurfer 8.2.0 uses the bundled fspython with TensorFlow 2.13.1 built WITHOUT GPU support
(`tf.config.list_physical_devices('GPU')` returns `[]` on a machine with a working CUDA 12.4 torch). Measured on a 24-core
workstation: `--parc --robust --cpu --threads 6` takes about 85 s per 1 mm MPRAGE, plus about 20 s model load per call. Running
batches of 40 images as a folder (`--i <folder> --o <folder>`) loads the model once per batch. Three batches in parallel (about
10 GB RAM each) give about 1652 sessions in 13-15 h on one workstation, with no GPU needed, so a local LLM can keep the GPU.
FreeSurfer 8.2 `recon-all -all` measured 40-48 min per session with `-openmp 4`, 3 in parallel, peak RAM 17-28 GB per run
(mri_synthseg / mri_synthmorph stages); the literature figure of 4-7 h per recon-all is for FreeSurfer 6/7.

## Traegt
Compute plans for cohorts of 1000+ sessions on single workstations; the choice between SynthSeg-in-FreeSurfer and a standalone
SynthSeg/FastSurfer with GPU; the decision not to stop a local LLM server for a SynthSeg batch.

## Traegt nicht
Standalone SynthSeg (own TensorFlow with CUDA) and FastSurfer (PyTorch) -- both use the GPU; FreeSurfer versions other than 8.2.0.

## Bruchindikator
A FreeSurfer release whose fspython lists a GPU, or a measured --robust time far from 85 s on comparable hardware.

## Ablesung
12.10.2026 16:36 fspython TF check; 16:29 Clara's 2-session ND test (85 s each); 16:40 one-image smoke test of the batch script
(71 s incl. load); recon-all times from alle.log 12.10. (5 sessions, 40-48 min).

## Verknuepft
- [longitudinal-volumetry-needs-error-statistics](../rules/longitudinal-volumetry-needs-error-statistics.md)
- [cohort-copies-need-a-gzip-sweep](../rules/cohort-copies-need-a-gzip-sweep.md)
