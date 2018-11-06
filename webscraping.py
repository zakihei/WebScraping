#!/usr/bin/python env
#-*- coding utf-8 -*-
#Ref:https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406

import urllib3 
import requests 
from bs4 import BeautifulSoup

"""以下、webページのタイトルを取得する"""

url = "https://www.nikkei.com/"

#r = requests.get(url)

http = urllib3.PoolManager()
r = http.request('GET', url)

soup = BeautifulSoup(r.data, 'html.parser')

title_tag = soup.title

title = title_tag.string

print(title_tag)

print(title)


