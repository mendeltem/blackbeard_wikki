---
id: base-die-shifts-value-to-foundry
typ: mechanismus
status: vorschlag
thema: knowledge/memory_technology_roadmap
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Report Speicher-Roadmap nach HBM4E (Stichtag 26.07.2026), eingetragen 2026-10-06
verweist_auf: [backend-and-base-die-are-separate-capacity, cowos-capacity-and-package-area, yield-trough, tools-need-stated-preconditions]
---

# Der HBM-Basisdie wird ein Logikprodukt und verschiebt Wertschöpfung zur Foundry

## Aussage
Ab HBM4 wird der Basisdie auf einem Logikprozess gefertigt: bei SK Hynix und Micron bei TSMC (12-nm-Klasse, für kundenspezifisches HBM4E 3-nm-Klasse), bei Samsung im eigenen 4-nm-Prozess. Kundenspezifisches HBM verlagert Controller und Teile der Schnittstelle in den Basisdie.

Zwei Wirkungen, die gegeneinander laufen:
- HBM wird weniger austauschbar. Höhere Wechselkosten; Micron stellt für kundenspezifisches HBM4E höhere Bruttomargen in Aussicht.
- Ein Teil der Wertschöpfung geht an die Foundry und an den Kunden, der das Design vorgibt. Der Speicherhersteller wird teilweise Auftragsfertiger. Für die Rechnung ist der Basisdie Materialaufwand zu Foundry-Marge und ein eigener Engpass.

Samsung ist der einzige Anbieter mit allem aus einer Hand. Das ist eine strukturelle Weichenstellung, kein gradueller Unterschied.

## Trägt
Die Pflicht, in der Margenrechnung ab HBM4 den Basisdie-Kostenblock getrennt zu führen.

## Trägt nicht
Das Vorzeichen des Nettoeffekts auf die Marge. Im Projekt als leicht positiv eingeschätzt, solange DRAM-Fertigung und Stapeln der Engpass bleiben; das ist ein Urteil, keine Rechnung. Prozessknoten und der berichtete Plan, dass Nvidia ab 2. Hj. 2027 einen eigenen Basisdie entwirft, sind nicht nachgeprüft.

## Bruchindikator
Ein Speicherhersteller weist sinkende HBM-Bruttomarge bei steigendem HBM-ASP aus, oder ein Kunde bezieht den Basisdie direkt und kauft nur noch Stapel.

## Ablesung
Herstellerangaben in Calls und Präsentationen, Tier 1a; Micron-Aussage zu Margen aus einem Earnings Call, im Report mit widersprüchlichem Datum, nicht nachgeprüft.

## Verknüpft
- [backend-and-base-die-are-separate-capacity](../../memory_supply/rules/backend-and-base-die-are-separate-capacity.md)
- [cowos-capacity-and-package-area](../../compute_bottlenecks/mechanisms/cowos-capacity-and-package-area.md)
- [yield-trough](../../memory_supply/axioms/yield-trough.md)
- [tools-need-stated-preconditions](../../analysis_method/rules/tools-need-stated-preconditions.md)
