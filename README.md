# 🧪 LabraAI – Autonomous Research Assistant for Scientific Hypothesis Generation

LabraAI is an **AI-powered research assistant** that helps researchers generate **novel scientific hypotheses** by retrieving, embedding, and synthesizing research papers and datasets. It combines robust retrieval with LLM reasoning to mimic parts of a scientist’s workflow.

---

## ✨ Key Features

* **Research Domain Input**: Enter a scientific domain or question (e.g., "Quantum materials" or "Cancer immunotherapy").
* **Document Retrieval**: Fetches relevant papers from arXiv, PubMed, and other sources using advanced retrieval techniques.
* **Embedding + Vector Store**: Uses **SciBERT embeddings** stored in **ChromaDB** for semantic search.
* **Grounded Hypothesis Generation**: Uses **Claude 3 (Haiku)** or other pluggable LLMs as the reasoning engine to generate novel hypotheses grounded in retrieved knowledge.
* **Knowledge Graphs & Citations** (planned): Builds citation networks and knowledge graphs for structured insights.
* **Interactive Refinement**: Users can refine hypotheses with feedback loops.
* **CLI + Optional Web UI**: Start with a CLI interactive flow; a React frontend can be added for better UX.

---

## 📂 Project Structure

```
LabraAI/
│── backend/
│   ├── main.py              # FastAPI entry point / CLI runner
│   ├── vectorstore/         # SciBERT + ChromaDB embeddings & persistence
│   ├── retriever/           # Retriever logic (LangChain + arXiv or local PDFs)
│   ├── llm/                 # LLM integration (Anthropic/OpenAI/Gemini adapters)
│   └── utils/               # Helper functions (pdf parsing, chunking, config)
│
│── frontend/                # (optional)
│   ├── src/
│   │   ├── components/      # React UI components
│   │   ├── pages/           # Main app pages
│   │   └── App.jsx          # Root app
│   └── package.json
│
│── data/                    # Research papers & datasets (PDFs)
│── requirements.txt         # Python dependencies (pins recommended)
│── docker-compose.yml       # Optional deployment setup
│── README.md                # This file
```

> Note: The repo can run as a CLI-first project (recommended while developing). Frontend is optional and can be added later.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository

```bash
git clone https://github.com/yourusername/LabraAI.git
cd LabraAI
```

### 2️⃣ Backend setup

```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate

pip install -r ../requirements.txt
```

> If you don't have a `requirements.txt` yet, please ask me and I will generate a recommended one pinned to compatible versions.

### 3️⃣ Environment variables

Create a `.env` file in the **project root** (or `backend/`) with the provider key you will use:

```ini
# Only set the key(s) for the provider(s) you plan to use
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_gemini_api_key

# Optional runtime settings
EMBEDDING_MODEL=allenai/scibert_scivocab_uncased
CHROMA_DIR=backend/chroma_db
PDF_DIR=backend/data/pdfs
```

**Security:** Add `.env` to `.gitignore` to avoid leaking secrets.

### 4️⃣ Run backend (CLI / dev)

From project root:

```bash
PYTHONPATH=. python -m backend.main
```

You should see logs indicating ingestion and number of documents, and then the interactive prompt:

```
SpecialIssueFlyer processed and stored.
Number of documents in vector store: N
🔍 Ask a research question (or type 'exit'):
```

### 5️⃣ Optional frontend (if implemented)

```bash
cd frontend
npm install
npm run dev
# open http://localhost:5173 or the port configured by your frontend
```

---

## 🔍 Usage (CLI)

1. Start backend (see above).
2. When prompted, type your research question or domain, e.g.:

   * `what is SpecialIssueFlyer about`
   * `summarize key contributions`
   * `suggest a follow-up experiment on X`
3. The system will retrieve context, call the LLM, and present grounded hypotheses or answers.

**Exit** by typing `exit`.

---

## 🧠 Example Workflow

**User:** `What are novel approaches in quantum materials?`

**LabraAI:**

1. Retrieves 8–10 recent arXiv / PDF documents related to the query.
2. Embeds and ranks relevant chunks from the vector store.
3. Passes top-k context to the LLM with a hypothesis-generation prompt template.
4. Returns structured hypotheses with rationale and supporting source ids.

Example output snippet:

```json
{
  "hypotheses": [
    {
      "id": "h1",
      "text": "Combining diffusion-based generative models with transformer embeddings can improve low-resolution structure predictions.",
      "rationale": "Recent papers show promising generative priors; combining architectures could address sparse-data settings.",
      "supporting_chunks": ["doc1_chunk3", "doc5_chunk1"]
    }
  ]
}
```

---

## 🚧 Roadmap / Future Work

* [ ] Integrate **PubMed** & **Semantic Scholar** APIs for broader coverage
* [ ] Implement a **Knowledge Graph** & Citation Network for graph-based reasoning
* [ ] Add **hypothesis ranking** (novelty scoring + plausibility)
* [ ] Build a **React** frontend with visualizations (KG, citations, documents)
* [ ] Add an **active learning** loop using user feedback
* [ ] Containerize and deploy (Docker, Kubernetes)

---

## 🧰 Troubleshooting (common issues & fixes)

### 1) OpenAI `RateLimitError: insufficient_quota`

* Cause: OpenAI API key has exhausted its quota.
* Fix: Add billing / replace provider or use Anthropic/Gemini key.

### 2) Gemini: `GenerateContentRequest.contents is not specified`

* Cause: Empty prompt or empty `HumanMessage` passed to Gemini.
* Fix:

  * Ensure `query` in `main.py` is non-empty before calling the chain.
  * Verify the chain's prompt template includes the retrieved context and the question.

### 3) `AttributeError: GenerationConfig.Modality` or proto / protobuf errors

* Cause: Version mismatch between Google libraries and `langchain_google_genai`.
* Fix: Pin versions in `requirements.txt` (see suggested pins) and `pip install --force-reinstall`.

### 4) No documents retrieved (retriever returns `[]`)

* Cause: Poor chunking, wrong embedding model, or query too generic.
* Fix:

  * Try a more specific query or term present in your PDFs.
  * Rebuild the index with a different embedding model (all-MiniLM for general use).
  * Ensure PDFs were parsed correctly (print a sample chunk).

---

## 🤝 Contributing

Contributions welcome! Suggested workflow:

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit and push
4. Open a Pull Request with a clear description and reproduction steps

---


