# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0428
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : stack__.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()


if __name__ == '__main__':
    myStack = Stack()
    for _ in range(9):
        myStack.push(_)
    print(myStack.size())
    print(myStack.peek())
    print(myStack.pop())
    print(myStack.size())
