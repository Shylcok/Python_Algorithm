# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : coffee.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 某餐馆有n张桌子，
# 每张桌子有一个参数：a 可容纳的最大人数；
# 有m批客人，每批客人有两个参数:b人数，c预计消费金额。
# 在不允许拼桌的情况下，请实现一个算法选择其中一部分客人，使得总预计消费金额最大

# 输入描述:
#
# 输入包括m+2行。 第一行两个整数n(1 <= n <= 50000),m(1 <= m <= 50000)
#  第二行为n个参数a,即每个桌子可容纳的最大人数,以空格分隔,范围均在32位int范围内。
#  接下来m行，每行两个参数b,c。分别表示第i批客人的人数和预计消费金额,以空格分隔,范围均在32位int范围内。

# 输出描述:
#
# 输出一个整数,表示最大的总预计消费金额


# n张桌子,m批客人
n, m = map(int, input().split(' '))

# a 可容纳的最大人数
lyst = map(int, input().split(' '))

# 客人有两个参数:
# b人数，c预计消费金额。
lyst_b = []
lyst_c = []
for _ in range(m):
    b, c = input().split(' ')
    lyst_b.append(b)
    lyst_c.append(c)


