# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 电话号码分身.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 继MIUI8推出手机分身功能之后，
# MIUI9计划推出一个电话号码分身的功能
# ：首先将电话号码中的每个数字加上8取个位，
# 然后使用对应的大写字母代替
nums = {"ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}
# 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
N = input()
strings = []
for _ in range(int(N)):
    strings.append(input())

for x in nums:
    for y in strings:
        if x == y:
            print(nums[y])
