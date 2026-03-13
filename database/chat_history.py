import sqlite3

DB = "database/elderly_chatbot.db"


def save_chat(user, bot):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat_history(user_text,bot_text) VALUES(?,?)",
        (user, bot)
    )

    conn.commit()

    conn.close()