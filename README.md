# RAG Pipeline

A Retrieval-Augmented Generation (RAG) pipeline built with LangChain, HuggingFace, and FAISS.

## Project Structure

```
RAG_Pipeline/
│
├── data/
│   ├── raw/
│   │   └── papers/
│   │       └── transformer_paper.pdf
│   └── processed/
│
├── src/
│   ├── loaders/
│   │   └── pdf_loader.py
│   ├── chunking/
│   │   └── text_splitter.py
│   ├── embeddings/
│   │   └── embedding_model.py
│   ├── vectordb/
│   │   └── faiss_store.py
│   ├── retrieval/
│   │   └── retriever.py
│   ├── llm/
│   │   └── llm_model.py
│   ├── pipeline/
│   │   └── rag_pipeline.py
│   └── utils/
│       └── prompt_template.py
│
├── experiments/
│   └── baseline_rag.py
│
├── evaluation/
│   └── rag_evaluation.py
│
├── requirements.txt
└── README.md
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Your PDF

Place your PDF document in `data/raw/papers/`. By default the experiment uses:

```
data/raw/papers/transformer_paper.pdf
```

### 3. Run the Baseline Experiment

```bash
python experiments/baseline_rag.py
```

## Pipeline Overview

| Step | Module | Description |
|------|--------|-------------|
| Load | `src/loaders/pdf_loader.py` | Load PDF pages via PyPDFLoader |
| Chunk | `src/chunking/text_splitter.py` | Split text into 500-token chunks (100 overlap) |
| Embed | `src/embeddings/embedding_model.py` | HuggingFace `all-MiniLM-L6-v2` embeddings |
| Index | `src/vectordb/faiss_store.py` | FAISS vector store |
| Retrieve | `src/retrieval/retriever.py` | Top-k retriever |
| Generate | `src/llm/llm_model.py` | Mistral-7B-Instruct via HuggingFace pipeline |

## Evaluation

```bash
python evaluation/rag_evaluation.py
```

Runs keyword-overlap scoring on predefined test queries.

## Models Used

- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **LLM**: `mistralai/Mistral-7B-Instruct-v0.1`
