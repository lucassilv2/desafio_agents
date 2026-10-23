from google.adk.agents import Agent
from google.adk.tools import google_search, google_maps_grounding, AgentTool

search_agent = Agent(
    name="search_agent",
    model="gemini-3.8-live", #live so funciona audio, mas não funciona texto. Talvez seja necessário usar o Gemini 3.8 Flash para texto.
    description="Searches the web with Google Search.",
    instruction="You are an expert researcher. You always stick to the facts.",
    tools=[google_search],
)

maps_agent = Agent(
    name="maps_agent",
    model="gemini-3.8-live",
    description="Finds places and location information with Google Maps.",
    instruction="You answer questions about places, addresses and locations using Google Maps.",
    tools=[google_maps_grounding],
)

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-3.8-live",
    description="Agent to answer questions using Google Search and Google Maps.",
    instruction=(
        "You are an expert researcher. Use search_agent for general facts and "
        "maps_agent for places and locations. You always pay close attention to facts."
    ),
    tools=[AgentTool(agent=search_agent), AgentTool(agent=maps_agent)],
)
