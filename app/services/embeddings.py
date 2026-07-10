from langchain_google_genai import GoogleGenerativeAIEmbedding 
from app.services.config import GOOGLE_API_KEY

def get_embeddings():
    return GoogleGenerativeAIEmbedding(model='models/text-embedding-004',google_api_key=GOOGLE_API_KEY)
