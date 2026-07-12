from app.agents.base_agent import BaseAgent
from app.models.root_cause_model import RootCauseAnalysis
from app.models.troubleshooting_model import TroubleshootingPlan

class TroubleshootingAgent(BaseAgent):
    def troubleshoot(self,incident: str, root_cause: RootCauseAnalysis,context: str)->TroubleshootingPlan:
        prompt = f"""
You are an Enterprise Incident Troubleshooting expert.

Incident:
{incident}

Root Cause Analysis:
{root_cause.model_dump_json(indent=2)}

Enterprise Context:
{context}

Generate:

- Diagnostic Steps
- Probable Resolution
- Escalation Required
- Notes

Base every recommendation only on the supplied context.
"""

        return self.ask_structured(
            prompt,
            TroubleshootingPlan,
        )