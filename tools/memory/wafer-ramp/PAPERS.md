# Quellen und Methode

## Methode
Logistische Kurve (Verhulst), auf zwei Eckpunkte normiert. Kein Fit, keine Schaetzung aus Daten: Die Form ist gesetzt, die Endpunkte sind gemeldet.

    f(i) = 1 / (1 + exp(-k (i - mitte)))
    wert(i) = start + (ziel - start) * (f(i) - f(0)) / (f(n) - f(0))

Fuer Hochlaufkurven in der Halbleiterfertigung gibt es keine allgemein anerkannte Parametrisierung; k und die Lage der Mitte sind Annahmen und deshalb Parameter.

## Daten, die als Eckpunkte benutzt wurden
- SK Hynix M15X: Serienstart Februar 2026, 10k Wafer je Monat, Vollausbau 55k bis 60k Ende 2026. Firmenangaben und Branchendienste, kein Tier-1a-Beleg fuer den Monatsverlauf.
- GB je Wafer, Tauschverhaeltnis HBM gegen DDR5: Faustzahlen aus Branchendiensten, siehe knowledge/memory_supply/mechanisms/hbm-eats-wafer-area.md.

## Keine DOI
Dieses Tool stuetzt sich auf keine peer-reviewte Arbeit.
