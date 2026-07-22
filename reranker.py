from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query, retrieved_chunks, top_k=8):

    pairs = []

    for item in retrieved_chunks:
        pairs.append([query, item["document"]])

    scores = model.predict(pairs)

    ranked = []

    for item, score in zip(retrieved_chunks, scores):

        ranked.append(
            {
                "document": item["document"],
                "metadata": item["metadata"],
                "score": float(score)
            }
        )

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked[:top_k]