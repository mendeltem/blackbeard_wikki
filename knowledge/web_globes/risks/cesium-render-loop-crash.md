---
id: cesium-render-loop-crash
typ: risiko
status: getragen
thema: knowledge/web_globes
stand: 2026-10-07
herkunft: Chat Earth Digital Twin (claude.ai), 2026-10-02
verweist_auf: [cesium-api-drift]
---

# Cesium-Dauerrendern plus Hover-Umstyling crasht nach Minuten: "RangeError: Too many properties to enumerate"

## Aussage
Ein CesiumJS-Globus (1.95, cdnjs) mit Standard-Renderloop (60 fps durchgehend)
und einer Hover-Hervorhebung, die bei jedem Länderwechsel das `material` der
GeoJSON-Polygone neu setzt, stürzt nach einigen Minuten Nutzung ab:
Dialog "An error occurred while rendering. Rendering has stopped.",
`RangeError: Too many properties to enumerate`. Der Fehler ist im
Cesium-Forum als Crash unter GPU-/Speicherdruck bekannt, ohne geklärte
Einzelursache.

Gegenmittel (im Projekt eingebaut, Wirkung nicht nachgemessen, deshalb hier
als Annahme):
1. `requestRenderMode: true` plus `maximumRenderTimeInterval`, rendern nur
   bei Änderung statt durchgehend; nach eigenen Änderungen `scene.requestRender()`.
2. Hover nicht per Umstyling der Länder-Entities, sondern eine einzige
   wiederverwendete Highlight-Entity mit `CallbackProperty`-Hierarchie;
   das vermeidet Geometrie-Neubauten bei jedem Grenzübertritt.
3. `scene.renderError.addEventListener` mit Neustart des Renderloops
   (`viewer.useDefaultRenderLoop = true`) statt des blockierenden Dialogs
   (`showRenderLoopErrors: false`).

## Trägt
Jede länger offene Cesium-Seite mit Hover-Interaktion über viele Polygone
(Globus mit Länder-Tooltips, Supply-Atlas-artige Seiten, Dashboards).

## Trägt nicht
Kurz geöffnete Seiten; der Crash brauchte Minuten. Nicht-Cesium-Globen
(three.js, eigene Canvas-Renderer).

## Bruchindikator
Crash tritt trotz der drei Gegenmittel weiter auf; dann liegt die Ursache
woanders (Treiber, WebGL-Kontextverlust) und dieser Eintrag greift zu kurz.

## Ablesung
Eigener Vorfall 2026-10-02 (Screenshot des Dialogs), reproduziert beim
Nutzer auf normalem Laptop. Forum: community.cesium.com Thread 45760
"Crashes after launch: Too many properties to enumerate" (2026-04), dort
ebenfalls ohne Auflösung. Gegenmittel: Cesium-Doku zu requestRenderMode
(Tier 1b), Wirksamkeit bei uns blind.

## Verknüpft
- [cesium-api-drift](../rules/cesium-api-drift.md)
