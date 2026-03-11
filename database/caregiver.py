import sqlite3

DB = "database/elderly_chatbot.db"


def add_caregiver(name, phone, relation):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO caregivers(name,phone,relation) VALUES(?,?,?)",
        (name, phone, relation)
    )

    conn.commit()
    conn.close()

    print("Caregiver added successfully")


def get_all_caregivers():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT id,name,phone,relation FROM caregivers")

    rows = cursor.fetchall()

    conn.close()

    return rows