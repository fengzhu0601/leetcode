#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

namelist = bsObj.findAll("span", {"class":"green"})
for name in namelist:
    print(name.get_text())

bs1 = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
print(bs1)

bs2 = bsObj.findAll("span", {"class":{"green", "red"}})
print(bs2)

bs3 = bsObj.findAll(text = "the prince")
print(len(bs3))

bs4 = bsObj.findAll(id = "text")
print(bs4[0].get_text())