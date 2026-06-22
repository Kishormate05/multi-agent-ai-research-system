from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

response = client.search(
    query="What is Agentic AI?",
    max_results=1
)

print(response)