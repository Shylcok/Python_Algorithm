# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0422
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : lnode.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


# djb2
def djb2(s):
    h = 0
    for c in s:
        h = h * (2 ** 6) + h + ord(c)
    return h


# sdbm
def sdbm(s):
    h = 0
    for c in s:
        h = h * (2 ** 6) - h + ord(c)
    return h


def main():
    string = 'name'
    print(djb2(string),'\n')
    print(sdbm(string))

if __name__ == '__main__':
    main()