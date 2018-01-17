#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib():
    a, b = 0, 1
    while True:
        yield a
        if a > 10:
            return a
        else:
            a, b = b, a+b


for i in fib():
    print(i)



def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)
        else:
            print("no no no")

search = grep('fengzhu')
next(search)
search.send("I Love you")
search.send("I Love fengzhu")
search.send("BieWanr Love fengzhu")
search.close()