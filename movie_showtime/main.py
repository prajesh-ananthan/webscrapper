"""
Spyder Crawler
:copyright: (c) 2017 by Prajesh Ananthan.

"""
import re

import requests


def main():
    url = "http://www.cinema.com.my/showtimes/cinema.aspx?id=647#7BMxHAFGK1L43vGJ.97"
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        htmlText = response.text
        # splitList = htmlText.split("ShowtimesList")
        print(htmlText)


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


if __name__ == '__main__':
    main()
