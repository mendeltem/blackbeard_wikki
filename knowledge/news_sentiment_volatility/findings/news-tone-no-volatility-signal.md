---
id: news-tone-no-volatility-signal
typ: befund
status: vorschlag
thema: knowledge/news_sentiment_volatility
stand: 2026-10-12
herkunft: Projekt Sentiment-Briefing AI/DRAM (Cloud-Sitzung), 2026-09-30 bis 2026-10-12
verweist_auf: [news-volume-memory-volatility, krx-run-timing, finbert-reads-memory-prices-negative]
---

# Ton der Tech-Schlagzeilen sagt die Schwankung am Folgetag nicht voraus (Backtest 2 Jahre)

## Aussage
Backtest 2024-10-01 bis 2026-09-29: 14.940 Techmeme-Schlagzeilen (Suche mit Datumsfilter), bewertet mit FinBERT (ProsusAI/finbert, Wert = P(pos) - P(neg)), Thema per Stichwortregel (AI 11.686, DRAM 411). Ziel: |Log-Rendite| am naechsten Handelstag nach dem Lauf, Basislinie Volatilitaetsballung (|ret| Vortag, 5-Tage-Mittel), Berichtstage als Kontrolle, Newey-West (5 Lags).
NVDA: R2 nur Ballung 0,052, mit |z-Sentiment|, Quellenstreuung, ln(1+n) 0,057 (Zuwachs 0,005), Wald p = 0,38, n = 463.

## Trägt
Bei n = 463 waere ein R2-Zuwachs ab etwa 0,022 mit Power 0,8 sichtbar gewesen (F-Test, 3 Variablen). Der Ton der allgemeinen KI-Nachrichten taugt fuer NVDA nicht als Volatilitaetsvorhersage in dieser Groessenordnung.

## Trägt nicht
Kein Urteil ueber Richtung, ueber andere Bewertungsmodelle (LLM-Bewertung je Quelle laeuft prospektiv seit 2026-09-30) oder ueber Fachquellen; die Historie kommt fast nur aus Reichweitenquellen ueber Techmeme. Bewertung nur nach Ueberschrift.

## Bruchindikator
Prospektive Hypothese H2 (LLM-Sentiment, Parkinson-Volatilitaet) nach 146 NVDA-Handelstagen signifikant.

## Ablesung
Eigene Rechnung; Kurse aus github.com/mendeltem/AI_Companys, Schlagzeilen Techmeme. Keine Fremdquelle.

## Verknüpft
- [news-volume-memory-volatility](news-volume-memory-volatility.md)
- [krx-run-timing](../rules/krx-run-timing.md)
