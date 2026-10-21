---
id: moving-after-calibration
typ: befund
status: vorschlag
thema: knowledge/webcam_eye_tracking
stand: 2026-10-21
herkunft: Claude (Alita), own app mendeltem/camera-eye-tracker (b1c666a, 5f6e037), geometry and a toy simulation; user observation 2026-10-21 that the phone had to stay still
verweist_auf: [camera-only-gaze-on-phones]
---

# Moving head or phone after calibration: fix the features and calibrate with movement, not the gyroscope

## Aussage
A per-person regression fitted while head and phone stay still breaks when either moves, because its weights for
head pose and face position were fitted on a tiny spread and a move multiplies them by values far outside it. Four
parts address this without a trained network:

1. **Iris offset along the image axes, not in the eye's own frame.** The iris sits in front of the eyeball centre,
   so its image offset measures the angle between the gaze and the eye-to-camera line. To first order this stays
   constant when the head moves or turns while the eyes hold a screen point, and it rotates with the screen when the
   head rolls, as the gaze point does. The eye-frame offset used before turns with the head and is wrong under roll.
2. **A movement phase in the calibration**: about 5 s with the eyes on one dot while the head turns left, right, up
   and down. These frames teach the fit which feature changes (lids, blendshapes, pose) do not move the gaze point.
   Features are held within the calibrated range plus one standard deviation.
3. **Distance from the iris size.** The visible iris is 11.7 ± 0.5 mm wide across a wide population (Vakunov & Lagun
   2020, Google Research blog, 2020-08-06, https://research.google/blog/mediapipe-iris-real-time-iris-tracking-depth-estimation/;
   4.3 % mean relative depth error against an iPhone depth sensor). The gaze offset from the camera scales with the
   distance, so predictions are scaled by iris size at calibration / iris size now.
4. **The slow offset as a Kalman state** (Kalman 1960, J Basic Eng 82(1):35-45, doi:10.1115/1.3662552): a random walk
   whose variance grows with time and with the pose change since the last correction. A tap where the user looks is
   the measurement; after a large move the app shows a centre dot to look at and tap.

The phone gyroscope does not help here: it measures the phone turning in the room, while the gaze point depends on
the phone relative to the head, which the camera already sees. Walking with the phone held still in front of the
face reads as movement, and iOS needs an extra permission. A Kalman filter helps for drift, and for jitter only as
much as the One Euro filter already does.

## Trägt
Hand-held phone use with small head and grip changes after one calibration. In a toy simulation that follows the
geometry above (tests/gaze.test.mjs), after a head turn the error stays at the still error with the movement phase
(about 1 % of the screen) and grows to about 28 % of the screen without it.

## Trägt nicht
Not measured on a real phone yet; the toy simulation only confirms the mechanism under its own assumptions. The
eye-corner midpoint is not the eyeball centre, so large head turns leave a parallax error. One offset serves the whole
screen and every pose. Turning the phone between portrait and landscape still needs a new calibration.

## Bruchindikator
On a real phone, the test-dot error or tap errors after a deliberate head turn of about 10 degrees grow as much with
the new calibration as with the old one (compare via the app's data export).

## Ablesung
App 5f6e037 live at https://mendeltem.github.io/camera-eye-tracker/ (2026-10-21): unit tests 18/18, headless browser
test 12/12 locally, from a fresh clone and against the live site. The result card offers "Save the data" (features,
targets, times; no picture) so model variants can be compared on a real calibration.
