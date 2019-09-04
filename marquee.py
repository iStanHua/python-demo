#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
marquee.py
"""

import os
import time

str = 'Welcome to 1000 Phone Chengdu Campus      '
while True:
    print(str)
    time.sleep(0.2)
    str = str[1:] + str[0:1]
    # for Windows use os.system('cls') instead
    os.system('cls')
