---
id: krx-run-timing
typ: regel
status: getragen
thema: knowledge/news_sentiment_volatility
stand: 2026-10-12
herkunft: Projekt Sentiment-Briefing AI/DRAM (Cloud-Sitzung), 2026-09-30 bis 2026-10-12
verweist_auf: [krx-latest-row-provisional]
---

# Morgenlauf in Europa: Ziel fuer koreanische Aktien ist der uebernaechste Schluss

## Aussage
Ein Lauf um 07:30 Berlin liegt in der laufenden KRX-Sitzung (Eroeffnung 02:00, Schluss 08:30 Berlin, Sommerzeit). Artikel bis 07:30 koennen ueber diese Sitzung berichten. Fuer Vorhersagetests gilt:
- Ziel fuer KRX-Aktien = Schluss der ersten Sitzung, die nach dem Lauf beginnt = uebernaechster Schluss; fuer US-Aktien der naechste.
- Basislinie (Vortagesvolatilitaet usw.) nur aus abgeschlossenen Handelstagen.
- Lauftage zwischen zwei neuen Schlusskursen (Wochenende, Feiertag) zu einem Block zusammenfassen, nach Artikelzahl gewichtet.

## Trägt
Ohne diese Zuordnung zaehlen Berichte ueber die Bewegung selbst als Vorhersage. Gefunden beim Backtest, vor den ersten prospektiven Daten korrigiert.

## Trägt nicht
Andere Laufzeiten: Zuordnung je Boerse aus Eroeffnungszeit und Laufzeit neu bestimmen.

## Bruchindikator
Keiner, Rechenregel.

## Ablesung
Handelszeiten KRX und Nasdaq, allgemein bekannt.

## Verknüpft
- [krx-latest-row-provisional](krx-latest-row-provisional.md)
