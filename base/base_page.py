#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/9 13:02
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : base_page.py
# @Software: PyCharm

class BasePage:

    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    def send_keys(self, loc, value):
        self.driver.locator_element(loc).send_keys(value)

    def click(self, loc):
        self.driver.locator_element(loc).click()
