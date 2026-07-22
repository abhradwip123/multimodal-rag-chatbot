import streamlit as st

def upload_pdf():

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    return uploaded_file