# local_llm_operation: Kurzstand

Stand 2026-10-06. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Lokale Modelle auf Victus (RTX 4070 8 GB, Qwen3.6-35B-A3B). Zahlen nicht übertragbar ohne Nachmessen.

**Getragen:** MoE-Offloading `-ngl 99 -ncmoe N`, 19,4 t/s unter Windows 10. Needle-Treffer bis 125k Token, `num_ctx 131072` passt in den RAM. Ollama kuerzt zu lange Prompts stumm auf 32k, das Modell antwortet dann falsch und sicher. `-np 1`, Historie nie umschreiben. Zählen braucht Thinking (Faktor 20). Regellisten im System-Prompt lassen kleine Modelle ablehnen. Prefill und Decode getrennt messen. Größe aus Tensortabelle, nicht aus Metadaten.

**Vorschlag:** Ubuntu statt Windows 10 mit gleichen Flags 29,5 t/s Decode und 500 t/s Prefill (Version nicht gleich). Hermes Agent mit lokalem Qwen loest abgegrenzte Aufgaben, Schwaechen bei Format und Rueckfragen. Hermes gibt Programmieraufgaben lokal an OpenCode ab (160 s), kein zweiter Slot. Vor jeder Messung fremde GPU-Prozesse pruefen (Prefill 30 statt 397 t/s). `opencode run` haengt ohne `</dev/null`. Laya als Weiche vor dem Agenten: 24/30, 0,1 s als Dienst, als Tool im Agenten kein Gewinn. Schlanker Hermes (`-t terminal,file --ignore-rules`) halbiert den Prompt. Nous-Repo hermes-agent-self-evolution faellt stumm von GEPA auf MIPROv2 zurueck. 20 Alltagsaufgaben ueber die API: Qwen3.6 mit Denken 20/20 (Median 21 s), ohne 17/20; Qwen3.5-9B ohne Denken 13/20 bei 0,6 s Median, mit Denken 18/20 und dreimal langsamer als Qwen3.6. Ollama-Standardkontext 4096 schneidet auch Denkteile ab.

**Offen:** mmap gegen `--load-mode none`. Dichtes Qwen3.8-27B gegen das MoE auf 8 GB (geschaetzt 5-8 gegen 30-35 t/s). Wie viel Thinking Routineaufgaben brauchen. Minimaler Harness (Pi, unter 1000 Token) gegen OpenCode. Webrecherche Oktober 2026 (fast nur Herstellerzahlen): sechs Messungen zu `--n-cpu-moe`-Sweep, MTP, KV-Cache, Prefix-Cache, Laya gegen Arch-Router/kNN, Shell-Waechter.

**Lesen bei:** llama.cpp, Ollama, Hermes Agent, OpenCode, lokale LLMs, VRAM, Quantisierung, langer Kontext, Linux gegen Windows, Router, Laya, Jev, Agenten-Harness, MTP, Speculative Decoding, Guard, Modellwahl 8/24 GB.

**Auf den Seiten:** Karten der Gruppe „KI am lokalen Arbeitsplatz“: [lokale Sprachmodelle](https://mendeltem.github.io/ai_use_cases_overview/#uc=local-language-models), [Offline-Coding](https://mendeltem.github.io/ai_use_cases_overview/#uc=offline-coding-website-building), [lokales Fine-Tuning](https://mendeltem.github.io/ai_use_cases_overview/#uc=local-fine-tuning-of-open-models), [private Wissensbasis](https://mendeltem.github.io/ai_use_cases_overview/#uc=private-knowledge-base-over-your-own-files).

**Risiko, neu 2026-10-07 (Alita, 24 GB):** Ein Kernel-Update nimmt bei Secure Boot den NVIDIA-Treiber mit, wenn der lokale MOK-Schluessel nicht eingetragen ist; der Modellserver steht dann still, ohne dass ein Log den Treiber nennt. Vor dem Neustart `dkms status` und `mokutil --list-enrolled` pruefen; Abhilfe `apt install linux-modules-nvidia-<treiber>-<kernel>-generic`.

**Befund, neu 2026-10-07 (Alita):** OpenCode laeuft gegen llama-server allein ueber `opencode.json` (openai-compatible, baseURL, Modell-ID wie in /v1/models). Mit `--parallel 1` wartet es hinter einem laufenden Agenten und wirkt haengend; `curl /slots` zeigt den belegten Slot.

**Befund, neu 2026-10-07 (Alita):** Ein 177B-MoE (Flash-Next GSQ-RCO) laeuft auf 24 GB mit `--n-cpu-moe`, mmap und `--lazy-mode on`: 5,5 bis 6,7 GB VRAM bei allen Experten im RAM, 127 bis 251 tok/s Prompt, 11 bis 15 tok/s Erzeugung; mit 16 Schichten auf der Karte 17 bis 24 GB VRAM und 20 bis 23 tok/s. RAM (RSS plus Seitencache ~60 von 62 GB) ist der Engpass; neben einem Training bleibt nur IQ2_XS. Kurze Prompts taeuschen beim Tempo, Q2_0 ist auf CUDA langsamer als IQ2_XS.
