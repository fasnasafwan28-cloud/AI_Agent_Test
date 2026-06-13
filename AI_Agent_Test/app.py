import os
import streamlit as st

from pdf_loader import load_pdf
from vector_store import create_vectorstore
from retriever import get_answer

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="PDF QA Agent",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Main page */
.main {
    padding-top: 1rem;
}

/* Title */
h1 {
    text-align: center;
}

/* Answer box */
.answer-box {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    border-left: 6px solid #4CAF50;
    font-size: 18px;
    color: #222;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-top: 10px;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}

/* Text input */
.stTextInput > div > div > input {
    border-radius: 10px;
}

/* File uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed #4CAF50;
    padding: 10px;
    border-radius: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f5f5f5;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<h1>📄 PDF Question Answering Agent</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Upload one or more PDFs and ask questions about their content.</p>",
    unsafe_allow_html=True
)

# -----------------------------
# Create Upload Folder
# -----------------------------
os.makedirs("uploads", exist_ok=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:



    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.write("### Uploaded Files")

        pdf_paths = []

        for uploaded_file in uploaded_files:

            st.info(f"📄 {uploaded_file.name}")

            pdf_path = os.path.join(
                "uploads",
                uploaded_file.name
            )

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            pdf_paths.append(pdf_path)

        # -----------------------------
        # Process PDFs Button
        # -----------------------------
        if st.button("Process PDFs"):

            with st.spinner("Processing PDFs..."):

                all_chunks = []

                for pdf_path in pdf_paths:

                    chunks = load_pdf(pdf_path)

                    all_chunks.extend(chunks)

                vectorstore = create_vectorstore(all_chunks)

                st.session_state.vectorstore = vectorstore

            st.success(
                f"✅ {len(uploaded_files)} PDF(s) processed successfully!"
            )

# -----------------------------
# Question Section
# -----------------------------
question = st.text_input(
    "Ask a question about the uploaded PDFs"
)

if st.button("Get Answer"):

    if "vectorstore" not in st.session_state:

        st.warning(
            "Please upload and process PDF files first."
        )

    elif question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner("Searching documents..."):

            answer = get_answer(
                st.session_state.vectorstore,
                question
            )

        st.subheader("📌 Answer")

        st.markdown(
            f"""
            <div class="answer-box">
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🚀 Built with Streamlit, LangChain and FAISS")
