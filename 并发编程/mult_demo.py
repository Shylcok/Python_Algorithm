# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : mult_demo.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import multiprocessing as mp
import threading as td
from time import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        stop = time()
        print('[time] %s' % (stop - start))
        return func

    return wrapper


def job(q):
    res = 0
    for i in range(1000000):
        res += i + i ** 2 + i ** 3
    q.put(res)


@timer
def multcore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    res = q.get()
    res1 = q.get()
    print('multi_core -> ',res + res1)


@timer
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    print('normal -> ', res)


@timer
def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    res = q.get()
    res1 = q.get()
    print('multi_thread -> ', res + res1)


if __name__ == '__main__':
    normal()
    multcore()
    multithread()
