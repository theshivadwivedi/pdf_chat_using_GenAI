import streamlit as st

from pdf_loader import load_and_split_pdf
from vector_store import create_vectorstore
from llm_chain import build_chain


st.set_page_config(
    page_title="PDF Chat",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Chat with your PDF")
st.write("Ask questions and get answers directly from your document.")

st.divider()

# Session state
if "chain" not in st.session_state:
    st.session_state.chain = None

if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False


# Layout
left, right = st.columns([1, 2])

with left:
    st.subheader("📤 Upload PDF")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        label_visibility="collapsed"
    )

with right:
    st.subheader("ℹ️ Status")
    if st.session_state.pdf_loaded:
        st.success("PDF processed and ready")
    else:
        st.info("Upload a PDF to begin")


# PDF processing
if uploaded_file and not st.session_state.pdf_loaded:
    with st.spinner("Reading and indexing PDF..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        chunks = load_and_split_pdf("temp.pdf")
        vectorstore = create_vectorstore(chunks)
        st.session_state.chain = build_chain(vectorstore)
        st.session_state.pdf_loaded = True

    st.success("PDF is ready for questions ✅")

st.divider()

# Chat section
st.subheader("💬 Ask Questions")

question = st.text_input(
    "Type your question here",
    disabled=not st.session_state.pdf_loaded,
    placeholder="e.g. Summarize this document in 5 points"
)

if question and st.session_state.chain:
    with st.spinner("Generating answer..."):
        answer = st.session_state.chain.invoke(question)

    st.markdown("### 🧠 Answer")
    st.write(answer)
