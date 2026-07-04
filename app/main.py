import streamlit as st
import chromadb

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Company Policy Assistant",
    page_icon="📘",
    layout="centered"
)

# -----------------------------
# Connect to vector database
# -----------------------------
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("policy_chunks")

# -----------------------------
# Retrieval helper
# -----------------------------
def retrieve_answer(query: str, n_results: int = 3, distance_threshold: float = 1.2):
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )

    if not results.get("documents") or not results["documents"][0]:
        return None

    top_chunk = results["documents"][0][0].replace("**", "")
    top_filename = results["metadatas"][0][0]["filename"]
    top_section = results["metadatas"][0][0]["section_title"]
    top_distance = results["distances"][0][0]

    # Guardrail: refuse weak matches
    if top_distance > distance_threshold:
        return {
            "refused": True,
            "reason": f"Top match distance too high ({top_distance:.4f})",
            "results": results
        }

    return {
        "refused": False,
        "answer": top_chunk,
        "primary_filename": top_filename,
        "primary_section": top_section,
        "top_distance": top_distance,
        "results": results,
    }

# -----------------------------
# App header
# -----------------------------
st.title("📘 Company Policy Assistant")
st.caption(
    "Ask questions about the fictional Northstar Analytics company policy documents. "
    "Answers are based only on the policy corpus used in this project."
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("About this app")
    st.write(
        "This prototype uses a Retrieval-Augmented Generation (RAG) workflow. "
        "It searches policy chunks in a Chroma vector database and returns a grounded answer with citations."
    )

    st.subheader("Example questions")
    st.markdown(
        "- What are the password requirements?\n"
        "- How many remote days per week are allowed?\n"
        "- How many vacation days does a full-time employee with 0 to 2 years of service receive?\n"
        "- Are traffic fines reimbursable?"
    )

# -----------------------------
# User input
# -----------------------------
query = st.text_input(
    "Enter your question:",
    placeholder="Example: What are the password requirements?"
)

ask_button = st.button("Get Answer")

# -----------------------------
# Main logic
# -----------------------------
if ask_button:
    if not query.strip():
        st.warning("Please enter a question before clicking 'Get Answer'.")
    else:
        with st.spinner("Searching policy documents..."):
            response = retrieve_answer(query)

        if response is None:
            st.error("I could not find the answer in the company policy documents.")
        elif response["refused"]:
            st.error("I could not find the answer in the company policy documents.")
            with st.expander("Debug information"):
                st.write(response["reason"])
        else:
            st.subheader("Answer")
            st.success(response["answer"])

            st.subheader("Primary Citation")
            st.info(f"{response['primary_filename']} — {response['primary_section']}")

            with st.expander("View additional retrieved sources"):
                for i in range(min(3, len(response["results"]["ids"][0]))):
                    filename = response["results"]["metadatas"][0][i]["filename"]
                    section = response["results"]["metadatas"][0][i]["section_title"]
                    preview = response["results"]["documents"][0][i].replace("**", "")
                    distance = response["results"]["distances"][0][i]

                    st.markdown(f"**Source {i+1}:** {filename} — {section}")
                    st.write(f"Distance: {distance:.4f}")
                    st.write(preview[:300] + ("..." if len(preview) > 300 else ""))
                    st.divider()

# -----------------------------
# Footer note
# -----------------------------
st.markdown("---")
st.caption(
    "Note: This assistant answers questions only from the indexed company policy documents and may not answer questions outside that scope."
)
