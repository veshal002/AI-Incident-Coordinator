from app.agents.incident_classifier import IncidentClassifier
from app.agents.root_cause_agent import RootCauseAgent
from app.agents.troubleshooting_agent import TroubleshootingAgent
from app.agents.recommendation_agent import RecommendationAgent

from app.models.workflow_models import IncidentWorkflowResult

from app.retrievers.hybrid_retriever import HybridRetriever
from app.services.context_formatter import ContextFormatter


class CoordinatorAgent:

    def __init__(self):

        self.classifier = IncidentClassifier()

        self.retriever = HybridRetriever()

        self.root_agent = RootCauseAgent()

        self.troubleshooting_agent = TroubleshootingAgent()

        self.recommendation_agent = RecommendationAgent()
    
    def handle_incident(self, incident: str):

        classification = self.classifier.classify(incident)

        documents = self.retriever.retrieve(incident)

        context = ContextFormatter.format(documents)

        root = self.root_agent.analyze(incident,context)

        troubleshooting = (self.troubleshooting_agent.troubleshoot(
            incident,
            root,
            context
            )
        )

        recommendation = (
            self.recommendation_agent.recommend(
                incident,
                root,
                troubleshooting,
                context,
            )
        )

        return IncidentWorkflowResult(

            classification=classification,

            root_cause=root,

            troubleshooting=troubleshooting,

            recommendation=recommendation,
        )