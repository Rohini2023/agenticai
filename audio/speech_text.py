import whisper

model = whisper.load_model("base")

def speech_to_text(audio_file):

    print("🧠 Converting speech to text...")

    result = model.transcribe(
        audio_file,
        language="en",
        fp16=False
    )

    text = result["text"].strip()

    return text