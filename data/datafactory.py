#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : datafactory.py
@Time    : 2021/12/20 2:33 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
import random
import logging
from Notice.EnterpriseNotice import connect_enterprise


def whattoeat(to_eat_list):
    msgdata = "今晚的" + random.choice(to_eat_list) + "由旭公子买单"
    token = 'key=22d5e05e-1f8d-458a-9f6d-d04326f478c1'
    mentioned_list = ['18304648883']
    # logging.info(toeat)
    msg = connect_enterprise(token, msgdata, mentioned_list)
    return msg


# if __name__ == '__main__':
    # whattoeat(to_eat_list)
