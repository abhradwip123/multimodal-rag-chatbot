from pdf_reader import extract_text
from ocr_pdf_reader import extract_text_from_scanned_pdf

from chunker import chunk_text
from embedder import generate_embeddings
from vector_store import store_chunks

import os


def process_pdf(pdf_path):

    print("=" * 50)
    print("Reading PDF...")
    print("=" * 50)

    pages = extract_text(pdf_path)

    # If no selectable text → OCR
    if len(pages) == 0:

        print("Scanned PDF detected.")
        print("Running OCR...")

        pages = extract_text_from_scanned_pdf(pdf_path)

    total_characters = sum(len(page["text"]) for page in pages)

    print("Characters:", total_characters)

    chunks, metadata = chunk_text(pages)

    print("Chunks:", len(chunks))

    # Add file name to every metadata entry
    file_name = os.path.basename(pdf_path)

    for item in metadata:
        item["file_name"] = file_name

    embeddings = generate_embeddings(chunks)

    print("Embeddings:", len(embeddings))

    store_chunks(
        chunks,
        embeddings,
        metadata
    )

    return len(chunks)