#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 21:32
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode035.py
# @Software: PyCharm
"""
35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。



示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4



提示:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums 为 无重复元素 的 升序 排列数组
    -104 <= target <= 104


"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = pointer = 0
        value = nums[0]
        if value >= target:
            return 0
        if target > nums[end]:
            return end + 1
        while start <= end:
            length = end - start
            pointer = length // 2
            if pointer == 0:
                break
            value = nums[start + pointer]
            if value == target:
                return start + pointer
            elif value > target:
                end = start + pointer
            else:
                start = start + pointer
        return start + pointer + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    s = Solution()
    print(s.searchInsert(nums, target))
