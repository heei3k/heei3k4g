#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/3 15:15
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : text_util.py
# @Software: PyCharm

import os

from logging_tool.log_control import WARNING, ERROR

root_dir = os.path.dirname(os.path.dirname(__file__))  # 获取根目录
data_dir = os.path.join(root_dir, 'data')  # 获取yaml目录
default_filepath = os.path.join(data_dir, 'extract.txt')


def read_text(file_path=default_filepath):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    else:
        ERROR.logger.error(f"文件{file_path}不存在")


def write_text(file_path=default_filepath, data=None):
    if os.path.exists(file_path):
        if data:
            with open(file_path, encoding='utf-8', mode="a+") as f:
                f.write(data)
        else:
            WARNING.logger.warning("写入数据为空")
    else:
        ERROR.logger.error(f"文件{file_path}不存在")


def clear_text(file_path=default_filepath):
    # print("file path 为%s" % file_path)
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8', mode="w") as f:
            # print("开始清除yaml文件")
            f.truncate()


if __name__ == '__main__':
    print(default_filepath)
    write_text(data="tt")
