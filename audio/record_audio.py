# import sounddevice as sd
# import scipy.io.wavfile as wav


# def record_audio(duration=10, fs=16000):

#     print("🎤 Recording... Please speak")

#     audio = sd.rec(int(duration * fs),
#                    samplerate=fs,
#                    channels=1)

#     sd.wait()

#     output_file = "audio/input_audio.wav"

#     wav.write(output_file, fs, audio)

#     print("✅ Recording finished")

#     return output_file


import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

def record_audio(duration=10, fs=16000):

    print("🎤 Recording for 5 seconds... Speak now!")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # ❌ Reject silent audio
    if np.max(audio) < 0.01:
        print("❌ No speech detected")
        return None

    output_file = "audio/input_audio.wav"

    wav.write(output_file, fs, audio)

    print("✅ Recording finished")

    return output_file