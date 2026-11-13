# Pronunciation helper for film voices (Kokoro, Ming)

The text-to-speech voice reads technical words badly. Write the **spoken** text (`beats/*_beats.json`) the way it should
sound; the words drawn on screen keep the real spelling. Rule from the user (2026-11-06): **if you are not sure how a
hard word should sound, ask before rendering**, and add the answer here.

## Confirmed by the user (by ear)

| Written | Spoken text | Confirmed |
|---|---|---|
| Clé | Kleh | 2026-11-04 |
| BIANCA / Bianca | `[Bianka](/biˈɑŋkə/)` (Kokoro phoneme markup: German "Bianka", bee-AHN-ka; the plain respelling "Bianka" was read as BYE-un-ka) | 2026-11-13 |
| MRI | M. R. I. (spelled slowly, written with full stops in the spoken text; user 2026-11-10: "MRI is spoken fast"; the user has not yet confirmed the new sound, so not in pronounce.json) | 2026-11-10 |
| PYTHONNOUSERSITE | python no user site | 2026-11-06 |
| CUDA | Kuda | 2026-11-06 |
| A100 | A one hundred | 2026-11-06 |
| H100 / H200 | H one hundred / H two hundred | 2026-11-06 |
| L40S | L forty S | 2026-11-06 |
| pgpu / agpu (partitions) | PGPU / AGPU (capitals, see note) | 2026-11-06 |
| Apptainer | app-tainer | 2026-11-06 |
| AFNI | af-nee | 2026-11-06 |
| ANTs | ants | 2026-11-06 |
| microbleednet / truenet | micro bleed net / true net | 2026-11-06 |
| cu12 (wheel tag) | C U twelve | 2026-11-06 |

**Note on letter-by-letter words (2026-11-06):** the user wanted "P G P U" a little faster. Kokoro (af_heart) pauses at
spaced letters and reads a spaced or hyphenated "A G P U" / "A-G-P-U" as the article "uh" + GPU. Uppercase "PGPU" / "AGPU"
is spoken letter by letter like "CPU" and was the shortest (13.80 s against 14.08 s spaced, 13.90 s hyphenated, same
sentence; phonemes checked with the Kokoro G2P output). So: write short letter acronyms in capitals without spaces.

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
| entorhinal | en-toe-rye-null (SuperAgers film, 2026-11-09; espeak said "en-TOR-hin-al") |
| Northwestern | North-western |
| hyperintensities | hyper-intensities (unknown to Kokoro's dictionary) |
| microbleeds | micro-bleeds |
| multisite | multi-site |
| APOE | APOE (capitals: read A P O E); e2 / e4 spoken as "epsilon two / four" |
| thrombectomy | avoided: "patients whose clot was removed" (espeak stress was wrong) |
| Vallecas | avoided: "Madrid" (espeak guess "VAL-eh-kas") |
| MoCA | Mocha (moderation manuscript film, 2026-11-11; "Moka" is unknown to Kokoro, "Mocha" gives moh-kuh) |
| CES-D | CESD (capitals, read C E S D) |
| EQ-5D / EQ-5D-5L | EQ five D |
| RMI / Rivermead | RMI (capitals, letters); mostly said as "River mead" ("Rivermead" is unknown to Kokoro) |
| SD / SDs | SD / SDs (capitals, letters) |
| PCA | PCA (capitals, letters) |
| FDR, PMM, FMI | said in full: false discovery rate, predictive mean matching, fraction of missing information |
| MICE | not spoken in that film ("filling in"); the statistics name is said like the animal: "mice" |
| Rubin's rules | Reuben's rules ("Rubin" is unknown to Kokoro) |
| Cohen's d | Kohen's D ("Cohen" is unknown to Kokoro) |
| poorer | avoided: "worse" (espeak guess "poor-rer") |
| completers' | avoided: "patients seen at all visits" (unknown to Kokoro, espeak guess "com-PLEH-ters"; moderation_manuscript_v2, 2026-11-11) |
| Lead-DBS / Lead Mapper | Leed DBS / Leed Mapper (the toolbox for DBS leads; lnm_abstraction_mobility film, 2026-11-11) |
| Nichols (Nichols 2005) | Nickels ("Nichols" unknown to Kokoro) |
| GSP1000 | GSP one thousand (capitals, letters) |

The SuperAgers film (2026-11-09) wrote these respellings directly into its spoken text, not into pronounce.json, so that other films are not re-voiced by surprise. The moderation manuscript film (BAPTISe, 2026-11-11) did the same for its rows (MoCA to poorer); none of them is confirmed by ear yet.

## Machine-readable list and check (2026-11-09)
`pronounce.json` is the same table for the tools: `voice.py` applies it before speaking, and `src/say_check.py <film>` lists the words to hear and makes a listening file. Keep both files in step.

## How to use it

1. Before the voice step, search the spoken text for capitals, digits mixed with letters, command names and dots
   (`grep -E '[A-Z]{3,}|[a-z]+[0-9]|\.sh|--'`).
2. Replace each hit with the spoken form from the tables. Anything not in the tables: ask the user, then add it here.
3. Only the changed beats need a new voice; the engine skips unchanged text.

Sources: user decisions in the sessions of 2026-11-04 and 2026-11-06 (Clé/Bianca films, HPC tutorial film).
