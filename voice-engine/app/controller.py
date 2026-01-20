from app.tts_engine import TTSEngine

class SpeechController:  
    def __init__(self):
        self.engine = TTSEngine()

    def speak(self, text: str, speaker: str, language: str):
        return self.engine.generate(
            text=text,
            actor=speaker,
            language=language,
        )

