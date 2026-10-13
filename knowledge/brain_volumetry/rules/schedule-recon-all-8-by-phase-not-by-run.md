---
id: schedule-recon-all-8-by-phase-not-by-run
typ: regel
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: derived from the recon-all 8.2 phase profile on Alita, 13.10.2026; not yet run as a batch
verweist_auf: [recon-all-8-memory-peak-is-a-15-minute-phase]
---

# Schedule recon-all 8 by phase, not by run

## Aussage
On a single machine, gate recon-all 8.x on the memory-heavy Synth phase (first ~15 min, 26 GB resident),
not on the number of whole runs. Pattern: `recon-all -autorecon1` behind a semaphore of floor((RAM - 10 GB) / 28 GB)
slots, then `-autorecon2 -autorecon3` unrestricted up to cores / threads. Expected gain on a 24-core, 62 GB box:
3.4 to ~7.5 sessions per hour (20 to ~9 days for 1616 DEMDAS sessions), same software, same numbers.
On a cluster, submit one session per array task with the Synth-phase memory as the request (36 GB) and let the
scheduler pack.

## Trägt
- FreeSurfer 8.0 to 8.2 recon-all on CPU; any T1w cohort large enough that days matter.
- Resume semantics stay the same (lh/rh.thickness as the done criterion, stale done-marker removed).

## Trägt nicht
- recon-all 7.x (no heavy phase), FastSurfer (GPU segmentation), machines with RAM >= runs x 28 GB (gate is moot).
- Longitudinal stream (`-long`): base and long steps have their own profile, measure first.

## Bruchindikator
- A batch with the phase gate that still produces OOM kills or no throughput gain over MAX_P=2 on the same box.
- Status moves to "getragen" after the first full batch with measured throughput; to "gebrochen" if the gain is < 1.5x.

## Ablesung
blind until the first phase-gated batch runs; profile in the linked finding.

## Verknüpft
[recon-all-8-memory-peak-is-a-15-minute-phase](../findings/recon-all-8-memory-peak-is-a-15-minute-phase.md)
