#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-3-21 下午2:58'


from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv

url = "http://sz.58.com/pinpaigongyu/pn/{page}/?minprice=1000_1500"

# 页数序号
page = 0

# python3的形式
csv_file = open("rent.csv", "w", encoding='utf8', newline='')
csv_writer = csv.writer(csv_file, delimiter=",")

while True:
    page += 1
    print("fetch: %s" % url.format(page=page))
    '''
    response.status_code        http请求的返回状态，若为200则表示请求成功
    response.text 	            http响应内容的字符串形式，即返回的页面内容
    response.encoding           从http header 中猜测的相应内容编码方式
    response.apparent_encoding  从内容中分析出的响应内容编码方式（备选编码方式）
    response.content 	        http响应内容的二进制形式
    '''
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text, "lxml")

    house_list = html.select(".list > li")

    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = urljoin(url, house.select("a")[0]["href"])
        house_info_list = house_title.split()

        # 如果是合租则去掉
        if "合租" in house_info_list[0]:
            pass
        else:
            if "公寓" in house_info_list[1]:
                house_location = house_info_list[0]
            else:
                house_location = house_info_list[1]
            house_money = house.select(".money")[0].select("b")[0].string
            csv_writer.writerow([house_title, house_location, house_money, house_url])

csv_file.close()


