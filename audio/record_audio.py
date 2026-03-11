import sounddevice as sd
import scipy.io.wavfile as wav


def record_audio(duration=6, fs=16000):

    print("🎤 Recording... Please speak")

    audio = sd.rec(int(duration * fs),
                   samplerate=fs,
                   channels=1)

    sd.wait()

    output_file = "audio/input_audio.wav"

    wav.write(output_file, fs, audio)

    print("✅ Recording finished")

    return output_file