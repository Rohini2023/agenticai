from langchain_community.llms import Ollama
from agent.reminder_extractor import extract_reminder
from database.reminder import save_reminder
from database.caregiver import get_all_caregivers

llm = Ollama(model="llama3")

def reminder_tool(text):

    task, time = extract_reminder(text)

    if task == "" or task is None:
        return "I could not understand the reminder task."

    if time == "None" or time is None:
        return f"What time should I remind you to {task}?"

    save_reminder(task, time)

    return f"Reminder set for {task} at {time}"


def emergency_tool(text):

    caregivers = get_all_caregivers()

    for name, phone in caregivers:
        print("🚨 Alert sent to", name, phone)

    return "Emergency alert sent to caregivers"


def chat_tool(text):

    return llm.invoke(text)


def news_tool(text):

    prompt = "Give today's important news in short."

    return llm.invoke(prompt)