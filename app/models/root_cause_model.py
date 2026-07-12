from pydantic import BaseModel
from typing import List

class RootCauseAnalysis(BaseModel):
    root_cause: str
    confidence: float
    evidence: List[str]
    explanation: str