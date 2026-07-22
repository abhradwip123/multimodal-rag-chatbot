import vector_store


def keyword_search(query, file_name=None):

    results = vector_store.collection.get()

    matched = []

    documents = results["documents"]
    metadatas = results["metadatas"]
    ids = results["ids"]

    query_words = query.lower().split()

    for doc, meta, doc_id in zip(documents, metadatas, ids):

        # Search only inside the uploaded PDF
        if file_name is not None:
            if meta.get("file_name") != file_name:
                continue

        score = sum(
        word in doc.lower()
        for word in query_words
)

        if score > 0:
            matched.append(
                {
                    "id": doc_id,
                    "document": doc,
                    "metadata": meta,
                    "score": score
                }
            )

    matched.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matched