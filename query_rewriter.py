import ollama


def rewrite_query(query, history):

    if history.strip() == "":
        return query

    prompt = f"""
You are a query rewriting assistant.

Your job is to rewrite the user's latest question into a
complete standalone question using the conversation history.

Rules:

- Do NOT answer the question.
- Do NOT explain anything.
- Return ONLY the rewritten question.
- If the question is already complete,
return it unchanged.

Conversation History:

{history}

Current Question:

{query}

Standalone Question:
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

    return response["message"]["content"].strip()