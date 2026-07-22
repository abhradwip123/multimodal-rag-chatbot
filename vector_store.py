import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def clear_database():
    """
    Delete old collection and create a fresh one.
    """

    global collection

    try:
        client.delete_collection("documents")
    except:
        pass

    collection = client.get_or_create_collection(
        name="documents"
    )


def store_chunks(chunks, embeddings, metadata):

    ids = []
    metadatas = []

    for i in range(len(chunks)):

        ids.append(
            f"{metadata[i]['file_name']}_page_{metadata[i]['page']}_chunk_{i}"
        )

        metadatas.append(metadata[i])

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks.")