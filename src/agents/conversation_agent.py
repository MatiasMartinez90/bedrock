from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from src.prompts.system import conversation_agent_prompt

class Conversation(BaseModel):
    """
    Clase para la conversacion
    """
    response: str = Field(description="La respuesta del agente")

    
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

conversation_chain = conversation_agent_prompt | model.with_structured_output(Conversation)




