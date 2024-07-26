import os
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def llm():
    mistral_model = "mistralai/Mistral-7B-Instruct-v0.2"

    llm = HuggingFaceEndpoint(repo_id=mistral_model,
                              temperature=0.7)

    # api_key = os.environ.get("GROQ_API_KEY")

    # chat = ChatGroq(temperature=0, model_name="Llama-3.1-8b-Instant")
    return llm
