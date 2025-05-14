import chromadb
from dotenv import load_dotenv
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from schema import *
import json

import os

load_dotenv()

embed_model = OpenAIEmbedding(model="text-embedding-3-large", api_key=os.getenv("OPENAI_API_KEY"))
openai = OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))


chroma_db = chromadb.PersistentClient(path="./chroma")
chroma_collection = chroma_db.get_or_create_collection("embeddings")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)


def get_index(data):
    documents = SimpleDirectoryReader(input_files=[f"../data/{data}"]).load_data()
    index = VectorStoreIndex.from_documents(documents=documents, embed_model=embed_model, vector_store=vector_store)
    query_engine = index.as_query_engine(output_cls=ClassInfo, response_mode="compact", llm=openai)
    response = query_engine.query("Extract all exam and project names along with their corresponding dates or weeks from the syllabus calendar.")
    print(json.dumps(response))

    return response


def get_quizzes(data):
    documents = SimpleDirectoryReader(input_files=[f"../data/{data}"]).load_data()
    index = VectorStoreIndex.from_documents(documents=documents, embed_model=embed_model, vector_store=vector_store)
    query_engine = index.as_query_engine(output_cls=ListOfMCQuizzes, response_mode="compact", llm=openai)
    response = query_engine.query("Provide me 5 number of quizzes with software engineer related based on the documents")
    return response


def get_qa_quiz(data):
    documents = SimpleDirectoryReader(input_files=[f"../data/{data}"]).load_data()
    index = VectorStoreIndex.from_documents(documents=documents, embed_model=embed_model, vector_store=vector_store)
    query_engine = index.as_query_engine(output_cls=ListOfQAQuizzes, response_mode="compact", llm=openai)
    response = query_engine.query("Give me 5 opened answer with software engineer related based on the documents, leave user_answer as empty")
    print(response)
    return response


def get_roadmap(data):
    documents = SimpleDirectoryReader(input_files=[f"../data/{data}"]).load_data()
    index = VectorStoreIndex.from_documents(documents=documents, embed_model=embed_model, vector_store=vector_store)
    query_engine = index.as_query_engine(output_cls=Roadmap, response_mode="compact", llm=openai)
    response = query_engine.query("Give me a huge roadmap to effective study and master this class, where to practice, such as provided links, books. Please list all important concepts")
    print(response)
    return response




while (choice := input("Select your options: (1) for extract class data, (2) for Multiple choice, (3) for QA Quiz: , (4) for roadmap: \n")) != "quit":
    if choice == "1":
        get_index("CSC_101.pdf")
    elif choice == "2":
        get_quizzes("Use Cases, Requirements, Competitive Analysis.pdf")
    elif choice == "3":
        get_qa_quiz("Use Cases, Requirements, Competitive Analysis.pdf")
    elif choice == "4":
        get_roadmap("CSC648_848_Syllabus.pdf")
    
















