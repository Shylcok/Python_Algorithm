# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : lock_mulithread.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import threading


def job():
    global A, lock
    lock.acquire()
    for _ in range(10):
        A += 1
        print('job ->', A)
    lock.release()


def job1():
    global A, lock
    lock.acquire()
    for _ in range(10):
        A += 10
        print('job1 ->', A)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job)
    t2 = threading.Thread(target=job1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
