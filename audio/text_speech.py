# import pyttsx3
# import threading

# engine = pyttsx3.init()
# engine.setProperty("rate", 150)
# engine.setProperty("volume", 1.0)

# lock = threading.Lock()


# def speak(text):
#     print("🔊 Assistant:", text)

#     def run():
#         with lock:
#             engine.say(text)
#             engine.runAndWait()

#     threading.Thread(target=run).start()

import pyttsx3
import threading
import pythoncom   # 🔥 IMPORTANT


def speak(text):

    print("🔊 Assistant:", text)

    def run():
        try:
            # 🔥 Fix COM error
            pythoncom.CoInitialize()

            engine = pyttsx3.init()
            engine.setProperty("rate", 150)

            engine.say(text)
            engine.runAndWait()

            engine.stop()

            pythoncom.CoUninitialize()

        except Exception as e:
            print("TTS error:", e)

    threading.Thread(target=run).start()