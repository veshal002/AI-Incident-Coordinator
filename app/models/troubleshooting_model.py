from pydantic import BaseModel
from typing import List

class TroubleshootingPlan(BaseModel):
    diagnostic_steps: List[str]
    probable_resolution: str
    escalation_required: bool
    notes: str