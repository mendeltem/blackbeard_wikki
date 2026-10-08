# Installation

Python >= 3.10 mit nibabel, numpy, scipy, Pillow. Auf Alita vorhanden in der conda-Umgebung `dl`:

    /home/uchralt/miniconda3/envs/dl/bin/python -c "import nibabel, scipy, PIL; print('ok')"

Anderswo:

    pip install nibabel numpy scipy pillow

Test:

    /home/uchralt/miniconda3/envs/dl/bin/python tools/mri/mri_segmentation/qc_slice_viewer/tests/test_synthetic.py

Kein Netz, keine Modelle, keine Daten noetig; der Test baut sich synthetische Volumen.
