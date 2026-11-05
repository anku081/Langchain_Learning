from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from typing import Any, Dict
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="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")

@tool
def web_search(query: str) -> Dict[str, Any]:
    """search the web for information"""
    return tavily_client.search(query)

system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""
    