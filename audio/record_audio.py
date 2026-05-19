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


# import sounddevice as sd
# import scipy.io.wavfile as wav
# import numpy as np

# def record_audio(duration=10, fs=16000):

#     print("🎤 Recording for 5 seconds... Speak now!")

#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#     sd.wait()

#     # ❌ Reject silent audio
#     if np.max(audio) < 0.01:
#         print("❌ No speech detected")
#         return None

#     output_file = "audio/input_audio.wav"

#     wav.write(output_file, fs, audio)

#     print("✅ Recording finished")

#     return output_file


# import sounddevice as sd
# import scipy.io.wavfile as wav
# import numpy as np
# import time

# from audio.text_speech import speaking_now


# def record_audio(duration=5, fs=16000):

#     # 🔥 WAIT if chatbot speaking
#     while speaking_now():
#         print("⏳ Waiting for speech to finish...")
#         time.sleep(0.5)

#     print("🎤 Recording for 5 seconds... Speak now!")

#     audio = sd.rec(
#         int(duration * fs),
#         samplerate=fs,
#         channels=1,
#         dtype='float32'
#     )

#     sd.wait()

#     # 🔥 silence detection
#     volume = np.max(np.abs(audio))

#     print("🎚 Audio Level:", volume)

#     if volume < 0.01:
#         print("❌ No speech detected")
#         return None

#     # 🔥 normalize audio
#     audio = audio / np.max(np.abs(audio))

#     output_file = "audio/input_audio.wav"

#     wav.write(
#         output_file,
#         fs,
#         (audio * 32767).astype(np.int16)
#     )

#     print("✅ Recording finished")

#     return output_file


# =========================================
# FILE: audio/record_audio.py
# =========================================

# import sounddevice as sd
# import scipy.io.wavfile as wav
# import numpy as np
# import time

# from audio.text_speech import speaking_now


# def record_audio(duration=5, fs=16000):

#     # =====================================
#     # WAIT UNTIL TTS FINISHES
#     # =====================================

#     wait_count = 0

#     while speaking_now():

#         print("⏳ Waiting for speech to finish...")

#         time.sleep(0.5)

#         wait_count += 1

#         # 🔥 Safety timeout
#         if wait_count > 20:

#             print("⚠️ Force continue recording")

#             break

#     # =====================================
#     # START RECORDING
#     # =====================================

#     print(f"🎤 Recording for {duration} seconds... Speak now!")

#     audio = sd.rec(
#         int(duration * fs),
#         samplerate=fs,
#         channels=1,
#         dtype='float32'
#     )

#     sd.wait()

#     # =====================================
#     # CHECK SILENCE
#     # =====================================

#     volume = np.max(np.abs(audio))

#     print("🎚 Audio Level:", volume)

#     if volume < 0.01:

#         print("❌ No speech detected")

#         return None

#     # =====================================
#     # NORMALIZE AUDIO
#     # =====================================

#     audio = audio / np.max(np.abs(audio))

#     # =====================================
#     # SAVE AUDIO
#     # =====================================

#     output_file = "audio/input_audio.wav"

#     wav.write(
#         output_file,
#         fs,
#         (audio * 32767).astype(np.int16)
#     )

#     print("✅ Recording finished")

#     return output_file


import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import time

from audio.text_speech import speaking_now


def record_audio(duration=5, fs=16000):

    # 🔥 Wait ONLY while actually speaking
    wait_count = 0

    while speaking_now():

        print("⏳ Waiting for speech to finish...")

        time.sleep(0.5)

        wait_count += 1

        # 🔥 Safety break
        if wait_count > 20:
            print("⚠️ Force continue recording")
            break

    print("🎤 Recording for 5 seconds... Speak now!")

    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='float32'
    )

    sd.wait()

    volume = np.max(np.abs(audio))

    print("🎚 Audio Level:", volume)

    # 🔥 silence threshold
    if volume < 0.01:

        print("❌ No speech detected")

        return None

    # 🔥 normalize
    audio = audio / np.max(np.abs(audio))

    output_file = "audio/input_audio.wav"

    wav.write(
        output_file,
        fs,
        (audio * 32767).astype(np.int16)
    )

    print("✅ Recording finished")

    return output_file