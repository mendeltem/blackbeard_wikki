# Installation

## Geprüfte Umgebung

`vram_plan.py` und Tests: Ubuntu 26.04, Python 3.14.4, nur Standardbibliothek,
keine GPU. Unsloth selbst ist in dieser Umgebung **nicht** installiert worden.

## Abhängigkeiten

- `vram_plan.py`: Python 3.9+, keine Pakete.
- Training laut Unsloth-Doku (Stand 2026-10-06): Linux oder Windows, Python
  3.10 bis 3.13 (3.14 nicht unterstützt), NVIDIA-GPU mit CUDA Capability ab
  7.0, CUDA 12.4+ (12.8+ für Blackwell), `unsloth` aus PyPI; torch wird über
  `--torch-backend=auto` passend gewählt.

## Schritte

Training, in eigener Umgebung (nicht in die System-Python installieren):

```bash
python3.12 -m venv ~/unsloth_env          # oder: uv venv --python 3.12 ~/unsloth_env
source ~/unsloth_env/bin/activate
pip install --upgrade pip && pip install uv
uv pip install unsloth --torch-backend=auto
python -c "import unsloth"                # muss ohne Fehler durchlaufen
```

Der Download umfasst torch mit CUDA, mehrere GB. Bei langsamer Leitung
`UV_HTTP_TIMEOUT=300` setzen.

Export nach Ollama braucht ein installiertes Ollama; den GGUF-Schritt erledigt
Unsloth selbst.
