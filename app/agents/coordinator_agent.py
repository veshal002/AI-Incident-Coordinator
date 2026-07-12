from app.agents.incident_classifier import IncidentClassifier
from app.agents.retrieval_agent import RetrievalAgent

from app.agents.reasoning_agents.root_cause_agent import RootCauseAgent
from app.agents.reasoning_agents.troubleshooting_agent import TroubleshootingAgent
from app.agents.reasoning_agents.recommendation_agent import RecommendationAgent
from app.agents.diagnostic_agent import DiagnosticsAgent

from app.models.workflow_models import IncidentWorkflowResult

from app.services.workflow_config import WORKFLOW


class CoordinatorAgent:

    def __init__(self):

        self.classifier = IncidentClassifier()

        self.retrieval_agent = RetrievalAgent()

        
        self.diagnostics_agent = DiagnosticsAgent()

        self.root_agent = RootCauseAgent()

        self.troubleshooting_agent = TroubleshootingAgent()

        self.recommendation_agent = RecommendationAgent()

    def handle_incident(self, incident: str):

        # Classify
        classification = self.classifier.classify(incident)

        # Workflow configuration
        workflow = WORKFLOW.get(
            classification.category,
            {}
        )

        context = ""

        # Retrieval
        if workflow.get("retrieval", False):

            retrieval_result = self.retrieval_agent.retrieve(
                incident=incident,
                classification=classification,
            )

            context += retrieval_result.context
        if workflow.get("diagnostics", False):

            diagnostics = self.diagnostics_agent.run(
                    incident=incident,
                    classification=classification,
    )

        context += "\n\n=== Diagnostics ===\n\n"
        context += diagnostics
        
        # Root Cause Analysis
        root = self.root_agent.analyze(
            incident,
            context,
        )

        # Troubleshooting
        troubleshooting = self.troubleshooting_agent.troubleshoot(
            incident,
            root,
            context,
        )

        # Recommendation
        recommendation = self.recommendation_agent.recommend(
            incident,
            root,
            troubleshooting,
            context,
        )

        return IncidentWorkflowResult(
            classification=classification,
            root_cause=root,
            troubleshooting=troubleshooting,
            recommendation=recommendation,
        )