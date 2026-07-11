from pathlib import Path

from langchain_community.document_loaders import(CSVLoader,DirectoryLoader,TextLoader,UnstructuredMarkdownLoader)
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.database.vector_store import get_vector_store
from app.services.document_loader import EnterpriseDocumentLoader

# LOAD
loader=EnterpriseDocumentLoader()
documents=loader.load_documents()

# SPLIT

splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)

chunks=splitter.split_documents(documents)

# store
vector_store=get_vector_store()
vector_store.add_documents(chunks)

print(f'indexed {len(chunks)} chunks.')