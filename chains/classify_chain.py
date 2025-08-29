from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


def get_classify_chain():
    llm = Ollama(model="gemma3:1b")
    prompt = PromptTemplate.from_template(
        "Classify the priority of this email as High, Medium, or Low:\n\n{email_content}\n\nPriority:"
    )
    return LLMChain(llm=llm, prompt=prompt)
