import networkx as nx


class EnterpriseGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_relationship(self, source, target, relation):
        self.graph.add_edge(source, target, relation=relation)

    def neighbors(self, node):
        if node not in self.graph:
            return []

        results = []

        for neighbor in self.graph.neighbors(node):
            relation = self.graph.edges[node, neighbor]["relation"]

            results.append({
                "target": neighbor,
                "relation": relation
            })

        return results