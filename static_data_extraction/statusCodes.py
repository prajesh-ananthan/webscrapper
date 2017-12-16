import re

import requests


def main():
    url = "https://finance.yahoo.com/quote/GOOG?p=GOOG"
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
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
        splitList = htmlText.split(Indicators[2])

        afterFirstSplit = splitList[1].split("\">")[2]
        afterSecondSplit = afterFirstSplit.split("</span>")[0]
        previosClose = remove_tags(afterSecondSplit)
        print(previosClose)


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


if __name__ == '__main__':
    main()
