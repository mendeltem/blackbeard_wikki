---
id: kromoss-text-to-image-install-on-24gb-card
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-20
herkunft: Alita (RTX A5000 24 GB, driver 550 = CUDA 12.4, 62 GB RAM), install 2026-10-20; no image generated yet
verweist_auf: [gpu-lock-dies-with-its-job, model-server-start-checks-card-and-picks-profile]
---

# Kromoss (5B text-to-image) installs on a 24 GB card with torch 2.9 cu126, but bf16 weights need CPU offload

## Aussage
Kromoss (lodestones, Apache-2.0) is a full fine-tune of MOSS-Image-Base at 1024 px: a 5B diffusion transformer
(42 blocks, width 3072), Qwen3.5-9B as text encoder and the small FLUX.2 VAE; an 8-step DMD2 LoRA is the recommended
fast path (8 steps, CFG 1). Install facts from 2026-10-20:
- The repo carries two layouts of the same weights: diffusers folders (transformer 10.2 GB, text encoder 16.8 GB, VAE
  0.25 GB) and ComfyUI single files (35 GB more, including an int8 ConvRot DiT of 5.4 GB). Download one layout with
  include patterns: about 28 GB with the LoRA instead of about 64 GB.
- `hf download` with one `--include` followed by several patterns fetched only part of them; one `--include` per
  pattern, or named files, worked (cause not checked).
- Loading needs `trust_remote_code` / `custom_pipeline` (one file, three identical copies). Read before running: it
  imports only torch, diffusers and transformers, with no network, subprocess or pickle loading.
- It needs torch >= 2.9. The cu126 wheel (torch 2.9.1) runs on a CUDA 12.4 driver: CUDA available, pipeline imports
  (with diffusers 0.41, transformers 5.20).
- bf16 transformer plus text encoder is about 27 GB, more than the card. The pipeline declares a CPU offload order
  (text encoder, transformer, VAE), so the encoder can leave the card before denoising; the ComfyUI int8 file is the
  other way down.

## Traegt
A local install next to other GPU users when the card is free for the run (take the GPU lock, stop the language model
server for the run).

## Traegt nicht
- Not measured yet: time per image, peak VRAM with offload, image quality. The vendor's only numbers are CLIP scores
  on 100 PartiPrompts (27.90 at 50 steps, 28.13 with the DMD2 LoRA at 8 steps, base 27.19).
- Running beside a loaded 27B language model (21 GB): no room.

## Bruchindikator
CUDA out of memory at 1024 px with model CPU offload and the 8-step LoRA: then try the int8 ConvRot weights or
sequential offload.

## Ablesung
- lodestones, Kromoss model card, https://huggingface.co/lodestones/Kromoss (accessed 2026-10-20): architecture,
  layouts, LoRAs, recommended settings, PartiPrompts CLIP scores, Apache-2.0.
- OpenMOSS-Team, MOSS-Image-Base, https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base (accessed 2026-10-20): base
  text-to-image model, about 5B parameters, Apache-2.0, technical report arXiv:2610.23374 (not opened).
- Own install on Alita 2026-10-20: file sizes from the Hub API matched the download; CUDA and import check passed.
