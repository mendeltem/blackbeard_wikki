---
id: news-volume-memory-volatility
typ: befund
status: vorschlag
thema: knowledge/news_sentiment_volatility
stand: 2026-10-12
herkunft: Projekt Sentiment-Briefing AI/DRAM (Cloud-Sitzung), 2026-09-30 bis 2026-10-12
verweist_auf: [news-tone-no-volatility-signal, preregistered-hypotheses]
---

# Ungewoehnlich viele Speicher-Schlagzeilen gehen groesseren Bewegungen von Samsung und SK Hynix voraus (schwach, instabil)

## Aussage
Gleicher Backtest wie [news-tone-no-volatility-signal](news-tone-no-volatility-signal.md). Variable: ln(1+n) der DRAM-Schlagzeilen im Block minus Mittel der vorherigen 60 Bloecke; Kontrollen |ret| Vortag, 5- und 60-Tage-Mittel, Berichtstag.
Koeffizient in Prozentpunkten |Rendite| je ln-Einheit, ganze Reihe: Samsung +0,70 (p 0,016), SK Hynix +0,68 (p 0,064), NVDA +0,47 (p 0,15), Micron +0,42 (p 0,23). Teil A (erste 60 %) gegen Teil B: Samsung -0,12 / +1,14, SK Hynix +0,20 / +0,93.

## Trägt
Alle vier Vorzeichen positiv. Als Hypothese H3 vorab festgelegt (siehe [preregistered-hypotheses](../open_checks/preregistered-hypotheses.md)).

## Trägt nicht
Keinen stabilen Effekt: der Effekt sitzt fast nur im juengeren Teil. DRAM ist auf Techmeme duenn (53 % der Bloecke ohne Artikel). Keine Kausalitaet: viele Meldungen koennen Folge von Bewegungen in anderen Maerkten sein.

## Bruchindikator
H3 nach 500 Handelstagen ab 2026-10-01 nicht signifikant (Holm, einseitig).

## Ablesung
Eigene Rechnung, Tier: keine Fremdquelle.

## Verknüpft
- [preregistered-hypotheses](../open_checks/preregistered-hypotheses.md)
