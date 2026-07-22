import vector_store
from embedder import model


def retrieve(query, file_name=None, n_results=25):

    query_embedding = model.encode(
        query,
        convert_to_numpy=True
    ).tolist()

    kwargs = {
        "query_embeddings": [query_embedding],
        "n_results": n_results,
    }

    if file_name is not None:
        kwargs["where"] = {
            "file_name": file_name
        }

    results = vector_store.collection.query(**kwargs)

    retrieved = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    ids = results["ids"][0]

    for doc, meta, doc_id in zip(documents, metadatas, ids):

        retrieved.append(
            {
                "id": doc_id,
                "document": doc,
                "metadata": meta
            }
        )

    return retrieved