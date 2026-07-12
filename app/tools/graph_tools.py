from langchain.tools import tool

from app.retrievers.graph_retriever import GraphRetriever


retriever = GraphRetriever()


@tool
def graph_search(entity: str):
    """
    Retrieve related enterprise systems.
    """

    results = retriever.retrieve(entity)

    if not results:
        return "No graph relationships found."

    lines = []

    for item in results:
        lines.append(
            f"{entity} --{item['relation']}--> {item['target']}"
        )

    return "\n".join(lines)