from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from utils.llm import llm

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "vectorstore/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


def ask_pdf(question):

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = ""

    sources = []

    for doc in docs:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get(
            "source",
            "Unknown PDF"
        )

        page = doc.metadata.get(
            "page",
            "Unknown Page"
        )

        sources.append(
            f"{source} (Page {page})"
        )

    prompt = f"""
You are an AI Research Assistant.

Answer the question only from the provided context.

Context:
{context}

Question:
{question}

Provide a detailed answer.
"""

    response = llm.invoke(prompt)

    source_text = "\n".join(
        list(set(sources))
    )

    return f"""
{response.content}

Sources Used:

{source_text}
"""