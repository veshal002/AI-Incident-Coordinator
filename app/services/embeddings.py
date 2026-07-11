from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from app.services.config import GOOGLE_API_KEY

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')