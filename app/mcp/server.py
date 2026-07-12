from mcp.server.fastmcp import FastMCP
from app.mcp.registry import register_tools

mcp = FastMCP("AI Incident Intelligence")

register_tools(mcp)

if __name__ == "__main__":
    mcp.run()