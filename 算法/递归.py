# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0315
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 递归.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from math import factorial


def countdown(i):
    print(i)

    if i >= 2:
        countdown(i - 1)
    return


def greet(name):
    print("Hello,", name, '!')
    greet2(name)
    print("getting ready 2 c bye")


def greet2(name):
    print("How r u,", name, '?')


def bye():
    print('bye')


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)


if __name__ == '__main__':
    a = factorial(5)
    print(a)
    b =fact(5)
    print(b)
