import pickle

from app.graph.enterprise_graph import EnterpriseGraph


class GraphStore:

    def __init__(self):
        self.graph = EnterpriseGraph()

    def add_relation(self, source, relation, target):
        self.graph.add_relationship(
            source,
            target,
            relation
        )

    def neighbors(self, entity):
        return self.graph.neighbors(entity)

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.graph, f)

    @staticmethod
    def load(path):
        with open(path, "rb") as f:
            return pickle.load(f)