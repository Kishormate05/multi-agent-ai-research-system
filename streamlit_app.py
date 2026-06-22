import streamlit as st

from app import run_workflow

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🤖",
    layout="wide"
)

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

    else:

        st.warning("⚠️ Please enter a query")