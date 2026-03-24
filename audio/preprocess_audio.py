import librosa
import numpy as np
import noisereduce as nr
import scipy.io.wavfile as wav
import os


# def preprocess_audio(file_path):

#     print("🔧 Preprocessing audio...")

#     audio, sr = librosa.load(file_path, sr=16000)

#     reduced_noise = nr.reduce_noise(y=audio, sr=sr)

#     normalized_audio = librosa.util.normalize(reduced_noise)

#     output_path = "audio/clean_audio.wav"

#     wav.write(
#         output_path,
#         sr,
#         (normalized_audio * 32767).astype(np.int16)
#     )

#     print("✅ Clean audio saved:", output_path)

#     return output_path

def preprocess_audio(file_path):

    if not file_path:
        return None

    print("🔧 Preprocessing audio...")

    audio, sr = librosa.load(file_path, sr=16000)

    reduced_noise = nr.reduce_noise(y=audio, sr=sr)

    normalized_audio = librosa.util.normalize(reduced_noise)

    output_path = "audio/clean_audio.wav"

    wav.write(
        output_path,
        sr,
        (normalized_audio * 32767).astype(np.int16)
    )

    print("✅ Clean audio saved:", output_path)

    return output_path