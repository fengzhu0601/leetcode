#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-4-11 下午1:12'

from urllib.parse import urlencode
import requests
import json

base_url = "https://y.qq.com/download/download.js?"

headers = {
    "referer": "https://y.qq.com/portal/search.html",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

def get_page(page):
    params = {
        "jsonpCallback": "MusicJsonCallback",
        "loginUin": "125384977",
        "hostUin": "0",
        "format": "jsonp",
        "inCharset": "utf8",
        "outCharset": "utf-8",
        "notice": "0",
        "platform": "yqq",
        "needNewCode": "0"
    }
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    for page in range(1, 21):
        json = get_page(1)
        print(json)



