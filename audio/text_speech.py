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



# import pyttsx3
# import threading
# import queue

# speech_queue = queue.Queue()
# speech_lock = threading.Lock()


# def speak_worker():
#     while True:
#         text = speech_queue.get()

#         if text is None:
#             print("🛑 Speech worker stopped")
#             break

#         try:
#             with speech_lock:
#                 print(f"🔊 Speaking: {text}")

#                 # fresh engine every time
#                 engine = pyttsx3.init()

#                 engine.setProperty("rate", 165)
#                 engine.setProperty("volume", 1.0)

#                 engine.say(text)
#                 engine.runAndWait()
#                 engine.stop()

#                 print("✅ Speech completed")

#         except Exception as e:
#             print("TTS Error:", e)

#         finally:
#             speech_queue.task_done()


# # 🔥 Start worker only once (IMPORTANT)
# worker_thread = threading.Thread(
#     target=speak_worker,
#     daemon=False   # 🔥 changed from True → False
# )
# worker_thread.start()


# def speak(text):
#     if text and text.strip():
#         print(f"📥 Added to speech queue: {text}")
#         speech_queue.put(text)



# import pyttsx3
# import threading
# import queue

# # =====================================
# # GLOBALS
# # =====================================

# speech_queue = queue.Queue()

# speech_lock = threading.Lock()

# # 🔥 Create engine ONLY ONCE
# engine = pyttsx3.init()

# engine.setProperty("rate", 165)

# engine.setProperty("volume", 1.0)


# # =====================================
# # SPEAK WORKER
# # =====================================

# def speak_worker():

#     while True:

#         text = speech_queue.get()

#         # 🔥 Stop worker
#         if text is None:

#             print("🛑 Speech worker stopped")

#             break

#         try:

#             with speech_lock:

#                 print(f"🔊 Speaking: {text}")

#                 engine.say(text)

#                 engine.runAndWait()

#                 print("✅ Speech completed")

#         except Exception as e:

#             print("TTS Error:", e)

#         finally:

#             speech_queue.task_done()


# # =====================================
# # START WORKER ONLY ONCE
# # =====================================

# worker_thread = threading.Thread(

#     target=speak_worker,

#     daemon=True
# )

# worker_thread.start()


# # =====================================
# # SPEAK FUNCTION
# # =====================================

# def speak(text):

#     if text and text.strip():

#         print(f"📥 Added to speech queue: {text}")

#         speech_queue.put(text)



# import pyttsx3
# import threading
# import queue

# # Global queue
# speech_queue = queue.Queue()

# # Global lock
# speech_lock = threading.Lock()

# # Global engine
# engine = pyttsx3.init()

# engine.setProperty("rate", 165)
# engine.setProperty("volume", 1.0)

# # 🔥 Track speaking state
# is_speaking = False


# def speak_worker():

#     global is_speaking

#     while True:

#         text = speech_queue.get()

#         if text is None:
#             break

#         try:
#             with speech_lock:

#                 is_speaking = True

#                 print(f"🔊 Speaking: {text}")

#                 engine.say(text)
#                 engine.runAndWait()

#                 print("✅ Speech completed")

#         except Exception as e:
#             print("TTS Error:", e)

#         finally:

#             is_speaking = False

#             speech_queue.task_done()


# # Start worker thread
# threading.Thread(
#     target=speak_worker,
#     daemon=True
# ).start()


# def speak(text):

#     if text and text.strip():

#         print(f"📥 Added to speech queue: {text}")

#         speech_queue.put(text)


# def speaking_now():
#     return is_speaking

# import pyttsx3
# import threading
# import queue

# speech_queue = queue.Queue()

# engine = pyttsx3.init()

# engine.setProperty("rate", 165)
# engine.setProperty("volume", 1.0)


# def speak_worker():

#     while True:

#         text = speech_queue.get()

#         if text is None:
#             break

#         try:

#             print(f"🔊 Speaking: {text}")

#             engine.say(text)

#             engine.runAndWait()

#             engine.stop()

#             print("✅ Speech completed")

#         except Exception as e:

#             print("TTS Error:", e)

#         finally:

#             speech_queue.task_done()


# # 🔥 Start ONLY ONCE
# threading.Thread(
#     target=speak_worker,
#     daemon=True
# ).start()


# def speak(text):

#     if text and text.strip():

#         print(f"📥 Added to speech queue: {text}")

#         speech_queue.put(text)


# # 🔥 NEW
# def speaking_now():

#     return not speech_queue.empty()

# =========================================
# FILE: audio/text_speech.py
# =========================================

# import pyttsx3
# import threading
# import queue

# # 🔥 Global speech queue
# speech_queue = queue.Queue()

# # 🔥 Initialize engine ONLY ONCE
# engine = pyttsx3.init()

# engine.setProperty("rate", 165)
# engine.setProperty("volume", 1.0)


# # =========================================
# # SPEECH WORKER THREAD
# # =========================================
# def speak_worker():

#     while True:

#         text = speech_queue.get()

#         try:

#             # stop thread safely
#             if text is None:
#                 break

#             print(f"🔊 Speaking: {text}")

#             engine.say(text)

#             engine.runAndWait()

#             engine.stop()

#             print("✅ Speech completed")

#         except Exception as e:

#             print("TTS Error:", e)

#         finally:

#             # 🔥 VERY IMPORTANT
#             speech_queue.task_done()


# # =========================================
# # START WORKER THREAD ONLY ONCE
# # =========================================
# threading.Thread(
#     target=speak_worker,
#     daemon=True
# ).start()


# # =========================================
# # MAIN SPEAK FUNCTION
# # =========================================
# def speak(text):

#     if text and text.strip():

#         # 🔥 Prevent huge responses
#         text = text[:250]

#         print(f"📥 Added to speech queue: {text}")

#         speech_queue.put(text)


# # =========================================
# # CHECK IF SPEAKING
# # =========================================
# def speaking_now():

#     return speech_queue.unfinished_tasks > 0



# import pyttsx3
# import threading
# import queue

# speech_queue = queue.Queue()

# engine = pyttsx3.init()

# engine.setProperty("rate", 165)
# engine.setProperty("volume", 1.0)


# def speak_worker():

#     while True:

#         text = speech_queue.get()

#         try:

#             if text is None:
#                 break

#             print(f"🔊 Speaking: {text}")

#             engine.say(text)

#             # 🔥 waits until speech fully completes
#             engine.runAndWait()

#             print("✅ Speech completed")

#         except Exception as e:

#             print("TTS Error:", e)

#         finally:

#             speech_queue.task_done()


# # 🔥 Start only once
# threading.Thread(
#     target=speak_worker,
#     daemon=True
# ).start()


# def speak(text):

#     if text and text.strip():

#         # 🔥 optional length limit
#         text = text[:400]

#         print(f"📥 Added to speech queue: {text}")

#         speech_queue.put(text)


# def speaking_now():

#     return speech_queue.unfinished_tasks > 0


import pyttsx3
import threading
import queue
import time

speech_queue = queue.Queue()

engine = pyttsx3.init()

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

# 🔥 REAL speaking flag
is_speaking = False


def speak_worker():

    global is_speaking

    while True:

        text = speech_queue.get()

        if text is None:
            break

        try:

            is_speaking = True

            print(f"🔊 Speaking: {text}")

            engine.say(text)

            engine.runAndWait()

            print("✅ Speech completed")

        except Exception as e:

            print("TTS Error:", e)

        finally:

            is_speaking = False

            speech_queue.task_done()


# 🔥 Start worker ONCE
threading.Thread(
    target=speak_worker,
    daemon=True
).start()


def speak(text):

    if text and text.strip():

        print(f"📥 Added to speech queue: {text}")

        speech_queue.put(text)


def speaking_now():

    global is_speaking

    return is_speaking