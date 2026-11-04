# local_llm_operation

Betrieb eines lokalen Sprachmodells auf eigener Hardware: was auf eine zu kleine
Karte passt, wie man es misst, und woran kleine Modelle zuverlaessig scheitern.

Alle Zahlen stammen von **Victus** (RTX 4070 Laptop 8 GB, Ryzen 7 7840HS,
31,3 GB RAM, Qwen3.6-35B-A3B). Bis 2026-08-29 unter Windows 10 mit UD-IQ4_XS und
llama.cpp b10603; ab 2026-10-03 unter Ubuntu 26.04 mit llama.cpp b11379 und Ollama.
Nicht auf andere Maschinen uebertragbar ohne Nachmessen.

| Typ | Eintrag | Inhalt |
|---|---|---|
| befund | [research-local-llm-for-patient-data-on-24gb-2026-10](findings/research-local-llm-for-patient-data-on-24gb-2026-10.md) | Literature (25 refs, checked): 4-5 bit plateau, ternary PTQ viable, tool calling is the weak spot, local open-weight models proven for clinical text; medical models not a default |
| befund | [local-vision-projector-present-but-not-loaded](findings/local-vision-projector-present-but-not-loaded.md) | The 927 MB mmproj projector **matches** the served 27B (base `qwen35`, projector `qwen3vl_merger`) and really sees images: a test instance with `--mmproj` returned HTTP 200 and described a synthetic image correctly. The defect is wiring, not capability — the **production** service still starts without `--mmproj`, so port 8000 still answers an image with HTTP 500. VRAM of the test setup measured (16178 MiB at 8k context, projector on CPU); context length, not the projector, is the OOM lever (2026-10-21) |
| befund | [vllm-on-a-cuda-12-7-cluster-driver](findings/vllm-on-a-cuda-12-7-cluster-driver.md) | PyPI vLLM (cu130) dies on driver 565; cu129 release wheel + torch cu129 + torchcodec cpu works; start 4.5 min; sbatch --test-only estimates useless |
| befund | [hospital-model-hub-api-aliases-and-small-benchmark](findings/hospital-model-hub-api-aliases-and-small-benchmark.md) | Hub API OpenAI-compatible, 5 aliases, tool calls ok; 13-task bench clea 100 %, frontier 96 %, fast 92 % (180 tok/s), eu 84 %; reasoning needs max_tokens >= 6000; Bonsai-27B local 92 % in 6.8 GB |
| befund | [pre-tool-hook-blocks-data-paths-for-remote-model](findings/pre-tool-hook-blocks-data-paths-for-remote-model.md) | Hermes pre_tool_call plugin = hard barrier for a remote-model agent (prompt rule = request); enable via plugins.enabled; .nii/sub- redaction too broad for code repos |
| regel | [group-drive-move-ask-what-alita-means](rules/group-drive-move-ask-what-alita-means.md) | "ALITA" is the group drive on the wiki hub, not a folder on the workstation (which is Alita); copy+checksum, 84 % full |
| befund | [clara-cle-agents-solve-bounded-code-tasks-slower](findings/clara-cle-agents-solve-bounded-code-tasks-slower.md) | Claude Code vs Hermes/OpenCode on the hub: bounded code tasks all correct, 6-18x slower; open review: Claude 6 extra real bugs, OpenCode 1, Hermes timeout |
| [local-model-server-runs-only-when-needed](rules/local-model-server-runs-only-when-needed.md) | regel | getragen |
| regel | [remote-model-gets-only-data-free-skills-and-redacted-text](rules/remote-model-gets-only-data-free-skills-and-redacted-text.md) | Shared skills split by data; OpenCode also reads ~/.claude/skills (OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1); Hermes skills.external_dirs; fallback reports redact ids |
| befund | [hpc-nodes-answer-only-ssh-and-shards-start-at-once](findings/hpc-nodes-answer-only-ssh-and-shards-start-at-once.md) | Cluster nodes: only port 22 from the intranet (an API needs a tunnel or gateway); GPU shard starts at once, a whole A100 waited ~9 h; 7 x 80 GB, 20 x 40 GB (2026-10-16) |
| mechanismus | [moe-expert-offloading](mechanisms/moe-expert-offloading.md) | `-ngl` plus `-ncmoe`: ein 35-B-Modell auf 8 GB VRAM, 19,4 t/s |
| mechanismus | [prefix-cache-single-slot](mechanisms/prefix-cache-single-slot.md) | `-np 1`, und warum Prompt-Kompaktierung den Cache zerstoert |
| befund | [rule-lists-make-small-models-refuse](findings/rule-lists-make-small-models-refuse.md) | Eskalationsliste im System-Prompt: 0 auf 100 Prozent nach dem Entfernen |
| befund | [ubuntu-faster-than-windows-same-flags](findings/ubuntu-faster-than-windows-same-flags.md) | Gleiche Flags, Ubuntu statt Windows 10: Decode 19,4 auf 29,5 t/s, Prefill 500 t/s |
| befund | [dna-llm-needs-current-llamacpp-tokenizer](findings/dna-llm-needs-current-llamacpp-tokenizer.md) | Carbon-X (DNA-LLM): llama.cpp ab b11742 noetig, Q8 15,8 GB, CPU 2,3 t/s |
| befund | [needle-recall-holds-to-125k](findings/needle-recall-holds-to-125k.md) | 20/20 Needle-Treffer bis 125k Token, Prefill flach bei 330-400 t/s |
| befund | [hermes-agent-local-qwen-benchmark](findings/hermes-agent-local-qwen-benchmark.md) | Hermes Agent + Qwen3.6 lokal: 14 Aufgaben inhaltlich geloest, Schwaechen Format und Rueckfrage |
| befund | [counting-needs-thinking](findings/counting-needs-thinking.md) | Laengen und Anzahlen brauchen Thinking, Kosten Faktor 20 |
| befund | [vendor-sampling-params-no-gain](findings/vendor-sampling-params-no-gain.md) | Sampling-Empfehlung der Modellkarte: 15/15 gegen 15/15 |
| risiko | [dynamic-quants-break-metadata-math](risks/dynamic-quants-break-metadata-math.md) | Groessenrechnung aus Metadaten liegt um Faktor zwei daneben |
| risiko | [ollama-silently-truncates-context](risks/ollama-silently-truncates-context.md) | Prompt ueber `num_ctx`: Ollama behaelt stumm 32k vom Ende, Modell nennt den Koeder |
| regel | [separate-prefill-from-decode](rules/separate-prefill-from-decode.md) | Durchsatz nie ueber die Wanduhr: 0,4 gegen 27,4 t/s |
| befund | [nemotron-bolt-74b-on-ampere-24gb](findings/nemotron-bolt-74b-on-ampere-24gb.md) | Nemotron 3.5 Bolt 24GB-GGUF laeuft ganz auf der A5000 (Ampere): 66-69 tok/s, 22,2 GB bei 16k, 88,5 % / 96,2 % im 13-Aufgaben-Test bei 1 500 / 4 096 Token; 27B gleicher Tag 100 % / 97,4 % -> 27B bleibt Standard |
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
| pruefpunkt | [local-stack-landscape-2026-10](open_checks/local-stack-landscape-2026-10.md) | Webrecherche Okt 2026: Modelle fuer 8/24 GB, MTP, `--n-cpu-moe`-Sweep, Router und Waechter, sechs Messungen; Nachtrag 23.10.: Nemotron 3.5 Bolt als einziger neuer 24-GB-Kandidat (Ampere ungenannt), DeepSeek-V4.1-Flash zu gross |
| befund | [decider-4b-matches-knn-on-60-routing-cases](findings/decider-4b-matches-knn-on-60-routing-cases.md) | decider-4b Q4 auf CPU 50/60 gegen kNN 49/60 auf dem Embedding-Server; ab p 0,8 21/21; deutsch besser als englisch; Vorsprung ist Rauschen, Konfidenz ist der Gewinn |
| pruefpunkt | [decision-model-as-profile-orchestrator](open_checks/decision-model-as-profile-orchestrator.md) | Laya/Jev/Arch-Router als Weiche: nur zwischen residenten Zielen (klein/gross/Cloud), nie je Anfrage zwischen exklusiven Profilen; Laya zero-shot 0,36, erst gegen kNN messen |
| pruefpunkt | [system-one-decision-layer-for-agent-harnesses](open_checks/system-one-decision-layer-for-agent-harnesses.md) | System One models (Jev, H2O-Lightning-4B, decider-4b, Kev) for model choice, prepared context, tool approval, evaluation in Hermes; local only, measure coverage at 5 % error vs kNN, shadow week first |
| regel | [every-agent-crash-becomes-a-lesson](rules/every-agent-crash-becomes-a-lesson.md) | Jeder Absturz: Kette aus Logs, jeden Fehler benennen, Abhilfe im Code mit Test, Befund im Wiki; Agent wartet statt Fenster zu schliessen |
| befund | [registry-pointed-at-half-a-model-agent-window-died](findings/registry-pointed-at-half-a-model-agent-window-died.md) | flash-Profil zeigte auf 1/2 GGUF-Teile -> Dienst starb -> agent exit -> totes tmux-Fenster; modellstart prueft jetzt alle Teile, agent.sh wartet bei Fehlstart |
| regel | [model-server-start-checks-card-and-picks-profile](rules/model-server-start-checks-card-and-picks-profile.md) | Modellserver nur starten, wenn die Karte Platz hat: Sperre, freier VRAM minus angemeldeter Bedarf des laufenden Laufs, Profil fuer diesen Start; passt nichts, rc 3 statt wartender Dienst |
| regel | [gpu-lock-dies-with-its-job](rules/gpu-lock-dies-with-its-job.md) | GPU lock held by the job itself (kernel flock), with expiry; an expired lock without GPU job for 2 h stops blocking and is reported once |
| befund | [landlock-write-lock-for-a-yolo-agent](findings/landlock-write-lock-for-a-yolo-agent.md) | Landlock write lock without root for an agent with approvals bypassed: 20/20 checks, real run denies writes outside the list; systemd-run without --scope and tmux escape |
| befund | [local-agent-harness-review-2026-10](findings/local-agent-harness-review-2026-10.md) | review against published practice: filesystem sandbox missing under yolo, same-model critic disagrees with checklist (28 % hit the round limit), caching 89 % reuse |
| befund | [hermes-oneshot-ignores-ephemeral-prompt-and-prefill](findings/hermes-oneshot-ignores-ephemeral-prompt-and-prefill.md) | three meanings of prefill; `hermes -z` drops HERMES_EPHEMERAL_SYSTEM_PROMPT and prefill turns, use -s skills; chat mode appends them after the date line |
| befund | [hermes-keeps-every-conversation-in-state-db](findings/hermes-keeps-every-conversation-in-state-db.md) | Hermes writes every message to state.db, no flag turns it off; a no-record session needs a throwaway HERMES_HOME in RAM, guard log stays |
| befund | [kromoss-text-to-image-install-on-24gb-card](findings/kromoss-text-to-image-install-on-24gb-card.md) | Kromoss 5B text-to-image: one weight layout (28 GB), custom pipeline read before use, torch 2.9 cu126 on CUDA 12.4 driver, bf16 needs CPU offload |

## Werkzeuge dazu

Die Werkzeuge liegen im Projekt-Repo, nicht hier - Pfade und Messwerte stehen
dort beieinander:
<https://github.com/mendeltem/local_models>

- `tools/detect.py` - rechnet `-ncmoe` aus GGUF-Tensor-Tabelle und freiem VRAM
- `tools/lok.py` - CLI fuer kleine Aufgaben, Batch-Modus, Eskalation per Exit-Code
- `docs/03-model-wiki.md` - welche Aufgabe mit welchen Einstellungen
