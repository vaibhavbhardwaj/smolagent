from smolagents import CodeAgent, DuckDuckGoSearchTool,LiteLLMModel,tool,VisitWebpageTool, FinalAnswerTool, Tool, tool
#from smolagents import CodeAgent, ToolCallingAgent, DuckDuckGoSearchTool, LiteLLMModel, PythonInterpreterTool, tool
#from typing import Optional

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5-coder:7b",
    api_base="http://localhost:11434",  # Adjust if using a remote server
    api_key="ollama"  # Replace with your API key if required
)

agent = CodeAgent(tools=[], model=model)
answer = agent.run("What is the cube of 2?")
print(answer)