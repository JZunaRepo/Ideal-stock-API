import requests
from config import key

stocks = ["AAPL"]

for stock in stocks:
  url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-05-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
  data = requests.get(url)
  print(data)
  json_data = data.json()
  results_data = json_data["results"]
  print(results_data)
