from typing import Optional, Type
from pydantic import BaseModel
from app.services.llm import get_llm


class LLMService:
    def __init__(self):
        self.llm = get_llm()

    def generate(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response
    
    def generate_structured(self, prompt: str, output_model: type[BaseModel]):
        structured_llm=self.llm.with_structured_output(output_model)
        return structured_llm.invoke(prompt)
