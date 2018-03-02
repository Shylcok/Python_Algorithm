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
import math
import time
from functools import wraps

# 冒泡排序：
my_list = []
[my_list.append(randint(0, 1000)) for x in range(1000)]
print('原数据\n', my_list)


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


@fn_timer
def bubble_sort(num_list):
    """
    冒泡排序的特点就是调整相邻两个对象的位置，每进行一次内循环，就可以将最大值调整到最后，
    这样以后就可以不必再考虑它了，在进行了n-1次内循环后，就得到了完整的有序列，
    时间复杂度为O(n^2)，虽然时间上不占优势，但是代码非常简洁，实现难度很低。。
    :param num_list:
    :return: sorted list
    """
    for i in range(len(num_list) - 1):
        for j in range(1, len(num_list) - i):
            if num_list[j - 1] > num_list[j]:
                num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
    return num_list


# 梳理排序

@fn_timer
def comb_sort(num_list, flag=False, s=1.3):
    """
    梳理排序，是基于冒泡排序的一种改进：
    :param s:
    :param flag:
    :param num_list:
    :return:
    """
    j = len(num_list)-1
    while (j > 1) or flag is True:
        i = 0
        j = max(math.floor(j / s), 1)
        flag = False
        while i + j <= len(num_list)-1:
            if num_list[i-1] > my_list[i + j-1]:
                num_list[i - 1], num_list[i + j - 1] = num_list[i + j - 1], num_list[i - 1]
                flag = True
            i = i + 1

    return num_list


@fn_timer
def py_sort(num_list):
    return sorted(num_list)


if __name__ == '__main__':
    print('经过冒泡排序后的数据\n', bubble_sort(my_list))
    print('经过梳理排序后的数据\n', comb_sort(my_list))
    print('经过sorted函数排序后的数据\n', py_sort(my_list))
