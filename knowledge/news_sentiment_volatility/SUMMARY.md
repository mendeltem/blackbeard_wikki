# news_sentiment_volatility: Kurzstand

Stand 2026-10-12. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md).

Ob Ton oder Menge von KI- und Speicher-Nachrichten die Groesse der naechsten Kursbewegung vorhersagt.

**Befunde (vorschlag, eigene Rechnung):** Backtest 2 Jahre, 14.940 Techmeme-Schlagzeilen mit FinBERT: der Ton sagt die NVDA-Schwankung nicht voraus (R2-Zuwachs 0,005, n 463). Ungewoehnlich viele Speicher-Schlagzeilen gehen groesseren Bewegungen bei Samsung (p 0,016) und SK Hynix (p 0,064) voraus, aber instabil zwischen den Zeitteilen. Die These "extrem positive Nachrichten vor starkem Fall" fand sich im juengeren Teil nicht wieder. FinBERT wertet Speicherpreisanstiege negativ.

**Regeln:** Morgenlauf in Europa: fuer KRX-Aktien uebernaechster Schluss als Ziel. Neueste KRX-Verlaufszeile ist vorlaeufig. Neubewertung in derselben Sitzung ist kein Reliabilitaetstest.

**Offen:** Vorab festgelegte Hypothesen H1 bis H3, Entscheidung nach 146 bzw. 500 Handelstagen.

**Lesen bei:** Sentiment, Nachrichtenanalyse, Kursvorhersage, Volatilitaet, Backtest, FinBERT, SK Hynix, NVDA.
