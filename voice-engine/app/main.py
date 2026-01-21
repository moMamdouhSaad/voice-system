from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.controller import SpeechController

app = FastAPI(title="Voice Engine API")

controller = SpeechController()


class TTSRequest(BaseModel):
    text: str
    speaker: str | None = None
    language: Optional[str] = None



@app.post("/tts")
def tts(request: TTSRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if not request.language:
        raise HTTPException(status_code=400, detail="Language is required")

    try:
        audio_path = controller.speak(
            text=request.text,
            speaker=request.speaker,
            language=request.language
        )

        return {
            "status": "success",
            "audio_path": audio_path,
            "language": request.language
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/speakers")
def list_speakers():
    samples_dir = "samples"
    if not os.path.exists(samples_dir):
        return []

    return [
        f for f in os.listdir(samples_dir)
        if f.lower().endswith(".wav")
    ]