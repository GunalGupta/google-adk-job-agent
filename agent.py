from google.adk.agents import Agent
from job_summary_agent.sub_agents.scrapy.agent import scrapy_agent
from job_summary_agent.sub_agents.filtery.agent import filtery_agent
from job_summary_agent.sub_agents.write.agent import write_agent
from job_summary_agent.sub_agents.mail.agent import mail_agent
from job_summary_agent.prompt import ROOT_AGENT_INSTR

root_agent = Agent(
    model="gemini-2.0-flash-001",
    name="job_summary_agent",
    description="Summarizes job postings for ex-servicemen",
    instruction=ROOT_AGENT_INSTR,
    sub_agents=[scrapy_agent, filtery_agent, write_agent, mail_agent]
)