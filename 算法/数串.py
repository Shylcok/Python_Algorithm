# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 数串.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
# 如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
# 如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
# 输入描述:
#
# 有多组测试样例，每组测试样例包含两行，
# 第一行为一个整数N（N<=100），
# 第二行包含N个数(每个数不超过1000，空格分开)。
#
# 输出描述:
#
# 每组数据输出一个表示最大的整数。

n = input()
nums = []
s = ''
[nums.append(_) for _ in input().split(' ')]


def find(array):
    global s

    if len(array) <= 0:
        return
    a = array[0]
    for b in array:
        if a + b < b + a:
            a = b
        s += a
        array.remove(a)
        find(array)
        return s


print(find(nums))
