#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : manage.py
@Time    : 2021/12/20 2:51 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

# uwsgi --http :9090 --wsgi-file manage.py