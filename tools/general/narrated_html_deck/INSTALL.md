# Install

```bash
conda create -n tts python=3.12 -y && conda activate tts
pip install "kokoro>=0.9" soundfile
conda install -c conda-forge ffmpeg -y      # needs libmp3lame
bash tests/test_build.sh python
```
The first run downloads Kokoro-82M from Hugging Face. English voices need espeak-ng only for rare words (optional).
