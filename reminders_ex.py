# import sqlite3

# DB = "database/elderly_chatbot.db"

# conn = sqlite3.connect(DB)

# cursor = conn.cursor()

# cursor.execute("""
# SELECT * FROM reminders
# """)

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# conn.close()

import sqlite3

# DB = "database/elderly_chatbot.db"

# conn = sqlite3.connect(DB)

# cursor = conn.cursor()

# cursor.execute("""
# DELETE FROM reminders
# """)

# conn.commit()

# conn.close()

# print("✅ All reminders deleted")


import sqlite3

DB = "database/elderly_chatbot.db"

conn = sqlite3.connect(DB)

cursor = conn.cursor()

# 🔥 DROP TABLE
cursor.execute("""
DROP TABLE IF EXISTS reminders
""")

conn.commit()

print("✅ reminders table deleted")

# 🔥 CREATE AGAIN
cursor.execute("""

CREATE TABLE reminders(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    task TEXT NOT NULL,

    reminder_time DATETIME NOT NULL,

    status TEXT DEFAULT 'pending',

    miss_count INTEGER DEFAULT 0,

    created_at DATETIME DEFAULT (
        datetime('now','localtime')
    )
)

""")

conn.commit()

print("✅ reminders table recreated")

conn.close()