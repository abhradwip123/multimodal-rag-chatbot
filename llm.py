try:
    import ollama
except ImportError as exc:
    raise ImportError(
        "The ollama package is required. Install it with `pip install ollama`."
    ) from exc


def generate_answer(query, context, history=""):

    prompt = f"""
You are a helpful AI assistant.

Use the conversation history only to understand follow-up questions.

Answer ONLY using the document context.

If the answer is not found in the document context, reply exactly:

"I could not find the answer in the document."

--------------------------------------------------

Conversation History:

{history}

--------------------------------------------------

Document Context:

{context}

--------------------------------------------------

Current Question:

{query}

--------------------------------------------------

Answer:
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]