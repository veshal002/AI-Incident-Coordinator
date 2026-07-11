from langchain_google_genai import ChatGoogleGenerativeAI

from app.services.config import GOOGLE_API_KEY

def get_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.5
    )

    return llm
