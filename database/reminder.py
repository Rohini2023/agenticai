# import sqlite3

# DB = "database/elderly_chatbot.db"


# def save_reminder(task, reminder_time):

#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO reminders(task, reminder_time) VALUES(?, ?)",
#         (task, reminder_time)
#     )

#     conn.commit()

#     reminder_id = cursor.lastrowid   # 🔥 IMPORTANT

#     conn.close()

#     return reminder_id

# def get_pending_reminders():

#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute(
#         "SELECT id, task, reminder_time FROM reminders WHERE status='pending'"
#     )

#     rows = cursor.fetchall()
#     conn.close()

#     return rows


# def mark_done(reminder_id):

#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute(
#         "UPDATE reminders SET status='done' WHERE id=?",
#         (reminder_id,)
#     )

#     conn.commit()
#     conn.close()

# from services.email_service import send_email
# from database.caregiver import get_all_caregivers
# import sqlite3
# from datetime import datetime
# from audio.text_speech import speak
# DB = "database/elderly_chatbot.db"


# def save_reminder(task, reminder_time):

#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     # 🔥 Convert datetime → string
#     if not isinstance(reminder_time, str):
#         reminder_time = reminder_time.isoformat()

#     cursor.execute("""
#         INSERT INTO reminders(task, reminder_time, status, miss_count)
#         VALUES (?, ?, 'pending', 0)
#     """, (task, reminder_time))

#     conn.commit()
#     reminder_id = cursor.lastrowid
#     conn.close()

#     return reminder_id


# def mark_done(reminder_id):
#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute("UPDATE reminders SET status='done' WHERE id=?", (reminder_id,))
#     conn.commit()
#     conn.close()


# def increment_miss(reminder_id):
#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute("""
#         UPDATE reminders 
#         SET miss_count = miss_count + 1, status='missed'
#         WHERE id=?
#     """, (reminder_id,))

#     conn.commit()

#     cursor.execute("SELECT miss_count FROM reminders WHERE id=?", (reminder_id,))
#     count = cursor.fetchone()[0]

#     conn.close()
#     return count


# def get_pending_reminders():
#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute("""
#         SELECT id, task, reminder_time 
#         FROM reminders WHERE status='pending'
#     """)

#     rows = cursor.fetchall()
#     conn.close()

#     return rows

# # def reminder_action(reminder_id, task):

# #     print(f"🔔 Reminder Triggered: {task}")

# #     # 🔊 Always speak
# #     speak(f"Reminder: {task}")

# #     # 🔥 Mark DONE immediately
# #     mark_done(reminder_id)



# def reminder_action(reminder_id, task):

#     print(f"🔔 Reminder Triggered: {task}")

#     try:
#         speak(f"Reminder: {task}")
#     except Exception as e:
#         print("Speak error:", e)

#     # 🔥 Mark as alerted (NOT pending anymore)
#     update_status(reminder_id, "alerted")

#     # 🔁 Increment miss count
#     miss_count = increment_miss(reminder_id)

#     print(f"⚠️ Miss count: {miss_count}")

#     # 🚨 After 3 misses → alert caregiver
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

#         # 🔥 FINAL STATE
#         update_status(reminder_id, "missed")



# def update_status(reminder_id, status):

#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()

#     cursor.execute(
#         "UPDATE reminders SET status=? WHERE id=?",
#         (status, reminder_id)
#     )

#     conn.commit()
#     conn.close()

















    ###########



import sqlite3
from datetime import datetime
from audio.text_speech import speak

DB = "database/elderly_chatbot.db"
def reminder_action(reminder_id, task):

    print(f"🔔 Reminder Triggered: {task}")

    try:
        speak(f"Reminder: Please take {task}")

        import time
        time.sleep(5)

        mark_done(reminder_id)

        print("✅ Reminder marked done")

    except Exception as e:
        print("Reminder Error:", e)

def save_reminder(task, reminder_time):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reminders(task, reminder_time, status, miss_count)
        VALUES (?, ?, 'pending', 0)
    """, (task, reminder_time))

    conn.commit()
    reminder_id = cursor.lastrowid
    conn.close()

    return reminder_id


# ✅ ONLY FUTURE REMINDERS
def get_pending_reminders():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, task, reminder_time 
        FROM reminders
        WHERE status='pending'
    """)

    rows = cursor.fetchall()
    conn.close()

    valid = []

    for r in rows:
        rid, task, time_str = r

        try:
            t = datetime.fromisoformat(str(time_str))

            if t > datetime.now():   # 🔥 FILTER EXPIRED
                valid.append(r)
            else:
                mark_done(rid)       # 🔥 AUTO CLEAN

        except:
            continue

    return valid


def mark_done(reminder_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE reminders 
        SET status='done' 
        WHERE id=?
    """, (reminder_id,))

    conn.commit()
    conn.close()


def increment_miss(reminder_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE reminders 
        SET miss_count = miss_count + 1 
        WHERE id=?
    """, (reminder_id,))

    conn.commit()

    cursor.execute("SELECT miss_count FROM reminders WHERE id=?", (reminder_id,))
    count = cursor.fetchone()[0]

    conn.close()
    return count