# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 二维数组.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 在一个二维数组中，
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，
# 输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array) - 1
        cols = len(array[0])- 1

        # 利用二维数组由上到下，由左到右递增的规律，
        # 那么选取右上角或者左下角的元素a[row][col]
        # 与target进行比较，
        # 当target小于元素a[row][col]
        # 时，那么target必定在元素a所在行的左边,
        # 即col - -；
        # 当target大于元素a[row][col]
        # 时，那么target必定在元素a所在列的下边,
        # 即row + +；
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False


if __name__ == '__main__':
    target, array = 5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    solution = Solution()
    res = solution.Find(target, array)
    print(res)
