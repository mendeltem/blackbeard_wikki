# web_globes

3D-Globen und Karten als Einzeldatei-HTML im Browser: freie Kachelquellen
ohne API-Key, Cesium-Fallen, Darstellung von Wandel über die Zeit.

Abgrenzung zu [ai_application_layer](../ai_application_layer/INDEX.md): dort
steht, was auf den Atlas-Seiten inhaltlich gezeigt wird; hier steht, wie man
solche Seiten technisch baut, ohne an Keys, API-Drift oder Renderlast zu
scheitern.

Stand 2026-10-07. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Freie Satelliten-Kachelquellen ohne API-Key](findings/free-satellite-tile-sources.md) | befund | getragen |
| [Historischer Wandel ist nur lokal sichtbar: Hotspots und Split-Vergleich](findings/global-imagery-change-is-local.md) | befund | getragen |
| [Cesium-Dauerrendern plus Hover-Umstyling crasht](risks/cesium-render-loop-crash.md) | risiko | getragen |
| [Cesium-Version pinnen, API-Drift einpreisen](rules/cesium-api-drift.md) | regel | getragen |

## Herkunft

Alle Einträge stammen aus dem Chat Earth Digital Twin (claude.ai,
2026-10-02): ein 3D-Globus als einzelne HTML-Datei mit Esri-Satellitenbildern,
Länder-Hover mit Wirtschaftsdaten (inkl. Export/Import), NASA-GIBS-Zeitreise
und Split-Vergleich. Verwandte Projekte: Supply Atlas 3D, erde-globus,
karten-simulation.
