"""
1. Find all 10 .md files in the corpus folder
2. For each file:
   a. Read the text
   b. Split it into chunks (by heading — lines starting with ##)
   c. For each chunk:
      - Embed it
      - Store it in ChromaDB with the filename as metadata
3. Print how many chunks were stored total

"""
import os
import ollama 
import chromadb

CORPUS_DIR = 'corpus'
EMBED_MODEL = 'nomic-embed-text'

def get_embedding(text: str) -> list[float]:
    response = ollama.embeddings(
        model = EMBED_MODEL,
        prompt = text,
    
    )
    return response['embedding']

def split_by_heading(text:str) -> list[str]:
    chunks =[]
    current_chunk = []
    for line in text.splitlines():
        if line.startswith("##") and len(current_chunk) != 0:
            chunks.append("\n".join(current_chunk))
            current_chunk =[line]
        else:
            current_chunk.append(line)
        
    chunks.append("\n".join(current_chunk))
    return chunks

def ingest():
    client = chromadb.PersistentClient(path = 'chroma_db')
    collection = client.get_or_create_collection('fnb_corpus')
    total_chunks = 0

    md_files = [f for f in os.listdir(CORPUS_DIR) if f.endswith(".md")]

    print(F"Found {len(md_files)} markdown files in Corpus")


    for filename in md_files:
        filepath = os.path.join(CORPUS_DIR, filename)
        with open(filepath, 'r', encoding='UTF-8') as f:
            text = f.read()
            
        chunks = split_by_heading(text)
        print(F"{filename} -> {len(chunks)}")

        for i, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)
            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[f"{filename}_chunk_{i}"],
                metadatas=[{"source": filename}]
            )
            total_chunks += 1
    print(f"\n✅ Done — {total_chunks} chunks stored from {len(md_files)} documents")

if __name__ == "__main__":
    ingest()

