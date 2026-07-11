from app.retrievers.keyword_retriever import KeywordRetriever
from app.retrievers.semantic_retriever import SemanticRetriever


class HybridRetriever:

    def __init__(self):
        self.semantic= SemanticRetriever()
        self.keyword= KeywordRetriever()

    def retrieve(self, query: str):

        semantic_docs = self.semantic.retrieve(query)

        keyword_docs = self.keyword.retrieve(query)

        merged=[]

        seen=set()

        for doc in semantic_docs + keyword_docs:
            if doc.page_content not in seen:
                merged.append(doc)

                seen.add(doc.page_content)
        
        return merged