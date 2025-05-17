from src.graph.state import State
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from src.utils.logging_config import get_logger
from src.nodes.retrieve import retrieve_node
from src.nodes.generate import generate_node



logger = get_logger(__name__)

memory = MemorySaver()





def create_chat_graph() -> StateGraph:
    """
    Crea el grafo de RAG usando LangGraph
    """
    logger.debug("Creando grafo de RAG")

    workflow = StateGraph(State)


    #ROUTER
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_edge(START, "retrieve")

    #CONVERSATION AGENT
    workflow.add_node("generate_answer", generate_node)

    workflow.add_edge("retrieve", "generate_answer")

    workflow.add_edge("generate_answer", END)

    graph = workflow.compile(checkpointer=memory)

    return graph







    






