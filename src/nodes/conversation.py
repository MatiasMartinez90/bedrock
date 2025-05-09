from src.graph.state import State

from src.agents.conversation_agent import conversation_chain

from src.utils.logging_config import get_logger

logger = get_logger(__name__)

def conversation_node(state: State):
    """
    Este nodo es el encargado de conversar con el usuario
    """
    logger.info("Conversation node")

    response = conversation_chain.invoke(
        {
            "input": state["messages"]
        }
    )

    return {"messages": [response.response]}




