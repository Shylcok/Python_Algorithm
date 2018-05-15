# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0322
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : lnode.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from functools import wraps
from random import randint
import numpy as np
import matplotlib.pyplot as plt

import time


def fac(i):
    if i == 1: return i
    return i * fac(i - 1)


def timer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print('the {func.__name__} \'s running time is %s'.format(func=func) % (t2 - t1))
        plt.scatter(0,t2-t1)
        plt.show()
        return func

    return wrap


def sum_(numlist):
    total = 0
    for x in numlist:
        total += x
    return total


def my_sum(numlist):
    if numlist is None:
        return numlist
    else:
        if len(numlist) > 1:
            return numlist[0] + my_sum(numlist[1:])
        else:
            return numlist[0]


@timer
def sum__(numlist):
    print(sum_(numlist))


@timer
def mysum(numlist):
    print(my_sum(numlist))


@timer
def syssum(numlist):
    print(sum(numlist))


s = [randint(1, 100) for _ in range(100)]
sum__(s)
mysum(s)
syssum(s)