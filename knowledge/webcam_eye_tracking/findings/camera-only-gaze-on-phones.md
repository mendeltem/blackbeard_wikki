---
id: camera-only-gaze-on-phones
typ: befund
status: vorschlag
thema: knowledge/webcam_eye_tracking
stand: 2026-10-21
herkunft: Claude (Alita), literature check 2026-10-21 and own app mendeltem/camera-eye-tracker (fce963a)
verweist_auf: []
---

# Camera-only gaze on a phone: about 2-3 cm with landmark features and a per-person regression

## Aussage
Gaze from the normal front camera, in the browser, lands around 2-3 cm of error on a phone after a short calibration
(own estimate from the studies below, not measured on a real phone yet). Trained CNNs with heavy personal calibration
reach 0.5 cm, but only with large training sets and outlier users removed. The method that runs as a static page:
MediaPipe Face Landmarker (iris points), iris offset measured in each eye's own frame, head pose and face position as
extra features, ridge regression with lambda chosen by leave-one-dot-out cross-validation, One Euro smoothing,
blink frames skipped, held-out test dots scored before they join the training set.

| Study | Setup | Reported error |
|---|---|---|
| Krafka 2016, CVPR, arXiv:1606.05814 | phone, iTracker CNN, with calibration | 1.34 cm (1.71 cm without) |
| Valliappan 2020, Nat Commun 11:4553, doi:10.1038/s41467-020-18360-5 | phone on a stand, CNN fine-tuned per person | 0.46 cm; hand-held 0.50 cm |
| Papoutsaki 2016, IJCAI-16 3839-3845 | laptop, WebGazer ridge on eye patches | 4.17 deg in the lab |
| Semmelmann 2018, Behav Res Methods 50:451, doi:10.3758/s13428-017-0913-7 | desktop, WebGazer online | 207 px, 18 % of the screen |
| Davalos 2025, arXiv:2508.19544 (WebEyeTrack) | browser, few-shot model | 2.32 cm on GazeCapture, drifts over 20 min |
| Kaduk 2023, Behav Res Methods, doi:10.3758/s13428-023-02237-8 | desktop, vendor system, 120-point calibration, head guard | 1.4 deg |
| Heck 2023, HICSS-56 6820-6829, hdl:10125/103459 | review of 16 webcam trackers | gains small beyond about 4 calibration points; head motion, light, glasses cost most |

## Trägt
A browser demo or study that only needs which third of a phone screen someone looks at (three large targets, dwell
selection), no installation, nothing uploaded. Camera position is free: features in the eye's own frame plus head pose
let the calibration learn where the camera sits.

## Trägt nicht
Reading single words, small targets, long sessions without recalibration (drift), glasses with reflections, dark
rooms, a phone turned after calibration. WebGazer code is GPL-3.0 and GazeCapture data is research-only: do not copy
either into an MIT repo.

## Bruchindikator
The app's own test-dot error on a real phone well above 20 % of the screen diagonal in good light, or a study showing
landmark-plus-ridge on phones far worse than 3 cm.

## Ablesung
Live: https://mendeltem.github.io/camera-eye-tracker/ (2026-10-21). Headless Chromium with a fake camera passes the
whole chain (10/10 steps, also against the live site); the test cannot measure accuracy because a still photo does
not follow the dots. Real-phone error: not measured yet.
