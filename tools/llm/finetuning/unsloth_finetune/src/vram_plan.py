#!/usr/bin/env python3
"""vram_plan - welche Modellgroesse passt zum Finetuning mit Unsloth auf diese GPU?

    python3 vram_plan.py --vram 8
    python3 vram_plan.py --vram 8 --familie qwen3.5 --reserve 1.5
    python3 vram_plan.py --vram 24 --json

Die Zahlen sind Herstellerangaben aus der Unsloth-Dokumentation (Stand
2026-10-06), nicht gemessen. Zwei Tabellen:

  allgemein  QLoRA 4-bit und LoRA 16-bit je Modellgroesse
  qwen3.5    nur bf16-LoRA: Unsloth raet bei Qwen3.5 (dicht und MoE) von
             QLoRA ab, wegen hoeherer Quantisierungsabweichung

--reserve zieht ab, was die GPU nebenher braucht (Desktop, Treiber). Ein
geladenes Inferenzmodell (Ollama, llama-server) muss vorher entladen werden;
das ist nicht eingerechnet.
"""

import argparse
import json
import sys

# Modellgroesse in Mrd. Parametern -> GB VRAM
ALLGEMEIN = {
    "qlora": {3: 3.5, 7: 5, 8: 6, 9: 6.5, 11: 7.5, 14: 8.5, 27: 22, 32: 26, 40: 30, 70: 41, 81: 48, 90: 53, 405: 237},
    "lora16": {3: 8, 7: 19, 8: 22, 9: 24, 11: 29, 14: 33, 27: 64, 32: 76, 40: 96, 70: 164, 81: 192, 90: 212, 405: 950},
}
QWEN35_BF16 = {"0.8B": 3, "2B": 5, "4B": 10, "9B": 22, "27B": 56, "35B-A3B": 74, "122B-A10B": 256}
QUELLE = {
    "allgemein": "https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements",
    "qwen3.5": "https://unsloth.ai/docs/models/qwen3.5/fine-tune",
}


def plan(vram_gb, familie="allgemein", reserve_gb=1.0):
    """Was passt? Gibt je Verfahren die passenden Groessen und die groesste zurueck."""
    if vram_gb <= 0 or reserve_gb < 0:
        raise ValueError("vram muss > 0 und reserve >= 0 sein")
    frei = vram_gb - reserve_gb
    if familie == "qwen3.5":
        tabellen = {"bf16-lora": QWEN35_BF16}
    elif familie == "allgemein":
        tabellen = {f"{k}": {f"{g}B": v for g, v in t.items()} for k, t in ALLGEMEIN.items()}
    else:
        raise ValueError(f"unbekannte Familie: {familie}")
    ergebnis = {"vram_gb": vram_gb, "reserve_gb": reserve_gb, "frei_gb": frei, "familie": familie,
                "quelle": QUELLE[familie], "verfahren": {}}
    for verfahren, tabelle in tabellen.items():
        passt = [(g, v) for g, v in tabelle.items() if v <= frei]
        ergebnis["verfahren"][verfahren] = {
            "passt": [g for g, _ in passt],
            "groesste": passt[-1][0] if passt else None,
            "naechste_zu_gross": next(({"modell": g, "braucht_gb": v} for g, v in tabelle.items() if v > frei), None),
        }
    return ergebnis


def text(e):
    zeilen = [f"{e['vram_gb']} GB VRAM, {e['reserve_gb']} GB Reserve -> {e['frei_gb']:g} GB frei ({e['familie']})"]
    for verfahren, r in e["verfahren"].items():
        if r["groesste"]:
            zeilen.append(f"  {verfahren:9} bis {r['groesste']}  (passt: {', '.join(r['passt'])})")
        else:
            zeilen.append(f"  {verfahren:9} nichts passt")
        if r["naechste_zu_gross"]:
            n = r["naechste_zu_gross"]
            zeilen.append(f"            naechste Stufe {n['modell']} braucht {n['braucht_gb']} GB")
    zeilen.append(f"  Quelle (Herstellerangabe, nicht gemessen): {e['quelle']}")
    return "\n".join(zeilen)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Unsloth: welche Modellgroesse passt in den VRAM?")
    ap.add_argument("--vram", type=float, required=True, help="GB VRAM der GPU")
    ap.add_argument("--familie", choices=["allgemein", "qwen3.5"], default="allgemein")
    ap.add_argument("--reserve", type=float, default=1.0, help="GB, die nebenher belegt sind (Standard 1)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    e = plan(a.vram, a.familie, a.reserve)
    print(json.dumps(e, ensure_ascii=False, indent=1) if a.json else text(e))
    return 0


if __name__ == "__main__":
    sys.exit(main())
