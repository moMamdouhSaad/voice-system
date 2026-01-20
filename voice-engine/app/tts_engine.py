import os
import glob
import random

class TTSEngine:
    def __init__(self, samples_dir: str = "samples"):
        self.samples_dir = samples_dir
        from TTS.api import TTS
        self.tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

    def generate(self, text: str, actor: str, language: str):
        speaker_wavs = glob.glob(os.path.join(self.samples_dir, actor, "*.wav"))
        if not speaker_wavs:
            raise ValueError(f"No speaker WAV files found for actor: {actor}")

        # pick one randomly
        speaker_wav = random.choice(speaker_wavs)

        os.makedirs("outputs", exist_ok=True)
        output_path = "outputs/output.wav"

        self.tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language=language,
            file_path=output_path,
        )

        return output_path
