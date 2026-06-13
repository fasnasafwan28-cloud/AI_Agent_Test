# 📄 PDF Question Answering Agent

A local AI-powered PDF Question Answering application built with Streamlit, LangChain, Ollama, and FAISS.

Upload a PDF document and ask questions about its contents. The application retrieves relevant sections from the document and generates answers using a local Large Language Model (LLM).

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- FAISS
- PyPDF
---

### Models Used

- Embedding Model: `nomic-embed-text`
- LLM Model: `phi3`
---

## 💡 How It Works

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into chunks.
4. Generate embeddings using `nomic-embed-text`.
5. Store embeddings in a FAISS vector database.
6. Retrieve the most relevant chunks based on the user's question.
7. Pass the retrieved context to the `phi3` model.
8. Generate an answer using only the retrieved content.

---


## 👨‍💻 Author
Fasna Safvan


Built using Streamlit, LangChain, Ollama, and FAISS for local Retrieval-Augmented Generation (RAG).
