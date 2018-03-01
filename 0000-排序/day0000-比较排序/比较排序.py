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

# 冒泡排序：
my_list = []
[my_list.append(randint(0, 100)) for x in range(10)]
print('原数据\n', my_list)


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


print('经过冒泡排序后的数据\n', bubble_sort(my_list))



# 梳理排序
def comb_sort(num_list):
    """
    梳理排序，是基于冒泡排序的一种改进：
    :param num_list:
    :return:
    """
    pass
