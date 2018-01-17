#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os.path import basename
import urllib
from urllib import request
import re
import requests
import json

url = 'https://www.zhihu.com/question/37787176'

if not os.path.exists('images'):
    os.mkdir("images")


page_size = 50
offset = 0
url_content = request.urlopen(url).read().decode('utf-8')

with open('images/content.txt', 'w') as f:
    f.write(url_content)
# print(url_content)

answers = re.findall(r'h3 data-num="(.*?)"', url_content)
print(answers)

limits = int(answers[0])
print(limits)

# while offset < limits:
#     post_url = "http://www.zhihu.com/node/QuestionAnswerListV2"
#     params = json.dumps({
#         'url_token': 37787176,
#         'pagesize': page_size,
#         'offset': offset
#     })
#     data = {
#         '_xsrf': '',
#         'method': 'next',
#         'params': params
#     }
#