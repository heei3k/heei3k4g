#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/18 19:14
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode080.py
# @Software: PyCharm

"""
80. 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""


class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        slow = 2
        for fast in range(2, n):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
