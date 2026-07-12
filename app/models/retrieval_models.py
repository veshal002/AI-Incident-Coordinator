from pydantic import BaseModel

class RetrievalResult(BaseModel):
    context: str
    tools_used: list[str]