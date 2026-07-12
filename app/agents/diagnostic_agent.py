from langchain.agents import create_agent

from app.services.llm_service import LLMService

from app.mcp.mcp_tools.diagnostics.log_tool import search_logs
from app.mcp.mcp_tools.diagnostics.ping_tool import ping_service
from app.mcp.mcp_tools.diagnostics.health_tool import service_health


class DiagnosticsAgent:

    def __init__(self):

        self.agent = create_agent(
            model=LLMService().model,
            tools=[
                search_logs,
                ping_service,
                service_health,
            ],
        )

    def run(
        self,
        incident: str,
        classification,
    ):

        prompt = f"""
You are an Enterprise Diagnostics Agent.

Incident:
{incident}

Category:
{classification.category}

Your responsibility is to gather operational diagnostics.

Available capabilities include:
- Log search
- Service connectivity
- Service health

Only use the tools that are necessary.

Return only the collected diagnostic information.
"""

        response = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }]})

        return response["messages"][-1].content