# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0427
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : rest_max.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 题目描述
# 给定一个十进制的正整数number，选择从里面去掉一部分数字，希望保留下来的数字组成的正整数最大。

# 输入描述:
# 输入为两行内容，第一行是正整数number，1 ≤ length(number) ≤ 50000。
# 第二行是希望去掉的数字数量cnt 1 ≤ cnt < length(number)。

# 输出描述:
# 输出保留下来的结果。

# 示例1

# 输入
# 325
# 1
# 输出
# 35


def func(num, k):
    res = []
    for i in num:
        while res and k:
            if res[-1] < i:
                res.pop()
                k -= 1
            else:
                res.append(i)
                break
        else:
            res.append(i)
    while k:
        res.pop()
        k -= 1
    return ''.join(res)


number = input().strip()
cnt = int(input())

print(func(number, cnt))
