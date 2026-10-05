---
id: hybrid-bonding-forced-by-stack-height
typ: mechanismus
status: vorschlag
thema: knowledge/memory_technology_roadmap
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Report Speicher-Roadmap nach HBM4E (Stichtag 26.07.2026), eingetragen 2026-10-06
verweist_auf: [yield-trough, stacked-yield-is-decomposed, only-hbm4-is-jedec-standard]
---

# Hybrid Bonding kommt graduell und später; die Stapelhöhe erzwingt es

## Aussage
Stand der Verfahren: SK Hynix MR-MUF (alle Lagen in einem Schritt verlötet und vergossen), Samsung und Micron TC-NCF (Lage für Lage gepresst). Kupfer-Kupfer-Direktbonden war für HBM4 erwartet und kam nicht; berichtet wird die Einführung bei 16-Hi HBM4E bis 20-Hi HBM5, Spanne 2026 bis 2029.

Der Zwang kommt aus der Geometrie: die Packagehöhe ist begrenzt (775 µm). 16-Hi verlangt Dies von rund 30 µm (12-Hi rund 50 µm). Ab 20 bis 24 Lagen passen die Unterfüllschichten nicht mehr in die Höhe, und die Wärme aus den mittleren Dies kommt nicht heraus. Gegenkraft: JEDEC erwägt, die Höhengrenze für 20-Hi anzuheben, was den Zwang verschiebt.

## Trägt
Der Verfahrenswechsel ist ein gradueller Übergang mit Koexistenz über mehrere Generationen, kein Umschlag. Der Vorsprung bei MR-MUF hält so lange, wie die Höhengrenze konventionelles Bonden zulässt.

## Trägt nicht
Einen Termin; die Quellen widersprechen sich. Yieldangaben je Stapelhöhe sind Branchendienste, Warnsignal.

## Bruchindikator
Ein Hersteller liefert einen 16-Hi- oder 20-Hi-Stapel mit Hybrid Bonding im Volumen, oder JEDEC hebt die Höhengrenze an.

## Ablesung
JEDEC (Höhengrenze), Tier 1b; Herstellerangaben zu Verfahren, Tier 1a. Zeitpunkte aus Branchendiensten, Warnsignal. Aus dem Projekt-Report übernommen, nicht nachgeprüft.

## Verknüpft
- [yield-trough](../../memory_supply/axioms/yield-trough.md)
- [stacked-yield-is-decomposed](../../memory_supply/rules/stacked-yield-is-decomposed.md)
- [only-hbm4-is-jedec-standard](../findings/only-hbm4-is-jedec-standard.md)
