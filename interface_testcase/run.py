#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/23 16:17
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : run.py.py
# @Software: PyCharm

import os
import time
import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    # os.system("pytest --alluredir =./allure-results")
    os.system("allure serve ./allure-results --clean")