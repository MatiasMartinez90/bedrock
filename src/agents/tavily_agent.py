from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from src.prompts.system import system_prompt_template
from langchain_core.tools import tool
from langgraph.types import Command
from langgraph.prebuilt import InjectedState
from langchain_core.tools.base import InjectedToolCallId
from langchain_core.messages import ToolMessage
from typing import Annotated
from src.graph.state import State


from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def extract_content(results: dict) -> dict:
    content_fields = ['title', 'content']
    content_dict = {}

    for result in results['results']:
        for field in content_fields:
            content_dict[result['url']] = result[field]

    urls = [result['url'] for result in results['results']]

    return urls, content_dict


@tool
def tavily_search_tool(
    query: str,
    state: Annotated[State, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId]
):
    """
    Search the web for information
    """
    search = TavilySearch(max_results=5)
    results = search.invoke({"query": query})

    #EXTRACT CONTENT AND URLS FOR UPDATE STATE
    urls, content_dict = extract_content(results)

    results_dict = {}
    results_dict[query] = urls
            
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content=content_dict,
                    tool_call_id=tool_call_id
                )
            ],
            "query_history": [query],
            "retrieved_results": results_dict
        }
    )


model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

tools = [tavily_search_tool]
model_with_tools = model.bind_tools(tools)
tavily_agent = system_prompt_template | model_with_tools