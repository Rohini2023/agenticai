# import whisper

# model = whisper.load_model("base")

# def speech_to_text(audio_file):

#     print("🧠 Converting speech to text...")

#     result = model.transcribe(
#         audio_file,
#         language="en",
#         fp16=False
#     )

#     text = result["text"].strip()

#     return text


import whisper

model = whisper.load_model("small")


def speech_to_text(audio_file):

    if not audio_file:
        return ""

    print("🧠 Converting speech to text...")

    result = model.transcribe(
        audio_file,
        language="en",
        fp16=False
    )

    text = result["text"].strip()

    # ❌ Filter garbage / empty
    if not text or len(text.split()) < 1:
        return ""

    return text