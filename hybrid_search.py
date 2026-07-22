from retriever import retrieve
from keyword_search import keyword_search


def hybrid_search(query, file_name=None):

    # Vector Search
    vector_results = retrieve(
        query=query,
        file_name=file_name
    )

    # Keyword Search
    keyword_results = keyword_search(
        query=query,
        file_name=file_name
    )

    # Merge while removing duplicates
    merged = []
    seen = set()

    for item in vector_results + keyword_results:

        doc = item["document"]

        if doc not in seen:

            merged.append(item)
            seen.add(doc)

    return merged