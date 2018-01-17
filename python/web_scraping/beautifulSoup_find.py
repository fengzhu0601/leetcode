#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

# for child in bsObj.find("table", {"id":"giftList"}).children:
#     print(child)

# for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#     print(sibling)


images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])


aa = bsObj.findAll(lambda tag:len(tag.attrs) == 2)
print(aa)

