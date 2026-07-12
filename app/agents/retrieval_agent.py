from langchain.agents import create_agent

from app.services.llm_service import LLMService
from app.tools import graph_search,hybrid_search,sql_search
from app.models.retrieval_models import RetrievalResult

class RetrievalAgent:

    def __init__(self):

        llm = LLMService()

        self.agent = create_agent(
            model=llm,
            tools=[
                hybrid_search,
                sql_search,
                graph_search,
            ],
        )
    
    def retrieve(self,incident: str,classification: str):
        prompt = f"""
        You are an Enterprise Retrieval Agent.
        Incident:

        {incident}

        Classification:

        Category:
        {classification.category}

        Confidence:
        {classification.confidence}

        Reason:
        {classification.reason}

        Your job is to collect only the
        information required by downstream
        reasoning agents.

        You have access to tools that can retrieve:

        • Enterprise documentation

        • Historical incidents

        • Infrastructure inventory

        • Knowledge graph relationships

        Use as few tool calls as possible.
        Think before calling a tool.
        Return the retrieved context only.
        """
        response = self.agent.invoke(
        
        {
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }]})

        return RetrievalResult(
        context=response["messages"][-1].content,
        tools_used=[],  # extracted from intermediate steps if desired
        )