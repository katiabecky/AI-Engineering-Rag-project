# AI Tooling

## Overview
AI-assisted tooling played an important role in the development of this Retrieval-Augmented Generation (RAG) project. The project involved document ingestion, chunking, vector storage, retrieval, answer generation, and a simple Streamlit interface for a fictional company policy assistant. AI support was used primarily as a productivity aid to accelerate coding, improve structure, and clarify implementation steps. However, all outputs still required human review, testing, correction, and project-level decision-making.

## How AI Tools Were Used

### 1. Project Planning and Workflow Guidance
AI tooling was used to break the project into manageable phases. This was especially helpful at the beginning of the project, when the system architecture needed to be translated into beginner-friendly implementation steps. AI assistance helped organize the workflow into:
- environment setup,
- corpus creation,
- ingestion and chunking,
- vector database creation,
- retrieval,
- answer generation,
- and Streamlit app integration.

This planning support made the development process more structured and reduced confusion during implementation.

### 2. Code Drafting and Script Scaffolding
AI assistance was used to help draft Python scripts for:
- loading Markdown policy files,
- chunking documents by section heading,
- cleaning and normalizing chunks,
- exporting cleaned chunks to JSON,
- creating and testing a Chroma vector database,
- retrieving relevant chunks,
- building prompt structures,
- generating retrieval-based answers,
- and creating the Streamlit app.

In practice, AI helped produce initial script structures more quickly than writing everything manually from scratch. This was useful for reducing setup time and understanding how the different parts of the pipeline connect.

### 3. Debugging and Iterative Refinement
AI support was also useful during iterative testing. For example, when scripts were not yet producing the desired structure, the generated code could be revised in smaller steps. This was especially helpful in:
- distinguishing terminal commands from Python code,
- improving chunk structures,
- cleaning retrieved text,
- and adding app-level guardrails for out-of-scope questions.

One important example was the addition of a refusal mechanism. Early retrieval-only behavior returned irrelevant policy answers for unrelated questions such as weather or geography. AI-assisted iteration helped improve the app so that it now refuses questions outside the policy corpus, which is much more appropriate for a RAG-based system.

### 4. Documentation Support
AI tooling helped draft supporting documentation such as:
- `design-and-evaluation.md`,
- repository organization guidance,
- and explanatory text for how the system works.

This assistance improved the speed of documentation writing and helped present the project in a more professional and structured way. However, the final content still required manual review to ensure it matched the actual implementation.

## What Human Judgment Was Still Needed
Although AI tooling was helpful, the project still depended heavily on human judgment. AI did not replace the need to:
- decide the project scope,
- choose a fictional but coherent policy corpus,
- test whether outputs were correct,
- verify that the app behavior matched the assignment requirements,
- determine when retrieval quality was acceptable,
- and decide how to handle generated artifacts such as the Chroma database.

For example, the decision to use fictional company policy documents in Markdown format was a human design choice made to simplify ingestion and maintain a coherent corpus. Similarly, the decision to remove the generated `chroma_db/` folder from Git tracking was made for repository cleanliness and reproducibility.

## Benefits of AI Tooling in This Project
The main benefits of AI-assisted tooling in this project were:

1. **Faster development** — AI reduced the time needed to draft scripts and organize the workflow.
2. **Better clarity** — AI explanations made it easier to understand concepts such as chunking, embeddings, retrieval, and vector stores.
3. **Improved iteration** — code and app behavior could be refined quickly after each test.
4. **Documentation support** — AI helped produce clearer project documentation and implementation summaries.

For a beginner-friendly project like this one, these benefits were significant because they reduced friction in moving from concept to implementation.

## Limitations of AI Tooling
AI assistance was useful, but it also had limitations.

1. **AI-generated code still required testing** — even when the scripts looked correct, they had to be run and verified manually.
2. **Output quality depended on prompt quality** — vague instructions would have produced less useful results.
3. **AI did not automatically guarantee project correctness** — design decisions, file organization, GitHub setup, and evaluation still needed human oversight.
4. **Some improvements required iterative tuning** — for example, retrieval behavior for out-of-scope questions had to be refined through testing and adjustment.

These limitations show that AI worked best as an assistant rather than an autonomous developer.

## Reflection
Overall, AI tooling was a valuable support system in this project. It helped transform a complex RAG assignment into a sequence of manageable tasks and accelerated both coding and documentation. At the same time, the final project still reflects substantial human involvement in testing, validating, organizing, and refining the work.

In my view, the most effective use of AI in this project was not to fully automate development, but to act as a guided assistant for implementation and learning. This made it possible to understand the technical workflow more deeply while still producing a functional and submission-ready project.
