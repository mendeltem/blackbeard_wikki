---
id: free-satellite-tile-sources
typ: befund
status: getragen
thema: knowledge/web_globes
stand: 2026-10-07
herkunft: Chat Earth Digital Twin (claude.ai), 2026-10-02
verweist_auf: [cesium-api-drift, global-imagery-change-is-local]
---

# Echte Satellitenbilder im Browser ohne API-Key: Esri World Imagery und NASA GIBS

## Aussage
Drei Kachelquellen liefern ohne Anmeldung, Token oder Key echte Satelliten-
und Referenzbilder als XYZ/WMTS-Kacheln, direkt aus dem Browser:

1. **Esri World Imagery** (aktuelle Satelliten-/Luftbilder, bis Straßenebene,
   maximumLevel 19):
   `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`
2. **Esri Reference** (Grenzen und Ortsnamen als transparente Beschriftungsebene):
   `https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}`
3. **NASA GIBS, MODIS Terra TrueColor** (historische Tagesbilder ab 2000-02-24,
   ~250 m, maximumLevel 9, Datum steht in der URL):
   `https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Terra_CorrectedReflectance_TrueColor/default/{JJJJ-MM-TT}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg`

In CesiumJS genügt je Quelle ein `UrlTemplateImageryProvider`. Google-Earth-
Bildmaterial ist dagegen nur mit bezahltem API-Key nutzbar; Esri ist der
freie Ersatz mit sehr ähnlichem Bild.

Länderpolygone mit ISO3-Ids ohne eigenes Hosting: `Datamap.prototype.worldTopo`
aus datamaps 0.5.9 (cdnjs) plus topojson 1.6.9 liefert Natural-Earth-Grenzen
als eingebettetes TopoJSON; daraus lässt sich die Hover-Ebene eines Globus
bauen, ohne eine GeoJSON-Datei auszuliefern.

## Trägt
Jede Einzeldatei-HTML-Seite mit 3D-Globus oder Karte, die ohne Build und ohne
Secrets auskommen soll (Earth Digital Twin, Kartenprojekte). GIBS trägt
Zeitreihen: das Datum in der URL macht jede Tageskachel seit 2000 adressierbar.

## Trägt nicht
Offline-Betrieb; die Kacheln werden gestreamt. Esri nennt keine harte, aber
eine Fair-Use-Grenze, für Massenabruf (Tile-Scraping) nicht geeignet. GIBS
Level 9 reicht nicht für Stadtdetails. Lizenzlage für kommerzielle
Einbettung hier nicht geprüft.

## Bruchindikator
HTTP 403/404 auf den Template-URLs oder eine Esri-Ankündigung, World Imagery
hinter einen Key zu legen.

## Ablesung
Eigene Nutzung im Chat Earth Digital Twin, 2026-10-02: alle drei Quellen
gerendert (Screenshots). URL-Muster sind Herstellerdoku (Tier 1b),
Verfügbarkeitsbeginn MODIS 2000-02-24 laut NASA-GIBS-Doku.

## Verknüpft
- [cesium-api-drift](../rules/cesium-api-drift.md)
- [global-imagery-change-is-local](global-imagery-change-is-local.md)
