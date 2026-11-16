
from mcp.server import MCPServer
from pytrends_next import TrendReq
from functools import lru_cache

mcp = MCPServer("Google Trends Agent")

@lru_cache(maxsize=100)
def fetch_trends(keyword: str):
    pytrends = TrendReq()

    pytrends.build_payload(
        kw_list=[keyword],
        timeframe="today 12-m",
        geo="IN"
    )

    data = pytrends.interest_over_time()
    return data[-10:]


@mcp.tool()
def get_trends(keyword: str) -> list:
    """Get Google Trends interest data for India over the last 12 months."""
    return fetch_trends(keyword.strip().lower())


if __name__ == "__main__":
    mcp.run()
