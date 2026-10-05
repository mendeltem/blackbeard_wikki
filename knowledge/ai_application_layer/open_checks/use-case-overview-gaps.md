---
id: use-case-overview-gaps
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-05
herkunft: Gespräch Projekt AI_news, 2026-10-05
verweist_auf: [airport-biometric-checkin-use-case]
---

# Lücken in ai_use_cases_overview: Kandidatenliste

## Aussage
Der Flughafen-Check-in fehlte in der Übersichtsseite (siehe [airport-biometric-checkin-use-case](airport-biometric-checkin-use-case.md)). Ein sparsamer Erstdurchlauf am 2026-10-05 hat 30 bekannte, produktiv laufende KI-Anwendungen per Stichwortsuche gegen die Karten der Seite (Block `const UC`) gehalten, ohne Webrecherche. Kandidaten ohne Treffer in den Karten:

Ohne jeden Treffer: Kreditscoring/Underwriting, Hörgeräte mit KI, Smartphone-Fotografie (Computational Photography), Tutoring und adaptives Lernen, Liefer-Dispatch (Essenslieferung, Paketrouten), Briefsortierung mit Handschrifterkennung, kassenloser Handel (Just Walk Out).

Nur in der Lückenliste oder einem Nebensatz, ohne eigene Karte: Flugsicherung, Kennzeichenerkennung und Maut, Barrierefreiheit (Be My Eyes u. a.), Content-Moderation.

Stand 2026-10-05 abends: Flughafen-Karte eingetragen; die Seite hat inzwischen eine Karte "Rail predictive maintenance" (Gleisinspektion vermutlich abgedeckt, prüfen).

Treffer möglicherweise zufällig, Karte prüfen: Hafenautomation ("port" kann "support" sein), Gleisinspektion ("track" kann "tracking" sein).

## Zu prüfen
1. Samstag (viel Token-Budget): je Kandidat Webrecherche nach dem Muster des Flughafen-Falls, also Produktion ja/nein, Kennzahl mit Herkunft, Behörde gegen Firmenangabe, Einstufung Reife/Beleg/Wachstum.
2. Weitere Kandidaten systematisch sammeln: zuerst die Behördenverzeichnisse aus "Suchquellen", dann Lückenliste der Seite (Branchen ohne Karte) Branche für Branche gegen bekannte Produktivfälle halten.
3. Die zwei möglicherweise zufälligen Treffer gegen die Kartentexte lesen.
4. Je bestätigter Lücke Kartenentwurf an Mendel, gesammelt eintragen (Schreibzugriff auf ai_use_cases_overview nötig).

## Suchquellen für unauffällige Fälle
In dieser Reihenfolge nutzen (Nutzen je Aufwand). Quellenliste aus allgemeinem Wissen, Erreichbarkeit und Stand je Quelle beim Lauf prüfen.
1. Behördenverzeichnisse, Beleg meist solide:
   - US Federal AI Use Case Inventory (jährliche Meldepflicht der Bundesbehörden, Tausende Einträge): schnellster Abgleich gegen die Lückenliste.
   - FDA-Liste der KI-fähigen Medizinprodukte (über 1.000 Zulassungen, nach Fachgebiet).
   - EU-Datenbank für Hochrisiko-KI nach AI Act: prüfen, ob Registrierungen schon öffentlich sind.
   - Ausschreibungen: TED (EU), SAM.gov und USAspending (USA). Zeigt Käufe vor der Pressemitteilung.
2. Konferenzen mit Fokus auf eingesetzte Systeme: IAAI (AAAI, Preise für deployed applications), KDD Applied Data Science Track. Branchenmessen statt KI-Messen: RSNA, Hannover Messe, Automatica, Passenger Terminal Expo, Money20/20, Agritechnica, TOC Europe.
3. Unternehmensberichte außerhalb der Tech-Branche: Earnings Calls und Geschäftsberichte von Versicherern, Logistikern, Versorgern, Bergbau nach "AI" durchsuchen. Fallstudien der Ausrüster (Siemens, Rockwell, ABB, SITA, IDEMIA) nur zum Finden, nicht als Beleg. WEF Lighthouse nutzt die Seite schon.
4. Frühindikatoren: Stellenanzeigen für ML-Rollen in Nicht-Tech-Firmen, Patente, Zulassungen (EASA, FAA, Bahn).

## Trägt nicht
Dass die Kandidaten groß sind oder auf die Seite gehören. Die Liste stammt aus allgemeinem Wissen, ohne Quellen, und die Stichwortsuche kann Karten unter anderem Namen übersehen.

## Bruchindikator
Alle Kandidaten sind geprüft und eingetragen oder begründet verworfen.

## Ablesung
Lokale Stichwortsuche im Repo mendeltem/ai_use_cases_overview, Stand des Klons 2026-10-05. Inhalte blind.

## Verknüpft
- [airport-biometric-checkin-use-case](airport-biometric-checkin-use-case.md)
