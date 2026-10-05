# local_llm_operation: Kurzstand

Stand 2026-10-06. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Lokale Modelle auf Victus (RTX 4070 8 GB, Qwen3.6-35B-A3B). Zahlen nicht übertragbar ohne Nachmessen.

**Getragen:** MoE-Offloading `-ngl 99 -ncmoe N`, 19,4 t/s unter Windows 10. Needle-Treffer bis 125k Token, `num_ctx 131072` passt in den RAM. Ollama kuerzt zu lange Prompts stumm auf 32k, das Modell antwortet dann falsch und sicher. `-np 1`, Historie nie umschreiben. Zählen braucht Thinking (Faktor 20). Regellisten im System-Prompt lassen kleine Modelle ablehnen. Prefill und Decode getrennt messen. Größe aus Tensortabelle, nicht aus Metadaten.

**Vorschlag:** Ubuntu statt Windows 10 mit gleichen Flags 29,5 t/s Decode und 500 t/s Prefill (Version nicht gleich). Hermes Agent mit lokalem Qwen loest abgegrenzte Aufgaben, Schwaechen bei Format und Rueckfragen. Hermes gibt Programmieraufgaben lokal an OpenCode ab (160 s), kein zweiter Slot. Vor jeder Messung fremde GPU-Prozesse pruefen (Prefill 30 statt 397 t/s). `opencode run` haengt ohne `</dev/null`. Laya als Weiche vor dem Agenten: 24/30, 0,1 s als Dienst, als Tool im Agenten kein Gewinn. Schlanker Hermes (`-t terminal,file --ignore-rules`) halbiert den Prompt. Nous-Repo hermes-agent-self-evolution faellt stumm von GEPA auf MIPROv2 zurueck.

**Offen:** mmap gegen `--load-mode none`. Dichtes Qwen3.8-27B gegen das MoE auf 8 GB (geschaetzt 5-8 gegen 30-35 t/s). Wie viel Thinking Routineaufgaben brauchen. Minimaler Harness (Pi, unter 1000 Token) gegen OpenCode.

**Lesen bei:** llama.cpp, Ollama, Hermes Agent, OpenCode, lokale LLMs, VRAM, Quantisierung, langer Kontext, Linux gegen Windows, Router, Laya, Jev, Agenten-Harness.
