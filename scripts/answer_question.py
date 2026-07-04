import chromadb

# Step 1: Connect to the vector database
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("policy_chunks")

print("Policy Q&A assistant is ready.")
print("Type a question and press Enter.\n")

# Step 2: Ask the user for a question
query = input("Enter your question: ")

# Step 3: Retrieve top matching chunks
results = collection.query(
    query_texts=[query],
    n_results=3
)

# Step 4: Check if any results were returned
if not results["documents"] or not results["documents"][0]:
    print("\nI could not find the answer in the company policy documents.")
else:
    top_chunk = results["documents"][0][0]
    top_filename = results["metadatas"][0][0]["filename"]
    top_section = results["metadatas"][0][0]["section_title"]

    # Optional cleanup for Markdown bold markers
    cleaned_answer = top_chunk.replace("**", "")

    print("\n" + "=" * 70)
    print("GENERATED ANSWER")
    print("=" * 70)
    print(f"Answer:\n{cleaned_answer}\n")
    print("Primary Citation:")
    print(f"{top_filename} — {top_section}\n")

    print("Additional Retrieved Sources:")
    for i in range(min(3, len(results["ids"][0]))):
        print(f"- {results['metadatas'][0][i]['filename']} — {results['metadatas'][0][i]['section_title']}")
