from pydantic import BaseModel, Field

class GraphRelationship(BaseModel):
    source: str
    relation: str
    target: str

class GraphExtraction(BaseModel):
    relationships: list[GraphRelationship]