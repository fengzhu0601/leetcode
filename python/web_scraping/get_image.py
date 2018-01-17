#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.zhihu.com/question/37787176")
bsObj = BeautifulSoup(html, "lxml")

# images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# images = bsObj.findAll("noscript")
images = bsObj.findAll("meta", {"content":re.compile("https\:\/\/www\.zhihu\.com\/question\/37787176\/answer\/.*")})
for image in images:
    print(image["src"])
