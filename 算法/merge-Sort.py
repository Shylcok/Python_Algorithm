# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0303
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : merge-Sort.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint
import time
from functools import wraps


def fn_timer(func):
    @wraps(func)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (func.__name__, str(t1 - t0))
              )
        return result

    return function_timer


def merge(left, right, i=0, j=0):
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    # 归并
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == '__main__':
    my_list = []
    [my_list.append(randint(0, 100)) for _ in range(10)]
    result_sorted = merge_sort(my_list)
    print('原数组\n', my_list)
    print('归并排序后的数组\n', result_sorted)
