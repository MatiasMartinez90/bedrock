# Configuración de logging

import logging

# Configuración básica
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Configuración básica de logging
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),  # Log a consola
        logging.FileHandler("app.log")  # Log a archivo en directorio actual
    ]
)

def get_logger(name):
    """
    Obtiene un logger configurado para el módulo especificado.
    
    Args:
        name: Nombre del logger (normalmente __name__)
        
    Returns:
        Un objeto logger configurado
    """
    return logging.getLogger(name)



