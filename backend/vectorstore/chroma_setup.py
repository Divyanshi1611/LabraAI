import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./data/chroma_db"
))

collection = client.get_or_create_collection("papers")

def add_to_vectorstore(doc_id, text, embedding):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id]
    )
