# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0422
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : lnode.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
"""
动态规划
Dynamic Programming
"""
from functools import wraps


def fib(i):
    """
    O(2^n)
    :param i:
    :return:
    """
    if i <= 2: return 1
    return fib(i - 1) + fib(i - 2)


fib_ = lambda i: fib_(i - 1) + fib_(i - 2)

if __name__ == '__main__':
    print(fib(6))
    print(fib_(6))