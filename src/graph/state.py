#STATE OF THE GRAPH LANGGRAPH 

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import add_messages

def add_query_history(query_history: list, query: list) -> list:
    query_history.append(query)
    return query_history

#merge two lists of docs
def add_docs(docs1: list, docs2: list) -> list:
    return docs1 + docs2


class State(TypedDict):
    "Estado del grafo"
    messages: Annotated[list, add_messages]
    query: str
    query_history: Annotated[list, add_query_history]
    docs: Annotated[list, add_docs]
    response: str






