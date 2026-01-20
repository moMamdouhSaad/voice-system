import json
import os
import numpy as np
import soundfile as sf
from app.tts_engine import TTSEngine


class SpeechController:
    def __init__(self, samples_dir="samples", sample_rate=24000):
        self.engine = TTSEngine(samples_dir=samples_dir)
        self.sample_rate = sample_rate

    def _silence(self, seconds):
        return np.zeros(int(self.sample_rate * seconds), dtype=np.float32)

    def generate_from_script(self, script, actor, output_path):
        audio = []

        for item in script:
            wav = self.engine.generate(
                text=item["text"],
                actor=actor,
            )
            audio.append(wav)
            audio.append(self._silence(item.get("pause_after", 0.4)))

        audio = np.concatenate(audio)
        sf.write(output_path, audio, self.sample_rate)
        return output_path

    def generate_batch(self, json_path: str) -> list:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        actor = data["actor"]
        outputs = []

        os.makedirs("output", exist_ok=True)

        for item in data["items"]:
            path = self.generate_from_script(
                script=item["script"],
                actor=actor,
                output_path=f"output/{item['filename']}",
            )
            outputs.append(path)

        return outputs
