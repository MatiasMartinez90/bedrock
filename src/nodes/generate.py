from src.utils.logging_config import get_logger
from src.graph.state import State
from pydantic import BaseModel, Field
from langchain_aws import ChatBedrock
from langchain_core.messages import AIMessage
from src.prompts.system import generate_response_prompt

logger = get_logger(__name__)

class GenerateOutput(BaseModel):
    #response RAG
    response: str = Field(description="The response to the user's question")


model_id = "us.anthropic.claude-3-haiku-20240307-v1:0"

model = ChatBedrock(
    model_id=model_id,
    temperature=0
)
model_with_structured_output = model.with_structured_output(GenerateOutput)
generate_chain = generate_response_prompt | model_with_structured_output



def generate_node(state: State):
    logger.info("Generate node")

    docs = state["docs"]
    query = state["query"]
    
    # Generar la respuesta
    response = generate_chain.invoke({"docs": docs, "query": query})

    return {"messages": [AIMessage(content=response.response)], "response": response.response}
    


