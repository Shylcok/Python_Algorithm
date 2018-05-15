# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0511
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : sth_whith_Queue.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import threading
import time
from queue import Queue


def job(l,q):
    for i in range(len(l)):
        l[i] **= l[i]
    q.put(l)


def main():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 4, 4], [5, 4, 7], [1, 1, 1]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    res = []
    for _ in range(4):
        res.append(q.get())
    print(res)
    return


if __name__ == '__main__':
    main()
