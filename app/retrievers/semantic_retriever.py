from app.database.vector_store import get_vector_store

class SemanticRetriever:
    def __init__(self):
        self.vector_store=get_vector_store()

    def retrieve(self, query: str,k: int=4):
        docs= self.vector_store.similarity_search(query,k=k)
        return docs