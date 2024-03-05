#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/2 13:28
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : delete_zip.py
# @Software: PyCharm

import os

from logging_tool.log_control import LogHandler


# 实现功能：如果目标目录中同时存在子文件夹和文件，判断如果存在子文件夹和同名的zip等压缩包文件，则删除该文件
def remove_files_if_exist_same_name_folders(directory):
    # 遍历目录中的所有文件和子目录
    loop_dir = os.listdir(directory)
    log_handler = LogHandler(f"./delete.log", level='info')
    for item in loop_dir:
        item_path = os.path.join(directory, item)
        loop_dir.remove(item)
        # 检查是否为目录
        if os.path.isdir(item_path):
            # 第二次遍历，检查是否存在同名的文件
            for item_second in loop_dir:
                a = os.path.join(directory, item_second)
                if os.path.isfile(a) and os.path.exists(a):
                    item_second = os.path.join(directory, item_second).rsplit('.', 1)[0]
                    b = os.path.join(directory, item_path)
                    if item_second == b:
                        log_handler.logger.info(f"Removed file:{a}")
                        os.remove(a)


# 使用你的目录路径替换下面的路径
directory = r"D:\迅雷下载"
remove_files_if_exist_same_name_folders(directory)
