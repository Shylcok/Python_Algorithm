# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0322
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : abc.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import time
# 如果a+b+c=1000 而且a^2+b^2=c^2,求出所有的组合
""""""
"""枚举方法"""
# for a in range(0, 1001):
#     pass
# for b in range(0, 1001):
#     pass
# for c in range(0, 1001):
#     pass
"""嵌套"""
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
end_time = time.time()
print(end_time-start_time+"s")