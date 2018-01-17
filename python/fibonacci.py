#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b, a+b
#         n = n + 1
#     return 'done'
#
# print(fib(6))

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n = n + 1
    return 'done'

f = fib(6)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

for n in fib(6):
    print(n)

def triangles():
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x+1] for x in range(len(L) -1)]
        L.insert(0,1)
        L.append(1)
        if len(L) > 10:
            break

def print_triangles():
    for t in triangles():
        print(t)

print_triangles()
