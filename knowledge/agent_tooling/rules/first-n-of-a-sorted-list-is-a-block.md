---
id: first-n-of-a-sorted-list-is-a-block
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [count-cases-behind-a-pooled-number]
---

# Die ersten N einer sortierten Liste sind ein Block, kein Querschnitt

## Aussage
Dreimal an einem Tag aus den ersten N einer nach Kennung sortierten Liste hochgerechnet, dreimal
lag die Vollzaehlung deutlich anders:

| Was | Stichprobe (erste N) | Vollzaehlung | Fehler |
|---|---|---|---|
| Schnitte je Fall | 256 (erste 40) | 159 (alle 201) | Faktor 13 statt 9 |
| Faltenqualitaet | 2 von 5 Falten | alle 5 | Schluss zufaellig richtig |
| Dice eines Modells | 0,680 (erste 40) | 0,718 (alle 110) | 0,039 |

Kennungen tragen Struktur: `sub-001..060` ist eine Kohorte, `cv-001..201` mischt vier Kohorten in
Bloecken, Faltendateien liegen nach Variante. Die ersten 40 sind deshalb eine Kohorte, ein
Standort, eine Schichtdicke.

Regel: vollzaehlen, wenn es billig ist (110 NIfTI-Dateien zu messen kostete 14,8 s; die
Stichprobe sparte nichts und kostete einen falschen Befund). Wo eine Stichprobe noetig ist,
zufaellig ziehen statt vorn abschneiden: `rng.choice(liste, k, replace=False)` mit festem Seed,
Streuung mitberichten. Eine Zahl aus einer Stichprobe nie als Befund melden, sondern als
Schaetzung mit Fehlerspanne.

## Traegt
Jede Hochrechnung aus Dateilisten, Logs, Tabellen, die nach Kennung, Datum oder Pfad sortiert sind.

## Traegt nicht
Echte Zufallsstichproben.

## Bruchindikator
---

## Ablesung
Drei Vorfaelle 2026-09-15. Tier 1a.

## Verknuepft
- [count-cases-behind-a-pooled-number](count-cases-behind-a-pooled-number.md)
