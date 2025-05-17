# from src.utils.logging_config import get_logger
# from src.graph.state import State

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from pydantic import BaseModel, Field
# from typing import Literal
# from langchain_core.messages import AIMessage

# from src.prompts.system import router_prompt

# logger = get_logger(__name__)

# model = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

# class Router(BaseModel):
#     """
#     Clase para el router
#     """
#     agent: Literal["internet", "conversation", "deny"] = Field(description="El agente a usar")


# router_chain = router_prompt | model.with_structured_output(Router)


# def router_node(state: State):
    
#     """
#     Este nodo es el encargado de decidir que agente usar segun la intencion del usuario
#     """
#     logger.info("Router node")

#     response = router_chain.invoke(
#         {
#             "input": state["messages"]
#         }
#     )
#     logger.info(f"Router response: {response}")
#     return {"current_agent": response.agent}


# def deny_node(state: State):
#     """
#     Este nodo es el encargado de decirle al usuario que no puede ayudarle en ese momento
#     """
#     logger.info("Deny node")

#     response = "Lo siento, no puedo ayudarte en este momento"

#     return {"messages": [AIMessage(content=response)], "current_agent": "deny"}


# #CONDICIONAL EDGES ROUTER
# def conditional_edges_router(state: State):
    
#     current_agent = state["current_agent"]

#     mapping = {
#         "deny": "deny_agent",
#         "internet": "internet_agent",
#         "conversation": "conversation_agent"
#     }

#     return mapping[current_agent]

#Retrieve Node

from src.utils.logging_config import get_logger
from src.api.services.retriever import retrieve_docs
from src.graph.state import State

logger = get_logger(__name__)

def retrieve_node(state: State):
    logger.info("Retrieve node")
    query = state["query"]
    docs = retrieve_docs(query)


    return {"docs": docs, "query_history": [query]}


    
    







    


