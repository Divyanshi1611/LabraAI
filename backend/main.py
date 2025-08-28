from .embeddings.embed_and_store import process_pdf_and_store
from backend.retriever.retriever_chain import get_qa_chain
from dotenv import load_dotenv
load_dotenv()



if __name__ == "__main__":
    process_pdf_and_store("data/sample_docs/SpecialIssueFlyer.pdf")
    qa_chain = get_qa_chain()
    
    while True:
        query = input("\n🔍 Ask a research question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa_chain.invoke(query)
        print("\n💡 Answer:\n", answer)