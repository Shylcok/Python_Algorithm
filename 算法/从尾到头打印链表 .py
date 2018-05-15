# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0502
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 从尾到头打印链表 .py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 输入一个链表，从尾到头打印链表每个节点的值。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        a = []
        head = listNode
        while head:
            a.insert(0, head.val)
            head = head.next
        return a


# 运行时间：37ms
#
# 占用内存：5728k
