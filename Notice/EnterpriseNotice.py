#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : EnterpriseNotice.py
@Time    : 2021/12/17 2:51 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""

import json
import requests
import logging

"""
根据msgtype 发送text/link通知
"""

def connect_enterprise (token, msgdata, mentioned_list):
    token = token
    msgdata = msgdata
    mentioned_list = mentioned_list
    enterprise_token = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?' + token
    data =  {
        "msgtype": "text",
        "text": {
            "content": msgdata,
            "mentioned_mobile_list": mentioned_list
        }
    }
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    rs = requests.post(url=enterprise_token, data=json.dumps(data), headers=headers)
    msg = rs.json()
    logging.info(msg)
    # log.info(msg)
    return msg


if __name__ == '__main__':
    # token = ''
    token = 'key=22d5e05e-1f8d-458a-9f6d-d04326f478c1'
    # msgdata = "今晚上楼捏脚，全场由我旭公子买单"
    mentioned_list = ['18304648883', "@all"]
    connect_enterprise(token, msgdata, mentioned_list)
