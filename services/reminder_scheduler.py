# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# from audio.text_speech import speak

# from database.reminder import get_pending_reminders, mark_done

# scheduler = BackgroundScheduler()


# # 🔔 WHAT HAPPENS WHEN REMINDER TRIGGERS
# def reminder_action(reminder_id, task):

#     print(f"🔔 Reminder Triggered: {task}")

#     speak(f"Reminder: {task}")

#     # ✅ Mark as done
#     if reminder_id:
#         mark_done(reminder_id)


# # 📅 SCHEDULE NEW REMINDER
# def schedule_reminder(task, reminder_time, reminder_id=None):

#     # 🔥 Convert string → datetime if needed
#     if isinstance(reminder_time, str):
#         reminder_time = datetime.fromisoformat(reminder_time)

#     # ❌ Skip past time
#     if reminder_time < datetime.now():
#         print("⚠️ Skipping past reminder:", task)
#         return

#     print(f"⏰ Scheduling: {task} at {reminder_time}")

#     scheduler.add_job(
#         reminder_action,
#         trigger='date',
#         run_date=reminder_time,
#         args=[reminder_id, task],
#         id=str(reminder_id) if reminder_id else None,
#         replace_existing=True
#     )


# # 🔄 LOAD REMINDERS FROM DB (IMPORTANT 🔥)
# def load_existing_reminders():

#     reminders = get_pending_reminders()

#     print(f"📂 Loading {len(reminders)} reminders from DB...")

#     for reminder in reminders:
#         reminder_id, task, reminder_time = reminder

#         schedule_reminder(task, reminder_time, reminder_id)


# # ▶️ START SCHEDULER
# def start_scheduler():

#     scheduler.start()
#     print("✅ Scheduler started")

#     # 🔥 Load reminders on startup
#     load_existing_reminders()


from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from audio.text_speech import speak
from database.reminder import mark_done, increment_miss, get_pending_reminders
from database.caregiver import get_all_caregivers
from services.email_service import send_email

scheduler = BackgroundScheduler()


def reminder_action(reminder_id, task):

    print(f"🔔 Reminder: {task}")

    speak(f"Reminder: {task}")

    miss_count = increment_miss(reminder_id)

    print(f"⚠️ Miss count: {miss_count}")

    if miss_count >= 3:

        caregivers = get_all_caregivers()

        for row in caregivers:
            _, name, phone, relation, email, priority = row

            if email:
                send_email(
                    email,
                    "⚠️ REMINDER MISSED ALERT",
                    f"User missed reminder 3 times:\n\n📝 {task}"
                )

                print(f"📧 Miss alert sent to {name}")

        mark_done(reminder_id)


def schedule_reminder(task, reminder_time, reminder_id):

    run_time = reminder_time

    if run_time < datetime.now():
        print(f"⚠️ Skipping past reminder: {task}")
        return

    scheduler.add_job(
        reminder_action,
        'date',
        run_date=run_time,
        args=[reminder_id, task]
    )

    print(f"⏰ Scheduled: {task} at {run_time}")


def load_existing_reminders():

    reminders = get_pending_reminders()

    print(f"📂 Loading {len(reminders)} reminders...")

    for reminder_id, task, time_str in reminders:

        run_time = datetime.fromisoformat(time_str)

        if run_time > datetime.now():
            schedule_reminder(task, run_time, reminder_id)


def start_scheduler():

    print("✅ Scheduler started")

    scheduler.start()

    load_existing_reminders()