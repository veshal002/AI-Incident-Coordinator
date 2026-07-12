#

from app.database.sql.sqlite_manager import SQLiteManager

db = SQLiteManager()


def search_incidents(query: str) -> list[dict]:
    """
    Search structured incident records.

    NOTE:
    Temporary implementation.
    Later this will use LangChain SQLDatabase.
    """

    rows = db.fetch_all(
        """
        SELECT *
        FROM incidents
        LIMIT 5
        """
    )

    return rows