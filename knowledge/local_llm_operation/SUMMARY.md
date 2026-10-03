# local_llm_operation: Kurzstand

Stand 2026-10-03. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Lokale Modelle auf Victus (RTX 4070 8 GB, Qwen3.6-35B-A3B). Zahlen nicht übertragbar ohne Nachmessen.

**Getragen:** MoE-Offloading `-ngl 99 -ncmoe N`, 19,4 t/s. `-np 1`, Historie nie umschreiben. Zählen braucht Thinking (Faktor 20). Regellisten im System-Prompt lassen kleine Modelle ablehnen. Prefill und Decode getrennt messen. Größe aus Tensortabelle, nicht aus Metadaten.

**Offen:** mmap gegen `--load-mode none`.

**Lesen bei:** llama.cpp, lokale LLMs, VRAM, Quantisierung.
