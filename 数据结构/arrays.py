# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0506
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : arrays.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class Array(object):
    def __init__(self, capacity, fillValue=None):
        self._items = list()

        for count in range(capacity):
            self._items.append(fillValue)

    def __str__(self):
        return str(self._items)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value
