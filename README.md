# 🧪 LabraAI – Autonomous Research Assistant for Scientific Hypothesis Generation  

LabraAI is an AI-powered research assistant that mimics a scientist’s creative process.  
It retrieves cutting-edge research papers, processes scientific knowledge, and generates **novel hypotheses** or **experiment suggestions** by combining retrieved insights.  

This project is designed to assist researchers, students, and professionals in accelerating scientific discovery by leveraging advanced **RAG (Retrieval-Augmented Generation)** pipelines, embeddings, and LLM reasoning.  

---

## 🚀 Features  

- 📄 **Scientific Document Ingestion**: Process and embed PDFs, datasets, and papers.  
- 🔍 **Intelligent Retrieval**: Retrieve the most relevant research context from a vector store (SciBERT + ChromaDB).  
- 🧠 **Hypothesis Generation**: Generate grounded hypotheses using Claude/Gemini.  
- 🕸️ **Knowledge Graph Integration** *(Future Phase)*: Connect retrieved ideas with citation networks.  
- 🔄 **Interactive Refinement**: User feedback loop for improving hypotheses.  
- 🌐 **Web Interface**: Clean React.js frontend for easy interaction.  

---

## 🏗️ Architecture  

```mermaid
flowchart TD
    A[User Query] --> B[Retriever - ChromaDB + SciBERT]
    B --> C[Relevant Papers/Datasets]
    C --> D[LLM (Claude/Gemini)]
    D --> E[Hypothesis Generation]
    E --> F[User Feedback & Refinement]
