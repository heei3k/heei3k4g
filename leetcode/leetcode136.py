#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/9 18:12
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode136.py
# @Software: PyCharm
"""
136. 只出现一次的数字
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。



示例 1 ：

输入：nums = [2,2,1]
输出：1

示例 2 ：

输入：nums = [4,1,2,1,2]
输出：4

示例 3 ：

输入：nums = [1]
输出：1



提示：

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    除了某个元素只出现一次以外，其余每个元素均出现两次。


"""
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_s = set(nums)
        nums_r = list(reversed(nums))
        for num in nums_s:
            if nums.index(num) + nums_r.index(num) == len(nums) - 1:
                return num

    def singleNumber2(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 1]
    print(s.singleNumber(nums))
    nums = [4, 1, 2, 1, 2]
    print(s.singleNumber(nums))
    nums = [1]
    print(s.singleNumber(nums))
