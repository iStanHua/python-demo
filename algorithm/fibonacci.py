#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
输出斐波那契数列的前n个数
1 1 2 3 5 8 13 21 ...

algorithm/fibonacci.py
"""

a = 0
b = 1
n = int(input('请输入斐波那契数列个数: '))
for _ in range(n):
    a, b = b, a + b
    print(a, end=' ')
