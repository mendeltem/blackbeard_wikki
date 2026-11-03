---
id: model-hub-writes-explainer-films-under-a-harness
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-03
herkunft: own runs on Alita, 2026-11-03, hospital model hub Clé (aliases frontier, vision, clea, fast, eu) through its OpenAI-compatible API
verweist_auf: []
---

# A hub model can write narrated explainer films under a harness; blind code on private data needs checks a data gate cannot give

## Aussage
1. Long tasks on this hub come back empty unless `"chat_template_kwargs": {"enable_thinking": false}` is sent: hidden thinking uses up `max_tokens`, with finish_reason stop. Requests are cut near 50 s, so stream. Four parallel requests gave empties; one at a time works.
2. With that setting, frontier wrote a 29-minute, 18-chapter film from a public README: plan, narration, matplotlib drawing code. First-draft layouts are messy, so a rule-based check of the real text boxes belongs in the loop. An image model alone is not enough.
3. Check what a model was given before blaming it. A harness bug (`(.+)` with `re.S` swallowed the document) gave the writer empty sources. It invented facts and reversed who may see patient data, and the fact check reported zero complaints, because it compared with nothing. With the real text it read the table correctly and flagged 3 of 3 planted false claims. Assert the input size of every model call.
4. Zero complaints prove little in both directions: the same fact check raised six false alarms in one chapter, and it does not cover on-screen text. A rounding bug (`int(.57*100)` = 56) passed all checks and was seen by eye.
5. Timing contracts must be stated. The engine's `T.p(beat)` stays at 1 after its beat, so the model's beats piled up. The rule "one branch per beat, each its own screen" fixed this at once.
6. Screens stay emptier than hand-built ones (near-empty time 8 to 12 % against 1.3 %) even after showing content earlier, and a model that may not see data can only draw invented dots and schematics.
7. Code written blind can run on private data while the model sees only a description, invented data and group results that passed a rule-based output gate. The run reproduced the released counts exactly. But fixed axis limits silently dropped about a tenth of the real points, with "ok" from every check. Compute limits from the data, and count points outside the axes on the private run.
8. A guard that checks imports is not a sandbox: `from engine import *` also hands over `subprocess` and `Path`. Run such code in a kernel sandbox, with a namespace holding only what it needs.

## Trägt
Own runs 2026-11-03: serial test battery; three films with chapter reports; a one-chapter pilot, two runs. Software: [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (voice, CPU), [matplotlib](https://matplotlib.org), [ffmpeg](https://ffmpeg.org).

## Trägt nicht
One hub, one week, one writer model for the films. Keyword scoring of the battery was loose. The comparison films reused an existing plan and narration, so they do not test whether the model could do the analysis. The output gate thresholds are proposals awaiting a data protection officer. The hub's limits may change without notice.

## Bruchindikator
Empty answers return with the setting on; a film without the rule check passes review; an output gate release is shown to reveal an individual.

## Ablesung
Before a film or code task on this hub: thinking off, serial and streamed, assert input sizes, rule check in the loop, a person looks at the frames. Before private data: gate, sandbox, and a check on the private run that reports only counts.
