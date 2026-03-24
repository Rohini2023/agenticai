import sqlite3

DB = "database/elderly_chatbot.db"

def add_caregiver(name, phone, relation, email=None, priority=1):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO caregivers(name, phone, relation, email, priority) VALUES (?, ?, ?, ?, ?)",
        (name, phone, relation, email, priority)
    )

    conn.commit()
    conn.close()

    print("✅ Caregiver added successfully")


def get_all_caregivers():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, phone, relation, email, priority 
        FROM caregivers ORDER BY priority ASC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows