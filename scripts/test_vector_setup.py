from pathlib import Path
import json

# Step 1: Load the cleaned chunks JSON file
json_path = Path("data/clean_chunks.json")

with open(json_path, "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Successfully loaded {len(chunks)} chunks from JSON.\n")

# Step 2: Show one example chunk
print("Example chunk:")
print(chunks[0])
print("\n")

# Step 3: Test Chroma import
try:
    import chromadb
    print("Chroma imported successfully.")
except Exception as e:
    print("Error importing Chroma:")
    print(e)
