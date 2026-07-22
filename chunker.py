from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


def chunk_text(pages):

    chunks = []

    metadata = []

    for page in pages:

        page_chunks = splitter.split_text(
            page["text"]
        )

        for chunk in page_chunks:

            chunks.append(chunk)

            metadata.append(
                {
                    "page": page["page"]
                }
            )

    return chunks, metadata