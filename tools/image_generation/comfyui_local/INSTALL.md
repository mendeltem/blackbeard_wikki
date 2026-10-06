# Installation

## Geprüfte Umgebung
Noch keine. Geschrieben für Ubuntu 22.04/24.04, NVIDIA RTX A5000 (24 GB), Python 3.10+. Nicht ausgeführt (Stand 2026-10-06).

## 0. Vorab im Charité-Netz: Zertifikat und Proxy

Ohne diesen Schritt scheitern `apt`, `pip`, `git` und die Modell-Downloads von Hugging Face
mit Zertifikatsfehlern (Browser: „Potenzielles Sicherheitsrisiko“).

1. Charité-Stammzertifikat und Proxy-Adresse bei der Charité-IT anfragen.
2. Zertifikat systemweit installieren:
   ```bash
   sudo cp charite-root-ca.crt /usr/local/share/ca-certificates/
   sudo update-ca-certificates
   ```
3. Python und Hugging Face auf den Systemspeicher zeigen lassen (in `~/.bashrc`):
   ```bash
   export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
   export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
   # nur falls die IT einen Proxy vorgibt:
   # export http_proxy=http://PROXY:PORT
   # export https_proxy=http://PROXY:PORT
   ```
4. Test: `curl -I https://huggingface.co` muss `HTTP/2 200` liefern, ohne Zertifikatsfehler.

Nicht `--insecure`, `verify=False` oder `ssl_verify false` verwenden.

---

## 1. NVIDIA-Treiber prüfen

```bash
nvidia-smi
```

Erwartet: `RTX A5000`, 24564 MiB, und eine Treiberversion. Fehlt der Befehl:

```bash
sudo ubuntu-drivers install
sudo reboot
```

Ein separates CUDA-Toolkit ist nicht nötig: PyTorch bringt seine CUDA-Bibliotheken mit.

---

## 2. Grundpakete

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
```

---

## 3. ComfyUI installieren

Modelle sind groß (10–30 GB). Installationsort mit genug Platz wählen, z. B. `/data`:

```bash
df -h            # freien Platz prüfen, mindestens 100 GB empfohlen
cd /data         # oder ~ falls genug Platz
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
python3 -m venv venv
source venv/bin/activate
```

PyTorch mit CUDA installieren. Den aktuellen Befehl für „Linux / Pip / CUDA“ von
https://pytorch.org/get-started/locally/ nehmen, typischerweise:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install -r requirements.txt
```

GPU-Test:

```bash
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
# erwartet: True NVIDIA RTX A5000
```

---

## 4. Erster Start

```bash
cd /data/ComfyUI && source venv/bin/activate
python main.py --listen 127.0.0.1 --port 8188
```

Im Browser der Workstation: http://127.0.0.1:8188

---

## 5. Modell laden

### Welches Modell?

| Modell | Lizenz | VRAM | Wofür |
|---|---|---|---|
| FLUX.2 [dev] (FP8) | nicht-kommerziell | ~24 GB, knapp | beste Qualität, privat/Forschung |
| FLUX.2 [klein] 4B | Apache 2.0 | 12–16 GB | schnell, kommerziell erlaubt |
| Qwen-Image | Apache 2.0 | ab 16 GB | Text im Bild, kommerziell erlaubt |

Empfehlung zum Start: **FLUX.2 [klein] 4B** (lädt schnell, läuft sicher in 24 GB, freie Lizenz).
Danach bei Bedarf FLUX.2 [dev].

### Am sichersten über die eingebauten Vorlagen

1. In ComfyUI: Menü **Workflow → Browse Templates** (bzw. „Vorlagen“).
2. Vorlage für das gewünschte Modell (FLUX.2 oder Qwen-Image) öffnen.
3. ComfyUI zeigt an, welche Dateien fehlen, mit Download-Links und Zielordner
   (`models/diffusion_models`, `models/text_encoders`, `models/vae`).
4. Für FLUX.2 [dev]: vorher auf der Hugging-Face-Modellseite einloggen und die Lizenz akzeptieren.

Download per Kommandozeile (falls der Browser-Download nicht geht):

```bash
pip install -U "huggingface_hub[cli]"
hf auth login            # Token von https://huggingface.co/settings/tokens
hf download <repo> <datei> --local-dir models/diffusion_models
```

`<repo>` und `<datei>` aus dem Hinweis der Vorlage übernehmen.

### Test

Prompt eingeben, **Queue/Run** drücken. Das erste Bild dauert länger (Modell wird geladen).
Ergebnisse liegen in `ComfyUI/output/`.

---

## 6. ComfyUI als Dienst (startet automatisch)

`/etc/systemd/system/comfyui.service`:

```ini
[Unit]
Description=ComfyUI
After=network-online.target

[Service]
User=DEIN_LINUX_USER
WorkingDirectory=/data/ComfyUI
Environment=REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ExecStart=/data/ComfyUI/venv/bin/python main.py --listen 127.0.0.1 --port 8188
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now comfyui
systemctl status comfyui
```

---

## 7. API für den Skill freigeben

**Variante A – Claude Code läuft auf der Workstation (empfohlen):**
nichts weiter tun, `127.0.0.1:8188` genügt.

**Variante B – Zugriff von einem anderen Rechner:**
Port nicht ins Netz öffnen, sondern per SSH-Tunnel:

```bash
# auf dem anderen Rechner:
ssh -N -L 8188:127.0.0.1:8188 user@workstation
# danach dort erreichbar unter http://127.0.0.1:8188
```

ComfyUI hat keine Anmeldung. `--listen 0.0.0.0` würde die Oberfläche für das ganze
Netz öffnen; im Charité-Netz nur nach Absprache mit der IT.

### API-Test

```bash
curl -s http://127.0.0.1:8188/system_stats | python3 -m json.tool
```

Liefert GPU-Name und freien VRAM. Für Bild-Aufträge: in ComfyUI einen funktionierenden
Workflow über **Workflow → Export (API)** als JSON speichern. Diese Datei braucht der Skill.

---

## 8. Checkliste vor dem Skill

- [ ] `nvidia-smi` zeigt die A5000
- [ ] `torch.cuda.is_available()` ist `True`
- [ ] Ein Bild wurde in der Oberfläche erzeugt
- [ ] `curl http://127.0.0.1:8188/system_stats` antwortet
- [ ] Workflow als API-JSON exportiert

Danach: Skill `bild-generieren` anlegen, der den exportierten Workflow mit neuem Prompt an
`/prompt` schickt, auf das Ergebnis wartet und die PNG über `/view` herunterlädt.

---

## Fehlerbehebung

| Problem | Ursache / Lösung |
|---|---|
| `SSL: CERTIFICATE_VERIFY_FAILED` | Schritt 0, Charité-Zertifikat fehlt |
| `CUDA out of memory` bei FLUX.2 [dev] | FP8-Variante nehmen, Start mit `--lowvram`, andere GPU-Prozesse beenden |
| `torch.cuda.is_available()` = False | Treiber fehlt oder PyTorch ohne CUDA installiert (Schritt 1/3) |
| Erstes Bild sehr langsam | normal: Modell wird von der Platte in den VRAM geladen |
