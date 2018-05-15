# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0417
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : quick_sort.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import random
import time


def timer(func):
    def warps(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print('the time is ', (t2 - t1))
        return func

    return warps


def quick_sort_(data, left, right):
    if left < right:
        mid = partitons_(data, left, right)
        quick_sort_(data, left, mid - 1)
        quick_sort_(data, mid + 1, right)


def partitons_(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


@timer
def quick_sort(data, left, right):
    quick_sort_(data, left, right)


data = [random.randint(0, 50) for _ in range(10000)]

@timer
def sys_sort(data):
    return data.sort()


quick_sort(data, 0, len(data) - 1)
sys_sort(data)