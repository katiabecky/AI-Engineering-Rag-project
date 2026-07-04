# Design and Evaluation

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) policy assistant built for a fictional company, **Northstar Analytics, Inc.** The application answers employee questions using only a small internal corpus of company policy documents. The goal of the project is to demonstrate a complete RAG workflow: document collection, ingestion, chunking, embedding, vector search, grounded answer generation, citations, and basic guardrails.

The final prototype is implemented as a **Streamlit web application** backed by a **Chroma vector database**. Users can ask questions such as "What are the password requirements?" or "How many remote days per week are allowed?" and receive an answer grounded in the indexed policy corpus.

## Corpus and Data Sources
The policy corpus consists of six fictional but realistic Markdown documents for Northstar Analytics, Inc.:

1. `employee_handbook.md`
2. `vacation_policy.md`
3. `remote_work_policy.md`
4. `it_security_policy.md`
5. `code_of_conduct.md`
6. `expense_reimbursement_policy.md`

These files were selected to create a coherent internal knowledge base that supports practical employee policy questions. Markdown was chosen because it is lightweight, easy to edit, and easy to parse programmatically. It also preserves section headings clearly, which makes heading-based chunking straightforward.

## System Architecture
The project uses a multi-step RAG pipeline:

### 1. Document Storage
The source files are stored in `data/policies/`.

### 2. Ingestion
A Python ingestion script loads all `.md` files from the policy folder, reads their text content, and stores them in a structured list of document objects.

### 3. Chunking
Each document is split by Markdown section headings (`##`). This creates smaller policy sections such as:
- Purpose
- Eligibility
- Password Requirements
- Standard Arrangement
- Non-Reimbursable Expenses

This approach is better than treating each full document as one block because RAG retrieval works best with smaller, focused chunks.

### 4. Cleaning and Normalization
The chunks are cleaned by:
- removing extra whitespace
- skipping empty chunks
- assigning unique chunk IDs

The cleaned chunks are then saved to `data/clean_chunks.json` for reuse.

### 5. Embedding and Vector Storage
The cleaned chunks are added to a **Chroma** vector database stored locally in `chroma_db/`. Chroma generates embeddings and stores each chunk along with metadata such as:
- filename
- section title
- chunk ID

### 6. Retrieval
When a user asks a question, the app queries the Chroma collection and retrieves the top matching chunks. This semantic retrieval step allows the system to find relevant policy text even when the question wording differs from the original document wording.

### 7. Answer Generation
The current MVP answer generation is retrieval-based rather than full LLM synthesis. The app uses the top retrieved chunk as the primary answer and displays a citation for the source filename and section title.

### 8. Guardrails
A simple distance-based threshold was added to reduce incorrect answers for out-of-scope questions. If the top result is not relevant enough, the app refuses to answer and returns:

> I could not find the answer in the company policy documents.

This behavior is important because it prevents the assistant from confidently answering unrelated questions.

## Design Choices and Rationale

### Why Markdown files?
Markdown was chosen because it is easier to manage than PDFs for a beginner project. The files are readable, editable, and naturally structured with headings. This made ingestion and chunking simpler and more reliable.

### Why heading-based chunking?
Chunking by heading preserves meaning better than splitting by arbitrary length. For example, a policy section like "Password Requirements" or "Annual Vacation Allowance" becomes its own retrievable unit. This improves precision and makes citations more understandable.

### Why Chroma?
Chroma was selected because it is beginner-friendly, works locally, and integrates well with Python. It allowed the project to store embeddings persistently and test semantic retrieval without requiring a complex external database.

### Why Streamlit?
Streamlit was chosen for the frontend because it provides a fast and simple way to build a browser-based interface. It allowed the project to move from terminal scripts to a more professional, demo-ready application with limited setup overhead.

### Why use a retrieval-based MVP answer instead of a full LLM answer?
For this stage of the project, the goal was to build a reliable, explainable, grounded MVP. Using the top retrieved chunk directly made it easier to validate correctness and cite the source. A future version could pass the retrieved context into a full language model for more natural answer synthesis.

## Evaluation
The prototype was tested with both in-scope and out-of-scope questions.

### Test Cases

| Question | Expected Behavior | Actual Result |
|---|---|---|
| What are the password requirements? | Return IT security password rules | Correct |
| How many remote days per week are allowed? | Return remote work standard arrangement | Correct |
| Are traffic fines reimbursable? | Return non-reimbursable expenses rule | Correct |
| What is the weather today? | Refuse to answer | Correct |
| Who won the World Cup? | Refuse to answer | Correct |
| What is the capital of France? | Refuse to answer | Correct |

### Evaluation Summary
The app performed well on the tested in-scope questions. In each of the valid policy questions, the system retrieved the correct policy file and a highly relevant section. For out-of-scope questions, the distance-based refusal mechanism prevented misleading answers and produced an appropriate fallback response.

This shows that the current MVP satisfies three important goals:
1. retrieve relevant policy information,
2. answer grounded questions correctly,
3. refuse unrelated questions.

## Strengths of the Prototype
- Clear and coherent policy corpus
- Successful document ingestion and chunking
- Persistent vector database with semantic retrieval
- Browser-based interface using Streamlit
- Grounded answers with citations
- Basic refusal mechanism for out-of-scope questions

## Limitations
Although the prototype works well, it has several limitations:

1. **Top-chunk answer strategy**: The current answer is based mainly on the best retrieved chunk rather than synthesizing across multiple chunks.
2. **Simple refusal logic**: The distance threshold is heuristic and may need tuning if the corpus changes.
3. **No full LLM integration yet**: The system prepares prompts and retrieval context, but the production answer in the app is still retrieval-based rather than generated by a live LLM.
4. **Small corpus**: The project uses only six policy documents, which is fine for an MVP but not representative of a full enterprise knowledge base.

## Future Improvements
Several upgrades could strengthen the project:

- integrate a full LLM for more natural answer generation
- add reranking for better retrieval quality
- filter or de-prioritize metadata-only chunks
- improve formatting of answers into bullet points or summaries
- add conversation history or multi-turn support
- expand the policy corpus with more documents
- add automated evaluation scripts for larger test sets

## Conclusion
This project demonstrates a functional RAG-based company policy assistant built from scratch using Python, Chroma, and Streamlit. The final system can ingest a policy corpus, split it into meaningful chunks, store embeddings in a vector database, retrieve relevant sections, and present grounded answers with citations. It also correctly refuses unrelated questions, which strengthens its reliability.

Overall, the project succeeds as an MVP because it implements the core RAG workflow end to end and presents it through a usable web interface. While there is room for future enhancement, the current prototype already shows a practical and well-structured application of retrieval-augmented policy question answering.
