#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
求二个数的最大公约数和最小公倍数

gcd.py
"""

# 最大公约数


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


# 最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(108, 96))
print(lcm(108, 96))
