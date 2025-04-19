from job_summary_agent.websites import WEBSITES
from google.adk.tools import ToolContext

def get_websites(tool_context: ToolContext) -> list:
    """Returns the list of predefined websites to scrape."""
    return WEBSITES