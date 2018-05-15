# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0508
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 二叉树的深度.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


# 我们可以从根节点即左右子树来理解二叉树的深度。对于任意一棵非空二叉树，有如下四种情况：
#
# （1）如果一颗树只有一个节点，它的深度是1；
#
# （2）如果根节点只有左子树而没有右子树，那么二叉树的深度应该是其左子树的深度加1；
#
# （3）如果根节点只有右子树而没有左子树，那么二叉树的深度应该是其右树的深度加1；
#
# （4）如果根节点既有左子树又有右子树，那么二叉树的深度应该是其左右子树的深度较大值加1；


class Tree():
    def __init__(self, Node='root', left=None, right=None):
        self._Node = Node
        self.left = left
        self.right = right

    def isEmpty(self):
        return self._Node == None

    def depth(self):
        if self._Node == 'root':
            return 1

