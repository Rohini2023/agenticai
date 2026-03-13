from audio.record_audio import record_audio
from audio.preprocess_audio import preprocess_audio
from audio.speech_text import speech_to_text
from audio.text_speech import speak

from agent.agent_executor import run_agent

from services.reminder_scheduler import start_scheduler

import threading


def main():

    scheduler_thread=threading.Thread(
        target=start_scheduler
    )

    scheduler_thread.daemon=True

    scheduler_thread.start()

    while True:

        raw=record_audio()

        clean=preprocess_audio(raw)

        text=speech_to_text(clean)
        text = text.strip()
        if len(text) < 3:
             print("No valid speech detected")
             continue
        # if text == "":
        #     print("No speech detected")
        #     continue

        print("User:",text)
        if "stop assistant" in text or "exit" in text:
            speak("Stopping assistant")
            break
        response=run_agent(text)

        speak(response)


if __name__=="__main__":

    main()