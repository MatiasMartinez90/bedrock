from langchain_core.messages import HumanMessage
from src.graph.graph import create_chat_graph
from src.utils.logging_config import get_logger


logger = get_logger(__name__)
graph = create_chat_graph()


def invoke_graph(message: str, config_metadata: dict):

    config = {
        "configurable": {
            "thread_id": config_metadata["session_id"]
        }
    }


    result = graph.invoke(
        {"messages": [HumanMessage(content=message)]},
        config
    )
    return result