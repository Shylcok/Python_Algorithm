# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0414
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 冒泡查找.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import random
import time


def time_cl(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__, 'running time is ', t2 - t1, 'S')
        return func

    return wrapper


@time_cl
def _bubble_sort(num_list):
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    print(num_list)


@time_cl
def _bubble_sort2(num_list):
    for i in range(len(num_list) - 1):
        exchange = False
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                exchange = True
            if not exchange:
                break
    print(num_list)


def bubble_sort(num_list):
    return _bubble_sort(num_list)


def bubble_sort2(num_list):
    return _bubble_sort2(num_list)


data = list(range(10000))
random.shuffle(data)
bubble_sort(data)
bubble_sort2(data)
