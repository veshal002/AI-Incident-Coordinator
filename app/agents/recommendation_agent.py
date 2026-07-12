from app.agents.base_agent import BaseAgent
from app.models.recommendation_models import SolutionRecommendation
from app.models.root_cause_model import RootCauseAnalysis
from app.models.troubleshooting_model import TroubleshootingPlan


class RecommendationAgent(BaseAgent):

    def recommend(
        self,
        incident: str,
        root_cause: RootCauseAnalysis,
        troubleshooting: TroubleshootingPlan,
        context: str,
    ) -> SolutionRecommendation:

        prompt = f"""
You are an Enterprise Incident Resolution expert.

Incident:
{incident}

Root Cause:
{root_cause.model_dump_json(indent=2)}

Troubleshooting Plan:
{troubleshooting.model_dump_json(indent=2)}

Enterprise Context:
{context}

Generate:

- Immediate Actions
- Long-Term Actions
- Preventive Measures
- Priority
- Expected Outcome

Base your response only on the supplied enterprise context.
"""

        return self.ask_structured(
            prompt,
            SolutionRecommendation,
        )