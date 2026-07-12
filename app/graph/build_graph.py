from app.services.document_loader import EnterpriseDocumentLoader
from app.graph.graph_builder import GraphBuilder

loader=EnterpriseDocumentLoader()

documents=loader.load()

builder = GraphBuilder()

store=builder.build(documents)

store.save("graph.pkl")

print("Knowledge graph saved.")