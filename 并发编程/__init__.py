# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0503
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : __init__.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import threading
import time


def job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')


def main():
    added_thread = threading.Thread(target=job, name='T1')
    added_thread.start()
    added_thread.join()
    print('all done\n')


if __name__ == '__main__':
    main()
