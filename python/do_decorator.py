#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# python装饰器如何在实现了return调用函数语句后，继续打印表示调用结束的日志信息？
def log(func):
    def wrapper(*args, **kw):
        print('begin call')
        print('call %s():' % func.__name__)
        do_now = func(*args, **kw)
        print('end call')
        return do_now
    return wrapper


@log
def now():
    print('2017-10-28')


f = now
f()

#结果：
# begin call
# call now():
# 2017-10-28
# end call
