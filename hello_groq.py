GROQ_API_KEY="xyz"
LANGSMITH_API_KEY="xyz"

from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)

#print(llm)


class State(TypedDict):
    message:Annotated[list,add_messages]

graph_builder=StateGraph(State)

#print(graph_builder)

def chatbot(state:State):
    return {"messages":llm.invoke(state['messages'])}

graph_builder.add_node("chatbot",chatbot)

#print(graph_builder)
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

graph=graph_builder.compile()

from IPython.display import Image, display
try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    pass