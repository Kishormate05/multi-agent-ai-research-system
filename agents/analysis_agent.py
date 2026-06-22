from utils.llm import llm


def analyze_results(query, web_data, pdf_data):

    prompt = f"""
You are a Senior AI Research Analyst.

User Question:
{query}

Web Research:
{web_data}

PDF Research:
{pdf_data}

Tasks:

1. Combine both sources.
2. Remove duplicate information.
3. Highlight important insights.
4. Mention any differences between sources.
5. Create a structured analysis.

Format:

Executive Summary

Key Insights

Important Concepts

Source Comparison

Final Analysis
"""

    response = llm.invoke(prompt)

    return response.content