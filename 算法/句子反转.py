# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 句子反转.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


# def revo(s):
#     """
#     运行时间：43ms
#
#     占用内存：3560k
#
#     :param s:
#     :return:
#     """
#     string = s.split(' ')
#     s1 = ''
#     for x in string[::-1]:
#         if x is string[-1]:
#             s1 += x
#         else:
#             s1 += (' ' + x)
#     print(s1)
#
#
# s = input()
# revo(s)

print(' '.join(input().split(' ')[::-1]))

