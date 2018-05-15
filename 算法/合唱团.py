# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 合唱团.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 有 n 个学生站成一排，
# 每个学生有一个能力值，
# 牛牛想从这 n 个学生中按照顺序选取 k 名学生，
# 要求相邻两个学生的位置编号的差不超过 d，
# 使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

"""
每个输入包含 1 个测试用例。
每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，
接下来的一行，包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。
接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。
"""
from random import randint
N = int(input())
ais = input().split(' ')
k, d = input().split(' ')
for x in range(len(ais)):
    print(int(ais[randint(x-int(d)//2,x)]) * int(ais[randint(x,x+int(d)//2)]))