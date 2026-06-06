from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from rich import print

# Initialize the Tavily client with the API key from .env
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Define the tools for web search and URL scraping

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Title, URLs and Snippets."""
    results = tavily.search(query=query, max_results=5)

    out = []
    for r in results["results"]:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    return "\n================\n".join(out)

@tool
def scrape_url(url : str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading. """
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove scripts, styles, nav, and footer to get cleaner text
        for tag in soup(['script', 'style', 'nav', 'footer']):
            tag.decompose()
        return soup.get_text(separator="", strip=True)[:3000]  # Return first 3000 chars
    except Exception as e:
        return f"Error scraping URL: {e}"





