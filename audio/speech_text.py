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


# import whisper

# model = whisper.load_model("small")


# def speech_to_text(audio_file):

#     if not audio_file:
#         return ""

#     print("🧠 Converting speech to text...")

#     result = model.transcribe(
#         audio_file,
#         language="en",
#         fp16=False
#     )

#     text = result["text"].strip()

#     # ❌ Filter garbage / empty
#     if not text or len(text.split()) < 1:
#         return ""

#     return text






###### New 
from faster_whisper import WhisperModel

# 🔥 Load model once (important)
model = WhisperModel(
    "base",      # options: tiny, base, small
    device="cpu",
    compute_type="int8"   # fast + low memory
)


def speech_to_text(audio_file):

    print("🧠 Converting speech to text...")

    segments, info = model.transcribe(audio_file)

    text = ""

    for segment in segments:
        text += segment.text + " "

    text = text.strip()

    print("User:", text)

    return text