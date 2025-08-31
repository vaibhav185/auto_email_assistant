from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from putergenai import PuterClient
from config import PUTER_TOKEN, LLM_MODEL

from langchain_core.prompt_values import PromptValue

class PuterLLM:
    def __init__(self, client, model, temperature=0.7):
        self.client = client
        self.model = model
        self.temperature = temperature

    def __call__(self, prompt) -> str:
        # Convert LangChain PromptValue -> plain string
        if isinstance(prompt, PromptValue):
            prompt = prompt.to_string()
        else:
            prompt = str(prompt)

        resp = self.client.ai_chat(
            messages=[{"role": "user", "content": prompt}],
            options={"model": self.model, "temperature": self.temperature}
        )

        # ✅ Safe extraction
        try:
            return resp["response"]["result"]["message"]["content"].strip()
        except (KeyError, TypeError):
            try:
                return resp["response"]["result"].strip()
            except Exception:
                return str(resp).strip()


# Initialize Puter client
client = PuterClient(token=PUTER_TOKEN)


def get_classify_chain():
    llm = PuterLLM(client, model=LLM_MODEL, temperature=0.7)
    prompt = PromptTemplate.from_template(
        "Classify the priority of this email as High, Medium, or Low:\n\n{email_content}\n\nPriority:"
    )
    # return LLMChain(llm=llm, prompt=prompt)
    chain = prompt | llm
    return chain
