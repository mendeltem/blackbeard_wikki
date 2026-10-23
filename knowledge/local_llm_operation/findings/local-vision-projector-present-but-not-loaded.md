---
id: local-vision-projector-present-but-not-loaded
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-21
herkunft: Clara test set 2026-10-21 (Cle profile), tasks T18/T16; machine Alita, RTX A5000; projector test 2026-10-21
verweist_auf: [research-local-llm-for-patient-data-on-24gb-2026-10]
---

# The vision projector works with the served model - but the running service still does not load it

## Aussage
The projector `modelle/mmproj-F16.gguf` (927 MB) matches the served model and produces real image perception. A test
instance started with `--mmproj` on a free port (8010) loaded it as `loaded multimodal model` and answered an image
request with **HTTP 200** and a correct description of a synthetic test image (a large red circle with a black outline
containing a smaller white upright rectangle - all three described). The original defect is therefore **wiring, not
capability**: the file was always the right one, it was simply never passed to the server.

What has *not* changed: the **production** service (`llama-server.service`, port 8000) still starts without
`--mmproj`, so the patient-safe image route via the running service is still not operational as of this date. The
test was run on a separate instance on purpose, so the running service was never touched.

## Trägt
2026-10-21, four independent readings:
1. Architecture match, read from the GGUF headers: base model `general.architecture = qwen35`, projector
   `general.architecture = qwen3vl_merger`. The llama.cpp build in use contains the `PROJECTOR_TYPE_QWEN3VL` path
   (`tools/mtmd/clip.cpp`, `tools/mtmd/models/qwen3vl.cpp`), so the pair is supported.
2. The projector loads and llama.cpp recognises the pairing: `load_hparams: Qwen-VL models require at minimum 1024
   image tokens ...` - the VL code path is active, not skipped.
3. Server log of the test instance: `srv load_model: loaded multimodal model, 'modelle/mmproj-F16.gguf'`, then
   `listening on http://127.0.0.1:8010`.
4. End-to-end request: HTTP 200 with a description that matches the drawn shapes and colours; slot timings show
   `prompt eval ... / 324 tokens` (the image tokens were encoded) and 110 completion tokens.

## Trägt nicht
Also untested: image quality on real modality data (small lesions, faint WMH) rather than a synthetic drawing, and
whether the local stack keeps the image on the machine end to end. Concurrent use is untested: the measurements below
leave only ~1.6 GB free, so a second GPU-hungry job alongside the vision server would fail.

## Produktionskonfiguration nachgemessen (2026-10-21)
A second test instance on port 8011 used the **production** profile verbatim (`--ctx-size 81920`, `--n-gpu-layers 99`,
projector on CPU) and answered the same synthetic image with **HTTP 200** and a correct description ("a large red
circle with a black border on a light grey background contains a white rectangle with a black border at the bottom
centre"). VRAM held stable at **22492 MiB used / 1613 MiB free**, 52 C, 1 % utilisation, **zero** errors in the log
across the request. Image encoding took 2226 ms for 284 prompt tokens. So vision and the full 80k context coexist -
but the margin is thin, see the cost note.

## Bruchindikator
The production `llama-server.service` gains an `--mmproj` argument and an image sent to port 8000 returns a description
instead of HTTP 500. Or the reading above stops reproducing: the projector no longer loads, or the description does
not match the drawn image.

## Ablesung
- projector: `modelle/mmproj-F16.gguf`, 927,607,488 bytes; header architecture `qwen3vl_merger`
- base model: `modelle/Qwen3.8-27B-UD-Q4_K_M.gguf`; header architecture `qwen35`
- build support: `system/llama.cpp/tools/mtmd/clip.cpp` -> `case PROJECTOR_TYPE_QWEN3VL`; binary `llama-mtmd-cli` and
  `libmtmd.so` are built
- test instance log: `/tmp/vtest_server.log` -> `loaded multimodal model` + `listening on ...:8010`
- synthetic test image: `/tmp/vtest_synth.png` (drawn locally, no patient data)
- production startup script: `system/start.sh` -> `exec "$SERVER" ...` has no `--mmproj`; registry entries carry an
  `args` list that is appended via `REG_ARGS`, which is the natural place for a per-model projector
- prior reading (defect): `~/cle-arbeit/clara-pruefstand/ERGEBNIS.md` (2026-10-21)

## Kostenhinweis (VRAM)
Measured on the test instance (8k context, projector on CPU): the process held **16178 MiB**, remaining free 6293 MiB,
GPU 51 C at 1 % utilisation. The projector itself is 927 MB; the figure above is dominated by the 27B weights, not by
the projector. The production profile declares `braucht_mib` around 21500 for a full 80k context - before enabling
vision there, the context length is the lever, not the projector: an 80k KV cache plus image tokens is what threatens
the OOM that killed an earlier training run. Reduce context or accept a separate vision instance.

## Fallstrick bei der Kartenspuren-Auslesung
A fluttering VRAM band (here: 1624 MiB floor, spikes to ~2154 MiB every 15-30 s) is **not** evidence that the served
model wakes. On 2026-10-21 that pattern was produced by an unrelated short-lived CUDA context (a local PyTorch
measurement loop), while the 27B server had last written to its log 8 minutes earlier. A plain torch allocation moves
the same 1624 -> 1888 MiB and releases it on exit. Before blaming a service, compare the times: the server log's last
write must fall inside the fluttering window.
