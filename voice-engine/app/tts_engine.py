from TTS.api import TTS
from scipy.io.wavfile import write
import numpy as np
import os
from glob import glob
import librosa

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
SAMPLE_RATE = 24000
TARGET_RMS = 0.08  # calm, spiritual loudness

class VoiceEngine:
    def __init__(self, speaker_samples_dir: str):
        self.tts = TTS(model_name=MODEL_NAME)

        self.speaker_wavs = sorted(
            glob(os.path.join(speaker_samples_dir, "*.wav"))
        )

        if not self.speaker_wavs:
            raise ValueError("No WAV samples found for speaker")

    def _trim_silence(self, wav: np.ndarray) -> np.ndarray:
        wav_trimmed, _ = librosa.effects.trim(
            wav,
            top_db=25
        )
        return wav_trimmed

    def _normalize(self, wav: np.ndarray) -> np.ndarray:
        rms = np.sqrt(np.mean(wav ** 2))
        if rms > 0:
            wav = wav * (TARGET_RMS / rms)

        return np.clip(wav, -1.0, 1.0)

    def generate(self, text: str, output_path: str, mode: str = "spiritual"):
        if mode == "spiritual":
            text = self._prepare_spiritual_text(text)

        wav = self.tts.tts(
            text=text,
            speaker_wav=self.speaker_wavs,
            language="ar"
        )

        wav = np.array(wav, dtype=np.float32)

        wav = self._trim_silence(wav)
        wav = self._normalize(wav)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        write(output_path, SAMPLE_RATE, wav)

        return output_path

    

    def _prepare_spiritual_text(self, text: str) -> str:
        """
        Spiritual pacing WITHOUT harming Arabic pronunciation
        """

        # Normalize Arabic punctuation spacing only
        text = text.replace("،", "، ")
        text = text.replace("…", "… ")
        text = text.replace(".", "… ")

        # SAFE pauses: only after full phrases
        text = text.replace("، ", "، ")
        text = text.replace("… ", "…\n")
        text = text.replace("؟ ", "؟\n")

        # Remove aggressive symbols
        text = text.replace("!", "")

        return text.strip()


