from google.adk.agents import Agent
from job_summary_agent.tools.firecrawler import firecrawler
from .prompt import SCRAPY_AGENT_INSTR

scrapy_agent = Agent(
    model="gemini-2.0-flash-001",
    name="scrapy",
    description="Scrapes job postings from predefined websites",
    instruction=SCRAPY_AGENT_INSTR,
    tools=[firecrawler]
)