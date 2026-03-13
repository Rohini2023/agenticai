from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3")

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Classify the intent of the message.

Possible intents:
emergency
reminder
chat

Message:
{text}

Return only the intent.
"""
)

chain = LLMChain(llm=llm, prompt=prompt)


def detect_intent(text):

    intent = chain.run(text)

    return intent.strip().lower()