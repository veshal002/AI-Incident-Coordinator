from app.graph.graph_loader import enterprise_graph


class GraphRetriever:

    def retrieve(self, entity):

        return enterprise_graph.neighbors(entity)