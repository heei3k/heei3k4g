#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 10:05
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode209.py
# @Software: PyCharm
"""
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：

输入：target = 4, nums = [1,4,4]
输出：1

示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0



提示：

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 105



进阶：

    如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。


"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target <= max(nums):
            return 1
        n = len(nums)
        if target > sum(nums):
            return 0

        ans, rk, sum_ = n, n, sum(nums)
        for i in range(n):
            while rk > i:
                rk -= 1
                sum_ -= nums[rk]
                if sum_ < target:
                    ans = min(ans, rk - i + 2)
                    sum_ -= nums[i]
                    rk += 1
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(4, [1, 4, 4]))
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(s.minSubArrayLen(15, [1, 2, 3, 4, 5]))
