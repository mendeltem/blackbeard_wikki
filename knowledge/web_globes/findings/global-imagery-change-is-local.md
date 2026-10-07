---
id: global-imagery-change-is-local
typ: befund
status: getragen
thema: knowledge/web_globes
stand: 2026-10-07
herkunft: Chat Earth Digital Twin (claude.ai), 2026-10-02
verweist_auf: [free-satellite-tile-sources]
---

# Historische Satellitenbilder wirken auf Globus-Zoom statisch; sichtbarer Wandel braucht Hotspots und Split-Vergleich

## Aussage
Ein Jahr-Schieberegler über NASA-GIBS-Tagesbilder (MODIS, ~250 m) zeigt auf
globaler Zoomstufe fast keinen Unterschied zwischen z. B. 2003 und 2019:
was sich global sichtbar ändert, sind Wolken und Schneelage, nicht die
Landoberfläche. Der Nutzer liest das als "funktioniert nicht".

Wandel wird sichtbar durch drei Mittel zusammen:
1. **Hotspots anfliegen**, an denen die Änderung die Kachelauflösung
   übersteigt: Aralsee (45.2 N, 59.4 O), Küste Dubai (25.05 N, 55.2 O),
   Rondônia/Amazonas (-10.5 S, -63.5 W), Lake Mead (36.2 N, -114.6 W),
   Drei-Schluchten-Stausee (30.8 N, 111.0 O), Las Vegas (36.12 N, -115.17 W).
2. **Split-Screen**: historische Ebene mit `splitDirection` links, aktuelle
   Esri-Ebene rechts, Trennlinie per Maus; der Unterschied springt ins Auge,
   wo Nebeneinander-Umschalten unsichtbar bleibt.
3. **Monatswahl** statt fester Jahresmitte: Januar gegen Juli macht
   Saisonalität (Schnee, Vegetation) auch global sichtbar.

## Trägt
Jede Zeitreisen-Funktion auf Globus- oder Kartenseiten (Earth Digital Twin,
Atlas-Seiten mit Vorher/Nachher). Allgemeiner: ein Regler, dessen Effekt
unterhalb der Darstellungsauflösung liegt, braucht kuratierte Beispiele,
sonst gilt das Feature als kaputt.

## Trägt nicht
Hochauflösende historische Stapel (z. B. Google Earth Engine, Landsat auf
30 m serverseitig gerendert); dort ist Wandel auch ohne Hotspot-Kuratierung
sichtbar. Statistische Änderungsdetektion; hier geht es nur um Wahrnehmung.

## Bruchindikator
Eine frei nutzbare Kachelquelle mit hochauflösenden Jahresmosaiken; dann
entfällt die Begründung über die 250-m-Grenze.

## Ablesung
Eigene Beobachtung im Chat 2026-10-02 (Nutzerrückmeldung "doesn't change
much", danach Umbau auf Hotspots plus Split). Hotspot-Koordinaten sind die
im Projekt verbauten Werte, Änderungsgeschichte der Orte allgemeinkundig.

## Verknüpft
- [free-satellite-tile-sources](free-satellite-tile-sources.md)
