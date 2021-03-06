# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : bittree.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 题目描述
# 现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度
# 输入描述:
#
# 输入的第一行表示节点的个数n（1 ≤ n ≤ 1000，节点的编号为0到n-1）组成，
# 下面是n-1行，每行有两个整数，第一个数表示父节点的编号，第二个数表示子节点的编号
#
# 输出描述:
#
# 输出树的高度，为一个整数
#
# 输入
#
# 5
# 0 1
# 0 2
# 1 3
# 1 4
#
# 输出
#
# 3

num = int(input())
tree = {'0': [1, 0]}
for i in range(num - 1):
    parent, children = input().split()
    if parent in tree and tree[parent][1] < 2:
        tree[children] = [tree[parent][0] + 1, 0]
        tree[parent][1] += 1
depth = [x[0] for x in tree.values()]
print(max(depth))
