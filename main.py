from audio.record_audio import record_audio
from audio.preprocess_audio import preprocess_audio
from audio.speech_text import speech_to_text
from audio.text_speech import speak
from database.chat_history import save_chat
from agent.agent_executor import run_agent
from services.reminder_scheduler import start_scheduler

import threading


def main():

    # ✅ Start scheduler in background
    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    print("🟢 Assistant started...")

    while True:
        try:
            input("👉 Press ENTER to speak...")
            # 🎤 Record audio
            raw = record_audio()

            # ❌ If no audio captured
            if not raw:
                speak("I didn't catch that, please speak again")
                continue

            # 🔧 Preprocess
            clean = preprocess_audio(raw)

            if not clean:
                continue

            # 🧠 Speech → Text
            text = speech_to_text(clean)

            # ❌ Empty speech
            if not text:
                print("❌ No speech detected")
                continue

            text = text.strip()
            print("User:", text)

            # 🚨 Filter very short input
            if len(text.split()) < 2:
                speak("Please say a complete sentence")
                continue

            # 🚨 Filter very long/noisy input
            if len(text.split()) > 25:
                speak("Please speak clearly")
                continue

            # ✅ Exit handling (strong)
            if any(word in text.lower() for word in ["exit", "quit", "stop assistant"]):
                speak("Stopping assistant")
                print("🔴 Assistant stopped")
                break

            # 🤖 Run agent safely
            try:
                response = run_agent(text)
            except Exception as e:
                print("Agent error:", e)
                response = "Sorry, something went wrong"

            # 🔊 Speak response
            speak(response)
            save_chat(text, response)
        except KeyboardInterrupt:
            print("\n🔴 Interrupted manually")
            break

        except Exception as e:
            print("Main loop error:", e)
            speak("Something went wrong, please try again")


if __name__ == "__main__":
    main()