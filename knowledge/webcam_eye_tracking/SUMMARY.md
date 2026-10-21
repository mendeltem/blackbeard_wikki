# webcam_eye_tracking: Kurzstand

Stand 2026-10-21. Prefill for chats and agents. Details in [INDEX.md](INDEX.md).

**Camera-only gaze on phones (vorschlag):** about 2-3 cm error is realistic with MediaPipe iris landmarks, head pose
and a per-person ridge regression after a 9-dot calibration; trained CNNs with personal fine-tuning reach 0.5 cm
(Valliappan 2020), WebGazer about 4 deg on laptops (Papoutsaki 2016). Enough for three large targets, not for words.
Live app: https://mendeltem.github.io/camera-eye-tracker/. Real-phone error not measured yet.

**Offen:** measure the test-dot error on a real Android and iPhone.

**Lesen bei:** eye tracking, gaze, Blickverfolgung, webcam, front camera, MediaPipe, iris, WebGazer, calibration.
