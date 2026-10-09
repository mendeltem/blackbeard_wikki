# local_llm_operation

Betrieb eines lokalen Sprachmodells auf eigener Hardware: was auf eine zu kleine
Karte passt, wie man es misst, und woran kleine Modelle zuverlaessig scheitern.

Alle Zahlen stammen von **Victus** (RTX 4070 Laptop 8 GB, Ryzen 7 7840HS,
31,3 GB RAM, Qwen3.6-35B-A3B). Bis 2026-08-29 unter Windows 10 mit UD-IQ4_XS und
llama.cpp b10603; ab 2026-10-03 unter Ubuntu 26.04 mit llama.cpp b11379 und Ollama.
Nicht auf andere Maschinen uebertragbar ohne Nachmessen.

| Typ | Eintrag | Inhalt |
|---|---|---|
| mechanismus | [moe-expert-offloading](mechanisms/moe-expert-offloading.md) | `-ngl` plus `-ncmoe`: ein 35-B-Modell auf 8 GB VRAM, 19,4 t/s |
| mechanismus | [prefix-cache-single-slot](mechanisms/prefix-cache-single-slot.md) | `-np 1`, und warum Prompt-Kompaktierung den Cache zerstoert |
| befund | [rule-lists-make-small-models-refuse](findings/rule-lists-make-small-models-refuse.md) | Eskalationsliste im System-Prompt: 0 auf 100 Prozent nach dem Entfernen |
| befund | [ubuntu-faster-than-windows-same-flags](findings/ubuntu-faster-than-windows-same-flags.md) | Gleiche Flags, Ubuntu statt Windows 10: Decode 19,4 auf 29,5 t/s, Prefill 500 t/s |
| befund | [needle-recall-holds-to-125k](findings/needle-recall-holds-to-125k.md) | 20/20 Needle-Treffer bis 125k Token, Prefill flach bei 330-400 t/s |
| befund | [hermes-agent-local-qwen-benchmark](findings/hermes-agent-local-qwen-benchmark.md) | Hermes Agent + Qwen3.6 lokal: 14 Aufgaben inhaltlich geloest, Schwaechen Format und Rueckfrage |
| befund | [counting-needs-thinking](findings/counting-needs-thinking.md) | Laengen und Anzahlen brauchen Thinking, Kosten Faktor 20 |
| befund | [vendor-sampling-params-no-gain](findings/vendor-sampling-params-no-gain.md) | Sampling-Empfehlung der Modellkarte: 15/15 gegen 15/15 |
| risiko | [dynamic-quants-break-metadata-math](risks/dynamic-quants-break-metadata-math.md) | Groessenrechnung aus Metadaten liegt um Faktor zwei daneben |
| risiko | [ollama-silently-truncates-context](risks/ollama-silently-truncates-context.md) | Prompt ueber `num_ctx`: Ollama behaelt stumm 32k vom Ende, Modell nennt den Koeder |
| regel | [separate-prefill-from-decode](rules/separate-prefill-from-decode.md) | Durchsatz nie ueber die Wanduhr: 0,4 gegen 27,4 t/s |
| befund | [flash-next-177b-moe-on-24gb-card](findings/flash-next-177b-moe-on-24gb-card.md) | 177B-MoE auf 24 GB: Experten im RAM, Tabelle auf der Platte; 8 Laeufe, 127-349 tok/s Prompt, 11-23 tok/s Erzeugung; RAM ist der Engpass, Q2_0 auf CUDA nicht schneller |
| befund | [opencode-against-llama-server-one-slot](findings/opencode-against-llama-server-one-slot.md) | OpenCode 1.18 gegen llama-server per opencode.json (openai-compatible, kein Schluessel); bei einem Slot wartet es hinter dem Agenten und sieht haengend aus |
| befund | [hermes-delegates-to-opencode-locally](findings/hermes-delegates-to-opencode-locally.md) | Hermes gibt Aufgaben an OpenCode ab, lokal, 160 s; kein zweiter Slot fuer qwen35moe |
| risiko | [opencode-run-hangs-on-open-stdin](risks/opencode-run-hangs-on-open-stdin.md) | `opencode run` haengt ohne `</dev/null`, keine Anfrage erreicht das Modell |
| regel | [foreign-gpu-process-before-measuring](rules/foreign-gpu-process-before-measuring.md) | Vergessener `llama-server` auf der GPU: Prefill 30 statt 397 t/s |
| befund | [laya-router-before-agent](findings/laya-router-before-agent.md) | Laya als Weiche vor Hermes/OpenCode/Claude: 24/30, 0,1 s als Dienst, als Tool kein Gewinn |
| befund | [lean-hermes-toolsets](findings/lean-hermes-toolsets.md) | `-t terminal,file --ignore-rules`: 5 648 statt ~13 000 Token Prompt |
| befund | [everyday-tasks-qwen36-vs-qwen35-9b](findings/everyday-tasks-qwen36-vs-qwen35-9b.md) | 20 Alltagsaufgaben: Qwen3.6 20/20 mit Denken, 17/20 ohne; Qwen3.5-9B 13/20 in 31 s, mit Denken 18/20 und dreimal langsamer |
| risiko | [self-evolution-gepa-silently-falls-back](risks/self-evolution-gepa-silently-falls-back.md) | Nous-Repo: `dspy.GEPA` scheitert, stummer Rueckfall auf MIPROv2 |
| risiko | [secure-boot-kernel-update-unloads-nvidia-dkms](risks/secure-boot-kernel-update-unloads-nvidia-dkms.md) | Kernel-Update bei Secure Boot: lokal signiertes DKMS-Modul laedt nicht, GPU weg, kein Log sagt es; Abhilfe signiertes `linux-modules-nvidia`-Paket |
| befund | [guarded-outbound-research-local-first](findings/guarded-outbound-research-local-first.md) | Agent ohne Netz: Waechter sperrt nur eigene Kohorten, Recherche lokal ueber offene Literatur-APIs + 27B (68 s, keine Cloud), Cloud nur auf Zuruf; stiller Aussenweg war einen Monat tot |
| [Lokaler Rechercheschwarm: erster Lauf](findings/local-research-swarm-first-run-2026-10-09.md) | befund | gemessen |
| pruefpunkt | [mmap-vs-load-mode-none](open_checks/mmap-vs-load-mode-none.md) | Lademodus bei Expert-Offloading, ungemessen |
| pruefpunkt | [dense-27b-vs-moe-on-8gb](open_checks/dense-27b-vs-moe-on-8gb.md) | Qwen3.8-27B-Fine-Tunes mit weniger Denken gegen das MoE: geschaetzt 5-8 gegen 30-35 t/s |
| pruefpunkt | [reasoning-effort-for-routine-agent-tasks](open_checks/reasoning-effort-for-routine-agent-tasks.md) | Wie viel Thinking Routineaufgaben im Agenten brauchen, ungemessen |
| pruefpunkt | [minimal-harness-prompt-size](open_checks/minimal-harness-prompt-size.md) | Pi unter 1000 Token Prompt gegen OpenCode 10 879 und Hermes ~13 000 |
| pruefpunkt | [local-stack-landscape-2026-10](open_checks/local-stack-landscape-2026-10.md) | Webrecherche Okt 2026: Modelle fuer 8/24 GB, MTP, `--n-cpu-moe`-Sweep, Router und Waechter, sechs Messungen |
| befund | [decider-4b-matches-knn-on-60-routing-cases](findings/decider-4b-matches-knn-on-60-routing-cases.md) | decider-4b Q4 auf CPU 50/60 gegen kNN 49/60 auf dem Embedding-Server; ab p 0,8 21/21; deutsch besser als englisch; Vorsprung ist Rauschen, Konfidenz ist der Gewinn |
| pruefpunkt | [decision-model-as-profile-orchestrator](open_checks/decision-model-as-profile-orchestrator.md) | Laya/Jev/Arch-Router als Weiche: nur zwischen residenten Zielen (klein/gross/Cloud), nie je Anfrage zwischen exklusiven Profilen; Laya zero-shot 0,36, erst gegen kNN messen |

## Werkzeuge dazu

Die Werkzeuge liegen im Projekt-Repo, nicht hier - Pfade und Messwerte stehen
dort beieinander:
<https://github.com/mendeltem/local_models>

- `tools/detect.py` - rechnet `-ncmoe` aus GGUF-Tensor-Tabelle und freiem VRAM
- `tools/lok.py` - CLI fuer kleine Aufgaben, Batch-Modus, Eskalation per Exit-Code
- `docs/03-model-wiki.md` - welche Aufgabe mit welchen Einstellungen
