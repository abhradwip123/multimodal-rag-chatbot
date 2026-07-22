class ConversationMemory:

    def __init__(self):

        self.history = []

    def add(self, question, answer):

        self.history.append({

            "question": question,

            "answer": answer

        })

    def get_history(self):

        history_text = ""

        for item in self.history:

            history_text += f"User: {item['question']}\n"

            history_text += f"Assistant: {item['answer']}\n\n"

        return history_text

    def clear(self):

        self.history = []