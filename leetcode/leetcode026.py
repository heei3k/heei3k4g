#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/18 15:27
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode026.py
# @Software: PyCharm

"""
26. 删除有序数组中的重复项

给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

    更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
    返回 k 。

带office的方法是官方的解法，因为该数组已经确实是非严格递增数列，我的解法适合任意数组

"""
from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        k = 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                valid = True
                for t in range(i + 1):
                    if nums[j] == nums[t]:
                        valid = False
                if not valid:
                    break
                else:
                    nums[k] = nums[j]
                    k += 1
        nums = nums[:k]
        print(nums)
        return k

    def removeDuplicatesOffice(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums)
        return slow


nums = [1, 1, 2]
# print(Solution().removeDuplicates(nums))
print(Solution().removeDuplicatesOffice(nums))
print(nums)
