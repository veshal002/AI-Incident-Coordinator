from typing import List
from pydantic import BaseModel

class SolutionRecommendation(BaseModel):
    immediate_action: List[str]
    long_term_action: List[str]
    preventive_measures: List[str]
    priority: str
    expected_outcome: str