from pathlib import Path
import json

# Define folders
policy_folder = Path("data/policies")
output_folder = Path("data")
output_file = output_folder / "clean_chunks.json"

# Find all Markdown files
policy_files = list(policy_folder.glob("*.md"))

# Step 1: Load documents
documents = []

for file_path in policy_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    document = {
        "filename": file_path.name,
        "content": content
    }

    documents.append(document)

print(f"Loaded {len(documents)} documents.\n")

# Step 2: Chunk documents by Markdown heading '##'
raw_chunks = []

for doc in documents:
    sections = doc["content"].split("## ")

    for section in sections:
        section = section.strip()
        if not section:
            continue

        lines = section.split("\n", 1)
        section_title = lines[0].strip()

        if len(lines) > 1:
            section_content = lines[1].strip()
        else:
            section_content = ""

        raw_chunk = {
            "filename": doc["filename"],
            "section_title": section_title,
            "content": section_content
        }

        raw_chunks.append(raw_chunk)

print(f"Created {len(raw_chunks)} raw chunks.\n")

# Step 3: Clean and normalize chunks
clean_chunks = []

for i, chunk in enumerate(raw_chunks, start=1):
    cleaned_content = " ".join(chunk["content"].split())
    cleaned_title = " ".join(chunk["section_title"].split())

    if not cleaned_content:
        continue

    clean_chunk = {
        "chunk_id": f"{chunk['filename'].replace('.md', '')}_{i}",
        "filename": chunk["filename"],
        "section_title": cleaned_title,
        "content": cleaned_content
    }

    clean_chunks.append(clean_chunk)

print(f"Created {len(clean_chunks)} cleaned chunks.\n")

# Step 4: Save cleaned chunks to JSON
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(clean_chunks, json_file, indent=2, ensure_ascii=False)

print(f"Saved cleaned chunks to: {output_file}\n")

# Step 5: Preview first 5 chunks
for chunk in clean_chunks[:5]:
    print("=" * 60)
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Filename: {chunk['filename']}")
    print(f"Section title: {chunk['section_title']}")
    print(f"Chunk length: {len(chunk['content'])} characters")
    print("Preview:")
    print(chunk["content"][:250])
    print("\n")
