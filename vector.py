import chromadb
from dotenv import load_dotenv
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from schema import *

import os

load_dotenv()


chroma_db = chromadb.PersistentClient(path="./chroma")
chroma_collection = chroma_db.get_or_create_collection("embeddings")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

