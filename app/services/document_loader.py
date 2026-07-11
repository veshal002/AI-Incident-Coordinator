from pathlib import Path
from rank_bm25 import BM25

from langchain_community.document_loaders import ( CSVLoader, DirectoryLoader, TextLoader)



class EnterpriseDocumentLoader:

    def load_documents(self):
            data_path=Path("data")

            docs=[]

            docs.extend(
                CSVLoader(
                    str(data_path / "incidents" / "historical_incidents.csv")
                ).load()
            )

            docs.extend(
                DirectoryLoader(
                    str(data_path / "runbooks"),
                    glob="*.md",
                    loader_cls=TextLoader,
                ).load()
            )

            docs.extend(
                DirectoryLoader(
                    str(data_path / "sops"),
                    glob="*.md",
                    loader_cls=TextLoader,
                ).load()
            )

            docs.extend(
                DirectoryLoader(
                    str(data_path / "logs"),
                    glob="*.log",
                    loader_cls=TextLoader,
                ).load()
            )
            
            return docs