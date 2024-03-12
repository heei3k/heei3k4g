#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 22:59
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : test_bpm.py
# @Software: PyCharm
import os
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# from selenium.webdriver.remote.remote_connection import LOGGER

# from log_control import INFO

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


# # 关闭Selenium的日志记录
# LOGGER.setLevel(logging.WARNING)

class TestBpm:

    def test_login(self):
        # self.log_handler=LogHandler(r'D:\Download\export_data\log\test_bpm.log', level='info')

        binary_path = (r'C:\Program Files\Mozilla Firefox\firefox.exe')
        ops = Options()
        ops.binary_location = binary_path
        self.wd = webdriver.Firefox(options=ops,
                                    service=Service(executable_path=r'D:\tools\firefox_webdriver\geckodriver.exe'))
        self.wd.implicitly_wait(5)
        url = 'http://bpm.certusnet.com.cn/portal/index_blue.jsp'
        wd = self.wd
        wd.get(url)
        # user_id_element = wd.find_element(By.XPATH, "//input[@class='logininput' and @name='userid']")
        user_id_element = wd.find_element(By.NAME, 'userid')
        # password_element = wd.find_element(By.XPATH, "//input[@class='logininput' and @name='pwd']")
        password_element = wd.find_element(By.NAME, 'pwd')
        btn = wd.find_element(By.ID, 'loginBtn')
        user_id_element.clear()
        user_id_element.send_keys("lih")
        password_element.clear()
        password_element.send_keys('0252115135')
        btn.click()

        time.sleep(10)
        wd.quit()

if __name__ == '__main__':
    pytest.main()

