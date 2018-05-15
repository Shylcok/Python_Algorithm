# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : shared_mem.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import multiprocessing as mp

value = mp.Value('d', 1)
array = mp.Array('i', [1, 2, 3])
print(array)