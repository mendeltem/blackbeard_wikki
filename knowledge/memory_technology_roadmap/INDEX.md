# memory_technology_roadmap

Wohin sich Speichertechnik nach HBM4 entwickelt: was standardisiert ist und was nur Projektion, Bondverfahren, Basisdie, High Bandwidth Flash, 3D-DRAM. Die Mengen- und Flächenrechnung steht in [memory_supply](../memory_supply/INDEX.md), die Lastseite in [ai_demand_drivers](../ai_demand_drivers/INDEX.md).

Quellenlage: ein Recherche-Report des Projekts SK Hynix (Stichtag 26.07.2026), der sich zu großen Teilen auf Branchendienste, Herstellerfolien und eine akademische Roadmap stützt. Deshalb alles `vorschlag`. Was Standard ist und was Projektion, steht je Eintrag.

Stand 2026-10-06. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Nur HBM4 ist standardisiert, alles ab HBM5 ist Projektion](findings/only-hbm4-is-jedec-standard.md) | befund | vorschlag |
| [High Bandwidth Flash: angekündigt und simuliert, nicht als Silizium gemessen](findings/hbf-announced-not-demonstrated.md) | befund | vorschlag |
| [Der HBM-Basisdie wird ein Logikprodukt und verschiebt Wertschöpfung zur Foundry](mechanisms/base-die-shifts-value-to-foundry.md) | mechanismus | vorschlag |
| [Hybrid Bonding kommt graduell und später; die Stapelhöhe erzwingt es](mechanisms/hybrid-bonding-forced-by-stack-height.md) | mechanismus | vorschlag |
| [3D-DRAM ist der eine binäre Umschlag: er kann die Rangfolge neu ordnen](risks/three-d-dram-binary-reordering.md) | risiko | vorschlag |
