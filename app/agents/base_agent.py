from typing import Type
from pydantic import BaseModel


from app.services.llm_service import LLMService

class BaseAgent:
    def __init__(self):
        self.llm_service = LLMService()

    def ask(self,prompt: str) -> str:
        return self.llm_service.generate(prompt)
    
    def ask_structured(self, prompt: str , output_model:Type[BaseModel]):
        return self.llm_service.generate_structured(prompt,output_model)
