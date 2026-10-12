# news_sentiment_volatility

Ob Nachrichtenton oder Nachrichtenmenge zu KI und Speicher die Groesse kuenftiger Kursbewegungen (NVDA, SK Hynix, Samsung) vorhersagt: Backtest, Messfallen, vorab festgelegte Hypothesen. Gemeldete Firmenzahlen stehen in [memory_earnings](../memory_earnings/INDEX.md).

Stand 2026-10-12. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Ton der Tech-Schlagzeilen sagt die Schwankung am Folgetag nicht voraus (Backtest 2 Jahre)](findings/news-tone-no-volatility-signal.md) | befund | vorschlag |
| [Ungewoehnlich viele Speicher-Schlagzeilen gehen groesseren Bewegungen von Samsung und SK Hynix voraus (schwach, instabil)](findings/news-volume-memory-volatility.md) | befund | vorschlag |
| [Extrem positive Nachrichtenlage vor starkem Fall: Hinweis im aelteren Teil, im juengeren nicht wiedergefunden](findings/overreaction-thesis-not-replicated.md) | befund | vorschlag |
| [FinBERT wertet steigende Speicherpreise negativ, eine Herstellersicht-Bewertung positiv](findings/finbert-reads-memory-prices-negative.md) | befund | vorschlag |
| [Morgenlauf in Europa: Ziel fuer koreanische Aktien ist der uebernaechste Schluss](rules/krx-run-timing.md) | regel | getragen |
| [Neueste KRX-Kurszeile auf Verlaufsseiten ist vorlaeufig, Vortag immer nachpruefen](rules/krx-latest-row-provisional.md) | regel | getragen |
| [Neubewertung in derselben Sitzung misst keine Reliabilitaet](rules/same-session-rescoring-is-not-reliability.md) | regel | getragen |
| [Vorab festgelegte Hypothesen Sentiment gegen Kursschwankung, Entscheidungstermine](open_checks/preregistered-hypotheses.md) | pruefpunkt | offen |
