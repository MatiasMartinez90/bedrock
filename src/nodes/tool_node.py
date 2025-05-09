from src.agents.tavily_agent import tools
from langgraph.prebuilt import ToolNode


tool_node = ToolNode(tools=tools)


