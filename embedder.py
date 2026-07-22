from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embeddings(chunks):
    """
    Generate embeddings for text chunks.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings.tolist()