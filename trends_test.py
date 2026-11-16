
from pytrends_next import TrendReq

# Connect to Google Trends
pytrends = TrendReq()

# Search keyword
pytrends.build_payload(
    kw_list=["Python"],
    timeframe="today 12-m",
    geo="IN"
)

# Get interest over time
data = pytrends.interest_over_time()

print(type(data))
print(data)
