from pathlib import Path
import json
import chromadb

# Step 1: Load cleaned chunks from JSON
json_path = Path("data/clean_chunks.json")

with open(json_path, "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Loaded {len(chunks)} cleaned chunks.\n")

# Step 2: Create a persistent Chroma database folder
client = chromadb.PersistentClient(path="chroma_db")

collection_name = "policy_chunks"

# Step 3: Delete old collection if it already exists (to avoid duplicate IDs)
try:
    client.delete_collection(collection_name)
    print(f"Deleted old collection: {collection_name}")
except:
    print(f"No existing collection named '{collection_name}' found. Creating a new one.")

# Step 4: Create a fresh collection
collection = client.create_collection(name=collection_name)
print(f"Created collection: {collection_name}\n")

# Step 5: Prepare data for Chroma
documents = [chunk["content"] for chunk in chunks]
ids = [chunk["chunk_id"] for chunk in chunks]
metadatas = [
    {
        "filename": chunk["filename"],
        "section_title": chunk["section_title"]
    }
    for chunk in chunks
]

# Step 6: Add chunks to Chroma
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print(f"Added {len(documents)} documents to the vector store.\n")

# Step 7: Run a test query
query = "How many vacation days do employees get?"
results = collection.query(
    query_texts=[query],
    n_results=3
)

print(f"Test query: {query}\n")
print("Top results:\n")

for i in range(len(results["ids"][0])):
    print("=" * 60)
    print(f"Result {i+1}")
    print("Chunk ID:", results["ids"][0][i])
    print("Filename:", results["metadatas"][0][i]["filename"])
    print("Section title:", results["metadatas"][0][i]["section_title"])
    print("Preview:", results["documents"][0][i][:250])
    print()
