from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_summarize_chain():
    llm = Ollama(model="gemma3:1b")
    prompt = PromptTemplate.from_template(
        "Summarize the following email:\n\n{email_content}\n\nSummary:"
    )
    return LLMChain(llm=llm, prompt=prompt)
