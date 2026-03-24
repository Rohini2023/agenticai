import sqlite3

DB = "database/elderly_chatbot.db"


def save_chat(user, bot):

    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO chat_history(user_text, bot_text) VALUES (?, ?)",
            (user, bot)
        )

        conn.commit()
        conn.close()

        print("💾 Chat saved")

    except Exception as e:
        print("❌ Chat save error:", e)



def get_chat_history(limit=10):
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT user_text, bot_text FROM chat_history ORDER BY id DESC LIMIT ?",
            (limit,)
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    except Exception as e:
        print("❌ Fetch error:", e)
        return []