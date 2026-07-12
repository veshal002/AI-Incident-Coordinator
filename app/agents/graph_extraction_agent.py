from app.agents.base_agent import BaseAgent
from app.models.graph_models import GraphExtraction

class GraphExtractionAgent(BaseAgent):

    def extract(self, document: str) -> GraphExtraction:

        prompt = f"""
You are an enterprise knowledge graph extraction expert.

Extract important entities and their relationships.

Guidelines:
- Entities should be enterprise concepts like VPN, LDAP, Firewall,
  Authentication Server, Database, API Gateway, DNS, Users, etc.
- Use concise relation names like:
  uses
  connects_to
  depends_on
  causes
  blocks
  authenticates_with
  replicates_to

Return only meaningful relationships.

Document:

{document}
"""

        return self.ask_structured(
            prompt,
            GraphExtraction,
        )