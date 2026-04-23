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


# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# from audio.text_speech import speak
# from database.reminder import mark_done, increment_miss, get_pending_reminders
# from database.caregiver import get_all_caregivers
# from services.email_service import send_email

# scheduler = BackgroundScheduler()


# def reminder_action(reminder_id, task):

#     print(f"🔔 Reminder: {task}")

#     speak(f"Reminder: {task}")

#     miss_count = increment_miss(reminder_id)

#     print(f"⚠️ Miss count: {miss_count}")

#     if miss_count >= 3:

#         caregivers = get_all_caregivers()

#         for row in caregivers:
#             _, name, phone, relation, email, priority = row

#             if email:
#                 send_email(
#                     email,
#                     "⚠️ REMINDER MISSED ALERT",
#                     f"User missed reminder 3 times:\n\n📝 {task}"
#                 )

#                 print(f"📧 Miss alert sent to {name}")

#         mark_done(reminder_id)


# def schedule_reminder(task, reminder_time, reminder_id):

#     run_time = reminder_time

#     if run_time < datetime.now():
#         print(f"⚠️ Skipping past reminder: {task}")
#         return

#     scheduler.add_job(
#         reminder_action,
#         'date',
#         run_date=run_time,
#         args=[reminder_id, task]
#     )

#     print(f"⏰ Scheduled: {task} at {run_time}")


# def load_existing_reminders():

#     reminders = get_pending_reminders()

#     print(f"📂 Loading {len(reminders)} reminders...")

#     for reminder_id, task, time_str in reminders:

#         try:
#             run_time = datetime.fromisoformat(time_str)

#             if run_time > datetime.now():
#                 schedule_reminder(task, run_time, reminder_id)

#         except Exception as e:
#             print("Time parse error:", e)

# def start_scheduler():

#     print("✅ Scheduler started")

#     scheduler.start()

#     load_existing_reminders()





# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# from audio.text_speech import speak
# from database.reminder import mark_done, increment_miss, get_pending_reminders
# from database.caregiver import get_all_caregivers
# from services.email_service import send_email

# scheduler = BackgroundScheduler()


# # 🔔 MAIN TRIGGER
# def reminder_action(reminder_id, task):

#     print(f"🔔 Reminder Triggered: {task}")

#     # 🔥 SPEAK MULTIPLE TIMES (IMPORTANT)
#     for _ in range(2):
#         speak(f"Reminder: {task}")

#     # ✅ Immediately mark DONE (IMPORTANT FIX)
#     mark_done(reminder_id)

#     print("✅ Reminder marked done")


# # 📅 SCHEDULE
# def schedule_reminder(task, reminder_time, reminder_id):

#     if reminder_time < datetime.now():
#         print("⚠️ Skipping past reminder:", task)
#         mark_done(reminder_id)
#         return

#     scheduler.add_job(
#         reminder_action,
#         'date',
#         run_date=reminder_time,
#         args=[reminder_id, task],
#         id=str(reminder_id),
#         replace_existing=True
#     )

#     print(f"⏰ Scheduled: {task} at {reminder_time}")


# # 🔄 LOAD FROM DB
# def load_existing_reminders():

#     reminders = get_pending_reminders()

#     print(f"📂 Loading {len(reminders)} reminders...")

#     for rid, task, time_str in reminders:

#         try:
#             run_time = datetime.fromisoformat(str(time_str))
#             schedule_reminder(task, run_time, rid)

#         except Exception as e:
#             print("Time error:", e)


# # ▶️ START
# def start_scheduler():

#     scheduler.start()
#     print("✅ Scheduler started")

#     load_existing_reminders()





from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from audio.text_speech import speak
from database.reminder import mark_done, get_pending_reminders
import time

scheduler = BackgroundScheduler()


# 🔔 Reminder Trigger
def reminder_action(reminder_id, task):

    print(f"🔔 Reminder Triggered: {task}")

    try:
        # 🔥 only ONE speak call
        speak(f"Reminder: {task}")

        # wait for speech
        time.sleep(3)

        # mark done after alert
        mark_done(reminder_id)

        print("✅ Reminder marked done")

    except Exception as e:
        print("Reminder Error:", e)


# 📅 Schedule Reminder
def schedule_reminder(task, reminder_time, reminder_id):

    if reminder_time < datetime.now():
        print(f"⚠️ Skipping past reminder: {task}")

        mark_done(reminder_id)
        return

    scheduler.add_job(
        reminder_action,
        trigger="date",
        run_date=reminder_time,
        args=[reminder_id, task],
        id=str(reminder_id),
        replace_existing=True
    )

    print(f"⏰ Scheduled: {task} at {reminder_time}")


# 🔄 Load Existing Reminders
def load_existing_reminders():

    reminders = get_pending_reminders()

    print(f"📂 Loading {len(reminders)} reminders...")

    for reminder_id, task, time_str in reminders:

        try:
            run_time = datetime.fromisoformat(str(time_str))

            schedule_reminder(
                task,
                run_time,
                reminder_id
            )

        except Exception as e:
            print("Time Parse Error:", e)


# ▶️ Start Scheduler
def start_scheduler():

    print("🚀 Starting Scheduler...")

    scheduler.start()

    print("✅ Scheduler started")

    load_existing_reminders()