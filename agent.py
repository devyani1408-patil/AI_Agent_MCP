
import sys
from pathlib import Path

from google.adk.agents import Agent
from mcp import Client, StdioServerParameters


async def get_trends(keyword: str) -> str:
    """Get Google Trends interest data for a keyword in India."""

    server_path = Path(__file__).resolve().parent.parent / "server.py"

    server = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)]
    )

    async with Client(server) as client:
        result = await client.call_tool(
            "get_trends",
            {"keyword": keyword}
        )

    return str(result)


root_agent = Agent(
   model="gemini-3.5-flash-lite",
    name="google_trends_agent",
    description="An AI agent that analyzes Google Trends data.",
    instruction=(
        "You are a Google Trends analysis assistant. "
        "Use the get_trends tool to retrieve India Trends data. "
        "Explain the results in simple language."
    ),
    tools=[get_trends]
)
