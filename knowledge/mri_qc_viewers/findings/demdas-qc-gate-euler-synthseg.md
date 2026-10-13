---
id: demdas-qc-gate-euler-synthseg
typ: befund
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-12
herkunft: wd4 DEMDAS automated QC gate (Alita, demdas-gm/qc_gate.py, fehler_statistik.py, gm_qc_axial.py, FreeSurfer 8.2.0 mris_euler_number, mri_synthseg --qc), user request 12.10.2026 "automated QC gate per session, DEMDAS priority one"
verweist_auf: [qc-pages-explain-every-number-on-hover, qc-pages-english-sessions-in-one-window, demdas-cortical-thickness-qc-page]
---

# DEMDAS automated QC gate: Euler number + SynthSeg QC score per session

## Aussage

Every DEMDAS session is now scored automatically by a two-part quality gate
(`demdas-gm/qc_gate.py` -> `derivatives/demdas/gm_beispiel/qc_gate.csv`, one row per
BIDS session with a T1w). The gate combines

1. the **Euler number** of the FreeSurfer cortical surface reconstruction, and
2. the **SynthSeg segmentation QC score**.

A session is **FLAGGED** when either part fails; otherwise it is **PASS**. Flagged
sessions are excluded from a second, parallel set of error statistics
(columns `*_qc` on the volume-trend error page) so that the *effect of the gate* on
SDC95/ICC and longitudinal noise is directly visible.

**Why the Euler number.** The Euler number of a surface counts its topological holes:
`holes = (2 - Euler)/2` per hemisphere. A clean, fully closed cortical surface has
Euler = 2 and 0 holes; any defect, artefact or failed reconstruction step leaves a
hole, so a *more negative* Euler number means a more defective surface. Rosen et al.
(2018, *NeuroImage* 172:292-299, "Automated QC of FreeSurfer surface reconstruction")
showed that the Euler number is the **best automated correlate of a visual QC
judgement** of cortical surfaces, and that the cutoff is **study-internal** rather than
a universal constant. We therefore do not hard-code a cutoff: it is derived from the
cohort itself (below).

**Cohort cutoff (derived, not fixed).** Over the finished recon-all sessions the
cutoff is the lower Tukey fence of `euler_mean` (the mean of the left and right
hemisphere Euler numbers): `Q1 - 1.5 * IQR`. With the current cohort (55 finished
recon-all sessions of 64) the cutoff is **-107.75** (snapshot); a session is flagged on
Euler when
its `euler_mean` falls below it. In this cohort the fence sits at −107.75 (snapshot
2026-10-12) and one session (euler_mean −108) fell below it; that session also fails the
SynthSeg arm. The Euler arm is in place and will fire as defective reconstructions
appear.

**SynthSeg QC score.** `mri_synthseg --qc` predicts, for each tissue/structure, a
quality score in [0, 1] (how well the segmentation matches what the network expects;
higher = better). `synthseg_qc_min` is the **minimum over all structure columns** of
`seg/<id>_qc.csv` (the weakest tissue for that session). The gate flags a session when
`synthseg_qc_min < 0.65`. **0.65 is a working threshold** chosen to match the existing
manual QC practice on this dataset; it is to be **confirmed against the SynthSeg
README / the published `--qc` semantics** before it is treated as a fixed standard.

**Cohort result (2026-10-12, snapshot).** 64 sessions; 55 with a finished reconstruction
(Euler available), 9 still in recon-all (Euler empty, `recon_all_finished = 0`).
**28 of 64 sessions are FLAGGED** (27 by `synthseg_qc_min < 0.65` alone, 1 by both
`synthseg_qc_min < 0.65` and `euler_mean` below the fence); **36 PASS**. The flagged set
is dominated by low-SynthSeg-QC sessions; these are exactly the sessions a reviewer would
want to inspect first. The cutoff moves slightly as recon-all finishes more sessions
(cohort-internal statistic), so the exact number of Euler flags can change between runs.

**Where it is shown.**
- `demdas-gm/qc_gate.py` writes `derivatives/demdas/gm_beispiel/qc_gate.csv`
  (columns: subject, session, months, euler_lh, euler_rh, euler_mean, holes_mean,
  synthseg_qc_min, synthseg_qc_gm, synthseg_qc_wm, synthseg_qc_csf, recon_all_finished,
  flag_euler, flag_synthseg, flag_any). Idempotent; Euler results are cached so reruns
  are fast and recon-all progress is picked up on the next run.
- Error statistics page (`QUALITY_CONTROLL/DEMDAS/volumenverlauf/error_statistics.html`),
  section 4 "QC gate": histogram of `euler_mean` with the cutoff line, scatter
  `euler_mean` vs `synthseg_qc_min`, and the table of flagged sessions; test-retest and
  longitudinal sections carry the QC-passed subset as extra `*_qc` columns.
- GM axial QC page (`QUALITY_CONTROLL/DEMDAS/gm_beispiel_qc/index.html`): two new rows
  in the Session box, "Euler number (lh/rh)" and "QC gate" (PASS / FLAGGED: reason).
- Excel: sheet `QC_gate` in `DEMDAS_GM_Beispiel.xlsx` (and `error_statistics.xlsx`).

**Limits.** The Euler number is only defined once recon-all has finished the surface
steps; early sessions therefore carry an empty Euler and `recon_all_finished = 0` and
are **not** flagged on Euler (they are judged by SynthSeg alone when a segmentation
exists). The gate is a triage aid, not a replacement for a visual check: a PASS means
"nothing automated objected", a FLAG means "look at this one". The SynthSeg threshold
0.65 is provisional (see above). All numbers are cohort-level; no participant
identifiers are published on the QC pages.

**References.**
- Rosen B.R. et al. (2018). Automated QC of FreeSurfer surface reconstruction. NeuroImage 172:292-299.
- SynthSeg: Maffei et al. (2018), and the `mri_synthseg --qc` documentation (threshold to be confirmed against the README).
