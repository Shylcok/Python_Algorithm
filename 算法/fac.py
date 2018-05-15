# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : fac.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint


def factors(num, fac=None):
    if fac is None:
        fac = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            fac.append(i)
            factors(num // i, fac)
            break
    else:
        fac.append(num)


facs = []
n = randint(2, 10 ** 8)
factors(n, facs)
res = '*'.join(map(str, facs))
if n == eval(res):
    print(n, '=', res)
