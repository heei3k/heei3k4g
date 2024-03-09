#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/6 11:22
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : decrypt_util.py
# @Software: PyCharm

import base64
import hashlib


def calculate_md5(string):
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    return md5.hexdigest()


# # 调用函数并打印结果
# result = calculate_md5("https://aod.cos.tx.xmcdn.com/storages/4598-audiofreehighqps/B3/1A/GKwRIJEFdTVVAAOgSQD7LMxO-aacv2-48K.m4a")
# print(result)


def base64_encode(text):
    encode_data = base64.b64encode(text.encode())
    return encode_data


def base64_decode(encode_data):
    decode_data = base64.b64decode(encode_data)
    return decode_data


def sha256_encode(inStr: str):
    sha256 = hashlib.sha256()  # 实例化对象
    sha256.update(inStr.encode('utf-8'))  # 使用update方法加密
    return sha256.hexdigest()  # 调用hexdigest方法获取加密结果


if __name__ == '__main__':
    text = 'aHR0cHM6Ly9hb2QuY29zLnR4LnhtY2RuLmNvbS9zdG9yYWdlcy80NTk4LWF1ZGlvZnJlZWhpZ2hxcHMvQjMvMUEvR0t3UklKRUZkVFZWQUFPZ1NRRDdMTXhPLWFhY3YyLTQ4Sy5tNGE='
    # encode_data = base64_encode(text)
    # decode_data = base64_decode(encode_data)
    # print('Base64 编码：', encode_data)
    # print('Base64 解码：', decode_data)

    print(base64_decode(text))
