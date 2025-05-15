import os
from dotenv import load_dotenv
load_dotenv()

if os.getenv("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY is not set")

if os.getenv("TAVILY_API_KEY") is None:
    raise ValueError("TAVILY_API_KEY is not set")



from src.graph.graph import create_chat_graph
from langchain_core.messages import HumanMessage


graph = create_chat_graph()


if __name__ == "__main__":
    

    config = {"configurable": {"thread_id": 0}}

    content = "Como estás?"

    result = graph.invoke(
        {"messages": [HumanMessage(content=content)]},
        config
    )

    print(result)

    #STREAMING
    # events = graph.stream(
    #     {"messages": [HumanMessage(content="Como estás?")]},
    #     config,
    #     stream_mode="values"
    # )

    # for event in events:
    #     event["messages"][-1].pretty_print()

    

   




