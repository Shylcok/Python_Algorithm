# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0506
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : Grid.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

from 数据结构.arrays import Array


class Grid(object):
    def __init__(self, rows, columns, fill_value=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self._data)

    def get_width(self):
        return len(self._data[0])

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        res = ''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                res += str(self._data[row][col]) + ' '
            res += '\n'
        return res


mygrid = Grid(2, 3, 'JY')
print(mygrid.get_width())
print(mygrid.get_height())
print(mygrid.__str__())
