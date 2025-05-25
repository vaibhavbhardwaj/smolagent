from smolagents import ToolCallingAgent,DuckDuckGoSearchTool,LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5-coder:7b",
    api_base="http://localhost:11434",  # Adjust if using a remote server
    api_key="ollama"  # Replace with your API key if required
)

agent = ToolCallingAgent(tools=[DuckDuckGoSearchTool()], model=model)

answer = agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")
print(answer)