# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0515
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : demo.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import multiprocessing as mp


def job(*args):
    global A
    for _ in range(10):
        A += 1
        print(A)


def job1(*args):
    global A
    for _ in range(10):
        A += 10
        print(A)


if __name__ == '__main__':
    # Global Value A
    A = 0
    # Add a lock
    lock = mp.Lock()
    # Add tow new process
    job_one = mp.Process(target=job, args=())
    job_tow = mp.Process(target=job1, args=())
    # Start them
    job_one.start()
    job_tow.start()
    # Join them into Process
    job_one.join()
    job_tow.join()
