#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : forforfor.py
@Time    : 2021/12/20 6:15 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
from data.datafactory import *


def test111(to_eat_list):
    for x in range(2):
        a = whattoeat(to_eat_list)
        print(a)
    return True


if __name__ == '__main__':
    to_eat_list = ['木屋烧烤烤全羊', '烤羊腿', '海底捞火锅', '朋友圈烤羊排']
    test111(to_eat_list)
