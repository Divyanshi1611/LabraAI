from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from .arxiv_fetcher import fetch_arxiv_abstracts

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_qa_chain():
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # More general model

    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )

    # Ask user for research domain and fetch arXiv papers
    research_domain = input("Enter a research domain for hypothesis generation: ")
    populate_vectorstore_with_arxiv(db, embedding_model, research_domain)

    print("Number of documents in vector store:", len(db.get()))

    llm = ChatGoogleGenerativeAI(
        google_api_key=GEMINI_API_KEY,
        model="gemini-2.5-flash",
        temperature=0.2,
        max_output_tokens=1024
    )

    # Custom prompt for hypothesis generation
    from langchain.prompts import PromptTemplate
    QA_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template="Given the following research abstracts:\n{context}\nSuggest a novel research hypothesis or experiment for the domain. Question: {question}\nHypothesis:"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(),
        chain_type_kwargs={"prompt": QA_PROMPT}
    )

    return qa_chain

def populate_vectorstore_with_arxiv(db, embedding_model, research_domain):
    abstracts = fetch_arxiv_abstracts(research_domain, max_results=5)
    for idx, abstract in enumerate(abstracts):
        embedding = embedding_model.embed_documents([abstract])[0]
        db.add_texts([abstract], embeddings=[embedding], ids=[f"arxiv_{idx}"])
    print(f"Added {len(abstracts)} arXiv abstracts to vector store.")
