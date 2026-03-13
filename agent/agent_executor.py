from langchain_ollama import OllamaLLM
from agent.tools import reminder_tool, emergency_tool, chat_tool, news_tool


llm = OllamaLLM(model="llama3")


def detect_intent(text):

    prompt = f"""
You are an intent classifier for an elderly voice assistant.

Classify the message into ONE of these categories:

emergency → user in danger, fall, pain, help
reminder → user wants to set reminder
news → user asks for news
chat → normal conversation

Examples:

Message: remind me to take medicine at 8 pm
Intent: reminder

Message: I fell down help me
Intent: emergency

Message: what is today's news
Intent: news

Message: how are you
Intent: chat

Message:
{text}

Return ONLY one word:
emergency
reminder
news
chat
"""

    intent = llm.invoke(prompt)

    return intent.strip().lower()


def run_agent(text):

    intent = detect_intent(text)

    print("Detected intent:", intent)

    if "emergency" in intent:

        return emergency_tool(text)

    elif "reminder" in intent:

        return reminder_tool(text)

    elif "news" in intent:

        return news_tool(text)

    else:

        return chat_tool(text)