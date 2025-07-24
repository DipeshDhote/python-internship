from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_community.document_loaders import WikipediaLoader
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()


# Define state
class QandA(TypedDict):
    messages: str

# Load Wikipedia API Wrapper
api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=300)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Create Wikipedia Tool
@tool
def wikipedia_search(messages: str) -> dict:
    """Search Wikipedia and return result in a dict."""
    result = wiki_tool.invoke(messages)
    return {"messages": result}

# Create the LangGraph
graph = StateGraph(QandA)

# Add node and edges
graph.add_node("wikipedia", wikipedia_search)
graph.add_edge(START, "wikipedia")
graph.add_edge("wikipedia", END)

# Compile agent
agent = graph.compile()

# Interactive loop
conv = []

while True:
    print("For exit, write - exit")
    inp = input("Enter your query: ")
    conv.append(f"User: {inp}")

    if inp.lower() == "exit":
        break

    res = agent.invoke({"messages": inp})
    print(res['messages'])
    conv.append(f"AI Message: {res['messages']}")

# Save conversation to a text file
with open("conversation.txt", "w", encoding="utf-8") as file:
    for line in conv:
        file.write(line + "\n")

print("Saved the conversation in 'conversation.txt'")
