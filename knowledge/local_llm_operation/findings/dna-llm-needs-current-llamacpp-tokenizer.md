---
id: dna-llm-needs-current-llamacpp-tokenizer
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-11-04
herkunft: Install of Carbon-X on Alita 2026-11-04 (RTX A5000 24 GB, i9-12900K); model card read the same day
verweist_auf: [moe-expert-offloading]
---

# A DNA language model (Carbon-X) needs a current llama.cpp build; older builds tokenize DNA wrongly

## Aussage
1. Carbon-X (HuggingFaceBio, 14.8B, based on Qwen3-14B, DNA plus English, Apache 2.0) ships official GGUF files;
   Q8_0 (15.8 GB) is the recommended one, Q4_K_M 9.6 GB. The model card says llama.cpp from build b11742 is required,
   older builds tokenize DNA incorrectly. Our August builds were too old; a fresh CUDA build (sm_86) from the
   llama.cpp main branch of 2026-11-04 (commit 5851a8e) loads it.
2. Q8_0 fits a 24 GB card only when it is nearly free (about 17 GB needed); with a training run on the card it runs on
   the CPU: 2.3 tok/s with 6 threads (own measurement, 2026-11-04).
3. Smoke test: reverse complement of ATGCGTAC answered correctly (GTACGCAT); the model wraps sequences in `<dna>` tags.
   Use `chat_template_kwargs: {"enable_thinking": false}` to match the card's evaluation setup.

## Trägt
One install, one smoke question. No benchmark of biological accuracy.

## Trägt nicht
Variant-effect or pathogenicity claims; the card's own evaluations were not repeated.

## Bruchindikator
Odd or split DNA tokens in answers: check the llama.cpp build first.

## Ablesung
Sources: model card https://huggingface.co/HuggingFaceBio/Carbon-X and GGUF card https://huggingface.co/HuggingFaceBio/Carbon-X-GGUF (read 2026-11-04); llama.cpp https://github.com/ggml-org/llama.cpp (commit 5851a8e). Genetic data is sensitive: only public or synthetic sequences unless cleared.
