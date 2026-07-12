import networkx as nx
import pickle

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
        
        return list(self.graph.neighbors(node))
    
    def save(self,path):
        with open(open,"wb") as f:
            pickle.dump(self.graph,f)
    
    def load(self,path):
        with open(path,"rb") as f:
            self.graph=pickle.load(f)