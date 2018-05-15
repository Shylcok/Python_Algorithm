# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0502
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 水仙花数.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

start, stop = map(int, input().split(' '))
res = [153, 370, 371, 407]
a = []
for x in range(start, stop + 1):
    if x not in res:
        continue
    a.append(x)

if len(a) is not 0:
    for x in a:
        print(x, end=' ')
else:
    print('no')
