---
id: unsloth-finetune
bereich: tools/llm/finetuning
stand: 2026-10-06
herkunft: Claude-Code-Sitzung Victus
sprache: prompt, python
---

# unsloth-finetune

## Zweck

Skill, der einen Agenten durch ein LoRA-Finetuning mit
[Unsloth](https://github.com/unslothai/unsloth) auf einer kleinen GPU fuehrt:
lohnt es sich ueberhaupt, Abnahme vorher, GPU frei machen, Modellgroesse
waehlen, Daten, Training, Messen, Export nach Ollama. Dazu `vram_plan.py`, das
aus den Unsloth-Tabellen ausrechnet, welche Modellgroesse in den VRAM passt.

## Wann verwenden, wann nicht

Verwenden: ein lokales Modell soll eine enge, wiederkehrende Aufgabe lernen,
Prompting wurde gemessen und reicht nicht, es gibt einige hundert Beispiele.

Nicht verwenden: fuer neues Wissen oder aktuelle Fakten; fuer eine Weiche
zwischen wenigen Zielen (dafuer ein Entscheidungsmodell); fuer grosse
MoE-Modelle auf kleinen GPUs (Qwen3.5/3.6-35B-A3B braucht rund 74 GB).

## Aufruf

Skill: `src/SKILL.md` in den Skill-Ordner des Agenten legen (Claude Code,
Hermes: `~/.hermes/skills/<kategorie>/unsloth-finetune/SKILL.md`), oder im
Chat darauf verweisen.

VRAM-Plan:

```bash
python3 src/vram_plan.py --vram 8
python3 src/vram_plan.py --vram 8 --familie qwen3.5 --reserve 1.5 --json
```

## Eingabe und Ausgabe

`vram_plan.py`: GB VRAM, Familie (`allgemein` oder `qwen3.5`), Reserve in GB.
Ausgabe je Verfahren die passenden Groessen, die groesste und die naechste zu
grosse Stufe; als Text oder JSON. Beispiel fuer 8 GB:

```
8.0 GB VRAM, 1.0 GB Reserve -> 7 GB frei (qwen3.5)
  bf16-lora bis 2B  (passt: 0.8B, 2B)
            naechste Stufe 4B braucht 10 GB
```

## Teststand

2026-10-06, Victus (Ubuntu 26.04, Python 3.14.4, keine GPU noetig):
`python3 -m unittest discover -s tests` - 9 Tests bestanden.

Nicht geprueft: das Training selbst. Unsloth ist auf Victus nicht installiert;
die Code-Schritte im Skill stammen aus der Unsloth-Dokumentation.

## Grenzen

- Die VRAM-Zahlen sind Herstellerangaben (Unsloth-Doku, Stand 2026-10-06),
  nicht gemessen. Laengere Sequenzen oder groessere Batches brauchen mehr.
- Unsloth benennt Seiten und Parameter haeufig um; vor dem Einsatz die
  Doku der gewaehlten Modellfamilie gegenlesen.
- Studio (Web-Oberflaeche) steht teilweise unter AGPL-3.0, der Kern unter
  Apache-2.0.
