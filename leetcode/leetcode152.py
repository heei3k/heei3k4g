#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 22:06
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode152.py
# @Software: PyCharm

from typing import List


class Solution:
    def __init__(self):
        self.all_list = []

    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        self.sub_product(nums, 0, length)
        return max(self.all_list)

    def sub_product(self, nums, start, end):
        if start >= end:
            return
        res = nums[start]
        for i in range(start + 1, end):
            if nums[i] < 0:
                self.all_list.append(res)
                self.sub_product(nums, i + 1, end)
                res *= nums[i]
            elif nums[i] == 0:
                self.all_list.append(0)
                self.sub_product(nums, i + 1, end)
                break
            else:
                if res <= 0:
                    self.sub_product(nums, i, end)
                if res != 0:
                    res *= nums[i]
        self.all_list.append(res)
