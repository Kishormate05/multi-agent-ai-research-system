from utils.llm import llm


def generate_report(query, analysis):

    prompt = f"""
You are a Professional Research Report Writer.

User Query:
{query}

Analysis:
{analysis}

Generate a professional markdown report.

Format:

# Title

## Executive Summary

## Key Findings

## Important Concepts

## Recommendations

## Future Scope

## Conclusion

Make the report detailed and professional.
"""

    response = llm.invoke(prompt)

    return response.content