#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-4-10 下午4:14'

import requests
from bs4 import BeautifulSoup
import time
import re
import pymysql

def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html, db):
    soup = BeautifulSoup(html, 'lxml')
    cursor = db.cursor()
    for dd in soup.find_all(name='dd'):
        top = dd.find(attrs={'class': re.compile('board-index.*')})
        name = dd.find(attrs={'class': 'name'})
        star = dd.find(attrs={'class': 'star'})
        release_time = dd.find(attrs={'class': 'releasetime'})

        print("NO." + top.string + "\t" + "电影名: " +name.string.strip() + "\t" + star.string.strip() + "\t" + release_time.get_text().strip())
        sql = 'insert into movies(id, name, star, release_time) values(%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (int(top.string), name.string.strip(), star.string.strip(), release_time.get_text().strip()))
            db.commit()
        except:
            print("rollback=====")
            db.rollback()
        # with open('movie_top.txt', 'a', encoding='utf-8') as file:
        #     file.write("NO." + top.string + "\t" + "电影名: " +name.string.strip() + "\t" + star.string.strip() + "\t" + release_time.get_text().strip()+"\n")

def main(db, offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    print("爬取网页: " + url)
    ## User-Agent浏览器标识信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
        "Host": "maoyan.com"
    }
    html = get_one_page(url, headers)
    parse_page(html, db)

def create_db():
    db = pymysql.connect(host='192.168.10.107', user='root', password='123456', port=3307)
    cursor = db.cursor()
    cursor.execute('select version()')
    data=cursor.fetchone()
    print('Database version:', data)
    cursor.execute("create database spiders default character set utf8")
    db.close()

def create_db_table():
    db = pymysql.connect(host='192.168.10.107', user='root', password='123456', port=3307, db='spiders')
    cursor=db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS movies (id INT(32) NOT NULL, name VARCHAR(255) NOT NULL, star VARCHAR(255) NOT NULL, release_time VARCHAR(255) NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()


if __name__ == '__main__':
    create_db_table()
    db = pymysql.connect(host='192.168.10.107', user='root', password='123456', port=3307, db='spiders', use_unicode=True, charset='utf8')
    for i in range(10):
        main(db, offset=i*10)
        time.sleep(1)
    db.commit()
    db.close()



