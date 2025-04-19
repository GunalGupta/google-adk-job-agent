from google.adk.agents import Agent
from .prompt import FILTERY_AGENT_INSTR

filtery_agent = Agent(
    model="gemini-2.0-flash-001",
    name="filtery",
    description="Filters job postings based on user preferences",
    instruction=FILTERY_AGENT_INSTR,
    tools=[],
)