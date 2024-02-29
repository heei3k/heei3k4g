#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/21 10:44
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : api_server.py
# @Software: PyCharm
import requests

from flask import Flask

import interface_testcase.debug_talk.gen_md5 as gen_md5


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

# 自定义接口：post请求，data传参
@app.route('/get_token', methods=['POST'])
def login():
    username = requests.values.get('username')
    password = requests.values.get('password')
    if username==str(gen_md5('admin')).upper() and password==str(gen_md5('123')).upper():
        return {'error_code':'0','message':'登录成功','data':[{'api_token':gen_md5('admin123')}]}
    else:
        return {'error_code': '-1', 'message': '参数有误', 'data': []}


if __name__ == '__main__':
    app.run()
