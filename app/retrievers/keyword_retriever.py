from pathlib import Path
from rank_bm25 import BM25Okapi

from app.services.document_loader import EnterpriseDocumentLoader
class KeywordRetriever:
    def __init__(self):
        self.loader = EnterpriseDocumentLoader()
        self.documents=self.loader.load_documents()

        corpus= [
            doc.page_content.split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(corpus)


    def retrieve(self, query: str, k: int = 4):
        scores = self.bm25.get_scores(query.split())

        ranked = sorted(
            zip(scores,self.documents),
            reverse=True,
            key=lambda x: x[0])

        return [doc for _, doc in ranked[:k]]