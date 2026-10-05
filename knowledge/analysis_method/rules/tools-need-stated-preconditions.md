---
id: tools-need-stated-preconditions
typ: regel
status: getragen
thema: knowledge/analysis_method
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [unverifiable-rival-position, revenue-only-via-proxies, capex-discipline-after-2023, volume-times-price-scissors, contract-stability, sk-hynix-customer-concentration-f1]
---

# Ökonomische Werkzeuge nur mit ausgeschriebener Vorbedingung

## Aussage
Ein Werkzeug wird nur benannt angewandt, mit ausgeschriebener Vorbedingung und der Angabe, was es nicht trägt. Ohne geprüfte Vorbedingung ist es Dekoration und wird gestrichen. Werkzeuge ordnen Zahlen, sie erzeugen keine.

| Werkzeug | Wo | Vorbedingung | Trägt | Trägt nicht |
|---|---|---|---|---|
| Nash-Gleichgewicht | Investitionszwang der Hyperscaler | nur ordinale Auszahlungen; Positionsverlust schlechter als Überinvestition | Stabilität der Konfiguration und die Bedingung ihres Zerfalls | Beträge, Zeitpunkt, Rentabilität. Erzeugt es eine Zahl, ist das ein Fehler |
| Cournot mit Kapazitätsbindung | Angebotsseite Speicher | wenige Anbieter, Menge als Strategie, Kapazität irreversibel und beobachtbar | Disziplin ohne unterstellte Absprache; wer ausbricht | Dauer der Disziplin. Für CXMT und YMTC nur mit Vorbehalt, Kapazität nicht beobachtbar |
| Verhandlung über Außenoptionen | Nvidia gegen Käufer, Speicherhersteller gegen Nvidia | bilaterale Rente, benannte Außenoption beider Seiten, bekannte Kundenkonzentration | ASIC-Programme als Verhandlungsvermögen lesen | Stückzahlen für ASICs; ohne Konzentrationsdaten nur Vorzeichen |
| Mehrmarktkontakt | Nvidia und Hyperscaler untereinander | dieselben Spieler in mehreren Märkten, Seitenzahlungen möglich | gedämpfte Investitionsschwankung, wirkt gegen den Investitionszwang | Nachweis einer Absprache; nicht auf die Vertragsschicht Speicher gegen Kunde anwendbar |
| Jevons und Rebound | Effizienzgewinne je Token | Endnachfrage preiselastisch, Markt nicht gesättigt | aus weniger Speicher je Token folgt nicht weniger Gesamtnachfrage | "Effizienz erhöht die Nachfrage immer". Nur Rebound über 100 % ist Jevons |
| Marshall, abgeleitete Nachfrage | ASP des Speichers | Speicher als Vorleistung mit gerechnetem Kostenanteil am System | kleiner Kostenanteil, unelastische Nachfrage, Preisspielraum | denselben Spielraum bei steigendem Anteil: ein höherer ASP verkleinert den eigenen Spielraum |
| Peitscheneffekt | Phantomnachfrage | abgeleitete Nachfrage mit Vorlaufzeit über mehrere Stufen | Amplitudenverstärkung stromaufwärts | Saldierung mit der Dämpfung durch Anzahlungen; beide Kräfte getrennt ausweisen |

Falsifikator für Jevons: das Token-Volumen wächst langsamer als der Effizienzgewinn. Dann ist der Rebound unvollständig, und der Effizienzgewinn schlägt auf die Bitnachfrage durch.

## Trägt
Die Form, in der ein Modellargument zulässig ist.

## Trägt nicht
Dass die Vorbedingungen erfüllt sind; das ist je Anwendung zu prüfen. Der Projektprompt nennt außerdem Wrightsches Gesetz, Engpasstheorie und Optionswert des Wartens; deren Text liegt nicht vollständig vor und ist hier nicht ergänzt.

## Bruchindikator
Keiner. Verfahrensregel.

## Ablesung
Keine. Token-Volumen für den Jevons-Falsifikator nennen einige Anbieter selbst (Tier 1a, uneinheitlich definiert; Definition mitführen).

## Verknüpft
- [unverifiable-rival-position](../../ai_demand_drivers/axioms/unverifiable-rival-position.md)
- [revenue-only-via-proxies](../../ai_demand_drivers/axioms/revenue-only-via-proxies.md)
- [capex-discipline-after-2023](../../memory_supply/mechanisms/capex-discipline-after-2023.md)
- [volume-times-price-scissors](../../ai_application_layer/mechanisms/volume-times-price-scissors.md)
- [contract-stability](../../memory_earnings/axioms/contract-stability.md)
- [sk-hynix-customer-concentration-f1](../../memory_earnings/findings/sk-hynix-customer-concentration-f1.md)
