from app.controller import SpeechController

controller = SpeechController()

outputs = controller.generate_batch("scripts/batch.json")

print("Generated files:")
for o in outputs:
    print("-", o)
