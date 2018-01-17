#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    ddt = b*b - 4 * a *c
    if ddt < 0 :
        print("无解")
        return 0
    else:
        x1 = ((-b) + math.sqrt(ddt))/(2*a)
        x2 = ((-b) - math.sqrt(ddt))/(2*a)
        return x1,x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))