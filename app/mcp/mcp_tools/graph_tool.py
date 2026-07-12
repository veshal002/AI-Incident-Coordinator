from app.retrievers.graph_retriever import GraphRetriever

retriever = GraphRetriever()


def search_graph(entity: str):
    """
    Search enterprise dependency graph.
    """

    return retriever.retrieve(entity)