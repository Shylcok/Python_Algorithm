# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0419
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : dp_dongtaiguihua.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# sum fibs
from functools import wraps
import time


def fib_(i):
    """
    default func
    :param i:
    :return:
    """
    if i < 2:
        return 1
    return fib_(i - 1) + fib_(i - 2)


def memo(func):
    """
    第一种带备忘录的递归实现方式
    :param func:
    :return:
    """
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fib(i):
    """
    因为是递归形式，
    所以有限的栈深度是它的硬伤，
    有些问题难免会出现栈溢出.
    :param i:
    :return:
    """
    if i < 2:
        return 1

    return fib(i - 1) + fib(i - 2)


def fib_iter(i):
    c = 0
    n = 0
    a, b = 1, 1
    if i < 2:
        return 1
    while i > 2:
        c = a + b
        a = b
        b = c
        n = n + 1
        while n == i:
            break
    return c
    pass


if __name__ == '__main__':
    # print(fib(100))
    print(fib_iter(100))
