import glob
import soundfile as sf
from TTS.api import TTS


class TTSEngine:
    def __init__(self, samples_dir="samples"):
        self.samples_dir = samples_dir
        self.tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2"
        )

    def generate(self, text: str, actor: str, language="ar"):
        speaker_wavs = glob.glob(f"{self.samples_dir}/{actor}/*.wav")

        if not speaker_wavs:
            raise ValueError(f"No samples found for actor: {actor}")

        wav = self.tts.tts(
            text=text,
            speaker_wav=speaker_wavs,
            language=language,
        )
        return wav

    def save(self, wav, path):
        sf.write(path, wav, 24000)
