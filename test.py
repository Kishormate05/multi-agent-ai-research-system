from utils.llm import llm

response = llm.invoke("What is Agentic AI?")

print(response.content)