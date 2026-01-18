from TTS.api import TTS
import glob
import os

# ----------------------------
# Configuration
# ----------------------------
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
SAMPLES_DIR = "samples/actor1"
OUTPUT_PATH = "output/output1.wav"
TEXT = " الصَّوتُ هو الجِسرُ الخَفِيُّ بينَ الفِكرةِ والإحساس، بهِ تتحوَّلُ المعاني الصَّامتة إلى حضورٍ حيٍّ، ويصيرُ ما في الداخل مسموعًا ومؤثِّرًا في العالَم من حولِنا."
LANGUAGE = "ar"

# ----------------------------
# Load model
# ----------------------------
print("Loading model...")
tts = TTS(MODEL_NAME)
print("Model loaded")

# ----------------------------
# Load speaker samples
# ----------------------------
speaker_wavs = glob.glob(os.path.join(SAMPLES_DIR, "*.wav"))

if not speaker_wavs:
    raise RuntimeError("No WAV files found in samples folder")

print(f"Found {len(speaker_wavs)} speaker samples")

# ----------------------------
# Generate speech
# ----------------------------
print("Generating voice...")
tts.tts_to_file(
    text=TEXT,
    speaker_wav=speaker_wavs,
    language=LANGUAGE,
    file_path=OUTPUT_PATH
)

print(f"Done ✅ File saved as: {OUTPUT_PATH}")
