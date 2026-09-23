# test_loop.py — Milestone 1: Single hard-coded proof-of-concept
# Uses Ollama for embeddings (avoids sentence-transformers DLL issue)

import chromadb
import ollama

EMBED_MODEL = "nomic-embed-text" # dedicated embedding model
CHAT_MODEL  = "llama3:latest"   # used for generation

# ── 1. Load one document ──────────────────────────────────────────────
doc_path = "corpus/01_account_types_eligibility.md"
with open(doc_path, "r", encoding="utf-8") as f:
    content = f.read()

print("✓ Document loaded")

# ── 2. Embed the document using Ollama ────────────────────────────────
def get_embedding(text: str) -> list[float]:
    response = ollama.embeddings(model=EMBED_MODEL, prompt=text)
    return response["embedding"]

doc_embedding = get_embedding(content)
print(f"✓ Document embedded — vector length: {len(doc_embedding)}")

# ── 3. Store in ChromaDB ──────────────────────────────────────────────
client = chromadb.Client()
collection = client.get_or_create_collection("test_collection")

collection.add(
    documents=[content],
    embeddings=[doc_embedding],
    ids=["doc_01"],
    metadatas=[{"source": "01_account_types_eligibility.md"}]
)

print("✓ Document stored in ChromaDB")

# ── 4. Ask a hard-coded question ──────────────────────────────────────
question = "What account types are available at FNB?"

# ── 5. Embed the question and retrieve the most relevant chunk ────────
question_embedding = get_embedding(question)
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=1
)

retrieved_chunk = results["documents"][0][0]
source = results["metadatas"][0][0]["source"]

print(f"\n--- Retrieved from: {source} ---\n")
print(retrieved_chunk[:500])  # preview first 500 chars

# ── 6. Generate an answer with Ollama ─────────────────────────────────
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
    model=CHAT_MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_message}
    ]
)

print("\n--- Answer ---\n")
print(response["message"]["content"])
print(f"\nSource: {source}")
