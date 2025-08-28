# LabraAI: Autonomous Research Assistant for Scientific Hypothesis Generation

LabraAI is an **AI-powered autonomous research assistant** designed to help researchers generate **novel scientific hypotheses** by retrieving, analyzing, and synthesizing cutting-edge research papers and datasets. It mimics a scientist’s creative process by combining retrieval, reasoning, and hypothesis generation.

---

## 🚀 Features
- **Research Domain Input**: Enter a scientific domain or question (e.g., "Quantum materials" or "Cancer immunotherapy").
- **Document Retrieval**: Fetches relevant papers from arXiv, PubMed, and other sources using advanced retrieval techniques.
- **Embedding + Vector Store**: Uses **SciBERT embeddings** stored in **ChromaDB** for semantic search.
- **Grounded Hypothesis Generation**: Uses **Claude 3 (Haiku)** as the reasoning LLM to generate new hypotheses grounded in retrieved knowledge.
- **Knowledge Graphs & Citations**: (Planned) Builds citation networks and knowledge graphs for structured insights.
- **Interactive Refinement**: Users can refine hypotheses with feedback loops.
- **Web Interface**: Clean React.js frontend for interactive Q&A and exploration.

---

## 🛠️ Tech Stack
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)  
- **Frontend**: [React.js](https://reactjs.org/) + [TailwindCSS](https://tailwindcss.com/)  
- **LLM**: [Claude 3 Haiku](https://www.anthropic.com/) (via `anthropic` API)  
- **Embeddings**: [SciBERT](https://huggingface.co/allenai/scibert_scivocab_uncased)  
- **Vector Database**: [ChromaDB](https://www.trychroma.com/)  
- **Retriever**: [LangChain](https://www.langchain.com/) + arXiv API integration  
- **Other Tools**:  
  - Sentence Transformers (`sentence-transformers`)  
  - PyPDF for PDF parsing  
  - Docker for deployment  

---

## 📂 Project Structure
