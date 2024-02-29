#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/27 15:48
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : fiddler_util.py
# @Software: PyCharm


import os
import urllib.request


class FiddlerUtil:

    @staticmethod
    def is_fiddler_enabled():
        proxy_handler = urllib.request.getproxies()
        return "http" in proxy_handler or "https" in proxy_handler


# 清除系统代理设置，以便进行测试
# 实际代码中不建议这样做，这里只是为了演示
# os.putenv('HTTP_PROXY', '')
# os.putenv('HTTPS_PROXY', '')

# 检查代理设置
if __name__ == '__main__':
    if FiddlerUtil.is_fiddler_enabled():
        print("Fiddler may be running.")
    else:
        print("Fiddler is not running.")
