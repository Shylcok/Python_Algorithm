# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0313
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : QuickSort.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 迭代：


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    a = [13, 22, 3, 5, 44, -5, 6]
    print(quick_sort(a))
