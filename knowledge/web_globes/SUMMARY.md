# web_globes: Kurzstand

Stand 2026-10-07. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Wie man 3D-Globen und Karten als Einzeldatei-HTML baut, ohne API-Keys und ohne an Cesium zu scheitern.

**Kachelquellen (getragen):** Esri World Imagery (Satellit bis Level 19), Esri Reference (Labels) und NASA GIBS MODIS (Tagesbilder ab 2000-02-24, Datum in der URL, Level 9) laufen ohne Key per `UrlTemplateImageryProvider`. Google-Earth-Bilder brauchen einen bezahlten Key; Esri ist der freie Ersatz. Länderpolygone mit ISO3 ohne Hosting: datamaps worldTopo (TopoJSON, cdnjs).

**Cesium-Fallen:** Dauerrendern plus Hover-Umstyling der Polygone crasht nach Minuten (RangeError: Too many properties to enumerate); Gegenmittel requestRenderMode, eine wiederverwendete Highlight-Entity, renderError-Neustart (Wirkung nicht nachgemessen). API-Drift: `.otherwise` → `.catch` (seit 1.92), `ImagerySplitDirection` → `SplitDirection`; CDN-Version pinnen, Enums per Oder-Fallback.

**Darstellung:** Zeitreise über MODIS wirkt global statisch (nur Wolken/Schnee ändern sich). Sichtbarer Wandel braucht kuratierte Hotspots (Aralsee, Dubai, Rondônia, Lake Mead, Drei Schluchten, Las Vegas), Split-Screen-Vergleich gegen heute und Monatswahl.

**Offen:** nichts.

**Lesen bei:** Globus, Weltkarte, Cesium, Satellitenbilder, Kacheln, Supply Atlas, Earth Digital Twin, Zeitreise, Vorher/Nachher.
