---
id: cesium-api-drift
typ: regel
status: getragen
thema: knowledge/web_globes
stand: 2026-10-07
herkunft: Chat Earth Digital Twin (claude.ai), 2026-10-02
verweist_auf: [cesium-render-loop-crash, free-satellite-tile-sources]
---

# Cesium-Version pinnen und API-Drift einpreisen: .otherwise ist weg, SplitDirection wurde umbenannt

## Aussage
KI-generierter Cesium-Code mischt regelmäßig API-Stände. Zwei Fallen, die
bei uns real auftraten oder abgefangen wurden:

1. Seit Cesium 1.92 (2022) sind die when.js-Promises durch native ersetzt:
   `.otherwise(...)` existiert nicht mehr, es heißt `.catch(...)`.
   Symptom: `TypeError: ... .otherwise is not a function` erst zur Laufzeit,
   die Seite bleibt halb initialisiert (bei uns: Grenzen und Hover fehlten).
2. `ImagerySplitDirection` heißt in neueren Versionen `SplitDirection`,
   `scene.imagerySplitPosition` wurde zu `scene.splitPosition`.
   Robust: `const SPLIT = Cesium.SplitDirection || Cesium.ImagerySplitDirection`
   und Schreiben über `"splitPosition" in scene`.

Regel: Die CDN-Version im `<script>`-Tag ist die Wahrheit, nicht das
Trainingswissen des Agenten. Version explizit pinnen (z. B. 1.95 auf cdnjs,
`window.CESIUM_BASE_URL` setzen), bei Laufzeit-TypeErrors auf entfernte
Methoden zuerst die Migrationsliste der gepinnten Version prüfen, und
umbenannte Enums per Oder-Fallback abfangen.

## Trägt
Jede Einzeldatei-Seite, die Cesium (oder eine andere schnell wandernde
Bibliothek) vom CDN lädt und von einem Agenten geschrieben oder geändert wird.

## Trägt nicht
Gebundelte Projekte mit package.json und Typprüfung; dort fällt Drift beim
Build auf, nicht erst zur Laufzeit.

## Bruchindikator
Eine gepinnte Version, deren Kacheln oder Widgets gegen heutige Browser
brechen; dann zwingt der Pin selbst zum Upgrade und die Oder-Fallbacks
müssen mitwandern.

## Ablesung
Eigener Vorfall 2026-10-02: `.otherwise`-TypeError in der Konsole des
Nutzers, Fix auf `.catch` behob Grenzen und Hover. Promise-Umstellung in
1.92 laut Cesium-Changelog (Tier 1b). SplitDirection-Fallback eingebaut,
Umbenennung laut Changelog, bei uns nicht einzeln nachgestellt.

## Verknüpft
- [cesium-render-loop-crash](../risks/cesium-render-loop-crash.md)
- [free-satellite-tile-sources](../findings/free-satellite-tile-sources.md)
