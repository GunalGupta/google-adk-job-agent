from google.adk.agents import Agent
from .prompt import WRITE_AGENT_INSTR

write_agent = Agent(
    model="gemini-2.0-flash-001",
    name="write_agent",
    description="Composes a professional email with the job summary table",
    instruction=WRITE_AGENT_INSTR
)