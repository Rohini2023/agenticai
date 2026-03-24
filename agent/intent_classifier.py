# # from langchain_community.llms import Ollama
# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain

# # llm = Ollama(model="llama3")

# # prompt = PromptTemplate(
# #     input_variables=["text"],
# #     template="""
# # Classify the intent of the message.

# # Possible intents:
# # emergency
# # reminder
# # chat

# # Message:
# # {text}

# # Return only the intent.
# # """
# # )

# # chain = LLMChain(llm=llm, prompt=prompt)


# # def detect_intent(text):

# #     intent = chain.run(text)

# #     return intent.strip().lower()



# from langchain_ollama import OllamaLLM
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# llm = OllamaLLM(model="llama3")

# prompt = PromptTemplate(
#     input_variables=["text"],
#     template="""
# Classify the intent of the message.

# Possible intents:
# emergency
# reminder
# chat

# Message:
# {text}

# Return only one word: emergency OR reminder OR chat
# """
# )

# chain = LLMChain(llm=llm, prompt=prompt)


# def detect_intent(text):
#     text_lower = text.lower()

#     # 🔥 Rule-based (fast + reliable)
#     if any(word in text_lower for word in ["remind", "medicine", "tablet", "take"]):
#         return "reminder"

#     if any(word in text_lower for word in ["help", "emergency", "fell", "pain"]):
#         return "emergency"

#     # 🤖 LLM fallback
#     intent = chain.run(text)

#     return intent.strip().lower()


from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")


def detect_intent(text):
    text_lower = text.lower().strip()

    # ✅ EXIT
    if any(word in text_lower for word in ["exit", "quit", "stop"]):
        return "exit"

    # ✅ RULE-BASED
    if any(word in text_lower for word in ["remind", "medicine", "tablet", "take"]):
        return "reminder"

    if any(word in text_lower for word in ["help", "emergency", "fell", "pain"]):
        return "emergency"

    if "news" in text_lower:
        return "news"

    # 🤖 LLM fallback
    prompt = f"""
Classify the intent:

{text}

Return ONLY:
reminder OR emergency OR news OR chat
"""

    try:
        response = llm.invoke(prompt).strip().lower()

        if "reminder" in response:
            return "reminder"
        elif "emergency" in response:
            return "emergency"
        elif "news" in response:
            return "news"
        else:
            return "chat"

    except Exception as e:
        print("Intent LLM error:", e)
        return "chat"