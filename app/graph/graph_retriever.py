from app.graph.graph_store import GraphStore


class GraphRetriever:

    def __init__(self):

        self.store = GraphStore()

        self.store.load("graph.pkl")

    def retrieve(self, entity):

        return self.store.neighbors(entity)