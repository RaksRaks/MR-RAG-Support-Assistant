import os
import chromadb
import ollama

DB_PATH = "chroma_db"
EMBED_MODEL = "nomic-embed-text"

def get_embedding(text: str) -> list[float]:
    response = ollama.embeddings(
        model = EMBED_MODEL,
        prompt = text,
    
    )
    return response['embedding']
client = chromadb.PersistentClient(path = DB_PATH)
collection = client.get_collection('fnb_corpus')

questions = [
     "What are the requirements to open a cheque account?",
    "What fees are charged for international transfers?",
    "What documents do I need for FICA verification?",
    "How do I dispute a fraudulent transaction?",
    "What is the interest rate on personal loans?",
]
for question in questions:
    print("Testing the question: ", question)
    question_embedding = get_embedding(question)
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )
    
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        print(f"Source: {meta['source']}")
        print(doc[:200])
        print("---")






