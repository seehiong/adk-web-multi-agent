# agents/postgres_agent/agent.py

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from toolbox_core import ToolboxSyncClient
from .instructions import AGENT_INSTRUCTIONS

MODEL = "openrouter/z-ai/glm-4.5-air:free"
llm = LiteLlm(model=MODEL)

client = ToolboxSyncClient("http://127.0.0.1:5000") 
all_tools = client.load_toolset()

db_agent = Agent(
    name="PostgresAgent",
    model=llm,
    description="An intelligent database assistant for HDB resale transaction data",
    instruction=AGENT_INSTRUCTIONS,
    tools=all_tools,
)
