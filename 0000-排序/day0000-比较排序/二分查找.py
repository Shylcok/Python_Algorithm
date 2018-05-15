# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0315
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 二分查找.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint


def binary_search(arr, ele):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == ele:
            return mid
        if guess > ele:
            high = mid - 1
        else:
            low = mid + 1
    return None


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    # my_arr = [1, 3, 5, 7, 9]
    #
    # a = binary_search(my_arr, 5)
    # my_arr1 = []
    # [my_arr1.append(randint(1, 50)) for x in range(10)]
    # print(my_arr1)
    # b = selectionSort(my_arr1)
    # print(b)
    pass