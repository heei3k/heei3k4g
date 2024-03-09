#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/9 13:07
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    userid_loc = (By.NAME, 'userid')
    pwd_loc = (By.NAME, "pwd")
    submit_loc = (By.ID, 'loginBtn')

    def login_main_page(self, userid='lih', password='0252115135'):
        self.send_keys(LoginPage.userid_loc, userid)
        self.send_keys(LoginPage.pwd_loc, password)
        self.click(LoginPage.submit_loc)
