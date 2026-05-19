# from agent.intent_classifier import detect_intent
# from agent.tools import reminder_tool, emergency_tool, chat_tool, news_tool


# def run_agent(text):

#     intent = detect_intent(text)

#     print("Detected intent:", intent)

#     if intent == "exit":
#         return "Stopping assistant"

#     try:
#         if intent == "emergency":
#             return emergency_tool(text)

#         elif intent == "reminder":
#             return reminder_tool(text)

#         elif intent == "news":
#             return news_tool(text)

#         else:
#             return chat_tool(text)

#     except Exception as e:
#         print("Agent error:", e)
#         return "Sorry, something went wrong"


### new agent_executor.py with better structure and error handling


from agent.intent_classifier import detect_intent

from agent.tools import (
    reminder_tool,
    emergency_tool,
    chat_tool,
    news_tool
)


def run_agent(text):

    # 🔥 Detect intent
    intent = detect_intent(text)

    print("Detected intent:", intent)

    try:

        # ==================================
        # EXIT
        # ==================================

        if intent == "exit":

            response = "Stopping assistant"

            selected_tool = "exit"

        # ==================================
        # EMERGENCY
        # ==================================

        elif intent == "emergency":

            response = emergency_tool(text)

            selected_tool = "emergency_tool"

        # ==================================
        # REMINDER
        # ==================================

        elif intent == "reminder":

            response = reminder_tool(text)

            selected_tool = "reminder_tool"

        # ==================================
        # NEWS
        # ==================================

        elif intent == "news":

            response = news_tool(text)

            selected_tool = "news_tool"

        # ==================================
        # CHAT
        # ==================================

        else:

            response = chat_tool(text)

            selected_tool = "chat_tool"

        # 🔥 RETURN FULL RESULT
        return {

            "intent": intent,

            "tool": selected_tool,

            "response": response
        }

    except Exception as e:

        print("Agent error:", e)

        return {

            "intent": intent,

            "tool": "error",

            "response": "Sorry, something went wrong"
        }