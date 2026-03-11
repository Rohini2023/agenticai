import sqlite3

def init_db():

    conn = sqlite3.connect("database/elderly_chatbot.db")
    cursor = conn.cursor()

    # Caregiver table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS caregivers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        relation TEXT
    )
    """)

    # Reminder table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reminder_text TEXT,
        reminder_time TEXT
    )
    """)

    # Chat history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_text TEXT,
        bot_text TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database initialized successfully")


if __name__ == "__main__":
    init_db()