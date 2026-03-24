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


from langchain_ollama import OllamaLLM
import dateparser
import re
from datetime import datetime

llm = OllamaLLM(model="llama3")


# 🔥 CLEAN TIME TEXT (VERY IMPORTANT)
def clean_time_text(text):
    text = text.lower()

    # 10-20 → 10:20
    text = re.sub(r'(\d{1,2})-(\d{1,2})', r'\1:\2', text)

    # 10.20 → 10:20
    text = re.sub(r'(\d{1,2})[.](\d{1,2})', r'\1:\2', text)

    return text.strip()


def extract_reminder(text):

    prompt = f"""
Extract the reminder task and time.

Message:
{text}

Rules:
- If time missing → return "none"
- Include words like today, tomorrow, morning, evening

Return ONLY:

task: <task>
time: <time or none>
"""

    try:
        result = llm.invoke(prompt)
    except Exception as e:
        print("LLM error:", e)
        result = ""

    task = ""
    time_text = ""

    for line in result.split("\n"):

        if "task" in line.lower():
            task = line.split(":", 1)[-1].strip()

        if "time" in line.lower():
            time_text = line.split(":", 1)[-1].strip()

    # 🔥 CLEAN TIME FORMAT
    time_text = clean_time_text(time_text)

    # 🔥 PARSE DATE SAFELY
    parsed_time = dateparser.parse(
        time_text,
        settings={
            "PREFER_DATES_FROM": "future",
            "DATE_ORDER": "DMY"
        }
    )

    # 🔥 DEFAULT TIME (if missing)
    if not parsed_time:
        parsed_time = dateparser.parse(
            "today 9:00 AM",
            settings={"PREFER_DATES_FROM": "future"}
        )

    return task, parsed_time