from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks):

    embeddings = OllamaEmbeddings(
        model = "nomic-embed-text"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore