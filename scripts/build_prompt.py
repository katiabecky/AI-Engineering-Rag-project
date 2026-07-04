import chromadb

# Step 1: Connect to the existing Chroma database
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("policy_chunks")

print("Prompt builder is ready.")
print("Type a question and press Enter.\n")

# Step 2: Ask the user for a question
query = input("Enter your question: ")

# Step 3: Retrieve top matching chunks
results = collection.query(
    query_texts=[query],
    n_results=3
)

# Step 4: Build a context block from retrieved chunks
context_blocks = []

for i in range(len(results["ids"][0])):
    filename = results["metadatas"][0][i]["filename"]
    section_title = results["metadatas"][0][i]["section_title"]
    content = results["documents"][0][i]

    block = f"""Source {i+1}:
Filename: {filename}
Section: {section_title}
Content: {content}
"""
    context_blocks.append(block)

context_text = "\n".join(context_blocks)

# Step 5: Build the final prompt
prompt = f"""
You are a helpful company policy assistant.

Answer the user's question using only the information in the provided sources.
If the answer is not found in the sources, say:
"I could not find the answer in the company policy documents."

Keep the answer concise and accurate.
Always cite the source filename and section title you used.

User question:
{query}

Retrieved sources:
{context_text}

Answer:
"""

# Step 6: Print the final prompt
print("\n" + "=" * 70)
print("FINAL PROMPT TO SEND TO AN LLM")
print("=" * 70)
print(prompt)
