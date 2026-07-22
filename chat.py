from hybrid_search import hybrid_search
from reranker import rerank
from rerank_context import build_rerank_context
from llm import generate_answer
from memory import ConversationMemory
from query_rewriter import rewrite_query

# Create conversation memory
memory = ConversationMemory()

print("=" * 60)
print("          MULTIMODAL RAG CHATBOT")
print("=" * 60)
print("Type 'exit' to quit.")
print("Type 'clear' to clear conversation memory.\n")

while True:

    query = input("You: ").strip()

    # Exit
    if query.lower() == "exit":
        print("\nGoodbye!")
        break

    # Clear memory
    if query.lower() == "clear":
        memory.clear()
        print("\nConversation memory cleared.\n")
        continue

    print("\nSearching document...")

    # Retrieve conversation history
    history = memory.get_history()

    # Rewrite query
    new_query = rewrite_query(
        query,
        history
    )

    print("\nRewritten Query:")
    print(new_query)

    # Hybrid retrieval
    chunks = hybrid_search(new_query)

    # Rerank
    best_chunks = rerank(
        new_query,
        chunks
    )

    # Build context
    context = build_rerank_context(best_chunks)

    # Conversation history
    history = memory.get_history()

    print("\nConversation History:")
    print(history)

    # Generate answer
    answer = generate_answer(
        query=query,
        context=context,
        history=history
    )

    # Save conversation
    memory.add(
        question=query,
        answer=answer
    )

    # Print answer
    print("\nAI:")
    print(answer)

    # Print sources
    print("\nSources:")
    print("-" * 40)

    for chunk in best_chunks:

        meta = chunk["metadata"]

    file_name = meta.get("file_name", "Unknown File")

    if "page" in meta:
        print(f"{file_name} | Page {meta['page']}")
    elif "chunk_id" in meta:
        print(f"{file_name} | Chunk {meta['chunk_id']}")
    else:
        print(file_name)

    print("\n" + "=" * 60 + "\n")

