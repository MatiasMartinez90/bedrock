from fastapi import APIRouter
from src.utils.logging_config import get_logger

# Obtener logger para este módulo
logger = get_logger(__name__)

# Crear el router
router = APIRouter(prefix="", tags=["Sistema"])

@router.get("/health")
async def health_check():
    """
    Endpoint para verificaciones de salud.
    
    Retorna un estado "healthy" si el servicio está funcionando correctamente.
    Este endpoint es utilizado por los balanceadores de carga para verificar el estado del servicio.
    """
    logger.debug("Solicitud de verificación de salud recibida")
    return {"status": "healthy"} 