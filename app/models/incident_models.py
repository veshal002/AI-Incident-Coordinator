from pydantic import Field, BaseModel

class IncidentClassification(BaseModel):
    category: str = Field(description="The predicted incident category.")
    confidence: float = Field(description="Confidence score between 0 and 1.")
    reasoning: str = Field(description="Short explanation for the classification.") 