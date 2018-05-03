#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-4-12 上午10:30'

from urllib.parse import urlencode
import requests
import json
import urllib
import os
from bs4 import BeautifulSoup

headers = {
    "Host": "static.fg.blizzmi.cn",
    "referer": "https://static.fg.blizzmi.cn/game?type=h5&gamecode=nxzqd&username=&token=F5120E0B0DE7D2F7&language=zh-cn&view=single",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
}

url = "https://static.fg.blizzmi.cn/global/list/slot/2264/bin/manifest.json?0.5682511695775505"
base_res_url = "https://static.fg.blizzmi.cn/global/list/slot/2264/bin/"

def get_page():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def save_json(json):
    dir = "./2264"
    if not os.path.exists(dir):
        os.mkdir(dir)

    for (k, v) in json.items():
        res_url = base_res_url + v + "/" + k
        filename = res_url.split('/')[-1]
        try:
            response = requests.get(res_url)
            if response.status_code == 200:
                file_path = '{0}/{1}'.format(dir, filename)
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Downloaded', file_path)
        except requests.ConnectionError:
            print('failed to save json')

def get_blizzmi():
    try:
        response = requests.get("http://www.blizzmi.com/contact/")
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_blizzmi(page):
    soup = BeautifulSoup(page, 'lxml')
    for item in soup.find_all(attrs={'style': 'text-align: left; padding-left: 10px;'}):
        print(item.string)


if __name__ == '__main__':
    ## 爬取公司网页地址电话
    page = get_blizzmi()
    parse_blizzmi(page)
    ## 爬取游戏资源
    # json = get_page()
    # save_json(json)



