#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
找出2~99之间的素数

prime.py
"""

import math

print('找出2~99之间的素数')
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
