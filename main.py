from dotenv import load_dotenv
import os

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
# from tavily import TavilyClient

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search results
#     """
#     print(f"Searching for {query}")
#     # return "Tokyo weather is sunny"
#     return tavily.search(query=query)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
weatherHumanContent = "what is the weather in Tokyo?"
jobSearchHumanContent = "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"

def main():
    print("Hello from langchain-searchagent!")
    result = agent.invoke({"messages": [HumanMessage(content=jobSearchHumanContent)]})
    print(result)


if __name__ == "__main__":
    main()
