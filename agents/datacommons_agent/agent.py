# agents/datacommons_agent/agent.py

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    StreamableHTTPConnectionParams,
)
from google.adk.models.lite_llm import LiteLlm

from .instructions import AGENT_INSTRUCTIONS

MODEL = "openrouter/z-ai/glm-4.5-air:free"
llm = LiteLlm(model=MODEL)

dc_agent = LlmAgent(
    model=llm,
    name="DataCommonsAgent",
    instruction=AGENT_INSTRUCTIONS,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
            url=f"http://localhost:8001/mcp"
         )
        )
    ],
)