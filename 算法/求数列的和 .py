# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0503
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 求数列的和 .py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 题目描述
# 数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。

# 输入描述:
#
# 输入数据有多组，每组占一行，由两个整数n（n < 10000）和m(m < 1000)组成，n和m的含义如前所述。
# 输出描述:
#
# 对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。

# 示例1
# 输入
#
# 81 4
# 2 2
#
# 输出
#
# 94.73
# 3.41
from math import sqrt


def sqrt_(n, m):
    for _ in range(m):
        n += sqrt(n)
    return n


count = 0


def sqrt_2(n, m):
    global count
    if count > m:
        return
    count += 1
    return sqrt_2(sqrt(n), m)


print(sqrt_2(81, 4))
