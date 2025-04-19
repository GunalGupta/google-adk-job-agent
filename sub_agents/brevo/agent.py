from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from job_summary_agent.tools.brevo import send_email
from .prompt import BREVO_AGENT_INSTR

brevo_agent = Agent(
    model="gemini-2.0-flash-001",
    name="brevo",
    description="Sends an email using the Brevo API",
    instruction=BREVO_AGENT_INSTR,
    tools=[send_email]
)