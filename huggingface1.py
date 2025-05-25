from smolagents import CodeAgent, DuckDuckGoSearchTool,LiteLLMModel,tool,VisitWebpageTool, FinalAnswerTool, Tool, tool
#from smolagents import CodeAgent, ToolCallingAgent, DuckDuckGoSearchTool, LiteLLMModel, PythonInterpreterTool, tool
#from typing import Optional

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5-coder:7b",
    api_base="http://localhost:11434",  # Adjust if using a remote server
    api_key="ollama"  # Replace with your API key if required
)

# @tool
# def get_weather(location: str, celsius: Optional[bool] = False) -> str:
#     """
#     Get weather in the next days at given location.
#     Args:
#         location: the location
#         celsius: whether to use Celsius for temperature
#     """
#     return f"The weather in {location} is sunny with temperatures around 25°C."

#agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
#agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
#agent.run("Search for the best music recommendations for a party in india.")

# @tool
# def suggest_menu(occasion: str) -> str:
#     """
#     Suggests a menu based on the occasion.
#     Args:
#         occasion: The type of occasion for the party.
#     """
#     if occasion == "casual":
#         return "Pizza, snacks, and drinks."
#     elif occasion == "formal":
#         return "3-course dinner with wine and dessert."
#     elif occasion == "superhero":
#         return "Buffet with high-energy and healthy food."
#     elif occasion == "daru":
#         return "Whiskey with salad and peanuts."
#     else:
#         return "Custom menu for the butler."

# #agent = CodeAgent(tools=[suggest_menu], model=model)
# #agent.run("Prepare a superhero menu for the party.")

# from smolagents import CodeAgent
# import numpy as np
# import time
# import datetime

# agent = CodeAgent(tools=[], model=model, additional_authorized_imports=['datetime'])

# agent.run(
#     """
#     Alfred needs to prepare for the party. Here are the tasks:
#     1. Prepare the drinks - 30 minutes
#     2. Decorate the mansion - 60 minutes
#     3. Set up the menu - 45 minutes
#     3. Prepare the music and playlist - 45 minutes

#     If we start right now, at what time will the party be ready?
#     """
# )

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

@tool
def catering_service_tool(query: str) -> str:
    """
    This tool returns the highest-rated catering service in Gotham City.

    Args:
        query: A search term for finding catering services.
    """
    # Example list of catering services and their ratings
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }

    # Find the highest rated catering service (simulating search query filtering)
    best_service = max(services, key=services.get)

    return best_service

class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = """
    This tool suggests creative superhero-themed party ideas based on a category.
    It returns a unique party theme idea."""

    inputs = {
        "category": {
            "type": "string",
            "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
        }
    }

    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
            "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
            "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets."
        }

        return themes.get(category.lower(), "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")
@tool
def itsm_calling_agent(ticket: str)->str:
    """
    Suggest a ticket based on action.

    Args:
        ticket: the type of ticket user wants to create.
    """
    if ticket == "tsp":
        return "open tsp"
    elif ticket == "change":
        return "open CRQ for this change"
    elif ticket == "incident":
        return "Open incident."
    else:
        return "Custom menu for the itsm."


# Alfred, the butler, preparing the menu for the party
# agent = CodeAgent(
#     tools=[
#         DuckDuckGoSearchTool(),
#         VisitWebpageTool(),
#         suggest_menu,
#         catering_service_tool,
#         SuperheroPartyThemeTool()
#         ],
#     model=model,
#     max_steps=10,
#     verbosity_level=2
# )
agent = CodeAgent(tools=[itsm_calling_agent],model = model,max_steps=10,verbosity_level=2)
agent.run("I want to create a change ticket")
