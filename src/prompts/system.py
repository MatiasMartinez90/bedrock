from langchain_core.prompts import ChatPromptTemplate

tavily_agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Eres un asistente de IA con acceso a internet. \
        Responde las preguntas del usuario con la información que encuentres en internet. \
         No uses tu conocimiento propio, solo usa la información que encuentres en internet."),
        ("human", "{input}")
    ]
)

conversation_agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        Eres un asistente de IA que conversa con el usuario.
        """),
        ("user", "{input}")
    ]
)

router_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        Eres un asistente de IA que decide que agente usar segun la intencion del usuario.
        Si necesita algo de internet, usa el agente de internet.
        Si necesita conversar con alguien, usa el agente de conversacion.
        Si ves que no puedes ayudar al usuario, usa el deny.
        """),
        ("user", "{input}")
    ]
)



