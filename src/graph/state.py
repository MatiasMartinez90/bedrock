#STATE OF THE GRAPH LANGGRAPH 

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import add_messages

def add_query_history(query_history: list, query: list) -> list:
    query_history.append(query)
    return query_history



def add_retrieved_results(retrieved_results: dict, results: dict) -> dict:
    retrieved_results.update(results)
    return retrieved_results


class State(TypedDict):
    "Estado del grafo"
    messages: Annotated[list, add_messages]
    query_history: Annotated[list, add_query_history]
    retrieved_results: Annotated[dict, add_retrieved_results]
    current_agent: str 






