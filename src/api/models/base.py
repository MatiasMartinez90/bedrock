# Modelo para la solicitud de chat
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, Any

class ChatRequest(BaseModel):
    user_id: str = Field(..., description="ID único del usuario", min_length=1, max_length=50)
    session_id: str = Field(..., description="ID de la sesión para mantener contexto de conversación", min_length=3, max_length=50) 
    message: str = Field(..., description="Mensaje del usuario", min_length=1, max_length=2000)
    
    @field_validator('message')
    @classmethod
    def validate_message_content(cls, v):
        """Validar que el mensaje no esté vacío o solo contenga espacios"""
        if not v.strip():
            raise ValueError("El mensaje no puede estar vacío")
        return v.strip()

# Modelo para la respuesta de chat
class ChatResponse(BaseModel):
    response: dict
    metadata: Optional[Dict[str, Any]] = None
