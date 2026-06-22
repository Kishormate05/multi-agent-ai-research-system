from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.research_agent import research_topic
from agents.rag_agent import ask_pdf
from agents.analysis_agent import analyze_results
from agents.report_agent import generate_report


class AgentState(TypedDict):
    query: str
    web_result: str
    pdf_result: str
    analysis: str
    report: str


def research_node(state: AgentState):

    query = state["query"]

    state["web_result"] = research_topic(query)

    return state


def rag_node(state: AgentState):

    query = state["query"]

    state["pdf_result"] = ask_pdf(query)

    return state


def analysis_node(state: AgentState):

    state["analysis"] = analyze_results(
        state["query"],
        state["web_result"],
        state["pdf_result"]
    )

    return state


def report_node(state: AgentState):

    state["report"] = generate_report(
        state["query"],
        state["analysis"]
    )

    return state


graph = StateGraph(AgentState)

graph.add_node("research", research_node)
graph.add_node("rag", rag_node)
graph.add_node("analysis", analysis_node)
graph.add_node("report", report_node)

graph.add_edge(START, "research")
graph.add_edge("research", "rag")
graph.add_edge("rag", "analysis")
graph.add_edge("analysis", "report")
graph.add_edge("report", END)

app = graph.compile()


def run_workflow(query: str):

    result = app.invoke(
        {
            "query": query,
            "web_result": "",
            "pdf_result": "",
            "analysis": "",
            "report": ""
        }
    )

    return result


if __name__ == "__main__":

    query = input("Enter your query: ")

    result = run_workflow(query)

    print("\n")
    print("=" * 80)
    print(result["report"])
    print("=" * 80)