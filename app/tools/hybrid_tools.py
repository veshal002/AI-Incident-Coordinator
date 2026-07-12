from langchain.tools import tool

from app.retrievers.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()


@tool
def hybrid_search(
    query: str,
) -> str:
    """
    Search enterprise SOPs,
    runbooks,
    incident reports,
    logs,
    and documentation.
    """

    docs = retriever.retrieve(query)

    if not docs:

        return "No enterprise documents found."

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )