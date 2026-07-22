import streamlit as st


def create_sidebar():

    st.sidebar.title("⚙ Settings")

    st.sidebar.markdown("---")

    st.sidebar.subheader("Model")

    st.sidebar.success("Qwen2.5")

    st.sidebar.markdown("---")

    st.sidebar.subheader("Embedding")

    st.sidebar.info("BAAI/bge-small-en-v1.5")

    st.sidebar.markdown("---")

    st.sidebar.subheader("Current PDF")

    if "current_pdf" in st.session_state:
        st.sidebar.success(
            st.session_state.current_pdf
        )
    else:
        st.sidebar.warning("No PDF Uploaded")

    st.sidebar.markdown("---")

    st.sidebar.subheader("Conversation")

    if st.sidebar.button("🗑 Clear Chat"):

        st.session_state.messages = []

        if "memory" in st.session_state:
            st.session_state.memory.clear()

        st.rerun()