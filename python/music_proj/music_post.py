#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-4-11 下午3:29'

from urllib.parse import urlencode
import requests
import json
import pymysql

base_url = "https://music.2333.me/"

headers = {
    "origin": "https://music.2333.me",
    "referer": "https://music.2333.me/?name=%E5%91%A8%E6%9D%B0%E4%BC%A6&type=qq",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

def get_page(page):
    params = {
        "input": "周杰伦",
        'filter': "name",
        'type': 'qq',
        'page': page
    }
    # url = base_url + urlencode(params)
    url = base_url
    print("page:{0},url:{1}".format(page, url))
    try:
        response = requests.post(url, data=params, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def create_db_table():
    db = pymysql.connect(host='192.168.10.107', user='root', password='123456', port=3307, db='spiders')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS music(songid VARCHAR(255) NOT NULL, ' \
          'author VARCHAR(255) NOT NULL, title VARCHAR(255) NOT NULL, ' \
          'lrc text, pic VARCHAR(255) NOT NULL, ' \
          'link VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL,' \
          'url VARCHAR(255) NOT NULL, PRIMARY KEY (songid))'
    cursor.execute(sql)
    db.close()

def parse_page(json, db):
    if json:
        items = json.get("data")
        cursor = db.cursor()
        sql = 'insert into music(songid, author, title, lrc, pic, link, type, url) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in items:
            try:
                print(item.get('title'))
                songid = item.get('songid')
                author = item.get('author')
                title = item.get('title')
                lrc = item.get('lrc')
                pic = item.get('pic')
                link = item.get('link')
                music_type = item.get('type')
                url = item.get('url')

                cursor.execute(sql, (songid, author, title, lrc, pic, link, music_type, url))
                db.commit()
            except:
                print("rollback=====")
                db.rollback()


if __name__ == '__main__':
    create_db_table()
    db = pymysql.connect(host='192.168.10.107', user='root', password='123456', port=3307, db='spiders', use_unicode=True, charset='utf8')
    for page in range(1, 21):
        json = get_page(page)
        parse_page(json,db)




