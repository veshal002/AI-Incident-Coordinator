from pathlib import Path

from langchain.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool

from app.services.llm_service import LLMService


DB_PATH = Path("data/incidents.db")

db = SQLDatabase.from_uri(
    f"sqlite:///{DB_PATH}"
)

query_tool = QuerySQLDatabaseTool(
    db=db,
)

@tool
def sql_search(question: str) -> str:
    """
    Search enterprise structured information
    from the SQLite incident database.

    Use this tool whenever historical incidents,
    servers, applications or infrastructure
    information is required.
    """

    try:

        return query_tool.invoke(question)

    except Exception as e:

        return f"SQL Search Failed: {e}"