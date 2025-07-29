# retriever/claude_retriever.py

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.retrievers import ContextualCompressionRetriever
from langchain.chat_models import ChatAnthropic
from langchain.retrievers.document_compressors import LLMChainExtractor

def get_claude_retriever(persist_directory="chroma_db"):
    embedding_function = HuggingFaceEmbeddings(model_name="allenai/scibert_scivocab_uncased")
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_function
    )

    llm = ChatAnthropic(model="claude-3-opus-20240229", temperature=0)
    compressor = LLMChainExtractor.from_llm(llm)

    retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=vectordb.as_retriever()
    )
    
    return retriever
