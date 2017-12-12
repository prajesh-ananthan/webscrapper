import requests

url = "https://finance.yahoo.com/quote/GOOG?p=GOOG"

response = requests.get(url)
print(response)
print(response.status_code)

Indicators = ["Previous Close",
              "Open",
              "Bid",
              "Ask",
              "Day's Range",
              "52 Week Range",
              "Volume",
              "Avg. Volume",
              "Market Cap",
              "Beta",
              "PE Ratio (TTM)",
              "EPS (TTM)",
              "Earnings Date",
              "Forward Dividend & Yield",
              "Ex-Divident Date",
              "1y Target Est",
              ]

htmlText = response.text
splitList = htmlText.split("Previous Close")
# print(len(splitList))

# TODO: https://www.udemy.com/introduction-to-data-exractionweb-scraping-in-python/learn/v4/t/lecture/6694914?start=636
# Refer here for data: https://finance.yahoo.com/quote/GOOG?p=GOOG
# Figure how to retrieve the content
afterFirstSplit = splitList[1].split("\">")[1]
print(afterFirstSplit)

afterSecondSplit = afterFirstSplit.split("</td>")
print(afterSecondSplit)

# print("Search to find" , splitList[1].split("\">")[1])
