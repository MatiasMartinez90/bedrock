from fastapi import FastAPI
import os
from dotenv import load_dotenv
import uvicorn
from src.utils.logging_config import get_logger
from src.api.routes import chat, system

# Obtener logger para este módulo
logger = get_logger(__name__)

# Cargar variables de entorno
load_dotenv()

# Verificar variables de LangSmith (opcionales - solo se advierte si no están configuradas)
if os.getenv("LANGSMITH_API_KEY") is None or os.getenv("LANGSMITH_TRACING") is None or os.getenv("LANGSMITH_PROJECT") is None:
    logger.warning("LangSmith no está configurado")


# Crear la aplicación FastAPI
app = FastAPI(
    title="Ueno Data RAG Test API",
    description="API para interactuar con un agente LLM implementado con LangGraph",
    version="1.0.0"
)


# Incluir los routers
API_PREFIX = "/api/v1"
app.include_router(chat.router, prefix=API_PREFIX)
app.include_router(system.router)

if __name__ == "__main__":
    logger.info(f"Iniciando servidor FastAPI en http://0.0.0.0:8000 (API en {API_PREFIX})")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 