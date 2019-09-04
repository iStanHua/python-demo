#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
数字时钟

class/clock.py
"""

from time import time, localtime, sleep
import os


class Clock(object):

    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
    # if 'hour' in kw and 'minute' in kw and 'second' in kw:
    #     self._hour = kw['hour']
    #     self._minute = kw['minute']
    #     self._second = kw['second']
    # else:
    #     tm = localtime(time.time())
    #     self._hour = tm.tm_hour
    #     self._minute = tm.tm_min
    #     self._second = tm.tm_sec

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        os.system('cls')
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
