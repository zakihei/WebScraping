#-*- coding utf-8 -*-
"""
Webscraping
"""

__author__ = "Kohe Miyazaki"
__status__ = "settle"
__version__ = "0.0.1"
__date__ = "17 Nove 2018"

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    """
    @param site URLを引数として渡す
    @param r urlopenで帰って来たResponseオブジェクトを格納
    @param html HTMLデータを格納
    @param parser HTMLをパースするための文字列を格納
    @param sp BeautifulSoupのオブジェクト
    """
    def __init__(self, site):
        self.site = site
    #ulropen Webサイトにリクエストを送りResponseオブジェクトが帰ってくる
    #respons.read HTMLデータが帰ってくる 
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://www.nikkei.com/markets/kabu/"
Scraper(news).scrape()

