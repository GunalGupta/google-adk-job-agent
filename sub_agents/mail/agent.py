from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from job_summary_agent.tools.nodemailer import send_email
from .prompt import MAIL_AGENT_INSTR

mail_agent = Agent(
    model="gemini-2.0-flash-001",
    name="mail_agent",
    description="Sends the job summary email using nodemailer",
    instruction=MAIL_AGENT_INSTR,
    tools=[send_email]
)