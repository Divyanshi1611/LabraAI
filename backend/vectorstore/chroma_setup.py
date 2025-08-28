import chromadb

# Use PersistentClient for local storage. Set the path to your desired directory.
client = chromadb.PersistentClient(path="./data/chroma_db")

collection = client.get_or_create_collection("papers")

def add_to_vectorstore(doc_id, text, embedding):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id]
    )