from app.agents.base_agent import BaseAgent
from app.models.incident_models import IncidentClassification


class IncidentClassifier(BaseAgent):

    def classify(self, incident: str) -> IncidentClassification:

        prompt = f"""
You are an enterprise IT incident classifier.

Classify the incident into ONE category.

Possible Categories:

- Network
- Authentication
- Database
- Storage
- Security
- Application
- Infrastructure

Only return the category.

Incident:

{incident}
"""

        return self.ask_structured(prompt,IncidentClassification)