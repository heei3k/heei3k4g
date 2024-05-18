#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/18 11:47
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode001.py
# @Software: PyCharm

"""
88. 合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        print(nums1)
        for i in range(m + n):
            for j in range(m + n - 1 - i):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
        print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
