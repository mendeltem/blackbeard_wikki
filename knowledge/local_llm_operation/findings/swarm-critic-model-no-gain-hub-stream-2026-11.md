---
id: swarm-critic-model-no-gain-hub-stream-2026-11
typ: befund
status: gemessen
thema: knowledge/local_llm_operation
stand: 2026-11-05
herkunft: own comparison run on Alita, 2026-11-05, 8 public research tasks, 2 arms, balanced order
verweist_auf: [local-research-swarm-first-run-2026-10-09]
---

# A second-model critic in a research swarm cost 5 times the tokens and showed no measurable gain

## Aussage

Eight research tasks ran through a swarm in two arms: one hub model for everything (A), or the same writer plus a different, faster hub model as critic on pieces of 1500 characters with a revision step (B). B used 5.17 times the tokens (1,959,470 against 379,269). Supported share after correcting the scorer: 0.984 in A, 0.988 in B, with 2 wins, 4 ties and 2 losses for B. Draft against final, the critic mainly added "unconfirmed" marks (18 net over 8 tasks) and changed 11 diff lines beyond that. The fixed rule (share higher in at least 6 of 8, supported claims at least 90 %, tokens at most 1.5 times) kept A.

Two operating facts from the same work. The hub ends non-streamed calls at 50 s, either with a 502 or with a short error sentence delivered as a normal answer, which had been stored as a finished report section (3 of 8 and 2 of 5 sections on two mornings). Streaming passed long answers (7 of 7, up to 82 s), but 50 s of silence before the first token still ends a call.

Two scorer faults made B look better than it was. A judge shown text cut at a fixed length rejected sentences for being cut off (5 of 9 rejections), which turned 2 wins into 6. A citation pattern that knew only some styles counted 0 cited statements in texts with 28 references. Reading the rejections by hand found both.

## Trägt

- Own run 2026-11-05, 8 tasks, 16 final texts, 8 drafts, 64 search questions. Stored as a plan with the rule fixed before the runs, scripts, raw results and a recheck script; private project folder.
- All 430 numbers in the text bodies occur in the source material in both arms, and all DOI and URL references come from the material; 1 reference did not resolve.

## Trägt nicht

- Different models for the question step: the hub alias tried answered as the same model, so this was not tested.
- Whether a critic helps on another kind of text. Share sat near the ceiling of 1.0, and a number present in the material can still be attributed to the wrong claim.
- The judge is one model and saw a sample of 2 sections per text, with the recheck done post hoc.

## Bruchindikator

A rerun where final texts are judged in full, by sentence-complete pieces, shows a clear share gain for the critic at under 1.5 times the tokens.

## Ablesung

Keep one model and no critic in the swarm. Stream hub calls and treat an empty answer, a missing finish reason or an error sentence as a failure. Cut judge pieces at sentence ends, and read a scorer's rejections on texts from every arm before a full run.
