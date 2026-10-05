"""Tests fuer vram_plan.py. Keine GPU noetig."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))
import vram_plan  # noqa: E402


class TestPlan(unittest.TestCase):
    def test_8gb_laptop(self):
        # RTX 4070 Laptop 8 GB, 1 GB Reserve: QLoRA bis 9B, 16-bit-LoRA nichts
        e = vram_plan.plan(8, "allgemein", 1.0)
        self.assertEqual(e["verfahren"]["qlora"]["groesste"], "9B")
        self.assertIsNone(e["verfahren"]["lora16"]["groesste"])
        self.assertEqual(e["verfahren"]["lora16"]["naechste_zu_gross"], {"modell": "3B", "braucht_gb": 8})

    def test_8gb_qwen35_nur_bf16(self):
        e = vram_plan.plan(8, "qwen3.5", 1.0)
        self.assertEqual(list(e["verfahren"]), ["bf16-lora"])
        self.assertEqual(e["verfahren"]["bf16-lora"]["passt"], ["0.8B", "2B"])
        self.assertEqual(e["verfahren"]["bf16-lora"]["naechste_zu_gross"]["modell"], "4B")

    def test_grenze_genau_gleich_passt(self):
        e = vram_plan.plan(6.5, "allgemein", 0)
        self.assertEqual(e["verfahren"]["qlora"]["groesste"], "9B")

    def test_reserve_kann_alles_verdraengen(self):
        e = vram_plan.plan(4, "allgemein", 1.0)
        self.assertIsNone(e["verfahren"]["qlora"]["groesste"])

    def test_moe_qwen_braucht_viel(self):
        e = vram_plan.plan(80, "qwen3.5", 1.0)
        self.assertEqual(e["verfahren"]["bf16-lora"]["groesste"], "35B-A3B")

    def test_ungueltig(self):
        with self.assertRaises(ValueError):
            vram_plan.plan(0)
        with self.assertRaises(ValueError):
            vram_plan.plan(8, "llama")

    def test_tabellen_monoton(self):
        # groessere Modelle duerfen nie weniger brauchen; faengt Tippfehler in den Tabellen
        for t in list(vram_plan.ALLGEMEIN.values()) + [vram_plan.QWEN35_BF16]:
            werte = list(t.values())
            self.assertEqual(werte, sorted(werte))
        for g in vram_plan.ALLGEMEIN["qlora"]:
            self.assertLess(vram_plan.ALLGEMEIN["qlora"][g], vram_plan.ALLGEMEIN["lora16"][g])


class TestAufruf(unittest.TestCase):
    def test_cli_json(self):
        r = subprocess.run([sys.executable, str(SRC / "vram_plan.py"), "--vram", "8", "--json"],
                           capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(r.stdout)["verfahren"]["qlora"]["groesste"], "9B")

    def test_cli_text(self):
        r = subprocess.run([sys.executable, str(SRC / "vram_plan.py"), "--vram", "8", "--familie", "qwen3.5"],
                           capture_output=True, text=True, check=True)
        self.assertIn("bis 2B", r.stdout)
        self.assertIn("Herstellerangabe", r.stdout)


if __name__ == "__main__":
    unittest.main()
