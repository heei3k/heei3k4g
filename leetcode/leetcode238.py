#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 12:56
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode238.py
# @Software: PyCharm
"""
238. 除自身以外数组的乘积
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]

"""


class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [1] * length
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]
        # print(answer)
        R = 1
        for i in reversed(range(length)):
            answer[i] *= R
            R *= nums[i]
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
