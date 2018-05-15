# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0315
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : print_items.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from time import sleep
import time


def fn_timer(func):
    def wapper(*args,**kwargs):
        s = time.time()
        func(*args,**kwargs)
        e = time.time()
        print('the %s\'s ran time is %r' % (func.__name__, e - s))

    return wapper


@fn_timer
def print_items(list):
    for item in list:
        print(item)


@fn_timer
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)


if __name__ == '__main__':
    my_list = [1, 3, 5]
    print_items(my_list)
    print_items2(my_list)
