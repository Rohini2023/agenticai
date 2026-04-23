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

# import pyttsx3
# import threading
# import pythoncom   # 🔥 IMPORTANT


# def speak(text):

#     print("🔊 Assistant:", text)

#     def run():
#         try:
#             # 🔥 Fix COM error
#             pythoncom.CoInitialize()

#             engine = pyttsx3.init()
#             engine.setProperty("rate", 150)

#             engine.say(text)
#             engine.runAndWait()

#             engine.stop()

#             pythoncom.CoUninitialize()

#         except Exception as e:
#             print("TTS error:", e)

#     threading.Thread(target=run).start()



# import pyttsx3
# import threading
# import queue

# engine = pyttsx3.init()
# speech_queue = queue.Queue()

# def speak_worker():
#     while True:
#         text = speech_queue.get()
#         if text is None:
#             break

#         try:
#             engine.stop()
#             engine.say(text)
#             engine.runAndWait()
#         except Exception as e:
#             print("TTS Error:", e)

#         speech_queue.task_done()


# # 🔥 START WORKER THREAD (RUN ONLY ONCE)
# threading.Thread(target=speak_worker, daemon=True).start()


# def speak(text):
#     speech_queue.put(text)



# import pyttsx3
# import threading
# import queue

# speech_queue = queue.Queue()
# speech_lock = threading.Lock()


# def speak_worker():
#     while True:
#         text = speech_queue.get()

#         if text is None:
#             break

#         try:
#             with speech_lock:
#                 # 🔥 Create fresh engine every time
#                 engine = pyttsx3.init()

#                 engine.setProperty("rate", 165)   # speed
#                 engine.setProperty("volume", 1.0) # volume

#                 engine.say(text)
#                 engine.runAndWait()
#                 engine.stop()

#         except Exception as e:
#             print("TTS Error:", e)

#         speech_queue.task_done()


# # 🔥 Start worker only once
# threading.Thread(
#     target=speak_worker,
#     daemon=True
# ).start()


# def speak(text):
#     if text and text.strip():
#         print("🔊 Assistant:", text)
#         speech_queue.put(text)



import pyttsx3
import threading
import queue

speech_queue = queue.Queue()
speech_lock = threading.Lock()


def speak_worker():
    while True:
        text = speech_queue.get()

        if text is None:
            print("🛑 Speech worker stopped")
            break

        try:
            with speech_lock:
                print(f"🔊 Speaking: {text}")

                # fresh engine every time
                engine = pyttsx3.init()

                engine.setProperty("rate", 165)
                engine.setProperty("volume", 1.0)

                engine.say(text)
                engine.runAndWait()
                engine.stop()

                print("✅ Speech completed")

        except Exception as e:
            print("TTS Error:", e)

        finally:
            speech_queue.task_done()


# 🔥 Start worker only once (IMPORTANT)
worker_thread = threading.Thread(
    target=speak_worker,
    daemon=False   # 🔥 changed from True → False
)
worker_thread.start()


def speak(text):
    if text and text.strip():
        print(f"📥 Added to speech queue: {text}")
        speech_queue.put(text)