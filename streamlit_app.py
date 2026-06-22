import streamlit as st
import os

from app import run_workflow
from vectorstore.create_db import create_vector_db

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📂 PDF Management")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.sidebar.button("Create Vector Database"):

    if uploaded_files:

        os.makedirs("documents/pdfs", exist_ok=True)

        for file in uploaded_files:

            save_path = os.path.join(
                "documents/pdfs",
                file.name
            )

            with open(save_path, "wb") as f:
                f.write(file.getbuffer())

        with st.spinner("Creating FAISS Database..."):

            create_vector_db()

        st.sidebar.success(
            "✅ Vector Database Created Successfully"
        )

    else:

        st.sidebar.warning(
            "⚠️ Upload at least one PDF"
        )

# =====================================
# HISTORY
# =====================================

st.sidebar.markdown("---")
st.sidebar.subheader("🕒 Chat History")

for item in reversed(st.session_state.history):

    st.sidebar.write(
        f"• {item['query']}"
    )

# =====================================
# MAIN UI
# =====================================

st.title("🤖 Multi-Agent AI Research System")

st.write(
    "Research + RAG + Analysis + Report Generation"
)

query = st.text_input(
    "Enter your research query"
)

if st.button("Generate Report"):

    if query:

        with st.spinner("🤖 Multi Agents are working..."):

            result = run_workflow(query)

        st.success("✅ Report Generated Successfully")

        st.markdown(result["report"])

        st.session_state.history.append(
            {
                "query": query,
                "report": result["report"]
            }
        )

        st.download_button(
            label="📥 Download Report",
            data=result["report"],
            file_name="research_report.txt",
            mime="text/plain"
        )

    else:

        st.warning("⚠️ Please enter your query")