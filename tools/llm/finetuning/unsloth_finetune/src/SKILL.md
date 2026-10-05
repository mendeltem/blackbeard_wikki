---
name: unsloth-finetune
description: Ein Sprachmodell mit Unsloth per LoRA nachtrainieren, auf einer kleinen GPU (8-24 GB), und als GGUF in Ollama oder llama.cpp einsetzen. Verwenden, wenn ein lokales Modell eine enge, wiederkehrende Aufgabe (Format, Klassifikation, Stil, Fachsprache) zuverlaessig lernen soll und Prompting nachweislich nicht reicht. Nicht fuer neues Wissen oder aktuelle Fakten.
---

# Finetuning mit Unsloth auf kleiner GPU

Ablauf fuer einen Agenten. Die Codezeilen folgen der Unsloth-Dokumentation
(Stand 2026-10-06). In dieser Wiki-Umgebung gelaufen ist nur `vram_plan.py`
(siehe README), kein Training.

## 0. Erst pruefen, ob Finetuning das richtige Mittel ist

Finetuning lohnt nur, wenn alle drei gelten:
1. Die Aufgabe ist eng und wiederholt sich (gleiche Art Eingabe, gleiches Ausgabeformat).
2. Es gibt mindestens einige hundert gute Beispiele, oder sie lassen sich pruefbar erzeugen.
3. Ein kurzer Prompt mit zwei, drei Beispielen am Basismodell wurde **gemessen** und reicht nicht.

Nicht finetunen fuer: neues Wissen oder aktuelle Fakten (dafuer Suche oder
Dokumente im Kontext), eine Weiche zwischen wenigen Zielen (dafuer ein
Entscheidungsmodell wie Laya), oder wenn die Abnahme nur "klingt besser" waere.

## 1. Abnahme festlegen, bevor trainiert wird

- Testsatz: 10-20 % der Beispiele zurueckhalten, fest (z. B. per Hash des Textes), nie trainieren.
- Messgroesse maschinell: exakter Treffer, gueltiges JSON, Tests gruen, Label richtig.
  Kein Modell als Richter, wenn es sich vermeiden laesst.
- Basismodell mit demselben Prompt auf dem Testsatz messen. Das ist die Latte.

## 2. GPU frei machen

Ein Inferenzmodell im VRAM nimmt dem Training den Platz:

```bash
ollama ps && ollama stop <modell>        # oder llama-server beenden
nvidia-smi --query-compute-apps=pid,process_name,used_memory --format=csv
```

Mehr als nichts in der Liste: erst klaeren, dann trainieren.

## 3. Modellgroesse waehlen

```bash
python3 src/vram_plan.py --vram 8                     # QLoRA / 16-bit-LoRA, allgemein
python3 src/vram_plan.py --vram 8 --familie qwen3.5   # Qwen3.5: nur bf16-LoRA
```

Bei 8 GB: QLoRA bis etwa 9B, Qwen3.5 nur 0.8B oder 2B. Qwen3.5 (dicht und
MoE) laut Unsloth nicht mit QLoRA trainieren. Grosse MoE-Modelle wie
Qwen3.5/3.6-35B-A3B brauchen rund 74 GB, auf kleinen GPUs ausgeschlossen. Mit
der kleinsten passenden Groesse beginnen.

## 4. Daten

- Chatformat: Liste von `{"role": ..., "content": ...}` je Beispiel.
- Soll das Modell weiter "denken" (Thinking), mindestens 75 % der Beispiele mit
  Denkteil, sonst ganz ohne. Gemischt darunter verliert es die Faehigkeit.
- Dubletten entfernen; Testsatz darf keine Kopien aus dem Training enthalten.
- Keine Patientendaten, Zugangsdaten oder Daten Dritter ohne Freigabe.

## 5. Training

Installation: `INSTALL.md`. Geruest nach dem Unsloth-Notebook der gewaehlten
Familie; Feldnamen (`tokenizer` gegenueber `processing_class`) dort abgleichen,
weil TRL sie zwischen Versionen umbenennt.

```python
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3.5-2B",   # aus vram_plan
    max_seq_length=2048,
    load_in_4bit=False,                # Qwen3.5: kein QLoRA
)
model = FastLanguageModel.get_peft_model(
    model, r=16, lora_alpha=16, lora_dropout=0,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    use_gradient_checkpointing="unsloth",
)
trainer = SFTTrainer(
    model=model, tokenizer=tokenizer, train_dataset=train,
    args=SFTConfig(per_device_train_batch_size=2, gradient_accumulation_steps=4,
                   max_steps=60, learning_rate=2e-4, logging_steps=5, output_dir="out"),
)
trainer.train()
```

Erst ein kurzer Lauf (`max_steps=60`), Verlust ansehen, Testsatz messen. Erst
dann laenger trainieren. Laeuft der Speicher ueber: `max_seq_length` und
Batchgroesse senken, nicht die Reserve.

## 6. Messen

Testsatz mit demselben Prompt und demselben Chat-Template wie beim Training,
Basismodell gegen nachtrainiertes. Nur ein messbarer Gewinn auf dem
zurueckgehaltenen Teil zaehlt. Kein Gewinn: Ergebnis trotzdem festhalten.

## 7. Einsetzen

```python
model.save_pretrained_gguf("gguf", tokenizer, quantization_method="q4_k_m")   # oder "q8_0"
```

Unsloth schreibt dabei ein `Modelfile` mit dem Chat-Template des Trainings:

```bash
ollama create mein-modell -f gguf/Modelfile
ollama run mein-modell
```

Haeufigster Fehler danach: ein anderes Chat-Template oder EOS-Token als beim
Training. Dann antwortet das Modell schlecht, obwohl das Training gut war.
Immer das mitgeschriebene Template verwenden.

## 8. Festhalten

Ergebnis als Befund in die Wiki (`knowledge/<bereich>/findings/`): Modell,
Datenmenge, Schritte, Testsatz-Zahlen vorher und nachher, VRAM-Spitze,
Trainingsdauer, Unsloth-Version. Auch wenn es nichts gebracht hat.
