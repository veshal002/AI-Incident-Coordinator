from langchain_chroma import Chroma
from app.services.embeddings import get_embeddings

def get_vector_store():
    embeddings=get_embeddings()

    return Chroma(collection_name="enterprise_knowledge",
                  embedding_function=embeddings,
                  persist_directory="chroma_db")