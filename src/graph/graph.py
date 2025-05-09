from src.graph.state import State
from langgraph.graph import StateGraph, START, END

from src.nodes.chatbot import internet_node
from src.nodes.tool_node import tool_node
from langgraph.prebuilt import tools_condition
from src.utils.logging_config import get_logger
from langgraph.checkpoint.memory import MemorySaver


from src.nodes.router import router_node, deny_node, conditional_edges_router
from src.nodes.conversation import conversation_node



logger = get_logger(__name__)

memory = MemorySaver()





def create_chat_graph() -> StateGraph:
    """
    Crea el grafo de RAG usando LangGraph
    """
    logger.debug("Creando grafo de RAG")

    workflow = StateGraph(State)


    #ROUTER
    workflow.add_node("router", router_node)
    workflow.add_edge(START, "router")

    #CONVERSATION AGENT
    workflow.add_node("conversation_agent", conversation_node)

    #DENY AGENT
    workflow.add_node("deny_agent", deny_node)

    workflow.add_conditional_edges(
        "router",
        conditional_edges_router
    )

    workflow.add_edge("conversation_agent", END)
    workflow.add_edge("deny_agent", END)



    #REACT AGENT
    workflow.add_node("internet_agent", internet_node)
    workflow.add_node("search_tool", tool_node)
    
    workflow.add_conditional_edges(
        "internet_agent",
        tools_condition,
        {
            "tools": "search_tool",
            END: END
        }
    )
    workflow.add_edge("search_tool", "internet_agent")
    workflow.add_edge("internet_agent", END)

    graph = workflow.compile(checkpointer=memory)

    return graph







    






