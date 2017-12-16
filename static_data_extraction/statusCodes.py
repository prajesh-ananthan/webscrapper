"""
A simple Webscraper POC project that extracts data from Yahoo finances site
"""

import re

import requests


def main():
    url = "https://finance.yahoo.com/quote/GOOG?p=GOOG"
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        Indicators = {"Previous Close": [],
                      "Open": [],
                      "Bid": [],
                      "Ask": [],
                      "Day&#x27;s Range": [],
                      "52 Week Range": [],
                      "Volume": [],
                      "Avg. Volume": [],
                      "Market Cap": [],
                      "Beta": [],
                      "PE Ratio (TTM)": [],
                      "EPS (TTM)": [],
                      "Earnings Date": [],
                      "Forward Dividend & Yield": [],
                      "Ex-Divident Date": [],
                      "1y Target Est": []
                      }
        # TODO: Some values are not parsed properly to the dictionary due to HTML content
        # https://goo.gl/B2UcKw
        htmlText = response.text
        for indicator in Indicators:
            splitList = htmlText.split(indicator)
            afterFirstSplit = splitList[1].split("\">")[2]
            afterSecondSplit = afterFirstSplit.split("</span>")[0]
            data = remove_tags(afterSecondSplit)
            print(indicator + ": " + data)


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


if __name__ == '__main__':
    main()
