# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0422
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : mode_func.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
"""模运算"""
"""
A Mod B=A-(AdivB) * B
"""
"""
 python语言的取模运算：

如果 a/b = q, a%b = r （可表示为a/b=q … r）

#在python中，遇到取模运算时，可以先用向下取整的方式算出q，然后结合下面的公式算出r。

那么 a = b*q + r

另外， python中，含有负数的取模运算最终的结果符号和被取余的一方保持一致

如： 17 % -10 = 3 ；-17 % 10 = 3 
"""


def mod(A, B):
    return A - (A // B) * B


a = 10
b = 4
q = a // b
r = a % b
print(q)
print(r)
a = b * q + r
print(a)