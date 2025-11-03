# ADK Web Multi-Agent System

This repository demonstrates building a multi-agent system using **Google's ADK (Agent Development Kit)**. The system allows for natural language querying across two distinct data sources: a local **PostgreSQL** database for HDB resale data and the **Data Commons MCP API** for general global statistics.

The architecture implements a **Coordinator/Dispatcher** Pattern to route specialized queries to the correct agent.

## Project Structure

```bash
adk-web-multi-agent-system/
├── tools.yaml               # MCP Toolbox configuration for PostgreSQL tools
├── toolbox_playground.ipynb # Jupyter Notebook containing testing/execution code
├── pyproject.toml           # Project dependencies managed by uv
├── .gitignore
└── agents/                  # Directory for individual specialist agents
    ├── __init__.py          # Makes 'agents' a package
    ├── agent.py             # Defines the Coordinator LLM Agent
    ├── datacommons_agent/   # Agent for global Data Commons queries
    │   ├── __init__.py
    │   ├── agent.py         # Defines the Data Commons LLM Agent
    │   └── instructions.py
    └── postgres_agent/      # Agent for structured HDB PostgreSQL queries
        ├── __init__.py
        ├── agent.py         # Defines the PostgreSQL LLM Agent
        └── instructions.py
```

## Prerequisites & Setup

This project relies on external services and specific environment tools:

1. **PostgreSQL Database**: A local instance running on 127.0.0.1:5432 with the public.resale_transactions table populated (DDL provided in the blog post).

2. **Data Commons MCP Server**: Start a local instance using the Data Commons CLI:
  ```powershell
  uvx datacommons-mcp serve http --port 8000
  ```

3. **Toolbox (PostgreSQL Interface)**: The MCP tool server for PostgreSQL can be started from project root:
  ```powershell
  .\toolbox
  ```
4. **Python Environment**: Managed using `uv` for dependency isolation:
  ```powershell
  uv venv
 
  uv init 
  uv add google-adk litellm toolbox-core 
  ```

## Running the Agents

This project structure requires a **Coordinator Agent** (defined in the main execution logic) that hierarchically manages the `postgres_agent` and `datacommons_agent` via the `sub_agents` argument. 

To run the entire multi-agent system locally, execute the following command from your activated environment:

```powershell
adk web
```