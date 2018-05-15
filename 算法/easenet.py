# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0502
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : easenet.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数，
# 分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。

# 接下来的N行每行包含两个正整数，分别表示
# 该项工作的难度Di(Di<=1000000000)
# 和报酬Pi(Pi<=1000000000)。

# 接下来的一行包含M个正整数，
# 分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
# 保证不存在两项工作的报酬相同。

# 输出描述:
# 对于每个小伙伴，
# 在单独的一行输出一个正整数表示他能得到的最高报酬。
# 一个工作可以被多个人选择。




# 数量N
# 小伙伴的数量M
N, M = map(int, input().split(' '))

# 难度Di
a = []

# 报酬Pi
b = []
for x in range(N):
    Di, Pi = (map(int, input().split(' ')))
    a.append(Di)
    b.append(Pi)
# 小伙伴的能力值Ai
Ai = list(map(int, input().split(' ')))
print(a)
print(b)
print(Ai)
