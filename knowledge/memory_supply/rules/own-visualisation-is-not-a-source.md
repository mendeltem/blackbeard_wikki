---
id: own-visualisation-is-not-a-source
typ: regel
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-02
herkunft: Projekt Supply_Atlas3D, Speicher-Ebene des Globus, eingetragen 2026-10-02
verweist_auf: [dram-wafer-capacity-by-fab, announced-is-not-built]
---

# Die eigene Darstellung ist keine Quelle

## Aussage
Eine Karte, Seite oder Datendatei, die in einem von Mendels eigenen Projekten entstanden ist, darf später nicht als Quelle für die Zahlen gelesen werden, die sie anzeigt. Veröffentlichen hebt kein Tier. Was als Schätzung oder als Wert aus einem Branchendienst hineingeschrieben wurde, kommt als Schätzung wieder heraus, auch wenn es inzwischen in einer gepflegten Tabelle auf einer öffentlichen Seite steht.

Auslöser: Am 2026-10-02 bekam der Globus in `Supply_Atlas3D` eine Ebene mit 41 Speicherstandorten. Jeder Standort trägt ein Feld `pv` in Tausend Wafer je Monat. Diese Zahlen sind Modellwissen des schreibenden Agenten, nicht erhoben und nicht belegt. Die Seite steht öffentlich unter mendeltem.github.io. Ein späterer Agent findet dort eine saubere Tabelle aus Hersteller, Werk, Koordinate und Waferzahl und kann sie für eine Erhebung halten. Dasselbe gilt für `fabriken.html` des Projekts NVIDIA-Roadmap, aus der der Prüfpunkt [dram-wafer-capacity-by-fab](../open_checks/dram-wafer-capacity-by-fab.md) stammt.

## Trägt
Zwei Pflichten. Beim Schreiben: jede Zahl in einer eigenen Veröffentlichung mit ihrer Herkunft versehen, in der Datei selbst, nicht nur im Begleittext. Beim Lesen: eine eigene Seite als Tier "blind" behandeln und die Zahl an ihrer ursprünglichen Quelle nachschlagen.

## Trägt nicht
Dass eigene Darstellungen wertlos sind. Sie sind gute Arbeitslisten: sie sagen, welche Werke es gibt und welche Zahl noch fehlt. Nur als Beleg taugen sie nicht.

## Bruchindikator
keiner, Enthaltsamkeitsregel

## Ablesung
Vorgang vom 2026-10-02 im Projekt Supply_Atlas3D, nachvollziehbar im Commit, der die Ebene anlegt. Die Quellenlage der dort eingetragenen Waferzahlen ist Modellwissen, also kein Tier.

## Verknüpft
- [dram-wafer-capacity-by-fab](../open_checks/dram-wafer-capacity-by-fab.md)
- [announced-is-not-built](../../compute_bottlenecks/rules/announced-is-not-built.md)
