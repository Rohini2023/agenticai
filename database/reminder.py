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


import sqlite3
from datetime import datetime

DB = "database/elderly_chatbot.db"


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


def mark_done(reminder_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("UPDATE reminders SET status='done' WHERE id=?", (reminder_id,))
    conn.commit()
    conn.close()


def increment_miss(reminder_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE reminders 
        SET miss_count = miss_count + 1, status='missed'
        WHERE id=?
    """, (reminder_id,))

    conn.commit()

    cursor.execute("SELECT miss_count FROM reminders WHERE id=?", (reminder_id,))
    count = cursor.fetchone()[0]

    conn.close()
    return count


def get_pending_reminders():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, task, reminder_time 
        FROM reminders WHERE status='pending'
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows