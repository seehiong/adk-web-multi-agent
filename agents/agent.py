# agents/coordinator.py

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from agents.datacommons_agent.agent import dc_agent as datacommons_agent
from agents.postgres_agent.agent import db_agent as postgres_agent

COORDINATOR_MODEL = "openrouter/z-ai/glm-4.5-air:free" 
llm = LiteLlm(model=COORDINATOR_MODEL)

COORDINATOR_INSTRUCTION = """
You are the Master Coordinator for an intelligent assistant system. Your job is NOT to answer questions directly, but to delegate them to the correct specialist sub-agent.

**Delegate based on topic:**
1. **POSTGRESQL AGENT (`PostgresAgent`):** Route any request that involves **HDB resale transactions, flat prices, flat counts, town names (Tampines, Jurong West), or flat types ('4 ROOM', '3 ROOM')**. If the user mentions *any* HDB-specific term, delegate here.
2. **DATACOMMONS AGENT (`DataCommonsAgent`):** Route requests involving **global data, countries, continents, economics (GDP, income, inequality), health statistics, or general population data**.
3. **Other:** If the request is not clearly HDB-related and not clearly global data, default to routing to the `datacommons_agent` as it covers general knowledge.

**CRITICAL:** You must only output a **LLM-Driven Delegation call** using the format: `transfer_to_agent(agent_name='<target_agent_name>')`. Do not generate any other text or tool calls yourself.
"""

root_agent = LlmAgent(
    name="MasterCoordinator",
    model=llm,
    instruction=COORDINATOR_INSTRUCTION,
    description="Master router for HDB data and Global Data Commons queries.",
    
    sub_agents=[
        postgres_agent, 
        datacommons_agent
    ]
)
