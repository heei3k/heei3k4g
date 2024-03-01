#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/22 13:53
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : send_request.py
# @Software: PyCharm

"""
封装统一的接口请求，并假如终端打印和日志

"""
import requests

from logging_tool.log_control import INFO


class SendRequest:
    session = requests.session()

    def all_send_request(self, method, url, **kwargs):
        INFO.logger.info("\n")
        INFO.logger.info("---------接口测试开始----------")
        INFO.logger.info("接口地址 %s" % url)
        INFO.logger.info("请求方式 %s" % method)
        if "params" in kwargs.keys():
            INFO.logger.info("请求params %s" % kwargs["params"])
        if "json" in kwargs.keys():
            INFO.logger.info("请求json %s" % kwargs["json"])
        if "files" in kwargs.keys():
            INFO.logger.info("请求files %s" % kwargs["files"])
        if "data" in kwargs.keys():
            INFO.logger.info("请求data %s" % kwargs["data"])
        res = SendRequest.session.request(method, url, **kwargs)
        INFO.logger.info("接口返回：%s" % res.text)
        INFO.logger.info("---------接口测试结束----------")
        INFO.logger.info("\n")
        return res
