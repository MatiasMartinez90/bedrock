from src.graph.state import State

from src.utils.logging_config import get_logger
from src.agents.tavily_agent import tavily_agent

logger = get_logger(__name__)


def internet_node(state: State):
    """
    Este nodo es el agente que se encarga de responder las preguntas del usuario usando la API de Tavily.
    """
    response = tavily_agent.invoke({
        "input": state["messages"]
    })

    logger.info(f"Respuesta del chatbot: {response}")

    return {"messages": [response]}


