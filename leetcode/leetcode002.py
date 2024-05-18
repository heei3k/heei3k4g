#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/18 12:19
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode002.py
# @Software: PyCharm

"""
27.移除一个元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

    更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
    返回 k。

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(Solution().removeElement(nums, 2))
