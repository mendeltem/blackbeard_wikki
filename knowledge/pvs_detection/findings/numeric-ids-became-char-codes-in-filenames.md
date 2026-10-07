---
id: numeric-ids-became-char-codes-in-filenames
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-07
herkunft: PVS-Cluster Alita, Bestandsaufnahme der uebernommenen Edinburgh-MATLAB-Pipeline, 2026-10-07
verweist_auf: [pipeline-failures-and-names-before-tuning, pvs-apply-the-lesion-method]
---

# 30 von 103 Pipeline-Fehlschlaegen waren ein Typfehler: Zahl wurde zum Zeichen im Dateinamen

## Aussage
Die uebernommene PVS-Pipeline (MATLAB, Edinburgh; FreeSurfer, FSL, RORPO) liest die Fallkennungen
mit `readtable` aus einer CSV. Kennungen wie 1, 10, 100 werden dabei numerisch, und MATLAB macht aus
`[StudyTag '_T1w_reoriented']` das Zeichen `char(Fallnummer)` als Praefix jedes Dateinamens
(65 -> `A`, 100 -> `d`, 50 -> `2`, 58 -> `:`, 10 -> Zeilenumbruch). Faelle, deren Code ein
Shell-Sonder- oder Steuerzeichen ergibt, brechen in `fslreorient2std`/`run_samseg` ab (26 von 30);
vier weitere (Codes `.`, `0`, `2`, `C`) brechen spaeter und sind getrennt anzusehen. Die gemeldeten
Fehlertexte ("Error changing the orientation", "Unrecognized file type _template_LBG") und die leere
Spalte "Study Tag" in der Fehlerliste (`fprintf('%s', Zahl)`) sind Folgefehler derselben Ursache.
Ergebnis: 73 Faelle mit Masken statt 72 gemeldet; mit Textkennungen (z. B. `sub-001`) laufen alle.

## Traegt
Jede uebernommene Pipeline mit Kennungen aus CSV; jede Sprache, die Zahl und Zeichen implizit wandelt.
Vor dem Deuten von Fehlertexten: erstes Byte der erzeugten Dateinamen ansehen (`od -c`).

## Traegt nicht
Sagt nichts ueber die Qualitaet der Masken. Die vier Restfaelle sind nicht erklaert.

## Bruchindikator
Ein Lauf mit Textkennungen auf den 30 Faellen scheitert erneut.

## Ablesung
Eigene Zaehlung (`pvs-arena/skripte/bestandsaufnahme.py`, `daten/BESTANDSAUFNAHME.md`), Code
`PVS_lib/Utils/process_dataset_from_csv_files.m` Zeile 7 und 14. Patientendaten, nur Summen.

## Verknuepft
- [pipeline-failures-and-names-before-tuning](../../lesion_detection_method/rules/pipeline-failures-and-names-before-tuning.md)
- [pvs-apply-the-lesion-method](../../lesion_detection_method/open_checks/pvs-apply-the-lesion-method.md)
