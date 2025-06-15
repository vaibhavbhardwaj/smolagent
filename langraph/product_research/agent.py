""" Concept: An AI agent that helps a user find a product (e.g., a laptop, a car, a book) by 
dynamically asking clarifying questions. Instead of a fixed decision tree, the agent uses user 
responses and an understanding of product features to determine the next best question to ask to 
narrow down options. It could then search a product database and present recommendations. """

import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END,START
from typing import TypedDict, Annotated, Sequence,List,Union
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage,AIMessage,AnyMessage
from operator import add as add_messages
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


llm=ChatGroq(model="llama3-70b-8192")

def process(state:AgentState)->AgentState:
    """This node will solve the request you put"""
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    print(f"state is : {state['messages']}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

conversation_history = []


user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter: ")



