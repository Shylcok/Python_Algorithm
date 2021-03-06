# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0503
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : IDCARD.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 18位身份证的编码规则是：
# 前1、2位数字表示：所在省（直辖市、自治区）的代码
# 第3、4位数字表示：所在地级市（自治州）的代码
# 第5、6位数字表示：所在区（县、自治县、县级市）的代码；
# 第7—14位数字表示：出生年、月、日；
# 第15、16位数字表示：所在地的派出所的代码；
# 第17位数字表示性别：奇数表示男性，偶数表示女性；
# 第18位数字是校检码，用来检验身份证的正确性。
# 用户在输入身份证的过程中经常会输入错误，为了方便用户正确输入需要在输入过程中对用户的输入按照
# 6+8+4 的格式进行分组，实现一个方法接收输入过程中的身份证号，返回分组后的字符
# 输入描述:
#
# 输入数据有多行，每一行是一个输入过程中的身份证号
#
# 输出描述:
#
# 分组后的字符串
#
# 示例1
# 输入
#
# 5021
# 502104 198803
# 5021041988033084
# 502104198803308324
#
# 输出
#
# 5021
# 502104 198803
# 502104 19880330 84
# 502104 19880330 8324
ids = list()
for x in input().replace(' ',''):
    ids.append(x)

def split_(id_nums):
    s = ''
    i = len(id_nums)
    if len(id_nums) <= 6:
        print(s.join(ids[0:i]))
    elif len(id_nums) <= 14:
        print(s.join(ids[0:6]), s.join(ids[6:i]))
    else:
        print(s.join(ids[0:6]), s.join(ids[6:14]), s.join(ids[14:]))


split_(ids)
