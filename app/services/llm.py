from langchain_openrouter import ChatOpenRouter

from app.services.config import OPENROUTER_API_KEY


def get_llm():

    llm = ChatOpenRouter(
        model="google/gemma-4-26b-a4b-it:free",
        google_api_key=OPENROUTER_API_KEY,
        temperature=0.5
    )

    return llm
