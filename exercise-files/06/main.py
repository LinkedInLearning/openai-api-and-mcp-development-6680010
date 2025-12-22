
from autogen_agentchat.agents import AssistantAgent # type: ignore
from autogen_agentchat.teams import RoundRobinGroupChat  # type: ignore
from autogen_ext.models.openai import OpenAIChatCompletionClient # type: ignore
from autogen_agentchat.conditions import MaxMessageTermination # type: ignore
import asyncio
import os
from dotenv import load_dotenv
from rich.console import Console # type: ignore
from rich.pretty import pprint
from colorama import Fore


load_dotenv()
model_client = OpenAIChatCompletionClient(model="gpt-4o")
console = Console()
console.rule("[bold green] 🤖 Running A Multi Agent Workflow[/bold green]")

AGENT1_PROMPT = """
You are Developer Agent 1.

RESPONSIBILITY:
- Complete Task 1 ONLY.
- Do not attempt Task 2.
- Produce a clear, structured output.
- Validate your work.

IMPORTANT:
When Task 1 is fully complete, you MUST end your response with:
TASK_1_COMPLETE
"""

AGENT2_PROMPT = """
You are Developer Agent 2.

RULES:
- You MUST wait until Task 1 is completed.
- Use the output of Task 1 as input.
- Complete Task 2 ONLY.
- Deliver the final result.

IMPORTANT:
When finished, you MUST end your response with:
FINAL_OUTPUT
"""

COORDINATOR_PROMPT = """
You orchestrate a sequential multi-agent workflow.

WORKFLOW RULES:
1. Assign Task 1 to Dev_Agent_1.
2. Do NOT involve Dev_Agent_2 until Task 1 is complete.
3. Wait for the phrase 'TASK_1_COMPLETE'.
4. Then assign Task 2 to Dev_Agent_2.
5. Stop execution when 'FINAL_OUTPUT' is produced.

Do not solve tasks yourself.
"""

# ==========================================================
# PROJECT DEFINITION
# ==========================================================

PROJECT_DESCRIPTION = """
Project: Build a simple REST API specification.

Task 1:
- Design the API endpoints
- Define request/response schemas
- Document assumptions

Task 2:
- Add validation rules
- Define error handling strategy
- Produce final API spec
"""

# -------------------------------
# Developer Agent 1 (Task 1)
# -------------------------------


# -------------------------------
# Developer Agent 2 (Task 2)
# -------------------------------

# -------------------------------
# Coordinator / Orchestrator
# -------------------------------


# ==========================================================
# GROUP CHAT SETUP
# ==========================================================


# ==========================================================
# START WORKFLOW
# ==========================================================


# 8. Main async function to run the flow
async def main():
    """Run the multi-agent workflow.""" 
    pass

if __name__ == "__main__":
    asyncio.run(main())