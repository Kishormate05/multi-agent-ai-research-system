from tavily import TavilyClient
from dotenv import load_dotenv
from utils.llm import llm
import os

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def research_topic(query):

    try:

        results = tavily.search(
            query=query,
            max_results=3
        )

        research_data = ""

        for item in results.get("results", []):

            research_data += f"""
Title: {item.get('title', '')}
Content: {item.get('content', '')}
Source: {item.get('url', '')}

"""

        if not research_data:

            return "No web research results found."

        prompt = f"""
You are a senior research analyst.

Topic:
{query}

Research Data:
{research_data}

Generate:

1. Executive Summary
2. Key Findings
3. Important Trends
4. Challenges
5. Future Scope

Keep response structured.
"""

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        print(f"Tavily Error: {e}")

        return f"""
Executive Summary

Web research is currently unavailable.

Key Findings

- Tavily search request failed or timed out.
- The system will continue using PDF knowledge and internal analysis.

Important Trends

- External search unavailable.

Challenges

- Search timeout or API issue.

Future Scope

- Retry search later.
"""