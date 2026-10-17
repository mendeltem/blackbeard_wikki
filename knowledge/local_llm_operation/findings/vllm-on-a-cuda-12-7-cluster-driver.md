---
id: vllm-on-a-cuda-12-7-cluster-driver
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-17
herkunft: daily LLM API job (vLLM, Qwen3-14B) set up on the institute SLURM cluster, Alita session 2026-10-16/17
verweist_auf: [hpc-nodes-answer-only-ssh-and-shards-start-at-once]
---

# vLLM from PyPI fails on a CUDA 12.7 cluster driver; the cu129 release wheel plus a CPU torchcodec works

## Aussage
1. The GPU nodes run NVIDIA driver 565.57 (CUDA 12.7). `pip install vllm` (0.31.0) pulls torch 2.13.0+cu130 and fails at
   engine start: "The NVIDIA driver on your system is too old (found version 12070)".
2. The vLLM GitHub release ships a CUDA 12.9 wheel (`vllm-0.31.0+cu129-...whl`); with torch from the PyTorch cu129 index it
   starts on the 12.7 driver (CUDA minor-version compatibility). Not on PyPI: install the wheel URL with
   `--extra-index-url https://download.pytorch.org/whl/cu129`.
3. Second trap: `torchcodec` 0.17.0 from PyPI is a CUDA 13 build; vLLM imports it at start for audio and dies with
   "libnvrtc.so.13: cannot open shared object file". `torchcodec==0.17.0+cpu` (PyTorch cpu index) fixes it; a GPU-free
   import check (`python -c "import vllm.entrypoints.cli.benchmark.main"`) catches it before a GPU job.
4. Measured start (Qwen3-14B bf16, L40S 48 GB): weights 27.5 GiB from NFS in 26 s, torch.compile 37 s (cached afterwards),
   FlashInfer sampling JIT ~80 s once, ready after 4.5 min; KV cache 11 GiB = 72k tokens.
5. `sbatch --test-only` start estimates were useless here: it predicted February 2027 for a 1-CPU 5-min job that started
   at once, and 19:41 for a GPU job that started 15 min later.
6. `pip install` into a conda env without `PYTHONNOUSERSITE=1` reuses and even uninstalls packages in `~/.local`.

## Trägt
Job logs 11217816 (cu130, driver error), 11218248 (cu129, torchcodec error, then ready), 11218051 (cu129 + cpu torchcodec);
probe job in the compute partition.

## Trägt nicht
Other driver versions; newer vLLM releases may ship other variants.

## Bruchindikator
A cluster driver >= 580 (then the PyPI build works), or a vLLM release without a cu12x asset.

## Ablesung
- vLLM GPU installation docs: https://docs.vllm.ai/en/latest/getting_started/installation/gpu/ (checked 2026-10-16)
- vLLM release v0.31.0 assets via https://api.github.com/repos/vllm-project/vllm/releases/tags/v0.31.0 (cu129 wheel listed)
- PyTorch wheel index https://download.pytorch.org/whl/cu129 and /whl/cpu (torchcodec 0.17.0+cpu)
- own runs 2026-10-16 (package llm_api: setup_env.sh, llm_api.sbatch, scrontab 07:00 daily, 14 h)
