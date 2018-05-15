# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : fib_.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


def fib(i):
    """
    simple one
    :param i:
    :return:
    """
    if i < 2: return 1
    return fib(i - 2) + fib(i - 1)


from functools import wraps


def cachedFunc(func):
    """
    a func cache
    :param func:
    :return:
    """
    cache = {}

    @wraps(func)
    def wrap(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@cachedFunc
def fib_(i):
    if i < 2: return 1
    return fib_(i - 2) + fib_(i - 1)


def fib__(n, counter):
    pass
