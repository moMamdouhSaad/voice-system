import numpy as np
import soundfile as sf
from TTS.api import TTS
import glob
import os

# =========================
# CONFIG
# =========================
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
SPEAKER_WAV = glob.glob("samples/actor1/*.wav")  # ✅ multiple samples
LANGUAGE = "ar"
OUTPUT_FILE = "output.wav"
SAMPLE_RATE = 24000
SILENCE_SECONDS = 0.7

if not SPEAKER_WAV:
    raise RuntimeError("No wav files found in samples/actor1")

# =========================
# INIT
# =========================
print("Loading model...")
tts = TTS(model_name=MODEL_NAME)
print("Model loaded")

# =========================
# TEXT (WITH TASHKEEL)
# =========================
sentences = [
    "الصوتُ هو الجسرُ الهادئُ بين الفكرةِ والإحساس.",
    "حينَ يخرجُ بصدقٍ.",
    "يُصبحُ أعمقَ من الكلمات.",
    "وأقْرَبُ إلى الرّوح."
]

# =========================
# SILENCE BUFFER
# =========================
silence = np.zeros(int(SAMPLE_RATE * SILENCE_SECONDS), dtype=np.float32)

# =========================
# GENERATION
# =========================
audio_parts = []

for sentence in sentences:
    print(f"Generating: {sentence}")

    wav = tts.tts(
        text=sentence,
        speaker_wav=SPEAKER_WAV,
        language=LANGUAGE
    )
