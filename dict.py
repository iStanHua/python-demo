#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
字典

dict.py
"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict['Name'])

# 更新
dict['Age'] = 8
print('更新:%s' % str(dict))

# 添加
dict['School'] = 'STANHUA'
print('添加:%s' % str(dict))

# 浅复制
dict1 = dict.copy()
print('浅复制:%s' % str(dict1))

# 删除
del dict['Age']
print('删除:%s' % str(dict))

print(dict.items())
print(dict.values())
print(dict.keys())