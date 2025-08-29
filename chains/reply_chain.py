from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# def get_reply_chain():
#     llm = Ollama(model="gemma3:1b")
#     prompt = PromptTemplate.from_template(
#         "Generate a polite and professional reply to this email:\n\n{email_content}\n\nReply:"
#     )
#     return LLMChain(llm=llm, prompt=prompt)





from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from putergenai import PuterClient
from config import PUTER_TOKEN, LLM_MODEL   # store safely in config.py


# Create a thin wrapper so LangChain can call Puter
class PuterLLM:
    def __init__(self, client: PuterClient, model: str, temperature: float = 0.7):
        self.client = client
        self.model = model
        self.temperature = temperature

    def __call__(self, prompt: str) -> str:
        resp = self.client.ai_chat(
            messages=[{"role": "user", "content": prompt}],
            options={
                "model": self.model,
                "temperature": self.temperature
            }
        )
        return resp["response"]["result"]["message"]["content"].strip()


# Initialize Puter client
client = PuterClient(token=PUTER_TOKEN)

def get_reply_chain():
    llm = PuterLLM(client, model=LLM_MODEL, temperature=0.7)

    prompt = PromptTemplate.from_template(
        "Generate a polite and professional reply to this email:\n\n{email_content}\n\nReply:"
    )

    return LLMChain(llm=llm, prompt=prompt)
