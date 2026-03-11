import sqlite3

DB = "database/elderly_chatbot.db"


def save_reminder(text, time):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reminders(reminder_text,reminder_time) VALUES(?,?)",
        (text, time)
    )

    conn.commit()
    conn.close()

    print("Reminder saved")


def get_reminders():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT reminder_text,reminder_time FROM reminders")

    rows = cursor.fetchall()

    conn.close()

    return rows