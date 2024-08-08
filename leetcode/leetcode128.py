#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/28 10:34
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode128.py
# @Software: PyCharm
"""
128. 最长连续序列

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


"""
from typing import List


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        print(nums)
        start_index = 0
        start_num = nums[0]
        max_length = 1
        for i, element in enumerate(nums):
            if max_length < i - start_index + 1 and i - start_index == element - start_num:
                max_length = i - start_index + 1
            if i - start_index != element - start_num:
                start_index = i
                start_num = element

        return max_length

    def longestConsecutive2(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


nums = [0, -1]

print(Solution().longestConsecutive2(nums))
