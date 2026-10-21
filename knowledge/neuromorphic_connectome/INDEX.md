# neuromorphic_connectome

Ob ein echtes Konnektom als rekurrentes Substrat etwas traegt, das ein
Zufallsgraph gleicher Dichte nicht traegt. Nur oeffentliche Daten:
FlyWire-abgeleitete `fly783.csr` (138.639 Neuronen, 15.091.983 Kanten) und
das Free Spoken Digit Dataset (FSDD, 6 Sprecher, oeffentlich).

Die Frage ist bewusst eng gestellt. Nicht "kann man damit rechnen", sondern
**"traegt die konkrete biologische Verdrahtung selbst einen Vorteil"**. Dafuer
gehoert zu jedem Lauf ein Nullarm: grad-erhaltend (`dp`) und Erdoes-Renyi
(`er`) mit gleicher Neuronen- und Kantenzahl.

Der rote Faden: **ein Ergebnis ohne Nullarm ist kein Ergebnis.** Und ein
Vorteil, der innerhalb der Seed-Streuung liegt, ist keiner.

Stand 2026-10-21. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Das Fliegen-Konnektom traegt keinen Topologie-Vorteil, unter keiner Lernregel](findings/fly-connectome-topology-carries-no-advantage.md) | befund | getragen |
