from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os


def create_vector_db():

    PDF_FOLDER = "documents/pdfs"

    all_docs = []

    for file in os.listdir(PDF_FOLDER):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(PDF_FOLDER, file)

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            all_docs.extend(docs)

    print(f"Loaded {len(all_docs)} pages")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(all_docs)

    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local("vectorstore/faiss_index")

    print("FAISS Database Created Successfully")


if __name__ == "__main__":
    create_vector_db()