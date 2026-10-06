---
id: comfyui-local
bereich: tools/image_generation
stand: 2026-10-06
herkunft: Claude-Code-Sitzung, Projekt ai_use_cases_overview, 2026-10-06
sprache: bash
---

# Lokale Bildgenerierung mit ComfyUI auf einer 24-GB-Workstation

## Zweck
Bilder ohne API-Kosten und ohne Bildlimit auf einer eigenen GPU erzeugen und über
die HTTP-API von ComfyUI für einen Skill oder ein Skript bereitstellen.

Dieser Eintrag ist kein Skript, sondern eine Einrichtung (wie `tools/general/yt-dlp-windows`).
ComfyUI und die Modelle sind fremde Software; hier steht, welche Modelle auf 24 GB passen,
welche Lizenz sie haben und wie die Einrichtung in einem Klinik-Netz mit TLS-Inspektion gelingt.

## Wann verwenden, wann nicht
Verwenden: viele Bilder, unveröffentlichtes Material, das im Haus bleiben soll, oder kein Budget für eine Bild-API.

Nicht verwenden: wenige Bilder ohne eigene GPU (eine API ist dann einfacher), oder kommerzielle
Nutzung mit FLUX.2 [dev] (Lizenz nur nicht-kommerziell; dann FLUX.2 [klein] 4B oder Qwen-Image, beide Apache 2.0).

| Modell | Lizenz | VRAM | Quelle der Angabe |
|---|---|---|---|
| FLUX.2 [dev] FP8 | nicht-kommerziell | ~24 GB | Ratgeber 2026 [V] |
| FLUX.2 [klein] 4B | Apache 2.0 | 12–16 GB | Ratgeber 2026 [V] |
| Qwen-Image | Apache 2.0 | ab 16 GB | Ratgeber 2026 [V] |

[V] = Herstellerangabe oder Ratgeber, hier nicht gemessen.

## Aufruf
Nach der Installation (siehe [INSTALL.md](INSTALL.md)):

```bash
curl -s http://127.0.0.1:8188/system_stats
```

Bildauftrag: in ComfyUI einen Workflow über **Workflow → Export (API)** als JSON speichern
und per `POST /prompt` mit geändertem Prompt abschicken, Ergebnis über `/view` abholen.

## Eingabe und Ausgabe
Eingabe: Textprompt (und optional ein Workflow-JSON). Ausgabe: PNG in `ComfyUI/output/`.

## Teststand
Nicht getestet. Die Anleitung wurde ohne Zugriff auf die Workstation geschrieben.
Erster Lauf auf der A5000 steht aus; danach hier Datum, Umgebung und Ergebnis eintragen.

## Grenzen
- Im Klinik-Netz scheitern Downloads ohne installiertes Stammzertifikat (INSTALL.md, Schritt 0).
- ComfyUI hat keine Anmeldung; nur an `127.0.0.1` binden oder per SSH-Tunnel nutzen.
- „Bestes offenes Modell“ ist ein Community-Urteil, kein kontrollierter Benchmark.
- Der Skill, der die API anspricht, ist noch nicht gebaut.
