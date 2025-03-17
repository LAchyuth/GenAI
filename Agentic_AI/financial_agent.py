from phi.agent import Agent             # For creating agent
from phi.model.groq import Groq         # for accessing various model
from phi.tools.yfinance import YFinanceTools  # Accesing data from yahoofinance for this project
from phi.tools.duckduckgo import DuckDuckGo   # for web search
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Web Seach Agent(calling with parameters)
websearch_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id ="llama-3.1-8b-instant"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls = True,
    markdown = True,
)

## Financial Agent
finance_agent = Agent(
    name = "Financee AI Agent",
    model = Groq(id ="llama-3.1-8b-instant"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, 
                stock_fundamentals=True,company_news = True)],
    instructions = ["Use tables to display the data"],
    show_tool_calls = True,
    markdown = True,         
)

multi_ai_agent = Agent(
    team = [websearch_agent,finance_agent],
    instructions = ["Always include sources","Use table to display the data"],
    show_tool_calls = True,
    markdown = True 
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Tesla",stream =True)
