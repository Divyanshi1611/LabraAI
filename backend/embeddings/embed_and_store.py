import os
from .pdf_loader import extract_text_from_pdf
from .scibert_embedder import generate_embedding
from ..vectorstore.chroma_setup import add_to_vectorstore

def process_pdf_and_store(pdf_path):
    doc_id = os.path.basename(pdf_path).replace(".pdf", "")
    text = extract_text_from_pdf(pdf_path)
    embedding = generate_embedding(text)
    add_to_vectorstore(doc_id, text, embedding)
    print(f"{doc_id} processed and stored.")
