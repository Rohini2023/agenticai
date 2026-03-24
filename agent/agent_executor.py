from agent.intent_classifier import detect_intent
from agent.tools import reminder_tool, emergency_tool, chat_tool, news_tool


def run_agent(text):

    intent = detect_intent(text)

    print("Detected intent:", intent)

    if intent == "exit":
        return "Stopping assistant"

    try:
        if intent == "emergency":
            return emergency_tool(text)

        elif intent == "reminder":
            return reminder_tool(text)

        elif intent == "news":
            return news_tool(text)

        else:
            return chat_tool(text)

    except Exception as e:
        print("Agent error:", e)
        return "Sorry, something went wrong"