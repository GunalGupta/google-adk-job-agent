# File: job_summary_agent/tools/firecrawler.py
from firecrawl import FirecrawlApp
from google.adk.tools import ToolContext

def firecrawler(url: str, tool_context: ToolContext) -> str:
    """Scrapes the given URL using Firecrawl and returns the markdown content."""
    app = FirecrawlApp(api_key="FIRECRAWL_API_KEY")
    try:
        scrape_result = app.scrape_url(url, params={'formats': ['markdown']})
        return scrape_result['markdown']
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"