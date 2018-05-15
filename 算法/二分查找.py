# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0329
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 二分查找.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import time


def time_cl(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__, 'running time is ', t2 - t1)
        return func

    return wrapper


@time_cl
def bin_search(list, item):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess >= item:
            high = mid - 1
        else:
            low = mid + 1
    return None


data = list(range(10000))

bin_search(data, 6)
