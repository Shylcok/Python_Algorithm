# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0512
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : multi_pool_.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import multiprocessing as mp


def job(x):

    return x * x


def multicore():
    pool = mp.Pool()

    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    multires = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multires])


if __name__ == '__main__':
    multicore()
