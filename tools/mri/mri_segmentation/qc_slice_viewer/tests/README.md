# Tests

    /home/uchralt/miniconda3/envs/dl/bin/python tests/test_synthetic.py      # oder: pytest tests/

Baut zwei synthetische Faelle (64 x 72 x 40, 0,5 x 0,5 x 1 mm): drei Kugeln als Referenz, eine
Wahrscheinlichkeitskarte mit zwei Treffern, einem Fehlalarm und einem Ein-Voxel-Blob unter der
Groessenregel. Erwartet je Fall tp/fp/fn = 2/1/1. Prueft ausserdem Urteilsmodus, den Wortlaut bei
`reference_is: comparison`, einen Maskenlauf und einen Fall ohne Referenz. Laufzeit ~6 s, kein Netz.
