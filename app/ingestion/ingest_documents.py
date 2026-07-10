from pathlib import Path

from langchain_community.document_loaders import(CSVLoader,DirectoryLoader,TextLoader,UnstructuredMarkdownLoader)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.database.vector_store import get_vector_store

# Load
DATA_PATH=Path("data")

documents=[]

documents.extend(CSVLoader(str(DATA_PATH/"incidents"/'historical_incidents.csv')).load())

documents.extend(DirectoryLoader(str(DATA_PATH/'runbooks'),glob="*.md",loader_cls=UnstructuredMarkdownLoader).load())
documents.extend(DirectoryLoader(str(DATA_PATH/'sops'),glob="*.md",loader_cls=UnstructuredMarkdownLoader).load())
documents.extend(DirectoryLoader(str(DATA_PATH/'logs'),glob="*.log",loader_cls=TextLoader).load())

# SPLIT

splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)

chunks=splitter.split_documents(documents)

# store
vector_store=get_vector_store()
vector_store.add_documents(chunks)

print(f'indexed {len(chunks)} chunks.')