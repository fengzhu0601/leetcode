#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__author__ = 'fengzhu'
__date__ = '18-4-3 下午3:24'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
try:
    browser.get("https://y.qq.com")
    # browser.get("https://www.baidu.com")
    input = browser.find_elements_by_class_name("search_input__input")
    # input = browser.find_element_by_id("kw")
    print(input[0])
    input[0].send_keys("周杰伦")
    input[0].send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 100)
    wait.until(EC.presence_of_element_located((By.ID, 'song_box')))
    print("current_url: ", browser.current_url)
    print("cookies: ", browser.get_cookies())
    print("page: ", browser.page_source)
finally:
    browser.close()

# word = "周杰伦"
# url = "https://y.qq.com/portal/search.html#page={page}&searchid=1&remoteplace=txt.yqq.top&t=song&w={word}"
#
# # 页数序号
# page = 1
#
# # while True:
# #     page += 1
# print("fetch: %s" % url.format(page=page, word=word))
# '''
# response.status_code        http请求的返回状态，若为200则表示请求成功
# response.text 	            http响应内容的字符串形式，即返回的页面内容
# response.encoding           从http header 中猜测的相应内容编码方式
# response.apparent_encoding  从内容中分析出的响应内容编码方式（备选编码方式）
# response.content 	        http响应内容的二进制形式
# '''
#
# FormData = {}
# FormData

