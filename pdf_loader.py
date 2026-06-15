from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    filename = os.path.basename(pdf_path)

    for doc in documents:
        doc.metadata["source_file"] = filename

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(documents)

    return chunks