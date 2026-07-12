from app.graph.graph_store import GraphStore
from app.agents.graph_extraction_agent import GraphExtractionAgent

class GraphBuilder:
    def __inti__(self):
        self.store = GraphStore()
        self.extractor = GraphExtractionAgent

    def build(self,documents):
        for doc in documents:
            extraction=self.extractor.extract(doc.page_content)

            for relation in extraction.relationships:
                self.store.add_relation(relation.source,relation.relation,relation.target)

        return self.store