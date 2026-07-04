import chromadb

# Step 1: Connect to the existing Chroma database
client = chromadb.PersistentClient(path="chroma_db")

# Step 2: Open the existing collection
collection = client.get_collection("policy_chunks")

print("Policy chunk retriever is ready.")
print("Type a question and press Enter.\n")

# Step 3: Ask the user for a query
query = input("Enter your question: ")

# Step 4: Search the collection
results = collection.query(
    query_texts=[query],
    n_results=3
)

# Step 5: Display results
print(f"\nTop results for: {query}\n")

for i in range(len(results["ids"][0])):
    print("=" * 60)
    print(f"Result {i+1}")
    print("Chunk ID:", results["ids"][0][i])
    print("Filename:", results["metadatas"][0][i]["filename"])
    print("Section title:", results["metadatas"][0][i]["section_title"])
    print("Preview:", results["documents"][0][i][:250])
    print()
