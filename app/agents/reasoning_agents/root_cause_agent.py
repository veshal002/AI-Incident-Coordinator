from app.agents.base_agent import BaseAgent
from app.models.root_cause_model import RootCauseAnalysis

class RootCauseAgent(BaseAgent):
    def analyze(self,incident: str, context: str) -> RootCauseAnalysis:
        prompt = f"""
You are an Enterprise Incident Root Cause Analysis expert.

Your job is to identify the SINGLE most likely root cause.

Incident:

{incident}

Retrieved Enterprise Context:

{context}

Return:

- Root Cause
- Confidence
- Supporting Evidence
- Explanation

Base your answer ONLY on the provided context.
"""
        return self.ask_structured(prompt,RootCauseAnalysis)