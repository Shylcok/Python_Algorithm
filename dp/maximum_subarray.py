# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0422
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : maximum_subarray.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


def getMax(a, b):
    if a > b:
        return a
    return b


def find_subarry(arr, n):
    sum_ = arr[0]
    max_ = arr[0]
    for i in range(n):
        sum_ = getMax(sum_ + arr[i], arr[i])
        if sum_ > max_:
            max_ = sum_
        return max_


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(' ')))
    res = find_subarry(arr, n)
    print(res)