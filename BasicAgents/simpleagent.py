from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

# #os.environ['OPENAI_API_KEY'] = os.getenv['OPENAI_API_KEY']
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


agent=Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are an assistant please reply based ont he question",
    tools=[DuckDuckGoTools()],
    markdown=True
)

# agent.print_response("Who won the India vs Newzealand finals in CT 2025")
agent.print_response("Who is the new canadian prime minister in 2025")
# print(os.getcwd())