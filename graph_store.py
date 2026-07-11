import networkx as nx

class GraphStore:
    
    def __init__(self):
        self.graph =nx.DiGraph()

    def add_relation(self,source: str,relation: str, target: str):
        self.graph.add_node(source)
        self.graph.add_node(target)

        self.graph.add_edge(source,target,relation=relation)

    def neighbors(self,node: str):
        if node not in self.graph:
            return []
        
        return list(self.grpah.neighbors(node))