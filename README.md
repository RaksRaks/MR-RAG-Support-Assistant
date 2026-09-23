# FNB B4 RAG Support Assistant

A Retrieval-Augmented Generation (RAG) support assistant built for FNB B4 banking policies. The assistant answers questions grounded strictly in a corpus of 10 policy documents, cites its sources, and refuses to answer questions outside the corpus or requests for live account data.

Built as a capstone project for the FNB B4 AI programme.

---

## How It Works

1. Policy documents are chunked by section heading and embedded using `nomic-embed-text` via Ollama
2. Embeddings are stored in a persistent ChromaDB vector database
3. When a question is asked, it is embedded and the top 3 most relevant chunks are retrieved
4. The retrieved chunks are sent to `llama3` via Ollama with a system prompt that enforces grounded, cited answers
5. The assistant refuses any question it cannot answer from the documents

---

## Project Structure

```
corpus/             10 policy markdown documents + test questions CSV
src/
  test_loop.py      Milestone 1: single hard-coded proof of concept
  ingest.py         Milestone 2: ingestion pipeline (chunk, embed, store)
  retrieval_test.py Milestone 2: standalone retrieval sanity check
  rag.py            Milestone 3: core RAG pipeline with system prompt
  run_tests.py      Milestone 3: runs all 12 test questions and logs results
  chat.py           Milestone 5: CLI chat interface
logs/
  results_log.csv   Output from run_tests.py
docs/               Project brief and slides
retrieval_notes.md  Chunking and retrieval design decisions
guardrail_test_log.md Safety and refusal test log
scores.md           Evaluation scorecard (12/12)
reflection.md       Project reflection
```

---

## Setup

**Requirements:** Python 3.10+, Ollama running locally

1. Clone the repo and create a virtual environment:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Pull the required Ollama models:
```
ollama pull llama3
ollama pull nomic-embed-text
```

3. Run ingestion to build the vector database:
```
python src/ingest.py
```

4. Start the chat interface:
```
python src/chat.py
```

---

## Stack

- Python
- ChromaDB (persistent local vector store)
- Ollama (local LLM and embeddings)
- Models: `llama3` for generation, `nomic-embed-text` for embeddings
- No LangChain - hand-rolled retrieval loop for simplicity and transparency

---

## Evaluation

All 12 test questions scored correctly:
- 10 answerable questions: correct answers with source citations
- 2 trap questions: clean refusals (no hallucination)

See `scores.md` for the full scorecard.
