from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.controller import SpeechController

app = FastAPI(title="Voice Engine API")

controller = SpeechController()


class ScriptItem(BaseModel):
    text: str
    pause_after: float = 0.4


class BatchItem(BaseModel):
    filename: str
    script: List[ScriptItem]


class BatchRequest(BaseModel):
    actor: str
    items: List[BatchItem]


@app.post("/generate/batch")
def generate_batch(request: BatchRequest):
    outputs = []

    for item in request.items:
        path = controller.generate_from_script(
            script=[s.dict() for s in item.script],
            actor=request.actor,
            output_path=f"output/{item.filename}",
        )
        outputs.append(path)

    return {
        "status": "success",
        "generated": outputs,
    }
