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

    def test_off_duty(self):
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
        hr_tab = wd.find_element(By.XPATH, '//a[text()="人力资源（赛特斯）"]')
        hr_tab.click()
        wd.implicitly_wait(1)
        for i in range(9):
            print("进入到第{}页".format(i + 1))
            off_duty_tab = wd.find_element(By.XPATH, '//a/div[text()="请假申请流程"]')
            if i > 0:
                goto_page = wd.find_element(By.XPATH,
                                            '//a[onclick="return gotoPage(frmMain,\'WorkFlow_Execute_Worklist\',{});return false;"]'.format(
                                                i + 1))
                goto_page.click()
            off_duty_tab.click()
            for j in range(18):
                off_duty_application = wd.find_element(By.XPATH, '//td/a[text()="(填写申请)李华的请假申请"]')
                off_duty_application.click()

    def tear_down(self):
        wd = self.wd
        time.sleep(10)
        wd.quit()


if __name__ == '__main__':
    # pytest.main()
    text = 'kpi520'
    res = eval(text[3:-1])
    print(text[3:-1])
    print(res)
