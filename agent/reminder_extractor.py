from langchain_community.llms import Ollama
import dateparser

llm = Ollama(model="llama3")


def extract_reminder(text):

    prompt = f"""
Extract the reminder task and time from this message.

Message:
{text}

Return only in this format:

task: <task>
time: <time>
"""

    result = llm.invoke(prompt)

    task = ""
    time_text = ""

    for line in result.split("\n"):

        if "task" in line.lower():
            task = line.split(":")[-1].strip()

        if "time" in line.lower():
            time_text = line.split(":")[-1].strip()

    parsed_time = dateparser.parse(time_text)

    return task, str(parsed_time)