import time
from datetime import datetime

from database.reminder import get_reminders
from audio.text_speech import speak


def check_reminders():

    reminders=get_reminders()

    now=datetime.now().strftime("%Y-%m-%d %H:%M")

    for task,time_str in reminders:

        if time_str.startswith(now):

            speak("Reminder: "+task)


def start_scheduler():

    print("Scheduler started")

    while True:

        check_reminders()

        time.sleep(60)