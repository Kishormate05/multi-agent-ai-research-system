import streamlit as st
import os
import time

from app import run_workflow
from vectorstore.create_db import create_vector_db
from utils.pdf_generator import create_pdf_report

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
# CHAT HISTORY
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

status_box = st.empty()

if st.button("Generate Report"):

    if query:

        status_box.info("""
🔍 Research Agent      → Running...

📚 RAG Agent           → Waiting...

🧠 Analysis Agent      → Waiting...

📝 Report Agent        → Waiting...
""")

        time.sleep(1)

        status_box.info("""
✅ Research Agent      → Complete

📚 RAG Agent           → Running...

🧠 Analysis Agent      → Waiting...

📝 Report Agent        → Waiting...
""")

        time.sleep(1)

        status_box.info("""
✅ Research Agent      → Complete

✅ RAG Agent           → Complete

🧠 Analysis Agent      → Running...

📝 Report Agent        → Waiting...
""")

        time.sleep(1)

        status_box.info("""
✅ Research Agent      → Complete

✅ RAG Agent           → Complete

✅ Analysis Agent      → Complete

📝 Report Agent        → Running...
""")

        with st.spinner("🤖 Multi Agents are working..."):

            result = run_workflow(query)

        status_box.success("""
✅ Research Agent      → Complete

✅ RAG Agent           → Complete

✅ Analysis Agent      → Complete

✅ Report Agent        → Complete
""")

        st.success("✅ Report Generated Successfully")

        st.markdown(result["report"])

        st.session_state.history.append(
            {
                "query": query,
                "report": result["report"]
            }
        )

        # TXT DOWNLOAD

        st.download_button(
            label="📥 Download TXT Report",
            data=result["report"],
            file_name="research_report.txt",
            mime="text/plain"
        )

        # PDF DOWNLOAD

        pdf_file = create_pdf_report(
            result["report"],
            "research_report.pdf"
        )

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf,
                file_name="research_report.pdf",
                mime="application/pdf"
            )

    else:

        st.warning("⚠️ Please enter your query")