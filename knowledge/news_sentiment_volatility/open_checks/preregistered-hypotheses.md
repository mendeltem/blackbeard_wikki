---
id: preregistered-hypotheses
typ: pruefpunkt
status: offen
thema: knowledge/news_sentiment_volatility
stand: 2026-10-12
herkunft: Projekt Sentiment-Briefing AI/DRAM (Cloud-Sitzung), 2026-09-30 bis 2026-10-12
verweist_auf: [news-volume-memory-volatility, krx-run-timing]
---

# Vorab festgelegte Hypothesen Sentiment gegen Kursschwankung, Entscheidungstermine

## Aussage
Festgelegt 2026-09-30 vor den ersten prospektiven Daten (Mendel hat den gemeinsamen Test aller drei Sentimentvariablen gewaehlt).
- H1: Parkinson-Volatilitaet SK Hynix am Zielschluss ~ Ballung (Vortag, 5 Tage) + |DRAM-Sentiment kalibriert| + Quellenstreuung + ln(1+Artikelzahl). Wald-Test der drei Sentimentterme, Newey-West, Holm ueber H1/H2. Entscheidung nach 146 Handelstagen (Power 0,8 fuer R2-Zuwachs 0,05 bei Basis-R2 0,30).
- H2: dasselbe fuer NVDA mit AI-Sentiment.
- H3: |Rendite| SK Hynix und Samsung ~ Ballung + 60-Tage-Niveau + Berichtstag + DRAM-Schlagzeilenmenge ueber Normal (Techmeme, gleiche Methode wie Backtest). Einseitig, Holm. Entscheidung nach 500 Handelstagen ab 2026-10-01.
Messung H1/H2: taegliche LLM-Bewertung von 12 Quellen, Bayes-kalibriert gegen ein 5-Monats-Normal je Quelle.

## Trägt
Entscheidungsregeln, die nach den Daten nicht mehr geaendert werden.

## Trägt nicht
Bis zu den Terminen keine Aussage; Zwischenstaende entscheiden nichts.

## Bruchindikator
Siehe Entscheidungsregeln.

## Ablesung
Projektdatei FESTLEGUNG_2026-09-30.md (nicht in der Wiki).

## Verknüpft
- [news-volume-memory-volatility](../findings/news-volume-memory-volatility.md)
