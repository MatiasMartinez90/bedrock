# Ueno Data RAG Test

Este proyecto implementa un agente LLM basado en LangGraph y expone su funcionalidad a través de una API REST con FastAPI. Está diseñado para ser desplegado en AWS ECS como un contenedor Docker.

## Estructura del Proyecto

```
.
├── app.py                 # Aplicación FastAPI
├── main.py                # Script original para pruebas
├── Dockerfile             # Instrucciones para crear la imagen Docker
├── requirements.txt       # Dependencias del proyecto
├── docker-compose.yml     # Configuración para pruebas locales
├── env-example            # Variables de entorno (ejemplo)
└── src/                   # Código fuente del agente
    ├── agents/            # Implementaciones de agentes
    ├── config/            # Configuración del proyecto
    ├── graph/             # Definición del grafo LangGraph
    ├── nodes/             # Nodos del grafo
    ├── prompts/           # Prompts para los LLMs
    └── utils/             # Utilidades varias
```

## Variables de Entorno

El proyecto utiliza las siguientes variables de entorno:

```
# Obligatorias
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...

# LangSmith (opcionales, para tracing)
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=ls-...
LANGSMITH_PROJECT=ueno-data-rag-test
```

## Desarrollo Local

1. Clonar este repositorio
2. Crear un archivo `.env` con las claves API necesarias basándote en `env-example`
3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Ejecutar la aplicación:
   ```
   uvicorn app:app --reload
   ```
5. O utilizar Docker Compose:
   ```
   docker-compose up
   ```

## Endpoints

### POST /chat
Procesa un mensaje del usuario a través del agente LLM.

**Request:**
```json
{
  "user_id": "usuario123",
  "session_id": "sesion456",
  "message": "¿Cuál es la capital de Francia?"
}
```

**Response:**
```json
{
  "response": "La capital de Francia es París.",
  "metadata": {
    "user_id": "usuario123",
    "session_id": "sesion456"
  }
}
```

### GET /health
Endpoint para verificaciones de salud.

**Response:**
```json
{
  "status": "healthy"
}
```

## Despliegue en AWS ECS

### 1. Preparar la imagen Docker

```bash
# Construir la imagen
docker build -t ueno-data-rag-test:latest .

# Probar localmente
docker run -p 8000:8000 --env-file .env ueno-data-rag-test:latest
```

### 2. Subir la imagen a ECR

```bash
# Autenticar con ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# Crear repositorio en ECR (si no existe)
aws ecr create-repository --repository-name ueno-data-rag-test --region <region>

# Etiquetar la imagen
docker tag ueno-data-rag-test:latest <account-id>.dkr.ecr.<region>.amazonaws.com/ueno-data-rag-test:latest

# Subir la imagen
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/ueno-data-rag-test:latest
```

### 3. Crear el servicio ECS

1. Crear un Cluster ECS (si no existe)
2. Crear una definición de tarea:
   - Usar la imagen de ECR
   - Configurar las variables de entorno necesarias
   - Asignar suficiente memoria y CPU (recomendado mínimo 1GB de RAM)
   - Configurar los logs en CloudWatch
3. Crear un servicio:
   - Usar la definición de tarea
   - Configurar el balanceador de carga (opcional)
   - Configurar Auto Scaling (opcional)

### 4. Configurar las variables de entorno en ECS

Configurar las variables de entorno como secretos en AWS Secrets Manager o como variables de entorno en la definición de la tarea.