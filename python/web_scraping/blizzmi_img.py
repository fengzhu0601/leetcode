#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.request
from selenium import webdriver

url1 = "https://fg-lobby.dev.blizzmi.cn/"
url = "https://lobby2.fg.blizzmi.cn/"

# browser = webdriver.Chrome()
browser = webdriver.Firefox()

browser.get(url)
images = re.findall(r'ng-src="(.*?\.(jpg|png))"', browser.page_source)
x = 1
for image_tuple in images:
    imageurl = image_tuple[0]
    # imagename = "~/fengzhu/picture/" + str(x) + ".png"
    try:
        urllib.request.urlretrieve(imageurl, '/home/fengzhu/fengzhu/picture/%d.png' % x)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            x += 1
        if hasattr(e, "reason"):
            x += 1
    x += 1
# print(image_tuple[0])
browser.close()
