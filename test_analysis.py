from agents.research_agent import research_topic
from agents.rag_agent import ask_pdf
from agents.analysis_agent import analyze_results

query = "What is Agentic AI?"

web_result = research_topic(query)

pdf_result = ask_pdf(query)

analysis = analyze_results(
    query,
    web_result,
    pdf_result
)

print(analysis)