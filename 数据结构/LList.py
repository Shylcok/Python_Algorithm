# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0427
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : LList.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        empty?
        :return:
        """
        return self._head is None

    def prepend(self, elem):
        """

        :param elem:
        :return:
        """
        self._head = LNode(elem, self._head)

    def pop(self):
        """

        :return:
        """

        if self._head is None:
            raise NotImplementedError("in pop")
        e = self._head.elem
        self._head = self._head.next_
        return e

    def append(self, elem):
        """

        :param elem:
        :return:
        """
        if self._head is None:
            self._head = LNode(elem)
            return

        p = self._head
        while p.next_ is not None:
            p = p.next_
        p.next_ = LNode(elem)

    def pop_last(self):
        """

        :return:
        """
        if self._head is None:
            raise NotImplementedError('in pop_last')
        p = self._head
        if p.next_ is None:
            e = p.elem
            self._head = None
            return e
        while p.next_.next_ is not None:
            p = p.next_
        e = p.next_.elem
        p.next_ = None
        return e

    def print_all(self):
        """

        :return:
        """
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next_ is not None:
                print(',', end=' ')
            p = p.next_
        print(' ')


if __name__ == '__main__':
    ll = LList()
    ll.pop()