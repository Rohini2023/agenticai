# from langchain_ollama import OllamaLLM

# from agent.reminder_extractor import extract_reminder
# from database.reminder import save_reminder
# from database.caregiver import get_all_caregivers

# llm = OllamaLLM(model="llama3")

# def reminder_tool(text):

#     task, time = extract_reminder(text)

#     if task == "" or task is None:
#         return "I could not understand the reminder task."

#     if time == "None" or time is None:
#         return f"What time should I remind you to {task}?"

#     save_reminder(task, time)

#     return f"Reminder set for {task} at {time}"


# def emergency_tool(text):

#     caregivers = get_all_caregivers()

#     for name, phone in caregivers:
#         print("🚨 Alert sent to", name, phone)

#     return "Emergency alert sent to caregivers"


# def chat_tool(text):

#     return llm.invoke(text)


# def news_tool(text):

#     prompt = "Give today's important news in short."

#     return llm.invoke(prompt)


from langchain_ollama import OllamaLLM

from agent.reminder_extractor import extract_reminder
from database.reminder import save_reminder
from database.caregiver import get_all_caregivers
from services.reminder_scheduler import schedule_reminder
from services.email_service import send_email
from audio.text_speech import speak
from newsapi import NewsApiClient
llm = OllamaLLM(model="llama3:latest")


# # ✅ REMINDER TOOL
# from datetime import datetime, timedelta

# def reminder_tool(text):

#     task, time = extract_reminder(text)

#     if not task or task == "none":
#         return "What should I remind you about?"

#     if not time:
#         return f"When should I remind you to {task}?"

#     reminder_id = save_reminder(task, time)

#     from reminder_scheduler import schedule_reminder
#     schedule_reminder(task, time, reminder_id)

#     return f"Reminder set for {task} at {time.strftime('%I:%M %p')}"

from datetime import datetime

from agent.reminder_extractor import extract_reminder
from database.reminder import save_reminder
from services.reminder_scheduler import schedule_reminder


def reminder_tool(text):

    # STEP 1 → Extract task + time
    task, reminder_time = extract_reminder(text)

    if not task or task == "none":
        return "What should I remind you about?"

    if not reminder_time:
        return f"When should I remind you to {task}?"

    try:
        # STEP 2 → Save reminder in DB (STRING)
        reminder_id = save_reminder(
            task,
            reminder_time
        )

        # STEP 3 → Convert STRING → DATETIME
        run_time = datetime.fromisoformat(
            reminder_time
        )

        # STEP 4 → Schedule reminder
        schedule_reminder(
            task,
            run_time,
            reminder_id
        )

        # STEP 5 → User response
        formatted_time = run_time.strftime(
            "%I:%M %p"
        )

        return f"Reminder set for {task} at {formatted_time}"

    except Exception as e:
        print("Reminder Tool Error:", e)
        return "Sorry, I could not set the reminder"
# def reminder_tool(text):

#     task, time = extract_reminder(text)

#     # ❌ FIX: invalid task
#     if not task or task.lower() in ["none", ""]:
#         return "I could not understand the reminder"

#     # ❌ FIX: invalid time
#     if not time:
#         return f"What time should I remind you to {task}?"

#     # 🔥 FIX: if time is string → convert
#     if isinstance(time, str):
#         time = datetime.fromisoformat(time)

#     # 🔥 FIX: ensure future time
#     if time < datetime.now():
#         time = datetime.now() + timedelta(minutes=1)

#     reminder_id = save_reminder(task, time)
#     schedule_reminder(task, time, reminder_id)

#     formatted = time.strftime("%I:%M %p")

#     return f"Reminder set for {task} at {formatted}"

# 🚨 EMERGENCY TOOL
# def emergency_tool(text):

#     caregivers = get_all_caregivers()

#     if not caregivers:
#         return "No caregivers found"

#     for row in caregivers:
#         _, name, phone, relation, email, priority = row

#         if email:
#             send_email(
#                 email,
#                 "🚨 EMERGENCY ALERT",
#                 f"User needs immediate help!\n\n📝 Issue: {text}"
#             )

#             print(f"📧 Emergency email sent to {name}")

#     speak("Emergency alert sent")

#     return "Emergency alert sent to caregivers"


def emergency_tool(text):

    caregivers = get_all_caregivers()

    primary = sorted(caregivers, key=lambda x: x[5])[0]

    _, name, phone, relation, email, priority = primary

    if email:
        send_email(email, "🚨 EMERGENCY ALERT", text)
    speak("Emergency alert sent")
    return f"Emergency alert sent to {name}" 

# 💬 CHAT TOOL
def chat_tool(text):

    try:
        response = llm.invoke(text)
        return response.strip()
    except Exception as e:
        print("Chat error:", e)
        return "Sorry, I couldn't understand that."


# 📰 NEWS TOOL
# import requests
# # from langchain_ollama import OllamaLLM

# llm = OllamaLLM(model="llama3")

# API_KEY = "33d3a5b333ec42d383b2bb66394d423e"


# def detect_language(text):
#     text = text.lower()

#     if any(word in text for word in ["malayalam", "മലയാളം"]):
#         return "Malayalam"
#     elif any(word in text for word in ["tamil", "தமிழ்"]):
#         return "Tamil"
#     elif any(word in text for word in ["hindi", "हिंदी"]):
#         return "Hindi"
#     else:
#         return "English"


# newsapi = NewsApiClient(api_key="your_api_key_here")

# llm = OllamaLLM(model="llama3")


# def detect_language(text):
#     text = text.lower()

#     if any(word in text for word in ["malayalam", "മലയാളം"]):
#         return "Malayalam"
#     elif any(word in text for word in ["tamil", "தமிழ்"]):
#         return "Tamil"
#     elif any(word in text for word in ["hindi", "हिंदी"]):
#         return "Hindi"
#     else:
#         return "English"


# def detect_category(text):
#     text = text.lower()

#     if "sports" in text:
#         return "sports"
#     elif "technology" in text or "tech" in text:
#         return "technology"
#     elif "health" in text:
#         return "health"
#     elif "business" in text:
#         return "business"
#     else:
#         return "general"


# def news_tool(text):

#     lang = detect_language(text)
#     category = detect_category(text)

#     try:
#         # 🔥 Fetch real news
#         data = newsapi.get_top_headlines(
#             country="in",
#             category=category,
#             page_size=5
#         )

#         articles = data.get("articles", [])

#         if not articles:
#             return "No news available right now."

#         # 🔹 Extract headlines
#         raw_news = ""
#         for i, article in enumerate(articles, 1):
#             title = article.get("title") or ""
#             desc = article.get("description") or ""

#             if not title:
#                 continue

#             raw_news += f"{i}. {title}. {desc}\n"

#         # 🤖 LLM summarization
#         prompt = f"""
# Summarize the following news into 3 short, simple, voice-friendly points.

# Rules:
# - Very simple words (for elderly users)
# - Each point = one short sentence
# - No complex terms
# - Language: {lang}

# News:
# {raw_news}
# """

#         summary = llm.invoke(prompt)

#         return summary.strip()

#     except Exception as e:
#         print("News error:", e)
#         return "Unable to fetch news right now."


import feedparser
from langchain_ollama import OllamaLLM
from audio.text_speech import speak

# 🔥 LLaMA Model
llm = OllamaLLM(model="llama3:latest")


# 🌐 Detect Language
def detect_language(text):
    text = text.lower()

    if any(word in text for word in ["malayalam", "മലയാളം"]):
        return "Malayalam"

    elif any(word in text for word in ["tamil", "தமிழ்"]):
        return "Tamil"

    elif any(word in text for word in ["hindi", "हिंदी"]):
        return "Hindi"

    else:
        return "English"


# 📰 Detect News Category
def detect_category(text):
    text = text.lower()

    if "sports" in text:
        return "sports"

    elif "technology" in text or "tech" in text:
        return "technology"

    elif "health" in text:
        return "health"

    elif "business" in text:
        return "business"

    else:
        return "general"


# 🔗 Select RSS Feed URL
def get_news_url(language, category):

    # ✅ Malayalam Kerala News
    if language == "Malayalam":
        return "https://news.google.com/rss?hl=ml&gl=IN&ceid=IN:ml"

    # ✅ Tamil News
    elif language == "Tamil":
        return "https://news.google.com/rss?hl=ta&gl=IN&ceid=IN:ta"

    # ✅ Hindi News
    elif language == "Hindi":
        return "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"

    # ✅ English Category-Based News
    else:
        if category == "sports":
            return "https://news.google.com/rss/headlines/section/topic/SPORTS?hl=en-IN&gl=IN&ceid=IN:en"

        elif category == "technology":
            return "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=en-IN&gl=IN&ceid=IN:en"

        elif category == "health":
            return "https://news.google.com/rss/headlines/section/topic/HEALTH?hl=en-IN&gl=IN&ceid=IN:en"

        elif category == "business":
            return "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-IN&gl=IN&ceid=IN:en"

        else:
            return "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"


# 📰 MAIN NEWS TOOL WITH AUDIO OUTPUT
def news_tool(text):

    try:
        # 🔥 Detect language + category
        language = detect_language(text)
        category = detect_category(text)

        # 🔥 Get RSS URL
        url = get_news_url(language, category)

        print("📰 Fetching News From:", url)

        # 🔥 Parse RSS Feed
        feed = feedparser.parse(url)

        if not feed.entries:
            response = "No news available right now."
            speak(response)
            return response

        # 🔹 Extract Top 5 News
        raw_news = ""

        for i, entry in enumerate(feed.entries[:5], 1):
            title = entry.title if hasattr(entry, "title") else ""

            if not title:
                continue

            raw_news += f"{i}. {title}\n"

        print("📰 Raw News:\n", raw_news)

        # 🤖 LLaMA Prompt
        prompt = f"""
Summarize the following news into 3 short, simple, voice-friendly points.

Rules:
- Use very simple words for elderly users
- Keep each point short
- Easy to speak aloud
- No difficult words
- Language: {language}

News:
{raw_news}
"""

        summary = llm.invoke(prompt).strip()

        # 🔥 Final Voice-Friendly Response
        if language == "Malayalam":
            final_response = f"ഇന്നത്തെ പ്രധാന വാർത്തകൾ. {summary}"

        elif language == "Tamil":
            final_response = f"இன்றைய முக்கிய செய்திகள். {summary}"

        elif language == "Hindi":
            final_response = f"आज की मुख्य खबरें। {summary}"

        else:
            final_response = f"Today's important news. {summary}"

        print("🔊 Speaking News:", final_response)

        # 🔥 Audio Output
        speak(final_response)

        return final_response

    except Exception as e:
        print("News Error:", e)

        error_response = "Unable to fetch news right now."
        speak(error_response)

        return error_response