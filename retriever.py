from langchain_ollama import ChatOllama

SYSTEM_PROMPT = """
You are a PDF Question Answering Assistant.

Rules:

1. Answer ONLY using the provided context.
2. Do NOT use outside knowledge.
3. If the answer is not present in the context, respond exactly:

I don't know. The answer was not found in the uploaded PDFs.

4. Keep answers concise and factual.
"""

def get_answer(vectorstore, question):

    docs = vectorstore.similarity_search(
        question,
        k=5
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""

    llm = ChatOllama(
    model="phi3"
)

    response = llm.invoke(prompt)

    sources = list(
        set(
            doc.metadata.get(
                "source_file",
                "Unknown"
            )
            for doc in docs
        )
    )

    return response.content, sources