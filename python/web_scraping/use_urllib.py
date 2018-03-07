#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")

data = file.read()
print(data)

dataline = file.readline()
print(dataline)

fhandle = open("./1.html", "wb")
fhandle.write(data)
fhandle.close()

with open("./1.html", "wb") as f:
    f.write(data)

## 会产生缓存
filename = urllib.request.urlretrieve("http://www.baidu.com", filename="./2.html")
urllib.request.urlcleanup()

file.info()
file.getcode()
file.geturl()

urllib.request.quote("http://www.baidu.com")
urllib.request.unquote("http%3A//www.baidu.com")

"""
'''
User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36
'''
## 403错误
import urllib.request
import urllib.parse
import http.cookiejar

url = "https://segmentfault.com/q/1010000008880517/a-1020000008885648"
postdata = urllib.parse.urlencode(
    {
        "username":"125384977@qq.com",
        "password":"19880601fz"
    }
).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36")
data = urllib.request.urlopen(req).read()

with open("./4.html", "wb") as f:
    f.write(data)


url2 = "https://segmentfault.com/"
req2 = urllib.request.Request(url2,postdata)
req2.add_header("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36")
data2 = urllib.request.urlopen(req2).read()
with open("./5.html", "wb") as f:
    f.write(data2)

