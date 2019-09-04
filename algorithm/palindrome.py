#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
找出1~999之间的所有回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
如: 1-9 818

algorithm/palindrome.py
"""

print('找出1~999之间的所有回文数')
for num in range(1, 1000):
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        print(num, end=' ')
