from audio.record_audio import record_audio
from audio.preprocess_audio import preprocess_audio
from audio.speech_text import speech_to_text


def main():

    raw_audio = record_audio()
    print("RAW FILE:", raw_audio)

    clean_audio = preprocess_audio(raw_audio)
    print("CLEAN FILE:", clean_audio)

    text = speech_to_text(clean_audio)

    print("\n📝 Recognized Text:")
    print(text)


if __name__ == "__main__":
    main()