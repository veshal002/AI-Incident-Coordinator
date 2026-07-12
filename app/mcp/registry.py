# Retrieval tools 
from app.mcp.mcp_tools.sql_tool import search_incidents
from app.mcp.mcp_tools.hybrid_tool import search_documents
from app.mcp.mcp_tools.graph_tool import search_graph

# Diagnostics
from app.mcp.mcp_tools.diagnostics.log_tool import search_logs
from app.mcp.mcp_tools.diagnostics.ping_tool import ping_service
from app.mcp.mcp_tools.diagnostics.health_tool import service_health


def register_tools(mcp):

    @mcp.tool()
    def sql_search(query: str):
        """Search historical incidents."""
        return search_incidents(query)

    @mcp.tool()
    def hybrid_search(query: str):
        """Search enterprise documents."""
        return search_documents(query)

    @mcp.tool()
    def graph_search(entity: str):
        """Search enterprise dependency graph."""
        return search_graph(entity)
    
    @mcp.tool()
    def log_search(query: str):
        return search_logs(query)


    @mcp.tool()
    def ping(service: str):
        return ping_service(service)


    @mcp.tool()
    def health(service: str):
        return service_health(service)