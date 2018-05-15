# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0502
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : max_add.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 一个数组有 N 个元素，求连续子数组的最大和。
# 例如：[-1,2,1]，和最大的连续子数组为[2,1]，其和为 3

# 输入描述:
#
# 输入为两行。
# 第一行一个整数n(1 <= n <= 100000)，表示一共有n个元素
# 第二行为n个数，即每个元素,每个整数都在32位int范围内。以空格分隔。

# 输出描述:
#
# 所有连续子数组中和最大的值。

"""Solution"""
"""
还有一种更好的解法，只需要O（N）的时间。
因为最大 连续子序列和只可能是以位置0～n-1中某个位置结尾。
当遍历到第i个元素时，判断在它前面的连续子序列和是否大于0，
如果大于0，
则以位置i结尾的最大连续子序列和为元素i和前门的连续子序列和相加；
否则，
则以位置i结尾的最大连续子序列和为元素i。"""

N = int(input())
NUMS = list(map(int, input().split(' ')))
MAXSUM = maxhere = NUMS[0]
for x in range(N):
    if maxhere < 0:
        maxhere = NUMS[x]
    else:
        maxhere += NUMS[x]
    if maxhere > MAXSUM:
        MAXSUM = maxhere
print(MAXSUM)
