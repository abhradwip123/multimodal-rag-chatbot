def build_rerank_context(best_chunks):

    context = ""

    for chunk in best_chunks:

        context += chunk["document"]
        context += "\n\n"

    return context