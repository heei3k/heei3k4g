#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 22:05
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : test_leetcode152.py
# @Software: PyCharm

import allure

from leetcode.costTime import cost_time
from leetcode.leetcode152 import Solution


class Test_leetcode152:
    @allure.feature("leetcode152")
    @allure.story("leetcode152")
    @cost_time
    def test_case_1(self):
        nums = [-1, -2, -3, 0]
        sol = Solution()
        res = sol.maxProduct(nums)
        assert res == 6
