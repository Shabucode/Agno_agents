from agno.agent import Agent
# from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os

from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="qwen-2.5-32b"),
    tools=[DuckDuckGoTools],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="analyze financial data",
    model=Groq(id="qwen-2.5-32b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions="Use tables for display data",
    show_tool_calls=True,
    markdown=True,
)

# # Use the agents to interact with the web and finance APIs
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen-2.5-32b"),
    description="An AI team that can search the web for information and analyze financial data",    markdown=True,
    show_tool_calls=True,
)
agent_team.print_response("Analyze companies like Tesla, OpenAI and Apple and suggest which one to buy for long term")

