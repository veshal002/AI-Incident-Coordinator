from pydantic import BaseModel

from app.models.incident_models import IncidentClassification
from app.models.root_cause_model import RootCauseAnalysis
from app.models.troubleshooting_model import TroubleshootingPlan
from app.models.recommendation_models import SolutionRecommendation


class IncidentWorkflowResult(BaseModel):

    classification: IncidentClassification

    root_cause: RootCauseAnalysis

    troubleshooting: TroubleshootingPlan

    recommendation: SolutionRecommendation