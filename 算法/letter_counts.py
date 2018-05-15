# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0427
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : letter_counts.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 题目描述
# 给定一个英文字符串,请写一段代码找出这个字符串中首先出现三次的那个英文字符。
# 输入描述:
# 输入数据一个字符串，包括字母,数字等。
# 输出描述:
# 输出首先出现三次的那个英文字符

from collections import defaultdict

dd = defaultdict(int)
for _ in input():
    if _.isalpha():
        dd[_] += 1
        if dd[_] == 3:
            print(_)
            break
