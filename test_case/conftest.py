#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/22 16:17
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : conftest.py
# @Software: PyCharm

import pytest

from utils.yaml_util import clear_yaml

# @pytest.fixture(scope="session",autouse=True)
# def exc_sql():
#     print("请求之前，查询数据库")
#     yield
#     print("请求之后，关闭数据库")

# @pytest.fixture(scope="session",autouse=False,params=read_yaml("weixin.yaml"))
# # def set_epic(request):
# #     yield request.params

pytest.fixture(scope="function", autouse=True)


def exc_log():
    INFO.logger.info("\n")
    INFO.logger.info("---------接口测试开始----------")
    yield
    INFO.logger.info("---------接口测试结束----------")
    INFO.logger.info("\n")




@pytest.fixture(scope="session", autouse=True)
def clears():
    # current_file = __file__  # 获取当前执行的文件名（包括后缀）
    # current_dir = os.path.dirname(current_file)  # 获取当前执行的文件所在目录
    # file_path = os.path.join(current_dir, 'extract.yaml')
    clear_yaml()
