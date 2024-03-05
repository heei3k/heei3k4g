#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/24 19:32
# @Author  : Taoyuan
# @Version : 1.0
# @Contact : taoyuan0810@163.com
# @File    : debug_talk.py.py
# @Software: PyCharm
import hashlib
import random
import string
import time

from utils.yaml_util import read_yaml


class DebugTalk:
    @staticmethod
    def get_random_str(min_number, max_number):
        return str(random.randint(int(min_number), int(max_number)))

    @staticmethod
    def get_random_time():
        # return str(int(time.time()))[1:6]     #获取随机时间，得到的是时间戳
        return time.strftime('%H:%M:%S', time.localtime(time.time()))  # 获取本地时间，并将格式转换成时分秒

    @staticmethod
    def get_random_time_str():
        # return str(int(time.time()))[1:6]     #获取随机时间，得到的是时间戳
        return time.strftime('%H%M%S', time.localtime(time.time()))  # 获取本地时间，并将格式转换成时分秒

    @staticmethod
    def get_date_time():
        # return str(int(time.time()))[1:6]     #获取随机时间，得到的是时间戳
        return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 获取本地时间，并将格式转换成时分秒

    @staticmethod
    def get_milliseconds():
        return (round(time.time()))

    # MD5加密
    @staticmethod
    def gen_md5(*args):
        return hashlib.md5("".join(args).encode('utf-8')).hexdigest()

    # 从extract.yaml文件中读取字典key的值
    @staticmethod
    def read_extract_yaml(key):
        return read_yaml(key=key)

    @staticmethod
    def rand_chars():
        characters = string.ascii_letters + string.digits
        # 生成10个随机字符
        random_chars = ''.join(random.choices(characters, k=10))
        return random_chars

if __name__ == '__main__':
    print(DebugTalk.get_date_time())

    TOKEN = "debugtalk"
    data = '{"name": "user", "password": "123456"}'
    random = "A2dEx"
    print(read_yaml(key="access_token"))
