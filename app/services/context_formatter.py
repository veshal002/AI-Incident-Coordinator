class ContextFormatter:

    @staticmethod
    def format(documents):
        return "\n\n".join(doc.page_content for doc in documents)