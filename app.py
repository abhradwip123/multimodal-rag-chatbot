import os
import streamlit as st

from pipeline import process_pdf
from vector_store import clear_database

from sidebar import create_sidebar
from uploader import upload_pdf

from hybrid_search import hybrid_search
from reranker import rerank
from rerank_context import build_rerank_context
from llm import generate_answer
from memory import ConversationMemory
from query_rewriter import rewrite_query

from chat_ui import (
    initialize_chat,
    display_chat,
    add_user_message,
    add_assistant_message
)

from display_sources import show_sources

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Multimodal RAG",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

initialize_chat()

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

create_sidebar()

# ----------------------------------------------------
# TITLE
# ----------------------------------------------------

st.title("🤖 Multimodal RAG Chatbot")

st.write(
    "Upload a PDF and ask questions about it."
)

# ----------------------------------------------------
# UPLOAD DIRECTORY
# ----------------------------------------------------

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ----------------------------------------------------
# PDF UPLOAD
# ----------------------------------------------------

uploaded_file = upload_pdf()

if uploaded_file is not None:

    if (
        not st.session_state.pdf_processed
        or
        st.session_state.current_pdf != uploaded_file.name
    ):

        file_path = os.path.join(
            UPLOAD_DIR,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("📄 PDF uploaded successfully!")

        try:

            with st.spinner("Processing PDF..."):

                clear_database()

                total_chunks = process_pdf(file_path)

            st.success(
                f"✅ Processing complete! {total_chunks} chunks stored."
            )

            st.session_state.pdf_processed = True
            st.session_state.current_pdf = uploaded_file.name

        except Exception as e:

            st.error(f"Processing failed:\n\n{e}")

# ----------------------------------------------------
# CHAT
# ----------------------------------------------------

if st.session_state.pdf_processed:

    st.divider()

    st.subheader("💬 Chat with your PDF")

    display_chat()

    query = st.chat_input(
        "Ask a question about your PDF..."
    )

    if query:

        add_user_message(query)

        with st.chat_message("user"):
            st.markdown(query)

        history = st.session_state.memory.get_history()

        with st.spinner("🔍 Searching document..."):

            rewritten_query = rewrite_query(
                query,
                history
            )
            st.info(f"Rewritten Query: {rewritten_query}")

            retrieved_chunks = hybrid_search(
                rewritten_query,
                st.session_state.current_pdf
            )

            best_chunks = rerank(
                rewritten_query,
                retrieved_chunks,
                top_k = 8
            )
            st.write("## Retrieved Chunks")

            for i, chunk in enumerate(best_chunks):
                st.write(f"### Chunk {i+1}")
                st.write(chunk["document"][:800])
                st.write("---")

            context = build_rerank_context(
                best_chunks
            )

        with st.chat_message("assistant"):

            with st.spinner("🤖 Generating answer..."):

                answer = generate_answer(
                    query=query,
                    context=context,
                    history=history
                )

                st.markdown(answer)

        add_assistant_message(answer)

        st.session_state.memory.add(
            question=query,
            answer=answer
        )

        show_sources(best_chunks)

# ----------------------------------------------------
# CLEAR CHAT
# ----------------------------------------------------

if st.session_state.pdf_processed:

    if st.button("🗑 Clear Chat"):

        st.session_state.memory.clear()

        st.session_state.messages = []

        st.rerun()