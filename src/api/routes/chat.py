#route FASTAPI

from fastapi import APIRouter, HTTPException
from src.utils.logging_config import get_logger
from src.api.models.base import ChatRequest, ChatResponse
from src.api.services.graph import invoke_graph

# Obtener logger para este módulo
logger = get_logger(__name__)


# Crear el router
router = APIRouter(prefix="/chat", tags=["Chat"])



@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint para procesar mensajes de chat con el agente LLM.
    """
    try:
        logger.info(f"Solicitud de chat recibida - user_id: {request.user_id}, session_id: {request.session_id}")
        
        config = {
            "user_id": request.user_id,
            "session_id": request.session_id
        }

        result = invoke_graph(request.message, config)

        return ChatResponse(
            response=result,
            metadata={
                "user_id": request.user_id,
                "session_id": request.session_id
            }
        )
    except Exception as e:
        logger.error(f"Error en el procesamiento del mensaje: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error en el procesamiento del mensaje: {str(e)}")