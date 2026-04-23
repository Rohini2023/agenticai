# # from langchain_community.llms import Ollama
# # import dateparser

# # llm = Ollama(model="llama3")


# # def extract_reminder(text):

# #     prompt = f"""
# # Extract the reminder task and time from this message.

# # Message:
# # {text}

# # Return only in this format:

# # task: <task>
# # time: <time>
# # """

# #     result = llm.invoke(prompt)

# #     task = ""
# #     time_text = ""

# #     for line in result.split("\n"):

# #         if "task" in line.lower():
# #             task = line.split(":")[-1].strip()

# #         if "time" in line.lower():
# #             time_text = line.split(":")[-1].strip()

# #     parsed_time = dateparser.parse(time_text)

# #     return task, str(parsed_time)



# from langchain_ollama import OllamaLLM
# import dateparser
# import re
# from datetime import datetime

# llm = OllamaLLM(model="llama3")


# def clean_time_text(text):
#     # 🔥 Fix formats like 9.53 → 9:53
#     text = re.sub(r'(\d{1,2})[.](\d{1,2})', r'\1:\2', text)
#     return text


# def extract_reminder(text):

#     prompt = f"""
# Extract the reminder task and time from this message.

# Message:
# {text}

# Rules:
# - If time not mentioned, return "none"
# - If date words like tomorrow, today, morning exist, include them

# Return only:

# task: <task>
# time: <time or none>
# """

#     result = llm.invoke(prompt)

#     task = ""
#     time_text = ""

#     for line in result.split("\n"):
#         if "task" in line.lower():
#             task = line.split(":", 1)[-1].strip()

#         if "time" in line.lower():
#             time_text = line.split(":", 1)[-1].strip()

#     # 🔥 Clean time format
#     time_text = clean_time_text(time_text)

#     # 🔥 Parse datetime
#     parsed_time = dateparser.parse(
#         time_text,
#         settings={"PREFER_DATES_FROM": "future"}
#     )

#     # 🔥 If no time → default 9 AM
#     if not parsed_time:
#         parsed_time = dateparser.parse(
#             "today 9:00 AM",
#             settings={"PREFER_DATES_FROM": "future"}
#         )

#     return task, parsed_time


# from langchain_ollama import OllamaLLM
# import dateparser
# import re
# from datetime import datetime, timedelta

# llm = OllamaLLM(model="llama3:latest")


# def extract_reminder(text):

#     text_lower = text.lower()

#     # ✅ STEP 1: RULE-BASED TASK EXTRACTION
#     task = ""

#     if "take" in text_lower:
#         task = text_lower.split("take")[-1].strip()

#     elif "remind me to" in text_lower:
#         task = text_lower.split("remind me to")[-1].strip()

#     else:
#         task = text_lower

#     # Clean task
#     task = re.sub(r"(after.*|at.*|tomorrow.*|today.*)", "", task).strip()

#     # ❌ If still empty → fallback
#     if not task or len(task) < 2:
#         task = "medicine"

#     # ✅ STEP 2: TIME EXTRACTION (SMART)

#     time = None

#     # 🔥 AFTER X MINUTES
#     match = re.search(r'after (\d+) (minute|minutes)', text_lower)
#     if match:
#         mins = int(match.group(1))
#         time = datetime.now() + timedelta(minutes=mins)

#     # 🔥 AFTER X HOURS
#     match = re.search(r'after (\d+) (hour|hours)', text_lower)
#     if match:
#         hrs = int(match.group(1))
#         time = datetime.now() + timedelta(hours=hrs)

#     # 🔥 TOMORROW
#     if "tomorrow" in text_lower:
#         time = dateparser.parse("tomorrow 9:00 AM")

#     # 🔥 SPECIFIC TIME
#     if not time:
#         parsed = dateparser.parse(
#             text,
#             settings={"PREFER_DATES_FROM": "future"}
#         )
#         if parsed:
#             time = parsed

#     # ❌ FINAL FALLBACK
#     if not time:
#         time = datetime.now() + timedelta(minutes=1)

#     return task, time




from langchain_ollama import OllamaLLM
import dateparser
import re
from datetime import datetime, timedelta

llm = OllamaLLM(model="llama3:latest")


def extract_reminder(text):

    text_lower = text.lower()

    # -------------------------
    # STEP 1: TASK EXTRACTION
    # -------------------------
    task = ""

    if "remind me to" in text_lower:
        task = text_lower.split("remind me to")[-1].strip()

    elif "take" in text_lower:
        task = text_lower.split("take")[-1].strip()

    else:
        task = text_lower

    # Remove time words
    task = re.sub(
        r"(after.*|at.*|tomorrow.*|today.*)",
        "",
        task
    ).strip()

    # fallback
    if not task or len(task) < 2:
        task = "medicine"

    # -------------------------
    # STEP 2: TIME EXTRACTION
    # -------------------------
    reminder_time = None

    # after X minutes
    match = re.search(r'after (\d+) (minute|minutes)', text_lower)
    if match:
        mins = int(match.group(1))
        reminder_time = datetime.now() + timedelta(minutes=mins)

    # after X hours
    match = re.search(r'after (\d+) (hour|hours)', text_lower)
    if match:
        hrs = int(match.group(1))
        reminder_time = datetime.now() + timedelta(hours=hrs)

    # tomorrow
    elif "tomorrow" in text_lower:
        reminder_time = dateparser.parse(
            "tomorrow 9:00 AM"
        )

    # specific time
    if not reminder_time:
        parsed = dateparser.parse(
            text,
            settings={
                "PREFER_DATES_FROM": "future"
            }
        )

        if parsed:
            reminder_time = parsed

    # final fallback → 1 min later
    if not reminder_time:
        reminder_time = datetime.now() + timedelta(minutes=1)

    # -------------------------
    # STEP 3: FORMAT FIX 🔥
    # -------------------------
    reminder_time = reminder_time.replace(microsecond=0)

    # convert to SQLite-safe string
    formatted_time = reminder_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print("⏰ Final Reminder Time:", formatted_time)

    return task, formatted_time