from langchain_core.messages import HumanMessage

#list of Messages objects
init_messages = [
    ["Cuál es el capital de Francia?"],
    ["Hola, cómo estás?"],
    ["Creame una base de datos"],
    ["Hola, cómo estás?", "Cómo creo una base de datos?"]
]

outputs = [
    ["internet"],
    ["conversation"],
    ["deny"],
    ["conversation", "internet"]
]

#connects inputs and outputs with a file

#array of dictionaries with messages
inputs = [{"messages": [HumanMessage(content=message) for message in init_messages[i]]} for i in range(len(init_messages))]





