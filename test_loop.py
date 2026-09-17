# test_loop.py — Milestone 1: Single hard-coded proof-of-concept

from sentence_transformers import SentenceTransformer
import chromadb
import ollama

# ── 1. Load one document ──────────────────────────────────────────────
doc_path = "corpus/01_account_types_eligibility.md"
with open(doc_path, "r", encoding="utf-8") as f:
    content = f.read()

# ── 2. Embed and store in Chroma ──────────────────────────────────────
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection("test_collection")

# Store the whole doc as one chunk (just for this test)
embedding = embedding_model.encode(content).tolist()
collection.add(
    documents=[content],
    embeddings=[embedding],
    ids=["doc_01"],
    metadatas=[{"source": "01_account_types_eligibility.md"}]
)

# ── 3. Ask a hard-coded question ──────────────────────────────────────
question = "What account types are available at FNB?"

# ── 4. Retrieve the most relevant chunk ──────────────────────────────
question_embedding = embedding_model.encode(question).tolist()
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=1
)

retrieved_chunk = results["documents"][0][0]
source = results["metadatas"][0][0]["source"]

print(f"\n--- Retrieved from: {source} ---\n")
print(retrieved_chunk[:500])  # preview first 500 chars

# ── 5. Generate an answer with Ollama ─────────────────────────────────
system_prompt = """You are a banking support assistant.
Answer ONLY using the context provided below.
Always cite the source document filename at the end of your answer.
If the context does not contain enough information, say: 'I cannot answer this from the available documents.'
"""

user_message = f"""Context:
{retrieved_chunk}

Question: {question}
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)

print("\n--- Answer ---\n")
print(response["message"]["content"])
print(f"\nSource: {source}")
