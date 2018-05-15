# -*- coding: utf-8 -*-
# @Project : Algorithm_Python
# @Time    : 0515
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : Python脚本中执行shell命令.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import subprocess

# cmd = ('ls', '-l')
# subprocess.Popen(cmd)


import os
# os.system('cmd1&;&;cmd2')
# cmd1="cd../"
# cmd2="ls"
# cmd=cmd1+"&;&;"+cmd2


cmd1 = "cd ../"
cmd2 = "ls"
cmd = cmd1 + " && " + cmd2
subprocess.Popen(cmd, shell=True)
subprocess.call(cmd, shell=True)
