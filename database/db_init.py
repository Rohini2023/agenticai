import sqlite3

def init_db():

    conn = sqlite3.connect("database/elderly_chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS caregivers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    email TEXT,                       -- 🔥 for email alerts
    relation TEXT,
    priority INTEGER DEFAULT 1,       -- 🔥 primary / secondary caregiver
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
    
    # 🔥 UPDATED REMINDER TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        reminder_time DATETIME NOT NULL,
        status TEXT DEFAULT 'pending',
        miss_count INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
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