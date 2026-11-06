# Pronunciation helper for film voices (Kokoro, Ming)

The text-to-speech voice reads technical words badly. Write the **spoken** text (`beats/*_beats.json`) the way it should
sound; the words drawn on screen keep the real spelling. Rule from the user (2026-11-06): **if you are not sure how a
hard word should sound, ask before rendering**, and add the answer here.

## Confirmed by the user (by ear)

| Written | Spoken text | Confirmed |
|---|---|---|
| Clé | Kleh | 2026-11-04 |
| BIANCA / Bianca | Bianka | 2026-11-04 |
| PYTHONNOUSERSITE | python no user site | 2026-11-06 |
| CUDA | Kuda | 2026-11-06 |

## In use, not yet heard by the user

Spellings already in finished films (HPC tutorial, 2026-11-06). They sound right to the author; confirm or correct.

| Written | Spoken text |
|---|---|
| sbatch / srun / scancel | s batch / s run / s cancel |
| squeue / sq | s queue / s q |
| scrontab | s crontab |
| GRES | G R E S |
| nvidia-smi | nvidia s m i |
| .bashrc | bash r c |
| rm -rf | r m minus r f |
| FSL | F S L |
| SC hub | S C hub |
| L40S | L40 S |

## How to use it

1. Before the voice step, search the spoken text for capitals, digits mixed with letters, command names and dots
   (`grep -E '[A-Z]{3,}|[a-z]+[0-9]|\.sh|--'`).
2. Replace each hit with the spoken form from the tables. Anything not in the tables: ask the user, then add it here.
3. Only the changed beats need a new voice; the engine skips unchanged text.

Sources: user decisions in the sessions of 2026-11-04 and 2026-11-06 (Clé/Bianca films, HPC tutorial film).
