import csv
from nbformat import write
import requests
from config import key
import time

stocks = ["AAPL","DIS","TSLA","SBUX","HMC"]

for stock in stocks:
  url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-05-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
  data = requests.get(url)
  json_data = data.json()
  results = json_data['results']

  stock_data=[]

  for day in results:
    closing_price = day["c"]
    time_price=day['t']
    real_time = time.strftime('%Y-%m-%d', time.localtime(time_price/1000))
    
    dic = {
      'Date': real_time,
      'Closing_Price':closing_price
    }
    stock_data.append(dic)

    with open(f"{stock}.csv","w",newline='') as outfile:
      writer= csv.DictWriter(outfile, fieldnames=["Date","Closing_Price"])
      writer.writeheader()
      writer.writerows(stock_data)



