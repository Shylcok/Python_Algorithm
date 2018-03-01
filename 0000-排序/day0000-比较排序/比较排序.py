# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0301
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 比较排序.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint

# 冒泡排序：
my_list = []
[my_list.append(randint(0, 100)) for x in range(10)]
print(my_list)

for i in range(len(my_list)):
    for j in range(1, len(my_list) - i):
        if my_list[j - 1] > my_list[j]:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]

print(my_list)
# 冒泡排序的特点就是调整相邻两个对象的位置，每进行一次
