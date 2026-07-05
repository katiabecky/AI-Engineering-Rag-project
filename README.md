# AI Engineering RAG Project

## Project Overview
This project is a **Retrieval-Augmented Generation (RAG) company policy assistant** built for a fictional organization, **Northstar Analytics, Inc.** The system allows a user to ask questions about internal company policies and receive grounded answers based only on the indexed policy corpus.

The project was developed as an end-to-end RAG prototype and includes:
- a small, coherent company policy corpus,
- document ingestion and chunking,
- cleaned chunk export to JSON,
- semantic search using a Chroma vector database,
- a retrieval-based answer pipeline with citations,
- a Streamlit web interface,
- and a simple refusal mechanism for out-of-scope questions.

The goal of the project is to demonstrate a practical workflow for building a document-grounded question-answering assistant using Python.

## Features
- Loads policy documents from Markdown files
- Splits documents into section-based chunks
- Cleans and normalizes chunk text
- Stores chunk embeddings in a persistent Chroma vector database
- Retrieves relevant policy chunks using semantic search
- Displays grounded answers with source citations
- Refuses unrelated questions outside the policy corpus
- Provides a browser-based interface with Streamlit

## Corpus
The indexed corpus contains six fictional but realistic internal policy documents for Northstar Analytics, Inc.:
- `employee_handbook.md`
- `vacation_policy.md`
- `remote_work_policy.md`
- `it_security_policy.md`
- `code_of_conduct.md`
- `expense_reimbursement_policy.md`

These files are stored in:

```text
data/policies/
```

## Project Structure

```text
AI-Engineering-Rag-project/
├── app/
│   └── main.py
├── data/
│   ├── clean_chunks.json
│   └── policies/
│       ├── code_of_conduct.md
│       ├── employee_handbook.md
│       ├── expense_reimbursement_policy.md
│       ├── it_security_policy.md
│       ├── remote_work_policy.md
│       └── vacation_policy.md
├── scripts/
│   ├── ingest_policies.py
│   ├── test_vector_setup.py
│   ├── build_vector_store.py
│   ├── retrieve_chunks.py
│   ├── build_prompt.py
│   └── answer_question.py
├── tests/
├── .github/
│   └── workflows/
├── .gitignore
├── README.md
├── design-and-evaluation.md
├── ai-tooling.md
└── requirements.txt
```

## System Architecture
The application uses a simple RAG workflow:

1. **Document storage**  
   Policy files are stored in `data/policies/` as Markdown documents.

2. **Ingestion**  
   `scripts/ingest_policies.py` loads the Markdown files and reads their contents.

3. **Chunking**  
   Each document is split by Markdown section headings (`##`) into smaller policy chunks.

4. **Cleaning and normalization**  
   The chunks are cleaned, assigned IDs, and exported to `data/clean_chunks.json`.

5. **Embedding and vector storage**  
   `scripts/build_vector_store.py` loads the cleaned chunks and stores them in a persistent Chroma vector database located in `chroma_db/`.

6. **Retrieval**  
   Queries are matched semantically against indexed chunks using Chroma.

7. **Answer generation**  
   The MVP app returns the top retrieved chunk as the main grounded answer and displays its citation.

8. **Guardrails**  
   A distance-based threshold is used to refuse out-of-scope questions that do not match the policy corpus strongly enough.

9. **Frontend**  
   A Streamlit app in `app/main.py` provides the browser-based interface.

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/katiabecky/AI-Engineering-Rag-project.git
cd AI-Engineering-Rag-project
```

### 2. Create and activate a virtual environment
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage Instructions

### Step 1: Ingest and prepare the policy chunks
```bash
python scripts/ingest_policies.py
```

This will:
- load the policy files,
- split them into chunks,
- clean the chunk text,
- save the result to `data/clean_chunks.json`.

### Step 2: Build the Chroma vector store
```bash
python scripts/build_vector_store.py
```

This will:
- load the cleaned chunks,
- create embeddings,
- store them in the persistent Chroma database.

### Step 3: Run the Streamlit app
```bash
streamlit run app/main.py
```

If needed on Windows, this also works:
```bash
python -m streamlit run app/main.py
```

After launching, the app should open in a browser automatically. If not, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Usage Examples

### Example in-scope questions
- What are the password requirements?
- How many remote days per week are allowed?
- How many paid vacation days does a full-time employee with 0 to 2 years of service receive?
- Are traffic fines reimbursable?

### Example out-of-scope questions
- What is the weather today?
- Who won the World Cup?
- What is the capital of France?

For out-of-scope questions, the app should return a refusal message such as:

> I could not find the answer in the company policy documents.

## Example Workflow
A typical interaction looks like this:
1. The user enters a policy-related question.
2. The app retrieves the most relevant chunks from the Chroma database.
3. The top chunk is displayed as the answer.
4. The app shows the primary citation and additional retrieved sources.
5. If the question is unrelated to the corpus, the app refuses to answer.

## Evaluation Summary
The prototype was tested with both in-scope and out-of-scope questions.

### Correctly answered examples
- What are the password requirements?
- How many remote days per week are allowed?
- Are traffic fines reimbursable?

### Correctly refused examples
- What is the weather today?
- Who won the World Cup?
- What is the capital of France?

This shows that the MVP is able to:
- retrieve relevant policy content,
- answer grounded questions,
- and reject unrelated queries.

## Documentation
Additional project documentation is included in:
- `design-and-evaluation.md`
- `ai-tooling.md`

## Limitations
This is an MVP and has several limitations:
- The app currently uses the top retrieved chunk as the answer rather than full multi-chunk answer synthesis.
- Retrieval quality may vary depending on query wording.
- The refusal behavior uses a simple distance threshold and may require tuning for different corpora.
- The current corpus is intentionally small and fictional for demonstration purposes.

## Future Improvements
Possible next improvements include:
- integrating a full LLM for more natural answer generation,
- improving reranking and confidence estimation,
- expanding the policy corpus,
- adding automated evaluation scripts,
- improving answer formatting and multi-turn conversation support.

## Repository Link
GitHub repository:

[https://github.com/katiabecky/AI-Engineering-Rag-project](https://github.com/katiabecky/AI-Engineering-Rag-project)
