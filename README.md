# 🤖 Multimodal RAG Chatbot

A Multimodal Retrieval-Augmented Generation (RAG) chatbot built using **Streamlit**, **ChromaDB**, **Sentence Transformers**, **OCR**, **Hybrid Search**, and **Ollama**.

The chatbot can understand both digital and scanned PDFs, retrieve the most relevant information, rerank retrieved chunks, and answer user questions using a local Large Language Model.

---

## 🚀 Features

- Upload PDF documents
- Supports scanned PDFs using OCR
- Automatic text chunking
- Semantic embeddings using BAAI/bge-small-en-v1.5
- ChromaDB vector database
- Hybrid Search
  - Vector Search
  - Keyword Search
- Cross Encoder Reranking
- Conversation Memory
- Query Rewriting
- Local LLM using Ollama
- Streamlit Chat Interface
- Source Citation (Page Numbers)

---

## 🏗 Project Architecture

```
PDF
 │
 ▼
Text Extraction
 │
 ├── Digital PDF Reader
 └── OCR Reader
 │
 ▼
Chunking
 │
 ▼
Embedding Generation
 │
 ▼
ChromaDB Vector Store
 │
 ▼
Hybrid Search
 │
 ├── Vector Search
 └── Keyword Search
 │
 ▼
Cross Encoder Reranker
 │
 ▼
Context Builder
 │
 ▼
Query Rewriter
 │
 ▼
Conversation Memory
 │
 ▼
Ollama LLM
 │
 ▼
Answer
```

---

## 🛠 Tech Stack

- Python
- Streamlit
- ChromaDB
- LangChain Text Splitters
- Sentence Transformers
- Cross Encoder
- Ollama
- PyPDF
- EasyOCR
- Pillow
- OpenCV
- NumPy

---

## 📂 Project Structure

```
multimodal_rag_chatbot/
│
├── app.py
├── pipeline.py
├── pdf_reader.py
├── ocr_pdf_reader.py
├── image_reader.py
├── image_extractor.py
├── table_reader.py
├── chunker.py
├── embedder.py
├── vector_store.py
├── retriever.py
├── keyword_search.py
├── hybrid_search.py
├── reranker.py
├── rerank_context.py
├── llm.py
├── memory.py
├── query_rewriter.py
├── sidebar.py
├── uploader.py
├── chat_ui.py
├── metadata.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/abhradwip123/multimodal-rag-chatbot.git
```

Go inside the project

```bash
cd multimodal-rag-chatbot
```

Create virtual environment

```bash
python -m venv rag_env
```

Activate environment

Windows

```bash
rag_env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Download Ollama Model

```bash
ollama pull qwen2.5:3b
```

---

## Run the application

```bash
streamlit run app.py
```

---

## Future Improvements

- Image Captioning
- Table Understanding
- Multimodal Embeddings
- PDF Summarization
- Multi-document Chat
- Citation Highlighting
- Agentic RAG
- Web Search Integration

---

## Author

**Abhradwip Lala**

B.Tech CSE (AI & ML)

VIT Bhopal University
