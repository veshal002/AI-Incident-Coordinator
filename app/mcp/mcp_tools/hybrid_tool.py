
from app.retrievers.hybrid_retriever import HybridRetriever
from app.services.context_formatter import ContextFormatter

retriever = HybridRetriever()


def search_documents(query: str) -> str:
    """
    Search enterprise documentation,
    SOPs,
    runbooks,
    historical incidents,
    and logs.
    """

    documents = retriever.retrieve(query)

    return ContextFormatter.format(documents)